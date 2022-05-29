import numpy as np; import os; import pandas as pd

np.random.seed(1)

theta = [x/100 for x in range(1000, 9000)]

# Hematita

filepath_hematita = 'Base_Dados/Hematita/'
ds_hem = os.listdir(filepath_hematita)
tam_hem = len(ds_hem)

data_hem = np.zeros((tam_hem, len(theta)))
hem_feature = []

for i in range(0, tam_hem):
    df = pd.read_csv(filepath_hematita + ds_hem[i], sep=';')

    for j in range(len(df['2-THETA'])):
        for k in range(len(theta)): 
            if df['2-THETA'][j] == theta[k]:
                data_hem[i][k] = df['2-THETA'][j]
    for m in range(10):
      hem_feature.append(df['INTENSITY'][m])
    hem_feature.append(len(df['INTENSITY']))

# Magnetita

filepath_magnetita = 'Base_Dados/Magnetita/'
ds_mag = os.listdir(filepath_magnetita)
tam_mag = len(ds_mag)

data_mag = np.zeros((tam_mag, len(theta)))
mag_feature = []

for i in range(0, tam_mag):
    df = pd.read_csv(filepath_magnetita + ds_mag[i], sep=';')

    for j in range(len(df['2-THETA'])):
        for k in range(len(theta)): 
            if df['2-THETA'][j] == theta[k]:
                data_mag[i][k] = df['2-THETA'][j]
    for m in range(10):
      mag_feature.append(df['INTENSITY'][m])
    mag_feature.append(len(df['INTENSITY']))

# Goetita

filepath_goetita = 'Base_Dados/Goetita/'
ds_goe = os.listdir(filepath_goetita)
tam_goe = len(ds_goe)

data_goe = np.zeros((tam_goe, len(theta)))
goe_feature = []

for i in range(0, tam_goe):
    df = pd.read_csv(filepath_goetita + ds_goe[i], sep=';')

    for j in range(len(df['2-THETA'])):
        for k in range(len(theta)): 
            if df['2-THETA'][j] == theta[k]:
                data_goe[i][k] = df['2-THETA'][j]    
    for m in range(10):
      goe_feature.append(df['INTENSITY'][m])
    goe_feature.append(len(df['INTENSITY']))  

# Calcita

filepath_calcita = 'Base_Dados/Calcita/'
ds_cal = os.listdir(filepath_calcita)
tam_cal = len(ds_cal)

data_cal = np.zeros((tam_cal, len(theta)))
cal_feature = []

for i in range(0, tam_cal):
    df = pd.read_csv(filepath_calcita + ds_cal[i], sep=';')

    for j in range(len(df['2-THETA'])):
        for k in range(len(theta)): 
            if df['2-THETA'][j] == theta[k]:
                data_cal[i][k] = df['2-THETA'][j] 
    for m in range(10):
      cal_feature.append(df['INTENSITY'][m])
    cal_feature.append(len(df['INTENSITY']))