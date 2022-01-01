num1 = 42 #variable declaration
num2 = 2.3 #number data type
boolean = True #boolean data type
string = 'Hello World' #string data type
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #initialize list data type
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #initialize dictionary data type
fruit = ('blueberry', 'strawberry', 'banana') #initialize tuple data type
print(type(fruit)) #type check
print(pizza_toppings[1]) #access list value
pizza_toppings.append('Mushrooms') #add list value
print(person['name']) #access dictionary value
person['name'] = 'George' #change dictionary value
person['eye_color'] = 'blue' #add dictionary value
print(fruit[2]) #access tuple value

if num1 > 45: #if
    print("It's greater")
else:
    print("It's lower")

if len(string) < 5: #length check
    print("It's a short word!")
elif len(string) > 15: #else if
    print("It's a long word!")
else: #else
    print("Just right!")

for x in range(5): #NameError: name <variable name> is not defined
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3): #increment for loop
    print(x)
x = 0
while(x < 5): #start while loop, end while loop
    print(x) 
    x += 1 #increment while loop

pizza_toppings.pop()
pizza_toppings.pop(1) #delete list value

print(person)
person.pop('eye_color') #delete dictionary value
print(person) 

for topping in pizza_toppings: #start for loop
    if topping == 'Pepperoni':
        continue #continue for loop
    print('After 1st if statement')
    if topping == 'Olives':
        break #break for loop, end for loop

def print_hello_ten_times(): #function
    for num in range(10):
        print('Hello') #log statement

print_hello_ten_times() # function return

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): #function parameter
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4) #function argument


"""
Bonus section #multiline comment
"""

# print(num3) NameError: name <variable name> is not defined
# num3 = 72 #single line comments
# fruit[0] = 'cranberry' #TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) #KeyError: 'favorite_team'
# print(pizza_toppings[7]) #IndexError: list index out of range
#   print(boolean) #IndentationError: unexpected indent
# fruit.append('raspberry') #AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) #AttributeError: 'tuple' object has no attribute 'pop'