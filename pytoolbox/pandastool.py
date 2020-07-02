import pandas as pd
import numpy as np
# find the max value for each row and return the original df with an added col for the row.
def find_max_each_row(df, max_col_name = 'max_val'):
    df[max_col_name] = df.max(axis=1)

    return df
    
#df = pd.DataFrame(np.random.randn(5, 3), columns = ['x', 'y', 'z'], index=['a', 'c', 'e', 'f', 'h'])

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