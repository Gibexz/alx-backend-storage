#!/usr/bin/env python3
"""
module: exercise.py
"""
from typing import Any, Union
import redis
import uuid
from functools import wraps


def count_calls(method: callable) -> callable:
    """
    Tracks the number of calls made to a method in a Cache class.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """
        returns the given method after incrementing its call counter
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: callable) -> callable:
    """
    Stores the history of inputs and outputs for a particular function.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """
        returns the given method and stores its inputs/outputs
        """
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output
    return wrapper


def replay(method: callable) -> None:
    """
    Displays the history of calls of a particular function.
    """
    r = redis.Redis()
    method_name = method.__qualname__
    count = r.get(method_name).decode("utf-8")
    inputs = r.lrange(method_name + ":inputs", 0, -1)
    outputs = r.lrange(method_name + ":outputs", 0, -1)
    print("{} was called {} times:".format(method_name, count))
    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(method_name, i.decode("utf-8"),
                                     o.decode("utf-8")))


class Cache:
    """ Cache class """
    def __init__(self):
        """ constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store method """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    datatypes = Union[str, bytes, int, float]

    def get(self, key: str, fn: callable = None) -> datatypes:
        """
        a get method that take a key string argument and an
        optional Callable argument named fn. This callable will
        be used to convert the data back to the desired format.
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """ get_str method """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """ get_int method """
        return self.get(key, int)
