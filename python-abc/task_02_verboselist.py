#!/usr/bin/python3

class VerboseList(list):
    
    def append(self, item):
        print("Added [{}] to the list.".format(item))
        super().append(item)

    def extend(self, lista):
        print("Extended the list with [{}] items.".format(len(lista)))
        super().extend(lista)

    def remove(self, item):
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        print("Popped [{}] from the list.".format(super().pop(index)))
        
    