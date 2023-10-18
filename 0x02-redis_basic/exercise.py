#!/usr/bin/env python3
"""
module: exercise.py
"""
from typing import Union
import redis
import uuid


class Cache:
    """ Cache class """
    def __init__(self):
        """ constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store method """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    datatypes = Union[str, bytes, int, float]

    def get(self, key: str, fn: callable = None) -> datatypes:
        """ get method """
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
