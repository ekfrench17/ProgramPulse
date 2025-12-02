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
    'female':               female,
    'femall':               female,
    'femenino':             female,
    'femenina':             female,
    'f':                    female,
    'femenino.':            female,
    'woman':                female,
    'mujer':                female,

    'male':                 male,
    'masculino':            male,
    'make':                 male,
    'm':                    male,
    'he him male':          male,
    'hombre':               male,
    'man':                  male,
    

    'prefer not to answer': prefer_no_answer,
    'decline to answer':    prefer_no_answer,
    'prefiere no responder':prefer_no_answer,

    np.nan:                  np.nan,
    'other':                 other,
    'non-binary transwoman': other,
    None:                    np.nan,
    
    'no binario':           non_binary,
    'non-binary':           non_binary,
    'non binary':           non_binary,
    'mtf transgender-nonbinary': non_binary,

    'transgender male':      trans_male,
    
    'transgender female':    trans_fem,
    'transgÃ©nero femenino': trans_fem,
    
    }