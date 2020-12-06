import requests
import matplotlib.pyplot as plt
import json
import pandas

domain = "104.196.179.170/"
address = f'http://{domain}/api/traces'

operations = {
    "Recv./": "recv_home_page",
    "Recv./cart": "recv_cart",
    "Recv./cart/checkout": "recv_cart_checkout", 
    "Recv./product/0PUK6V6EV0": "recv_product_0PUK6V6EV0",
    "Recv./setCurrency": "recv_setCurrency",
    "Recv./product/L9ECAV7KIM": "recv_product_L9ECAV7KIM",
}

def get_all(operation_name):
    filename = operations[operation_name]
    payload = {"limit": 1000, "lookback": "1h", "operation": operation_name, "service": "frontend"}
    #import pdb;pdb.set_trace()
    results = requests.get(address, params=payload).json()
    with open(f'data/full_trace_{filename}.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
    lengths = [[r["duration"] / 1000 for r in result["spans"] if len(r["references"]) == 0][0] for result in results["data"]] # in microseconds
    series = pandas.Series(lengths)
    print(filename)
    print(series.describe())
    series.to_csv(f"data/durations_recorded_by_jaegar_{filename}.csv")

for operation in operations:
    get_all(operation)