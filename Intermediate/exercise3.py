flavor = ['vanilla', 'chocolate', 'strawberry', 'cookies n\' cream', 'bubblegum']
toppings = ['almonds', 'banana slices', 'chocolate syrup', 'caramel syrup', 'white chocolate chips']

ice_cream = dict(zip(flavor, toppings))

print(ice_cream)

# Update the value of chocolate to blue berries from banana slices
ice_cream['chocolate'] = 'blueberries'
print(ice_cream)
# Add matcha and ube to the dict
ice_cream.update({'matcha': 'pistachios', 'ube': 'mango slices'})
print(ice_cream)