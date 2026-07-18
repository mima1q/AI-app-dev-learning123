student={
    "name":"小明",
    "age":20,
    "score":95

}
print(student["name"])
print(student["age"])
student["grade"]="A"
student["score"]="98"
print(student)
del student["age"]
print(student)
print(student.keys())
print(student.values())
for key,value in student.items():
    print(f"{key}:{value}")