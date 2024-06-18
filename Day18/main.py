class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data.greet())
            current_node = current_node.next

person1 = Person("Sita", 30)
person2 = Person("Ram", 25)
person3 = Person("Hari", 35)


linked_list = LinkedList()
linked_list.append(person1)
linked_list.append(person2)
linked_list.append(person3)

linked_list.print_list()
