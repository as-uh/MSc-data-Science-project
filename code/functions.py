# Function to calculate the difference between the two values
def diff(x,y):
    if x>y:
        return (x-y)
    else:
        return(y-x)

    
# Function to convert string to list
def Converttolist(string): 
    string_list = list(string.split("; ")) 
    string_list = [a.strip() for a in string_list ]
    return string_list


# Function to remove duplicates
def remove_duplicate(x):
    return list(dict.fromkeys(x))