from country import Country, CountryEncoder
import json

# From Python to JSON
belgium = Country("Belgium", 11000000, ["Dutch", "French", "German"])
print(json.dumps(belgium, cls=CountryEncoder))


# From JSON to Python
canada = Country("Canada", 37742154, ["English", "French"])
# Use json.dump() to create a JSON file in writing mode
with open('canada.json','w') as f:
    json.dump(canada,f, cls=CountryEncoder)