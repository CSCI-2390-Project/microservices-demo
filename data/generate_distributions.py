import json
import pandas
import os
import matplotlib.pyplot as plt
from textwrap import wrap


ops = {}

for _, _, files in os.walk('.'):
    for name in files:
        if name.endswith('.json'):
            with open(name, "r+") as f:
                content = json.load(f)
                for trace in content["data"]:
                    for span in trace["spans"]:
                        operation = "".join(x if x.isalnum() else "_" for x in span["operationName"])
                        # in milliseconds
                        ops[operation] = ops.get(operation, []) + [span["duration"] * 0.001]

for operation, durations in ops.items():
    durations = pandas.Series(durations).sort_values()
    indices = [index / len(durations) for index in range(len(durations))]
    plt.title("\n".join(wrap(f"Latency Distribution of Operation {operation}", 60)))
    plt.xlabel("Percentile")
    plt.ylabel("Time (milliseconds)")
    plt.fill_between(indices, durations.values)
    plt.savefig(f"{operation}.png", format="png")
    plt.clf()