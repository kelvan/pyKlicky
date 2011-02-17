from os import path

class Folder:
    data = path.join(path.dirname(__file__), '..', 'data')
    sound = path.join(data, 'snd')
    spell = path.join(sound, 'spell')
    images = path.join(data, 'img')

class Sounds:
    enabled = True
    correct = 'correct.wav'
    incorrect = 'incorrect.wav'
