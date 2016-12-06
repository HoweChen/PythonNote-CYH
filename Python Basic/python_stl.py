from collections import OrderedDict

favourite_languages = OrderedDict()
# so that the dictionary will keep the order with input
favourite_languages['jen'] = 'python'
favourite_languages['sarah'] = 'c'
favourite_languages['edward'] = 'python'
favourite_languages['phil'] = 'ruby'

for key, value in favourite_languages.items():
    print(key + ',' + value)

result = (i for i in range(1, 20))
print(result)
