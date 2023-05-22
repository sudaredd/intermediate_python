import json

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": ["engineer", "programmer"]
}

personJson = json.dumps(person, indent=4)
print(personJson)

with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)


# convert json string to dictionary
person = json.loads(personJson)
print(person)

# load json file to dictionary
with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)