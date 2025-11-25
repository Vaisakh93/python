

from datetime import datetime
import json

def get_trip(city, date_str, comment):
    """
    Returns a dictionary containing trip information.
    """
    return {
        "city": city,
        "date": date_str,
        "comment": comment
    }

trips = [
    get_trip("alappuzha", "15-05-2023", "Aleppey Backwater Tour with Kerala Traditional Lunch."),
    get_trip("vagamon", "02-11-2023", "The cool and pleasant climate is a major draw for tourists."),
    get_trip("trivandrum", "28-08-2024", "The city offers a mix of landscapes, with easy access to beaches like Kovalam and Varkala, as well as hill stations like Ponmudi.")
]

for trip in trips:
    date_obj = datetime.strptime(trip["date"], "%d-%m-%Y")
    trip["date"] = date_obj.strftime("%B %d, %Y")

json_output = json.dumps(trips, indent=4)
print(json_output)
