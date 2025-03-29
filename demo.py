import pyarrow as pa
from pyiceberg.catalog import load_rest
from pyiceberg.expressions import GreaterThanOrEqual
from pyiceberg.schema import Schema
from pyiceberg.types import NestedField, StringType, DoubleType


catalog = load_rest(
    name="rest-catalog",
    conf={
        "uri": "http://localhost:8181/",
        "s3.endpoint": "http://localhost:9000",
        "s3.access-key-id": "admin",
        "s3.secret-access-key": "password",
    },
)

schema = Schema(
    NestedField(1, "city", StringType(), required=False),
    NestedField(2, "lat", DoubleType(), required=False),
    NestedField(3, "long", DoubleType(), required=False),
)
table = catalog.create_table_if_not_exists("default.cities", schema=schema)

df = pa.Table.from_pylist(
    [
        {"city": "Amsterdam", "lat": 52.371807, "long": 4.896029},
        {"city": "San Francisco", "lat": 37.773972, "long": -122.431297},
        {"city": "Drachten", "lat": 53.11254, "long": 6.0989},
        {"city": "Paris", "lat": 48.864716, "long": 2.349014},
    ],
)
table.overwrite(df)

res = table.scan(
    row_filter=GreaterThanOrEqual("lat", 50.0),
    selected_fields=("city",),
).to_arrow()

print("The following cities have a longitude above 50:")
for chunked_array in res:
    for chunk in chunked_array:
        print(f"- {chunk}")
