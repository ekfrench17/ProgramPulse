# Ethnicity Mapping Normalization

import numpy as np

# ethnicity
hispanic = 'Hispanic or Latino'
not_hispanic = 'Not Hispanic or Latino'

# multi-use
prefer_no_answer = 'Prefer not to answer'
other = 'Other'

ethnicity_mapping = {
    'Not Hispanic or Latino':   not_hispanic,
    'Non-Hispanic or Latino':   not_hispanic,
    'No hispano o latino':      not_hispanic,

    'Hispanic or Latino':       hispanic,
    'Hispano o latino':         hispanic,

    'Prefer not to Answer':     prefer_no_answer,
    'Decline to answer':        prefer_no_answer,
    'Prefiere no responder':    prefer_no_answer,
    
    np.nan:                     np.nan,
    None:                       np.nan 
    }