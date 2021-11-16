"""
1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
2. Change the last_name of the first student from 'Jordan' to 'Bryant'
3. In the sports_directory, change 'Messi' to 'Andres'
4. Change the value 20 in z to 30
"""

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

#1.
x[1][0] = 15
print(x)

#2.
students[0]["last_name"] = "Bryant"
print(students)

#3.
sports_directory["soccer"][0] = "Andres"
print(sports_directory)

#4.
z[0]["y"] = 30
print(z)


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):    
    for student in some_list:
        print("first_name" + " - " + student["first_name"] + ", " + "last_name" + " - " + student["last_name"])
iterateDictionary(students)

def iterateDictionary2(key_name, some_list):    
    for student in some_list:
        print(student[key_name])
iterateDictionary2("first_name", students)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dictionary):
    for key in some_dictionary:
        print("\n" + str(len(some_dictionary[key])) + " " + "LOCATIONS")
        for item in some_dictionary[key]:
            print(item)
printInfo(dojo)
