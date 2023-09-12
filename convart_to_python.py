import json 

to_read = open("Python intermediate/pdf4.quest4.json", "r")
json_to_dict = json.load(to_read)
print(json_to_dict)

json_to_dict ["name"] = "Ari"
json_to_dict ["age"] = 21
json_to_dict ["city"] = "Elad"

to_write = open("Python intermediate/after_running.json", "w")
to_write.write(json.dumps(json_to_dict))

to_write.close()
