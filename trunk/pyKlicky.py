from os import path, listdir
from random import randint

class Helper:
    def __init__(self, data='data', img=None, snd=None):
        if path.isdir(data):
            self.data_folder = data
        else:
            raise IOError

        self.img_path = self._check_folder(img, path.join(data, 'img'))
        self.snd_path = self._check_folder(snd, path.join(data, 'snd'))


    def _check_folder(self, p, default):
        if not p:
            p = default

        if path.isdir(p):
            return p
        else:
            raise IOError

    def get_image(self, img_name):
        p = path.join(self.img_path, img_name)
        if path.isfile(p):
            return open(p, 'rb')

    def get_image_list(self):
        return [x for x in listdir(self.img_path) if x.endswith('.png') or x.endswith('.jpg')]

    def get_random_image(self):
        ilist = self.get_image_list()
        img_name = ilist[randint(0, len(ilist) - 1)]
        return path.abspath(path.join(self.img_path, img_name))

    def get_random_word(self):
        return self.extract_word(self.get_random_image())

    def extract_word(self, fn):
        fn = path.basename(fn)
        try:
            return fn[:fn.rindex('.')]
        except ValueError:
            return fn

class History:
    items = []
    position = -1

    def __init__(self):
        pass

    def next(self):
        """
        increments position and returns item
        if there is no next item it raises IndexError
        """
        if self.is_last():
            raise IndexError

        self.position += 1

        return self.current

    def previous(self):
        """
        decrements position and returns item
        if there is no previous item it raises IndexError
        """
        if self.is_first():
            raise IndexError

        self.position -= 1

        return self.current

    def is_first(self):
        return self.position <= 0

    def is_last(self):
        return self.position == len(self.items) - 1

    @property
    def current(self):
        return self.items[self.position]

    def add(self, item, increment=True):
        self.items.append(item)

        if increment:
            self.position += 1

    def remove_all_undone(self):
        """
        removes everything after the current position in history
        """
        self.items = self.items[:self.position + 1]
