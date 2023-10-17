#!/usr/bin/env python3
"""
module: 9-insert_school
"""


def insert_school(mongo_collection, **kwargs):
    """
    function: insert a document into a collection
    """
    if mongo_collection is not None:
        inserted = mongo_collection.insert_one(kwargs)
        return inserted.inserted_id
