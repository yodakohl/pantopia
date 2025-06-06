# Pantopia

This repository contains a small proof-of-concept for calculating the "real cost"
of products. Each product's real cost is its base price plus a surcharge for
externalities like carbon footprint or resource depletion.

## Usage

1. Prepare a JSON file describing your products. Each entry should include a
   globally unique `sku` along with a short `description` and `origin` field.
   A sample file named `sample_data.json` is included:

```json
[
  {
    "sku": "11111111-1111-1111-1111-111111111111",
    "name": "Widget",
    "description": "A standard widget",
    "origin": "USA",
    "price": 10.0,
    "externalities": {
      "carbon": 1.0,
      "labor": 0.5,
      "resources": 0.25,
      "waste": 0.25
    }
  }
]
```

2. Run the CLI to calculate real costs:

```bash
python -m pantopia.cli sample_data.json
```

You can also display the cost for a single SKU:

```bash
python -m pantopia.cli sample_data.json --sku 11111111-1111-1111-1111-111111111111
```

## Testing

Run the unit tests with:

```bash
pytest
```
