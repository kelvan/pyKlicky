from pygame import mixer, error
from settings import Sounds, Folder
from os import path

class Sound:
    sounds = {}

    def __init__(self):
        mixer.init()
        if Sounds.enabled:
            self.sounds['correct'] = self._get_sound(Sounds.correct)
            self.sounds['incorrect'] = self._get_sound(Sounds.incorrect)

    def _get_sound(self, f):
        return mixer.Sound(path.join(Folder.sound, f))

    def play_correct(self):
        self.sounds['correct'].play()

    def play_incorrect(self):
        self.sounds['incorrect'].play()

    def spell(self, word):
        fn = path.join(Folder.spell, '%s.wav' % word[0].lower())
        mixer.music.load(fn)
        for letter in word[1:]:
            fn = path.join(Folder.spell, '%s.wav' % letter.lower())
            try:
                mixer.music.queue(fn)
            except error:
                print 'missing letter:', letter
        mixer.music.play()

    def read_word(self, word):
        self._get_sound('%s.wav' % word).play()
