#!/usr/bin/env python3
""" a Python script that provides some
stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx
    total_doc = nginx.count_documents({})
    get = nginx.count_documents({"method": {"$eq": "GET"}})
    post = nginx.count_documents({"method": {"$eq": "POST"}})
    put = nginx.count_documents({"method": {"$eq": "PUT"}})
    patch = nginx.count_documents({"method": {"$eq": "PATCH"}})
    delete = nginx.count_documents({"method": {"$eq": "DELETE"}})
    both = nginx.count_documents({"$and": [
                                          {"method": {"$eq": "GET"}},
                                          {"path": {"$eq": "/status"}}
                                          ]})
    print('{} logs'.format(total_doc))
    print("Methods:")
    print('\tmethod GET: {}'.format(get))
    print('\tmethod POST: {}'.format(post))
    print('\tmethod PUT: {}'.format(put))
    print('\tmethod PATCH: {}'.format(patch))
    print('\tmethod DELETE: {}'.format(delete))
    print('{} status check'.format(both))
