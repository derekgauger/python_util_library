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


# Asks the user a yes or no question
# Yes returns True
# No returns False
def ask_yes_no_question(prompt):
    user_input = input(prompt).lower()

    if user_input in ['y' or 'yes']:
        return True

    return False


# Uses regular expressions to search a file for capture groups
def search_file_for_info(file_name, regular_expression):
    import re

    with open(file_name) as file:
        lines = file.readlines()

    matches = []
    for line in lines:
        match = re.search(regular_expression, line)

        if match:
            match = match.groups()
            matches.append(match)

    return matches


# Uses regular expressions to search some text for capture groups
def search_text_for_info(search_text, regular_expression):
    import re

    match = re.findall(regular_expression, search_text)

    return match
