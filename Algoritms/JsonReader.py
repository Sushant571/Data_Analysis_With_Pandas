import json

with open('students.json') as f:
  data = json.load(f)
print(data)
