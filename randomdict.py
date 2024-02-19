
# From https://stackoverflow.com/a/70870131

try:
    from collections.abc import MutableMapping
except ImportError:
    from collections import MutableMapping

import random

__version__ = '0.2.1'

class RandomDict(MutableMapping):
    def __init__(self, default_factory=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default_factory = default_factory
        self.keys = {}
        self.values = []
        self.last_index = -1

    def __setitem__(self, key, val):
        i = self.keys.get(key, -1)
        if i > -1:
            self.values[i] = (key, val)
        else:
            self.last_index += 1
            i = self.last_index
            self.values.append((key, val))
            self.keys[key] = i
    
    def __delitem__(self, key):
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
        if key not in self.keys:
            if self.default_factory is None:
                raise KeyError(key)
            self[key] = self.default_factory()
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

def replace_dicts():
    # Replace dict with RandomDict
    import builtins
    builtins.dict = RandomDict

    # Replace defaultdict with RandomDict

    # stash the original import for use in a custom importer
    _original_import = builtins.__import__

    def _custom_import(name, globals=None, locals=None, fromlist=(), level=0):
        """Intercept imports of defaultdict to route to RandomDict"""
        module = _original_import(name, globals, locals, fromlist, level)
        if name == "collections" or (fromlist and "defaultdict" in fromlist):
            module.__dict__['defaultdict'] = RandomDict
        return module

    # Monkey-patch __import__
    builtins.__import__ = _custom_import
