#!/usr/bin/env python3

""" list all documents in a collection """


from pymongo import MongoClient


def list_all(mongo_collection):
    """ lists all docs in mongo_colleciont """
    documents = list(mongo_collection.find())
    return (documents if documents else [])
