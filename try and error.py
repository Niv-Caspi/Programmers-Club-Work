def modify_list(lst):
    lst.append(4)
    lst = [5, 6, 7]
    
numbers = [1, 2, 3]
modify_list(numbers)
print (numbers)

def modify_dict (dct):
    dct ['key2'] = "new_value"
    dct = {'new_key':"new_value"}
    
my_dict = {'key1':"value1", 'key2':"value2"}
modify_dict(my_dict)
print (my_dict["key2"])