#!/usr/bin/env python3
"""
Script to provide some stats about Nginx logs stored in MongoDB.
Database: logs
Collection: nginx
"""
from pymongo import MongoClient


if __name__ == "__main__":
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx

    # 1. Total number of logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # 2. Methods header
    print("Methods:")

    # 3. Count for each HTTP method
    methods =
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # 4. Count for GET requests to /status
    status_check_count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check_count} status check")

    # Close the connection (optional, as MongoClient manages connections,
    # but good practice in some contexts)
    client.close()
