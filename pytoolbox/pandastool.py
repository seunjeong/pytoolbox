import pandas as pd
import numpy as np

################################################################################
# How to use this module, e.g.,
#   from pytoolbox import pandastool
#   pandastool.make_df_from_list (list_, col_name) 
################################################################################

# find the max value for each row and return the original df with an added col for the row.
def find_max_each_row(df, max_col_name = 'max_val'):
    df[max_col_name] = df.max(axis=1)

    return df
    
#df = pd.DataFrame(np.random.randn(5, 3), columns = ['x', 'y', 'z'], index=['a', 'c', 'e', 'f', 'h'])


def make_df_from_list (list_, col_name):
    """
    @param:
        # example
        list_ = [('Jones LLC', 150, 200, 50),
                 ('Alpha Co', 200, 210, 90),
                ('Blue Inc', 140, 215, 95)]
        col_name = ['account', 'Jan', 'Feb', 'Mar']
    """

    df = pd.DataFrame.from_records(list_, columns=col_name)

    return df


#===============================================================================
# Combine two df's by column, equivalent to cbind of R 
#===============================================================================
def cbind_two_df (df_a, df_b):
    df = pd.concat ([df_a, df_b], axis=1)
    return df


#===============================================================================
# Combine two df's by row, equivalent to rbind of R 
#===============================================================================
def rbind_two_df (df_a, df_b):
    df = pd.concat ([df_a, df_b], axis=0)
    return df

#col_name = ['account', 'Jan', 'Feb', 'Mar']
#list_ = [('Jones LLC', 150, 200, 50), ('Alpha Co', 200, 210, 90), ('Blue Inc', 140, 215, 95)]
#dff = pandastool.make_df_from_list (list_, col_name)
