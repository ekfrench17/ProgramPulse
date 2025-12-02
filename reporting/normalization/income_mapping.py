# Income Mapping normalization

import numpy as np

# income variables
ami_30 = '0 - 30% AMI'
ami_50 = '31 - 50% AMI'
ami_80 = '51 - 80% AMI'
ami_over_80 = '> 80% AMI'

income_mapping_sbmtl = {
 'At or below 30% AMI': ami_30, 
 '0-30% AMI':ami_30,
 '0-30% del AMI':ami_30,
 'Al mismo nivel o por debajo del 30% del AMI':ami_30,

 'At or below 50% AMI': ami_50,
 '31-50% AMI':ami_50,
 '31-50% del AMI':ami_50,
 'Al mismo nivel o por debajo del 50% del AMI':ami_50,

 'At or below 80% AMI': ami_80,
 '51-80% AMI':ami_80,
 '51-80% del AMI':ami_80,
 'Al mismo nivel o por debajo del 80% del AMI':ami_80,

 'Above 80% AMI':ami_over_80,
 
 'Submittable AMI Table_Spa 2024.xlsx':np.nan,
  np.nan:np.nan
}
