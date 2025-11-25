

def create_record(city, comment, date_str):
    """
    Returns a travel record as a dictionary.
    city: string
    comment: string
    date_str: string in the format "dd-mm-yyyy"
    """
    return {
        "city": city,
        "comment": comment,
        "date": date_str
    }


import json
from datetime import datetime

records = [
    create_record("Munnar", "Known for its tea plantations and scenic beauty", "05-06-2022"),
    create_record("Kumarakom", "A popular destination on the Vembanad Lake, known for its bird sanctuary", "12-04-2023"),
    create_record("Marari Beach", "A peaceful and less crowded beach destination", "20-09-2021")
]

for record in records:
    original_date = datetime.strptime(record["date"], "%d-%m-%Y")
    record["date"] = original_date.strftime("%B %d, %Y")

json_string = json.dumps(records, indent=4)
print("JSON Output:")
print(json_string)

parsed_records = json.loads(json_string)

print("\nParsed Records:")
for r in parsed_records:
    print(r)
