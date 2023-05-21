from country import Country, CountryEncoder
import json


belgium = Country("Belgium", 11000000, ["Dutch", "French", "German"])
print(json.dumps(belgium, cls=CountryEncoder))
