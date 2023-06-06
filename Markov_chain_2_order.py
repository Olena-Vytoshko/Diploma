import random
from Markov_chain_1_order import *


# Треба буде поміняти
def filter_query():
    query = '''Select * from melody'''
    return query


def create_dict(connection_to_DB, filter_query):
    global list_of_lists
    list_of_lists = data_for_transition_matrix(connection_to_DB(), filter_query())
    chain = {}
    for lst in list_of_lists:
        n_notes = len(lst)
        for i, key1 in enumerate(lst):
            if n_notes > i + 2:
                key2 = lst[i + 1]
                note = lst[i + 2]
                if (key1, key2) not in chain:
                    chain[(key1, key2)] = [note]
                else:
                    chain[(key1, key2)].append(note)

    print('Chain size: {0} distinct notes pairs.'.format(len(chain)))
    return chain


def notes_sequence(chain):
    all_notes = sum(list_of_lists, [])
    print(len(all_notes))

    r = random.randint(0, len(all_notes) - 2)
    key = (all_notes[r], all_notes[r + 1])
    melody_sequence = str(key[0]) + ' ' + str(key[1])

    while len(melody_sequence) < 200:
        if key in chain:
            w = random.choice(chain[key])
            melody_sequence += ' ' + str(w)
            key = (key[1], w)
        else:
            break

    print(melody_sequence)
    numbers = [int(num) for num in melody_sequence.split()]
    return numbers


def get_track_2(melody_sim):
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

    mid.save('second_order.mid')
    print('New song was generated!')


# get_track_2(numbers)