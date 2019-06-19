places_to_visit = ['canada', 'argentina', 'italy', 'spain', 'croatia', 'germany']
print(places_to_visit)

# Temporary changes to list
print(sorted(places_to_visit))
print(places_to_visit)

print(sorted(places_to_visit, reverse=True)) # Varibale is always the first argument
print(places_to_visit)

# Permanent changes to list and back again
places_to_visit.reverse()
print(places_to_visit)
places_to_visit.reverse()
print(places_to_visit)

# Permanent sorting of list alphabetically and then reversed
places_to_visit.sort()
print(places_to_visit)
places_to_visit.sort(reverse=True)
print(places_to_visit)