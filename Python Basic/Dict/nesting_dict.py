prefs = {'Lisa Rose': {'Lady in the Water': 3.5, 'Snakes on a Plane': 3.5},
         'Gene Seymour': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0}}

result = {}

for person in prefs:
    for item in prefs[person]:
        result.setdefault(item, {})
        result[item][person] = prefs[person][item]
print(result)
