import os
import mido
import random
import midi
import music21
import pygame


# Зчитування послідовності нот одного файлу
# midi_file = mido.MidiFile('Accept - 01.mid')
# notes = []
#
# for message in midi_file.play():
#     if message.type == 'note_on':
#         notes.append(message.note)
#
# print(notes)


# # Зчитування кожного midi файлу з папки
# folder_path = "C:/Users/olena/OneDrive/Pulpit/midi_examples"
#
# list_of_lists = []
#
# for filename in os.listdir(folder_path):
#     if filename.endswith('.mid'):
#         midi_file = mido.MidiFile(os.path.join(folder_path, filename))
#         notes = []
#         for message in midi_file.play():
#             if message.type == 'note_on':
#                 notes.append(message.note)
# #                list_of_lists.append(notes)
#         print(f'Notes in {filename}: {notes}')
# print(list_of_lists)


# Спроба створити словник з ключами кортежами з трьох нот і значеннями четвертих нот - невдала спроба
# order = 3
# dictionary = {}
#
# for i in notes:
#     while len(notes) > order:
#         key = (notes[0], notes[1], notes[2])
#         value = (notes[3])
#         dictionary[key] = value
#         del notes[0]
# print(dictionary)


# # Список, в який додаватимуться рандомні числа від 0 до 1 для визначення станів
# random_states = []
#
# # Відкривання MIDI-файлу
# mid = mido.MidiFile('Accept - 01.mid')
#
# # Виведення кількості треків
# print("Кількість треків у MIDI-файлі:", len(mid.tracks)) # у файлі 2 треки (як і у всіх решта)


# # Функція, яка зчитує послідовність нот у файлі
# def read_notes(midi_file):
#     notes_from_file = []
#     for i, track in enumerate(mid.tracks):
#         for message in track:
#             if message.type == 'note_on':
#                 notes_from_file.append(message.note)
#     # for message in midi_file.play(): # це чомусь дуже довго працює
#     #     if message.type == 'note_on':
#     #         notes.append(message.note)
#     # print("Ноти: ", notes)
#     return notes_from_file

# print(read_notes(mid))

# Мелодія довжиною N має N-3 переходи
# def melody_creation(notes, melody_length):


import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow
from PyQt5.uic import loadUi


class MusicPlayer(QMainWindow):
    def __init__(self):
        super(MusicPlayer, self).__init__()
        loadUi('music_player.ui', self)

        self.mediaPlayer = QMediaPlayer(self)

        self.playButton.clicked.connect(self.play)
        self.stopButton.clicked.connect(self.stop)
        self.pauseButton.clicked.connect(self.pause)
        self.volumeSlider.valueChanged.connect(self.set_volume)
        self.positionSlider.sliderMoved.connect(self.set_position)
        self.mediaPlayer.positionChanged.connect(self.update_position)
        self.mediaPlayer.durationChanged.connect(self.update_duration)

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            return
        if self.mediaPlayer.state() == QMediaPlayer.PausedState:
            self.mediaPlayer.play()
            return

        file_name, _ = QFileDialog.getOpenFileName(self, "Open File")
        if file_name != '':
            self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(file_name)))
            self.mediaPlayer.play()

    def stop(self):
        self.mediaPlayer.stop()

    def pause(self):
        self.mediaPlayer.pause()

    def set_volume(self, value):
        self.mediaPlayer.setVolume(value)

    def set_position(self, position):
        self.mediaPlayer.setPosition(position)

    def update_position(self, position):
        self.positionSlider.setValue(position)

    def update_duration(self, duration):
        self.positionSlider.setMaximum(duration)


if __name__ == '__main__':
    app = QApplication(sys.argv)



