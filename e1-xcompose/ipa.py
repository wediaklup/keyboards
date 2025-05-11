import json


with open("ipa.json", "r") as f:
    data = json.load(f)

sequences = []

for second in data:
    number = second[""]
    for first in second:
        if first == "" or second[first] == "":
            continue
        sequences.append(f"<dead_doubleacute> <{first}> <{number}> : \"{second[first]}\"")

print("\n".join(sequences))

