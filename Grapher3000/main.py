from matplotlib import pyplot as plt
import pandas as pd
import json

with open("config.json", 'r') as env:
    environment = json.load(env)
    input_file = environment['input']

data = pd.read_csv(input_file)

fig = plt.figure(figsize=(10, 7))
result = plt.pie(data["Freq"], labels=data["Word"])
fig.savefig("result")

plt.show()
