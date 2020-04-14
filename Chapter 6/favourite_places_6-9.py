# Try It Yourself Exercise - Pg.112
# 6-9 Favourite Places
########################################################################################################################
# Make a dictionary called favourite_places
# Think of three names to store as keys in the dictionary
# Store one-three favourite places for each person
########################################################################################################################

favourite_places = {
    'brock': ['indoor center', 'rock climbing gym', 'home'],
    'carl': ['park', 'home'],
    'emily': ['art studio'],
}

for name, places in favourite_places.items():
    if len(places) > 1:
        print(f"\n{name.title()}'s favourite places are:")
        for place in places:
            print(f"\t{place.title()}")
    else:
        print(f"\n{name.title()}'s favourite place is:")
        for place in places:
            print(f"\t{place.title()}")