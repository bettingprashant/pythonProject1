my_shopping_list = ["bread","milk","butter"]
print(my_shopping_list[0])
print(len(my_shopping_list))

def bring_more_food(my_list):
    more_item = input("Enter the item\n")
    my_list.append(more_item)
    my_list.insert(1,more_item)
    # my_list.remove(more_item)
    # my_list.append("Cheese")
    return my_list

l = bring_more_food(my_shopping_list)
print(l)