# Removes the duplicates in a list and returns the filtered list
# Example: [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5] will reduce to [1,2,3,4,5]
def remove_duplicates(list):
    filtered_list =  []
    for element in list:
        if element not in filtered_list:
            filtered_list.append(element)

    return  filtered_list

# Converts a list to a dictionary
# element value -> key 
# element count in list -> value
# Example: [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5] will change to {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
def reduce_list_to_quantity_dict(list):
    dict = {}
    for element in list:
        if element in dict:
            dict[element] += 1
        else:
            dict[element] = 1
    
    return dict
    