import json
import argparse
from .real_cost import Externalities, real_cost

def load_data(path: str):
    with open(path) as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser(description="Calculate real cost of products")
    parser.add_argument("data", help="JSON file with product data")
    args = parser.parse_args()

    data = load_data(args.data)
    for item in data:
        ext = Externalities(**item["externalities"])
        rc = real_cost(item["price"], ext)
        print(f"{item['name']}: ${rc:.2f} (base ${item['price']:.2f})")

if __name__ == "__main__":
    main()
