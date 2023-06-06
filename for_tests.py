import random
import signal
import mido
import numpy as np
import time as tm
import os
import psycopg2
from collections import defaultdict, Counter

# # Підключення до моєї БД
# conn = psycopg2.connect(
#     dbname="MyDB",
#     user="Olena",
#     password="23032002",
#     host="localhost",
#     port="5432"
# )
#
# # Зчитування таблиці Мелодія
# cur = conn.cursor()
# cur.execute("SELECT * FROM Melody")
# rows = cur.fetchall()
# cur.close()
#
# # Сюди я поміщу списки з послідовностями нот з кожного файлу
# list_of_lists = []
#
# # Додаємо кожну зчитану з БД послідовність нот у вигляді списку у список
# for row in rows:
#     list_of_lists.append(eval(row[2]))
# print(list_of_lists)
#
# # # Створимо словник з квартетів і частоти їх зустрічання у наших файлах для одного з 30 списків
# # lst = list_of_lists[0]
# #
# # d = defaultdict(int)
# # for i in range(len(lst) - 3):
# #     key = tuple(lst[i:i + 4])
# #     d[key] += 1
# # new_dict = dict(d.items())
# # print(new_dict)
#
# # Зробимо те саме зі списком списків
# d = defaultdict(int)
# for sublist in list_of_lists:
#     for i in range(len(sublist)-3):
#         key = tuple(sublist[i:i+4])
#         d[key] += 1
#
# result = Counter(d)
# my_dict = dict(result)
# # print(my_dict)
#
# # Упорядкуємо словник у порядку зростання ключів
# sorted_keys = sorted(my_dict.keys())
# sorted_dict = {}
# for key in sorted_keys:
#     sorted_dict[key] = my_dict[key]
# print(sorted_dict)
#
#
# new_list = [tuple(key[:3]) for key in sorted_dict.keys()]
#
# print(len(new_list))
# print(len(set(new_list)))

# def execute_query(conn, query):
#     cur = conn.cursor()
#     cur.execute(query)
#     rows = cur.fetchall()
#     list_of_items = [str(row[0]) for row in rows]
#     cur.close()
#     conn.close()
#     return list_of_items


# # Чомусь не підключається
# db = QSqlDatabase.addDatabase("QPSQL")
#
#
# def db_connection():
#     global db
#     db.setDatabaseName('MyDB')
#     db.setHostName('localhost')
#     db.setUserName('Olena')
#     db.setPassword('23032002')
#     db.setPort(5432)
#     db.open()
#     return db
#
#
# db = db_connection()
#
# query = QSqlQuery(db)
# query.exec_('''SELECT Melody.*
#     FROM Melody
#     JOIN Artist ON Melody.ArtistID = Artist.ArtistID
#     WHERE Artist.ArtistName = 'JP'
#     ''')


import numpy as np
import random

tempo1 = np.array([ 0, 240, 240, 240, 240, 240, 240, 240 ])
tempo2 = np.array([ 0, 480, 240, 240, 480, 120, 120, 240 ])
tempo3 = np.array([ 0, 120, 120, 120, 120, 120, 240, 240 ])
tempo4 = np.array([ 0, 720, 360, 360, 240 ])
tempos = np.array([tempo1, tempo2, tempo3, tempo4])
pause = [ 120, 240, 480, 180, 360 ]

from mido import MidiFile, MetaMessage, bpm2tempo, Message, MidiTrack

mid = MidiFile(type=0)
track = MidiTrack()
track.name = 'track 007'
mid.tracks.append(track)

tempo = 120
cur_instrum= 2
random.seed()

notes_generated = [ 60, 60, 62, 64, 62, 64, 69, 71, 72, 67, 64, 65, 64, 65, 62, 64, 62, 64, 65, 64, 69, 60, 60, 60, 62, 64, 62, 64, 69, 71, 72, 67, 64, 65, 64, 65, 62, 64, 62, 64, 65, 64, 69, 60 ]

print(len(notes_generated))

mytempo = bpm2tempo(tempo)
track.append(MetaMessage('set_tempo', tempo=mytempo, time=0))
track.append(Message('program_change', program=cur_instrum, time=0))
track.append(MetaMessage('time_signature', numerator=4, denominator=4, notated_32nd_notes_per_beat=8))

############ write generated sequence in different tempos #########

cur_num_note = 0
cur_time = 0
max_num_note = len(notes_generated)

while cur_num_note<max_num_note:
    rnd = random.random()
    tempo_template_num = int(rnd*4)
    cur_tempo_template = tempos[tempo_template_num]
    print('cur tempo template # = ', tempo_template_num)
    for j in range(len(cur_tempo_template)):
        if j!=0:
            cur_time = cur_tempo_template[j]
        track.append(Message('note_on', note=notes_generated[cur_num_note], velocity=127, time=cur_time))
        rnd = random.random()
        if abs(rnd-0.5)<=0.45:
            track.append(Message('note_off', note=notes_generated[cur_num_note], velocity=90, time=0))
        else:
            rnd = random.random()
            cur_pause = pause[int(rnd*5)]
            track.append(Message('note_off', note=notes_generated[cur_num_note], velocity=90, time=cur_pause))
        cur_num_note = cur_num_note + 1
        if cur_num_note==max_num_note:
            break


##################################################################

mid.save('test.mid')



