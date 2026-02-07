people = [
    {"name": "Ola", "age": 22},
    {"name": "Mike", "age": 19},
    {"name": "Ana", "age": 22},
    {"name": "Zoe", "age": 30},
]

print("before:", people)
sorted_people = sorted(people, key=lambda p: p["age"])
print("after:", sorted_people)
