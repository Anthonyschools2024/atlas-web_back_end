#!/usr/bin/env python3
"""
Module with a function to list all documents in a MongoDB collection.
"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection: A PyMongo collection object.

    Returns:
        A list of documents from the collection.
        Returns an empty list if no documents are found.
    """
    documents = mongo_collection.find()
    if documents is None:
        return
    return list(documents)
