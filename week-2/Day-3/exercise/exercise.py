
#Exercise 1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = dict(zip(keys,values))
print(result)

#Exercise 2
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# ticket_price = {'free: 0','child:10','adult:15'}
total_cost = 0

for members,age in family.items():
  if age < 3:
      total_cost += 0
      cost = 0
  elif  3 <= age <= 12:
      total_cost += 10
      cost = 10
  else:
    total_cost += 15
    cost = 15
  print(f"{members} has to pay {cost}")
  # total_cost = total_cost + cost # or total_cost += cost
print(f"Your total cost is: ${total_cost}")

#Exercise 3
brand = {
  'name': 'Zara' ,
  'creation_date': 1975 ,
  'creator_name': 'Amancio Ortega Gaona', 
  'type_of_clothes': ['men', 'women', 'children', 'home'], 
  'international_competitors': ['Gap', 'H&M', 'Benetton'], 
  'number_stores': 7000 ,
  'major_color': {
  'France':['blue'], 
  'Spain': ['red'], 
  'US': ['pink', 'green']
  }
}
brand['number_stores'] = 2
client = ", ".join(brand["type_of_clothes"])
print(f"Zara clients are {client }.")
brand['contry_creation'] = "Spain"
print(brand)
if 'international_competitors' in brand:
  brand['international_competitors'].append('Desigual')
del brand['creation_date']
print(brand['international_competitors'][2])
color = ', '.join(brand['major_color']['US'])
print(f"The major colors are: {color}")
print(brand)
lengtOfDict = len(brand)
print("Number of key-value pairs in the dictionary:", lengtOfDict)
lenOfKeys = list(brand.keys())
print(f"This is the lenght of keys: {lenOfKeys}")
more_on_zara = {}
ze_keys = [['creation_date', 1975], ['number_stores', '10000']]
for i in range(len(ze_keys)):
	if ze_keys[i][0] in more_on_zara:
		more_on_zara[ze_keys[i][0]].append(ze_keys[i][1])
	else:
		more_on_zara[ze_keys[i][0]]= []
		more_on_zara[ze_keys[i][0]].append(ze_keys[i][1])
print(more_on_zara)
brand.update(more_on_zara)
print(brand)
stores = ", ".join(brand['number_stores'])
print(f"number of stores are: {stores }.")

#exercise 4
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

disney_users = []
for index in users:
  disney = int(input("Enter disney users: "))
  disney_users.append(disney)
disney_users_A = zip(users,disney_users)
print(dict(disney_users_A))
