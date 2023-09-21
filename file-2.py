import pymongo


def main():
    connection_string = "mongodb://localhost:27017/"
    client = pymongo.MongoClient(connection_string)
    aviv_db = client["Aviv's_people"]
    family_collection = aviv_db["family_database"]
    friend_collection = aviv_db["friends_database"]
    army_collection = aviv_db["army_database"]

    family_list = [
        {"name": "mother", "age": 45, "role": "teacher"},
        {"name": "father", "age": 46, "role": "engineer"},
        {"name": "brother", "age": 12, "role": "school"},
        {"name": "sister", "age": 24, "role": "student"},
    ]
    family_collection.insert_many(family_list)  # way 1 to insert to collection

    friends_list = [
        {"name": "Amit", "age": 20, "role": "waiter"},
        {"name": "Yonatan", "age": 24, "role": "doctor"},
        {"name": "Noa", "age": 22, "role": "student"},
        {"name": "Michal", "age": 21, "role": "baker"},
    ]
    for friend in friends_list:
        friend_collection.insert_one(friend)  # way 2 to insert to collection

    army_list = [
        {"id": 1, "name": "Aviv", "age": 20, "role": "Backend"},
        {"id": 2, "name": "Lihi", "age": 21, "role": "QA"},
        {"id": 3, "name": "Gabi", "age": 22, "role": "DevOps"},
        {"id": 4, "name": "Ori", "age": 23, "role": "Frond-end"},
        {"id": 5, "name": "Ido", "age": 22, "role": "developer"},
        {"id": 6, "name": "Yarden", "age": 24, "role": "DevOps"},
    ]
    army_collection.insert_many(army_list)  # way 3 to insert to collection (with id)

    army_collection.delete_one({"name": "Lihi"})  # delete Lihi from the army friends

    for collections_names in aviv_db.list_collection_names():  # print all the database
        for document in aviv_db[collections_names].find():
            print(document)

    #####################################################   file 3    #####################################################
    person = {"role": "DevOps", "age": {"$lt": 23}}
    print(army_collection.find_one(person))
    found_person = army_collection.find_one(person)
    print(found_person["name"])

    found_person_age = found_person["age"]
    update_role = army_collection.find_one(
        {"age": found_person_age, "_id": {"$ne": found_person["_id"]}}
    )
    army_collection.update_one(
        {"_id": found_person["_id"]}, {"$set": {"role": update_role["role"]}}
    )
    print(update_role)

    sort_army_friends = army_collection.aggregate(
        [{"$sort": {"age": -1}}, {"$out": "army"}]
    )

    for army_friend in sort_army_friends:
        print(army_friend)

    release_soldiers = {"age": {"$gt": 23}}
    update_friendship = army_collection.find(release_soldiers)
    friend_collection.insert_many(update_friendship)
    army_collection.delete_many(release_soldiers)


if __name__ == "__main__":
    main()
