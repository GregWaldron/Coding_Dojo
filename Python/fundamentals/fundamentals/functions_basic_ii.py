def countdown (number):
    list = []
    for x in range (number, -1, -1):
        list.append(x)
    return(list)
print(countdown(35))

def print_and_return (list):
    print(list[0])
    return list[1]
print_and_return ([11,40])

def first_plus_length (list):
    return (list[0] + len(list))
print(first_plus_length ([1,1,2,3,5,8]))

def values_greater_than_second (list):
    newlist = []
    if len(list)<2:
        return False
    for x in range (0, len(list)):
        if list[x] > list[1]:
            newlist.append (list[x])
    print("Number of Values:", len(newlist))
    return newlist
print(values_greater_than_second ([2,18,3,1,7,98,185]))

def this_length_that_value(size, value):
    newlist=[]
    for x in range (0, size):
        newlist.append(value)
    return newlist
print(this_length_that_value(6, 2))