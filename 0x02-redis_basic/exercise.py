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


class Cache:
    """ Cache class """
    def __init__(self):
        """ constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
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
