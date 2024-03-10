relative = ['Kring', 'Apol', 'Jotik']
age = [44, 72, 46]

# combine into 1 list
combined_list = zip(relative, age)

print(list(combined_list))

# convert to dictionary
relative_age = dict(zip(relative, age))
print(relative_age)