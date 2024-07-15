# List  ordered mutable allows duplicate elements
# mylist = ["banana","cherry","apple"]
# mylist2 = [1,2,3,4,5]

# newlist = mylist + mylist2

# print(newlist)
# mylist.reverse()
# mylist.sort()

# print(mylist)

# mylist.clear()
# if mylist:
#     print("Yes")
    
# else:
#     print("Dekhis khali xa")
# item = mylist.remove("cherry")
# print(mylist)

# mylist.insert(1,"Blueberry")
# print(mylist)
# mylist.pop()

# print(mylist)
# print(mylist)

# print(len(mylist))

# mylist.append("lemon")


# print(mylist)
# mylist2 = [5,True,"apple","apple"]

# print(mylist2)

# item = mylist[-1]
# print(item)

# # for i in mylist:
# #     print(i)

# if "banana" in mylist:
#     print("Yes banana found ")
    
# else:
#     print("Nope")

# print(mylist)

# print(mylist[1:5])

# mylist = [x for x in range(10)]
# list_org = ["Banana","cherry","apple"]
# list_cpy = list_org.copy()
# print(list_cpy) 

# list_cpy = list_org[:]

# a = [1,2,3,4,5,6]

# b = [i*i for i in a]

# print(b)

# Tuples: Ordered, Indexed, allows duplicate, unmutable

# mytuple = "Max",28,"Boston"
# print(mytuple)

# mytuple = tuple(["Max",25,"Boston"])
# print(type(mytuple))

# item = mytuple[2]
# print(item)

# mylist = [x for x in range(100)]

# mylist.append(10)
# mylist.append(10)
# mylist.append(10)
# mylist.append(10)

# print(mylist.count(10))

# my_list = [34,45,2,90,5,3,87]

# print(my_list.index(5))
# print(my_list.find(5))

mytuple = "keshab","Aryal","Arghakhanchi"

i1,*i2 = mytuple

print(i1)
print(i2)