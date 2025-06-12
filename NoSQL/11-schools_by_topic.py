#!/usr/bin/env python3
"""
Module with a function to find schools by a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection: A PyMongo collection object.
        topic (str): The topic to search for.

    Returns:
        A list of school documents that include the specified topic.
        Returns an empty list if no schools match the topic.
    """
    query_filter = {"topics": topic}
    schools = mongo_collection.find(query_filter)
    return list(schools)
