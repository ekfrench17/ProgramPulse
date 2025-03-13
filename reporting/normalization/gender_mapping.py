# Gender Mapping Normalization

import numpy as np

# multi-use
prefer_no_answer = 'Prefer not to answer'
other = 'Other'

# variables for gender nomalization
female = "Female"
male = "Male"
non_binary = "Non-Binary"
trans_fem = 'Transgender Female'
trans_male = 'Transgender Male'

gender_mapping = {
    'Female ':              female,
    'Male':                 male,
    'Prefer not to answer': prefer_no_answer,
    'Female':               female,
    'Male ':                male,
    'Decline to answer ':   prefer_no_answer,
    'Non-binary ':          non_binary,
    np.nan:                 np.nan,
    'Prefiere no responder ':prefer_no_answer,
    'Transgender Female':    trans_fem,
    'Femenino ':             female,
    'Other':                 other,
    None:                    np.nan,
    'Masculino ':            male,
    'Transgender Male':      trans_male,
    'Transgender Female ':   trans_fem,
    'Transgender Male ':     trans_male,
    'No binario ':           non_binary,
    'Other ':                other,
    'TransgÃ©nero femenino ':trans_fem
    }