import json
import re

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))

txt = "Cursul incepe la ora 8"

a = re.search("^Cursul.*8$", txt)

print(a)

y = re.findall("[ora8]", txt)

print(y)

if y:
  print("Da,este adevarat")
else:
  print("Fals,incepe de la 10")