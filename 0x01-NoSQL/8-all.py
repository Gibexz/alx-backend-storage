#!/usr/bin/env python3
"""
module: 8-all
"""


def list_all(mongo_collection):
    """
    function: list all documents in a collection
    """
    if mongo_collection is not None:
        return list(mongo_collection.find({}))
    else:
        return []
