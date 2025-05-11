import json


with open("greek.json", "r") as f:
    data = json.load(f)

sequences = []

shift = data[0]
base = data[1]

for key in shift:
    sequences.append(f"<{key.upper()}> : \"{shift[key]}\"")

for key in base:
    sequences.append(f"<dead_horn> <{key}> : \"{base[key]}\"")

print("\n".join(sequences))

