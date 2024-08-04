my_biodata = {'name': ' thejaswi',
              'age':18,
              'plcae': 'puttur',
              'place':'kabaka'}
print(type(my_biodata))
#Acces the value from a dictionary
print(my_biodata['name'])

my_biodata['name'] = 'govinda'
my_biodata['details'] = 'thejaswi_govind'
print(my_biodata)


#Access the item using key which has two methods
value = my_biodata.get('name')
print(value)


print(my_biodata.keys())
print(my_biodata.values())
print(my_biodata.items())

# Update the item of dictionary
my_biodata.update({'place' : 'Mangalore'})
print(my_biodata)

