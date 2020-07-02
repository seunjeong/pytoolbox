
# make a dict obj using key and value lists
def two_list_to_dic(key_list, value_list):
    """
    @example: 
    key_list = ['a', 'b', 'c']
    value_list = range (3)
    foo = two_list_to_dic (key_list, value_list)
    """
    zipped = zip(key_list, value_list)
    
    # Create a dictionary from zip object
    dict_obj = dict(zipped)

    return dict_obj

