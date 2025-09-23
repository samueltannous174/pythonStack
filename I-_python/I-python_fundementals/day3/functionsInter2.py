# 2


x = [[5,2,3], [10,8,9]]
x[1][0] = 15
print("Updated x:", x)

students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print("Updated students:", students)


sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print("Updated sports_directory:", sports_directory)



z = [{'x': 10, 'y': 20}]
z[0]['y'] = 30
print("Updated z:", z)



# 3

def iterateThroughList(list):
    for item in list:
        print(item)


# 4

def iterateDictionary(list):
    for item in list:
        output = []
        for key, value in item.items():
            output.append(f"{key} - {value}")
        print(", ".join(output))        




students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary(students)

# 5

def get_values_from_dict(list):
    values_list = []
    for item in list:                         
        for key, value in item.items():
            values_list.append(f" {value}")
    print(", ".join(values_list))

 


print(get_values_from_dict(students))

# 6
def iterateDictionary2(key_name, list):
    for item in list:
        if key_name in item:
            print(item[key_name])

print("First names:")
iterateDictionary2('first_name', students)

print("\nLast names:")

iterateDictionary2('last_name', students)


# 7 8

def printInfo(some_dict):
    for key, values in some_dict.items():
        print(f"{len(values)} {key}")
        for value in values:
            print(value)
        print()



dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
    }


print("printInfo output:")
printInfo(dojo)



