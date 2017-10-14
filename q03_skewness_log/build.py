from scipy.stats import skew
import pandas as pd
import numpy as np
<<<<<<< HEAD
#Calculating the Skewness and then removal of skewness using Log_transformation
ny_housing = pd.read_csv('data/train.csv')


# Solution
def skewness_log(data):
    #data transformation
    data['GrLivArea1'] = np.log(data['GrLivArea'])
    data['SalePrice1'] = np.log(data['SalePrice'])
    skewed_GrLivArea1 = skew(data['GrLivArea1'])
    skewed_SalePrice1 = skew(data['SalePrice1'])
    return skewed_GrLivArea1,skewed_SalePrice1
=======

data = pd.read_csv('data/train.csv')


# Write code here:

>>>>>>> ead7dd0dda06169bc83a097d0598bc2875ec7ae6
