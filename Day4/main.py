
my_list = [1, 2, 3, "hello", True]


first_element = my_list[0]
last_element = my_list[-1]


my_list[2] = "world"


my_list.append("!")
my_list.remove(2)  

if "hello" in my_list:
  print("hello is in the list")


list_length = len(my_list)  
concatenated_list = my_list + ["new", "items"]  

my_tuple = (1, 2, 3, "hello")

count = my_tuple.count(2) 
index = my_tuple.index("hello")  


my_string = "This is a string"


first_character = my_string[0]

substring = my_string[2:5] 


upper_string = my_string.upper()
lower_string = my_string.lower()
split_string = my_string.split()  

replaced_string = my_string.replace("This", "That")


print(my_list)
print(list_length)
print(concatenated_list)
print(count)
print(index)
print(upper_string)
print(lower_string)
print(split_string)
print(replaced_string)
