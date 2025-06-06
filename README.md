# Pantopia

This repository contains a small proof-of-concept for calculating the "real cost"
of products. Each product's real cost is its base price plus a surcharge for
externalities like carbon footprint or resource depletion.

## Usage

1. Prepare a JSON file describing your products. A sample file named
   `sample_data.json` is included:

```json
[
  {
    "name": "Widget",
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

## Testing

Run the unit tests with:

```bash
pytest
```
