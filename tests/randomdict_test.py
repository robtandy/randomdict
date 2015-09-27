from randomdict import RandomDict
from nose.tools import raises

def test_init_with_update():
    r = RandomDict({'a':1})
    assert 'a' in r

def test_len():
    r = RandomDict({'a':1})
    assert len(r) == 1

def test_delete():
    r = RandomDict({'a':1})
    del r['a']
    assert len(r) == 0

@raises(KeyError)
def test_delete_missing():
    r = RandomDict({'a':1})
    del r['b']

def test_many_inserts_deletes():
    r = RandomDict()
    for i in range(10000):
        r[i] = 1
    for i in range(10000):
        del r[i]
    assert len(r) == 0

def test_random_value():
    r = RandomDict()
    for i in range(10000):
        r[i] = i

    values = set(range(10000))
    for i in range(100000):
        assert r.random_value() in values

def test_random_key():
    import string

    r = RandomDict()
    for k in string.ascii_lowercase:
        r[k] = 1
    keyset = set(string.ascii_lowercase)

    while len(r) > 0:
        k = r.random_key()
        assert k in keyset
        del r[k]

def test_random_item():
    import string

    r = RandomDict()
    for k in string.ascii_lowercase:
        r[k] = 1
    keyset = set(string.ascii_lowercase)

    while len(r) > 0:
        k,v = r.random_item()
        assert k in keyset
        assert v == 1
        del r[k]

@raises(KeyError)
def test_empty_random_key():
    r = RandomDict()
    r.random_key()

@raises(KeyError)
def test_empty_random_value():
    r = RandomDict()
    r.random_value()

@raises(KeyError)
def test_empty_random_item():
    r = RandomDict()
    r.random_item()
