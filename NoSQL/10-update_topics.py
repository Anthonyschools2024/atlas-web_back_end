#!/usr/bin/env python3
"""
Module with a function to update topics for a school document.
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.

    Args:
        mongo_collection: A PyMongo collection object.
        name (str): The school name to update.
        topics (list of str): The list of topics approached in the school.
    """
    query_filter = {"name": name}
    new_values = {"$set": {"topics": topics}}
    
    mongo_collection.update_many(query_filter, new_values)
