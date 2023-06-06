import psycopg2
import pandas as pd
import numpy as np
from mido import MidiFile, MetaMessage, bpm2tempo, Message, MidiTrack


# Підключення до моєї БД
def connection_to_DB():
    connection = psycopg2.connect(
        dbname="MyDB",
        user="Olena",
        password="23032002",
        host="localhost",
        port="5432"
    )
    return connection


# Зчитування даних для побудови матриці переходів
def data_for_transition_matrix(connection, query):
    cur = connection.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()
    # Сюди я поміщу списки з послідовностями нот з кожного файлу
    list_of_lists = []
    # Додаємо кожну зчитану з БД послідовність нот у вигляді списку у список
    for row in rows:
        list_of_lists.append(eval(row[2]))
    return list_of_lists


def dict_creation(list_of_lists):
    # Створимо список ключів
    merged_list = []
    for lst in list_of_lists:
        merged_list.extend(lst)
    keys = sorted(set(merged_list))

    # Створимо значення у вигляді списків з частотою переходу в кожен стан
    values = []  # Список, в якому будуть списки-значення словника
    for value in keys:
        frequencies = [0] * len(keys)
        for row_for_test in list_of_lists:
            for idx, test_value in enumerate(row_for_test[:-1]):
                if test_value == value:
                    index = keys.index(row_for_test[idx + 1])
                    frequencies[index] += 1

        values.append(frequencies)

    # З'єднання ключів зі значеннями
    my_dict = dict(zip(keys, values))
    return my_dict


def normalization(my_dict):
    # Нормалізація
    for key, value in my_dict.items():
        sum_value = sum(value)
        my_dict[key] = [round(elem / sum_value, 3) for elem in value]

    # Додаток до нормалізації, щоб наступний крок працював хоч якось
    for key, value in my_dict.items():
        if sum(value) != 1:
            index = len(value) - 1
            while index >= 0 and value[index] == 0:
                index -= 1
            if index >= 0:
                value[index] += 1 - sum(value)
                value[index] = round(value[index], 3)
            my_dict[key] = value
    return my_dict


def transition_matrix(my_dict):
    keys = list(my_dict.keys())
    my_df = pd.DataFrame(data=my_dict, index=keys)
    my_df = my_df.transpose()
    return my_df


def markov_chain_first_order(my_df, notes_quantity):
    melody_sim = []
    melody_sim.append(my_df.iloc[0].index[5])
    note = np.random.choice(my_df.iloc[0].index, p=my_df.iloc[0])
    while len(melody_sim) < notes_quantity:
        note = np.random.choice(my_df.iloc[my_df.index.get_loc(note)].index, p=my_df.iloc[my_df.index.get_loc(note)])
        melody_sim.append(note)
    return melody_sim


def get_track(melody_sim):
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    tempo = 120
    mytempo = bpm2tempo(tempo)
    track.append(MetaMessage('set_tempo', tempo=mytempo, time=0))
    track.append(Message('program_change', program=0, time=0))
    track.append(MetaMessage('time_signature', numerator=4, denominator=4, notated_32nd_notes_per_beat=8))

    for i in range(len(melody_sim)):
        track.append(Message('note_on', note=melody_sim[i], velocity=80, time=120))
        track.append(Message('note_off', note=melody_sim[i], velocity=80, time=120))

    mid.save('first_order.mid')
    print('New song was generated!')


def filter_query():
    query = '''Select * from melody'''
    return query


def generate_melody_1_order(melody_length):
    (get_track(markov_chain_first_order(transition_matrix(normalization(dict_creation
                                       (data_for_transition_matrix(connection_to_DB(),
                                            filter_query())))), melody_length)))


generate_melody_1_order(100)