import json


with open("maths.json", "r") as f:
    data = json.load(f)

sequences = []

shift = data[0]
base = data[1]

for key in shift:
    sequences.append(f"<dead_ringabove> <{key.upper()}> : \"{shift[key]}\"")

for key in base:
    sequences.append(f"<dead_ringabove> <{key}> : \"{base[key]}\"")

print("\n".join(sequences))

