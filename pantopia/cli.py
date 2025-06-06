import json
import argparse
import sys
from .real_cost import real_cost
from .product import Product

def load_data(path: str):
    """Load product data from JSON and return a list of ``Product`` objects."""
    with open(path) as f:
        raw = json.load(f)
    return [Product.from_dict(item) for item in raw]

def main():
    parser = argparse.ArgumentParser(description="Calculate real cost of products")
    parser.add_argument("data", help="JSON file with product data")
    parser.add_argument("--sku", help="Display only the product with this SKU")
    args = parser.parse_args()

    data = load_data(args.data)
    if args.sku:
        data = [item for item in data if item.sku == args.sku]
        if not data:
            print(f"SKU {args.sku} not found", file=sys.stderr)
            return

    for item in data:
        rc = real_cost(item.price, item.externalities)
        print(f"{item.sku} {item.name}: ${rc:.2f} (base ${item.price:.2f})")

if __name__ == "__main__":
    main()
