# CRUD Python Module for the Austin Animal Center Database

from pymongo import MongoClient
from pymongo.errors import PyMongoError


class AnimalShelter(object):
    """CRUD operations for the Animal collection in MongoDB."""

    def __init__(self, username, password):
        """Initialize authenticated connection to MongoDB."""

        self.client = MongoClient(
            "mongodb://localhost:27017",
            username=username,
            password=password,
            authSource="admin",
            serverSelectionTimeoutMS=5000
        )

        # Force MongoDB authentication immediately
        self.client.admin.command("ping")

        self.database = self.client["aac"]
        self.collection = self.database["animals"]

    def create(self, data):
        """Insert a document into the animals collection."""

        if not isinstance(data, dict) or not data:
            return False

        try:
            result = self.collection.insert_one(data)
            return result.inserted_id is not None

        except PyMongoError as error:
            print("Create operation failed:", error)
            return False

    def read(self, query):
        """Return documents matching the query."""

        if not isinstance(query, dict):
            return []

        return list(self.collection.find(query))

    def update(self, query, new_values):
        """Update documents matching the query."""

        if not isinstance(query, dict):
            return 0

        if not isinstance(new_values, dict):
            return 0

        if not query or not new_values:
            return 0

        try:
            result = self.collection.update_many(
                query,
                {"$set": new_values}
            )

            return result.modified_count

        except PyMongoError as error:
            print("Update operation failed:", error)
            return 0

    def delete(self, query):
        """Delete documents matching the query."""

        if not isinstance(query, dict) or not query:
            return 0

        try:
            result = self.collection.delete_many(query)
            return result.deleted_count

        except PyMongoError as error:
            print("Delete operation failed:", error)
            return 0