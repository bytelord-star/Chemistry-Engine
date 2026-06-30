# Chemistry Engine

A modular chemistry engine written in Python.

## Current Features

- Formula parser
- Formula validator
- Element validator
- Molecular mass calculation
- Bond type prediction
- Molecular polarity prediction
- Compound classification
- Acid database
- Compound database

## Project Structure

```
DATA/
models/
scripts/
tools/
```

## Example

``` python
from models.compound.compound_engine import create_compound

compound = create_compound("H2O")

print(compound)
```

## Future

- Base database
- Salt database
- Organic compounds
- Reaction engine
- Balancing equations
- Solubility prediction
- AI assistant