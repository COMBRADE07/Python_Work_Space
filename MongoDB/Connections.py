import pymongo

"""
    creating client:         "mongodb://localhost:27017"
    creating database:       "localdb"
    creating collection:     "collection1"
    insert many rows:         collection1.insert_many(list_of_dict)
    
"""
if __name__ == '__main__':
    # creating client reference
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # creating db reference 'localdb'
    db = client['localdb']

    # creating collections "collection1"
    collection = db['student']

    # inserting document to collection
    document = [
            {"id": 101, "name": "Rhutik", "mark": 80},
            {"id": 102, "name": "Somesh", "mark": 65},
            {"id": 103, "name": "Vikrant", "mark": 70},
            {"id": 104, "name": "Anup", "mark": 95},
            {"id": 105, "name": "Sunil", "mark": 79},
            {"id": 106, "name": "Rajesh", "mark": 98}
    ]

    document1 = {"id": 101, "name": "Rhutik", "mark": 80}
    collection.insert_many(document)
    print("done")
