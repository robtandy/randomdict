## RandomDict ##

#### What is it?
Random dict is a dictionary compatible with python's `dict` but with a few methods added to facilitate fast random access of elements.  It inherits from `collections.MutableMapping` so it behaves exactly like a python `dict` once created.

#### Why?
Python's `dict` data structure doesn't provide fast random access to elements.  Existing ways are O(n) scaling, and get slow when the number of elements is large.

If you need to randomly access keys in a python dictionary, you have two choices out of the box:

1. `random.sample(the_dict, 1)` or `random.choice(list(the_dict))` both of these are O(n)
2.  `the_dict.pop()` This is O(1) but returns an arbitrary, rather than strictly random item.  The order of items returned depends on the underlying implentation of the dictionary.

If you need random key access and cannot afford the time penalty of the above methods, then `randomdict` is probably what you are looking for.

#### Installation
`randomdict` works and is tested on python2.6+, python3.1+

`pip install randomdict`

#### How?
```python
    from randomdict import RandomDict
    
    r = RandomDict() # use it just like a regular python dict
    r['a'] = True
    r['b'] = 2

    print r.random_key()
    print r.random_value()
    print r.random_item()
```

#### How slow was getting a random item anyway?
The following timings where done on python 2.7.3 with ipython:
```
    In [24]: r = randomdict.RandomDict()

    In [25]: for i in range(10000000): r[i] = random.random()

    In [26]: %timeit random.sample(r,1)
    10 loops, best of 3: 162 ms per loop

    In [27]: %timeit r.random_key()
    1000000 loops, best of 3: 1.74 µs per loop

``` 


