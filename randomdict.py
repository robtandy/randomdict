from collections import MutableMapping
import random

__version__ = '0.2.0'

class RandomDict(MutableMapping):
    def __init__(self, *args, **kwargs):
        """ Create RandomDict object with contents specified by arguments.
        Any argument
        :param *args:       dictionaries whose contents get added to this dict
        :param **kwargs:    key, value pairs will be added to this dict
        """
        # mapping of keys to array positions
        self.keys = {}
        self.values = []
        self.last_index = -1

        self.update(*args, **kwargs)

    def __setitem__(self, key, val):
        if key in self.keys:
            i = self.keys[key]
        else:
            self.last_index += 1
            i = self.last_index

        self.values.append((key, val))
        self.keys[key] = i
    
    def __delitem__(self, key):
        if not key in self.keys:
            raise KeyError

        # index of item to delete is i
        i = self.keys[key]
        # last item in values array is
        move_key, move_val = self.values.pop()

        if i != self.last_index:
            # we move the last item into its location
            self.values[i] = (move_key, move_val)
            self.keys[move_key] = i
        # else it was the last item and we just throw
        # it away

        # shorten array of values
        self.last_index -= 1
        # remove deleted key
        del self.keys[key]
    
    def __getitem__(self, key):
        if not key in self.keys:
            raise KeyError

        i = self.keys[key]
        return self.values[i][1]

    def __iter__(self):
        return iter(self.keys)

    def __len__(self):
        return self.last_index + 1

    def random_key(self):
        """ Return a random key from this dictionary in O(1) time """
        if len(self) == 0:
            raise KeyError("RandomDict is empty")
        
        i = random.randint(0, self.last_index)
        return self.values[i][0]

    def random_value(self):
        """ Return a random value from this dictionary in O(1) time """
        return self[self.random_key()]

    def random_item(self):
        """ Return a random key-value pair from this dictionary in O(1) time """
        k = self.random_key()
        return k, self[k]
