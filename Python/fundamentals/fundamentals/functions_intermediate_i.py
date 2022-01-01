
# 1. Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)

students[0]["last_name"] = "Bryant"
print(students)

sports_directory["soccer"][0] = "Andres"
print(sports_directory)

z[0]["y"] = 30
print (z)

# 2. Iterate Through a List of Dictionaries

def iterateDictionary(some_list):
    for x in range (0, len(some_list)):
        # for key in some_list[x]:
        print ((list(some_list[x])[0]) + " - " +  some_list[x]["first_name"] + ", " + (list(some_list[x])[1]) + " - " +  some_list[x]["last_name"])
            # print(some_list[x][key] + some_list[x]["first_name"] + ", " + some_list[x]["last_name"])

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary(students) 

# 3. Get Values From a List of Dictionaries

def iterateDictionary2 (key_name, some_list):
    for x in range (0, len(some_list)):
        print(some_list[x][key_name])

iterateDictionary2("first_name", students)
iterateDictionary2("last_name", students)


# 4. Get Values From a List of Dictionaries

def printInfo(dojo):
    for key in dojo:
        print (len(dojo[key]), key.upper())
        for x in range (0, len(dojo[key])):
            print (dojo[key][x])
        print (" ")

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)