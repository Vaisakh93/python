
web_dev = ["Rahul", "Sneha", "Arjun"]
data_science = ["Meera", "Kunal", "Rita"]
ui_ux = ["Sam", "Tina", "Neha"]

all_participants = [web_dev, data_science, ui_ux]

web_dev.append("Vikram")

data_science.insert(1, "Pooja")

ui_ux.pop()

data_science_copy = data_science.copy()
data_science.clear()

first_two_web = web_dev[:2]

name_lengths_ds = [len(name) for name in data_science_copy]

is_asha_present = ("Asha" in web_dev or "Asha" in data_science_copy or "Asha" in ui_ux)

first_participants_tuple = (web_dev[0],data_science_copy[0],ui_ux[0])

print("Web Development:", web_dev)
print("Data Science (original cleared):", data_science)
print("Data Science (copied):", data_science_copy)
print("UI/UX Design:", ui_ux)
print("All participants:", all_participants)
print("First two Web Dev:", first_two_web)
print("Name lengths (Data Science copy):", name_lengths_ds)
print("Is Asha present?:", is_asha_present)
print("Tuple of first participants:", first_participants_tuple)
