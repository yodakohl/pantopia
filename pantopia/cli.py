import json
import argparse
import sys
from .real_cost import Externalities, real_cost

def load_data(path: str):
    with open(path) as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser(description="Calculate real cost of products")
    parser.add_argument("data", help="JSON file with product data")
    parser.add_argument("--sku", help="Display only the product with this SKU")
    args = parser.parse_args()

    data = load_data(args.data)
    if args.sku:
        data = [item for item in data if item.get("sku") == args.sku]
        if not data:
            print(f"SKU {args.sku} not found", file=sys.stderr)
            return

    for item in data:
        ext = Externalities(**item["externalities"])
        rc = real_cost(item["price"], ext)
        sku = item.get("sku", item.get("id", ""))
        if sku:
            print(f"{sku} {item['name']}: ${rc:.2f} (base ${item['price']:.2f})")
        else:
            print(f"{item['name']}: ${rc:.2f} (base ${item['price']:.2f})")

if __name__ == "__main__":
    main()
