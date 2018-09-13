def capitalize_name(name):
    """
    name -> a string in the form "first last" all lowers case
    returns -> the string with both names capitalized
    ex: james bond -> James Bond
    """
    space_index = name.find(" ")
    first_char = name[0]
    second_char = name[space_index:(space_index+2)]
    cap_first = first_char.upper()
    cap_sec = second_char.upper()
    
    return cap_first+name[1:space_index]+cap_sec+name[(space_index+2):]

print(capitalize_name("kushendra ramrup"))

def init(name):
    """
    Input: name --> a string in the form "first last"
    Returns: a string in the form "F. Last" where it's a capitalized first inital 
    and capitalized last name
    """
    space_index = name.find(" ")
    first_char = name[0]
    cap_first = first_char.upper()
    sec_char = name[space_index:(space_index+2)]
    cap_sec = sec_char.upper()
    return cap_first+"."+cap_sec+name[(space_index+2):]

print(init("kushendra ramrup"))