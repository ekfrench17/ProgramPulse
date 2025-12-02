# mapping for fixing counties

county_list = ['Adams',
 'Alamosa',
 'Arapahoe',
 'Bent',
 'Boulder',
 'Broomfield',
 'Denver',
 'Douglas',
 'El Paso',
 'Garfield',
 'Hinsdale',
 'Jefferson',
 'La Plata',
 'Larimer',
 'Las Animas',
 'Logan',
 'Mesa',
 'Moffat',
 'Montezuma',
 'Montrose',
 'Morgan',
 'Prowers',
 'Pueblo',
 'Saguache',
 'Summit',
 'Teller',
 'Weld']

county_mapping ={
    'Adams County': 'Adams',
    'Adams': 'Adams',

    'Alamosa':'Alamosa',
    
    'Arapahoe':'Arapahoe',
    'Araphoe': 'Arapahoe',
    'Araphahoe': 'Arapahoe',
    'Aurora, Arapahoe County': 'Arapahoe',
    'Aurora,Arapahoe':'Arapahoe',
    'Aurora/Arapahoe': 'Arapahoe',

    'Bent': 'Bent',

    'Boulder': 'Boulder',

    'Broomfield': 'Broomfield',

    'Chaffee': 'Chaffee',

    'Clear Creek': 'Clear Creek',

    'Conejos': 'Conejos',
    'Conjeos': 'Conejos',

    'Crowley': 'Crowley',

    'Delta': 'Delta',

    'Denver':'Denver',
    'Denver and City Of Denver': 'Denver',
    'Denver/Adams': 'Denver',  # Consider combining Denver and Adams as just Denver if it fits
    'Denver County': 'Denver',
    'Denver Country': 'Denver',
    'Denver (Dhs Grant)': 'Denver',
    "DenverButWe'ReDoing": 'Denver',
    'DenverAndDenver':'Denver',
    'Aurora/Denver': 'Denver',

    'Douglas':'Douglas',
    'Douglass': 'Douglas',

    'Eagle': 'Eagle',

    'El Paso County': 'El Paso',
    'El Paso': 'El Paso',
    'ElPaso':'El Paso',
    '80010': 'El Paso',  # Or handle as a special case if needed
    'Colorado Springs': 'El Paso',
    'ColoradoSprings': 'El Paso',

    'Fremont': 'Fremont',

    'Garfield': 'Garfield',

    'Grand': 'Grand',

    'Gunnison': 'Gunnison',

    'Hinsdale': 'Hinsdale',

    'Jefferson':'Jefferson',
    'Jefferson County': 'Jefferson',
    'Jeffco': 'Jefferson',

    'Kit Carson': 'Kit Carson',

    'La Plata':'La Plata',

    'Las Animas':'Las Animas',

    'Lake':'Lake',

    'Larimer':'Larimer',
    'Larimar': 'Larimer',
    'Larimer County': 'Larimer',

    'Lincoln': 'Lincoln',

    'Logan':'Logan',

    'Mesa County': 'Mesa',
    'Mesa': 'Mesa',

    'Mineral': 'Mineral',
    'Minera': 'Mineral',

    'Moffat': 'Moffat',
    
    'Montezuma': 'Montezuma',
    
    'Montrose': 'Montrose',

    'Morgan': 'Morgan',

    'Otero': 'Otero',

    'Pitkin': 'Pitkin',

    'Prowers':'Prowers',

    'Pueblo': 'Pueblo',

    'Saguache':'Saguache',

    'Summit':'Summit',

    'Teller':'Teller',
    
    'Weld': 'Weld',

    'Yuma': 'Yuma'
}