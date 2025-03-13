# Language mapping normalization

import numpy as np

# multi-use
prefer_no_answer = 'Prefer not to answer'
other = 'Other'

# Language variables
english = 'English'
spanish = 'Spanish'
chinese = 'Chinese'
french = 'French'
korean = 'Korean'


language_mapping = {
    'English':english,
    'English ':english,
    'Ingles ':english,
    'Ingles':english,
    'English - United States':english,
    'English - Hong Kong':english,
    'InglÃ©s':english,
    'English - New Zealand':english,
    'English - Australia':english,
    'English - Canada':english,
    'English - United Kingdom':english,
    'English - Malta':english,
    'English - Philippines':english,
    'English - Ireland':english,

    'Spanish':spanish,
    'EspaÃ±ol ':spanish,
    'EspaÃ±ol':spanish,
    'Espanol':spanish,
    'Espanol ':spanish,
    'Spanish - Mexico':spanish,
    'EspaÃ±ol':spanish,
    'Spanish - United States':spanish,
    'Spanish - Peru':spanish,
    'Spanish - Venezuela':spanish,
    'Spanish - Nicaragua':spanish,
    'Spanish - Colombia':spanish,
    'Spanish - Chile':spanish,
    'Spanish - Argentina':spanish,
    'Spanish - Puerto Rico':spanish,
    'Spanish - Spain':spanish,
    'Spanish - Honduras':spanish,
    'Spanish - Costa Rica':spanish,

    'Chinese (Mandarin)':chinese,
    'Chinese (Simplified)':chinese,
    'Chinese':chinese,

    'French':french,
    'French - France':french,

    'Korean':korean,
    'Korean - South Korea':korean,

    None:np.nan,
    np.nan:np.nan,
    'Na':np.nan,
    'D':np.nan,
    'alicia_00_80239@yahoo.com':np.nan,
    'rogersphillip384@gmail.com':np.nan,
    'Na ':np.nan,
    'no data':np.nan,
    
    'Other':other,
    'Other- please state in comment box':other,
    'Also limited English':other, 
    'Other (please state in the box below)':other,
    'Mail':other,
    
    'Afrikaans':'Afrikaans',
    'Albanian':'Albanian',
    'Arabic':'Arabic',
    'Armenian':'Armenian',
    'Burmese':'Burmese',
    'Chuukese':'Chuukese',
    'Dair--Afghan dialect of Farsi':'Dair',
    'Finnish':'Finnish',
    'Fulani':'Fulani',
    'German':'German',
    'Haitian Creole':'Haitian Creole',
    'Italian':'Italian',
    'Kinyarwanda':'Kinyarwanda',
    'Marshallese':'Marshallese',
    'Nyanja':'Nyanja',
    'Oromo':'Oromo',
    'Romanian':'Romanian',
    'Russian': 'Russian',
    'Swahili':'Swahili'
}