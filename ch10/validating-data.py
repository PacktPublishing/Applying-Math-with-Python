import csv
import cerberus

schema = {"rows": {
    "type": "list",
    "schema": {
            "type": "dict",
            "schema": {
                "id": {"type": "string"},
                "number": {"type": "integer", "coerce": int},
                "lower": {"type": "float", "coerce": float, "min": -1.0, "max": 1.0},
                "upper": {"type": "float", "coerce": float, "min": -1.0, "max": 1.0},
            }
        }
    }
}


validator = cerberus.Validator(schema)


with open("sample.csv") as f:
    dr = csv.DictReader(f)
    document = {"rows": list(dr)}


validator.validate(document)

errors = validator.errors["rows"][0]

for row_n, errs in errors.items():
    print(f"row {row_n}: {errs}")

