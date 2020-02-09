# Try It Yourself Exercise - Pg.46
# 3-10 Use every function learnt in chapter 3
countries = ['japan', 'canada', 'new zealand', 'russia']
print(countries)
print(f"I really want to visit {countries[0].title()}!")
print(f"I wouldn't mind seeing {countries[-1].title()} though")
countries[2] = 'england'
print(countries)
countries.append('china')
countries.append('america')
print(countries)
countries.insert(2, 'sweden')
print(countries)
del countries[5]
print(countries)
least_interested = countries.pop()
print(f"I'm least interested in visiting {least_interested.title()}")
print(countries)
pricey = 'england'
countries.remove(pricey)
print(f"Visiting {pricey.title()} is probably too expensive at the moment")
print(countries)
print(f"Countries left to choose from are:\n{sorted(countries)}")
no_reason = 'sweden'
countries.remove(no_reason)
print(f"I don't really have a reason to visit {no_reason.title()}")
countries.sort(reverse=True)
print(f"The final {len(countries)} countries to choose from are:\n{countries}")