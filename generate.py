import numpy as np
import random
from mido import MidiFile, MetaMessage, bpm2tempo, Message, MidiTrack


tempo1 = np.array([ 0, 240, 240, 240, 240, 240, 240, 240 ])
tempo2 = np.array([ 0, 480, 240, 240, 480, 120, 120, 240 ])
tempo3 = np.array([ 0, 120, 120, 120, 120, 120, 240, 240 ])
tempo4 = np.array([ 0, 720, 360, 360, 240, 120, 240, 240 ])
tempos = np.array([tempo1, tempo2, tempo3, tempo4])
pause = [ 120, 240, 480, 180, 360 ]


mid = MidiFile(type=0)
track = MidiTrack()
track.name = 'track 007'
mid.tracks.append(track)

tempo = 120
cur_instrum= 2
random.seed()

notes_generated = [ 60, 60, 62, 64, 62, 64, 69, 71, 72, 67, 64, 65, 64, 65, 62, 64, 62, 64, 65, 64, 69, 60, 60, 60, 62, 64, 62, 64, 69, 71, 72, 67, 64, 65, 64, 65, 62, 64, 62, 64, 65, 64, 69, 60 ]

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


mid.save('test.mid')