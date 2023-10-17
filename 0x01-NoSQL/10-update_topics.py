#!/usr/bin/env python3
"""
module: 10-update_topics
"""


def update_topics(mongo_collection, name, topics):
    """
    Python function that changes all topics of a school document
    based on the name
    """
    if mongo_collection is not None:
        mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
        )
