"""
Task: Given a list and a number, create a new list that contains each number of list at most N times,
without reordering. For example if the input number is 2, and the input list is [1,2,3,1,2,1,2,3], you take [1,2,3,1,
2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to
[1,2,3,1,2,3]. With list [20,37,20,21] and number 1, the result would be [20,37,21].
"""

def delete_nth(in_list, max_e):
    # Create a new list
    new_list = []
    # Loop through the list
    for i in in_list:
        # If the element is in the list and the count is less than the max
        if i in new_list and new_list.count(i) < max_e:
            # Append the element to the list
            new_list.append(i)
        # If the element is not in the list
        elif i not in new_list:
            # Append the element to the list
            new_list.append(i)
    # Return the new list
    return new_list

def __main__():
    print (delete_nth([1,2,3,1,2,1,2,3], 2)) # [1,2,3,1,2,3]
    
if __name__ == "__main__":
    __main__()
