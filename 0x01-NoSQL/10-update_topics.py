#!/usr/bin/env python3
"""
change school topic
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    update many rows
    """
    return mongo_collection.update(
        {"name": name},
        {"$set": {"topics": topics}},
        {"multi": "true"}
    )
