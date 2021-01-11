import json

fav_number = float(input("What's your favourite number? "))

filename = 'fav_number.json'
with open(filename, 'w') as f:
    json.dump(fav_number, f)
    print(f"Thank you. We'll store your favourite number {fav_number} for next time.")