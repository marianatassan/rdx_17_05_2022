import numpy as np; import os; import pandas as pd

np.random.seed(1)

theta = [x/100 for x in range(1000, 9000)]

# Hematita

filepath_hematita = 'C:/Users/Marcos Tassan/Documents/Mariana/rdx_17_05_2022/rdx_17_05_2022/Base_Dados/Hematita'
ds_hem = os.listdir(filepath_hematita)
tam_hem = len(ds_hem)

data_hem = np.zeros((tam_hem, len(theta)))
#np.set_printoptions(threshold=sys.maxsize)

for i in range(0, tam_hem):
    df = pd.read_csv('Base_Dados/Hematita/' + ds_hem[i], sep=';')

    for j in range(len(df['2-THETA'])):
        for k in range(len(theta)): 
            if df['2-THETA'][j] == theta[k]:
                data_hem[i][k] = df['2-THETA'][j]
                
       
# Magnetita

filepath_magnetita = 'C:/Users/Marcos Tassan/Documents/Mariana/rdx_17_05_2022/rdx_17_05_2022/Base_Dados/Magnetita'
ds_mag = os.listdir(filepath_magnetita)
tam_mag = len(ds_mag)

data_mag = np.zeros((15,3), dtype=np.float64)
#np.set_printoptions(threshold=sys.maxsize)

for i in range(0, tam_mag):
    df = pd.read_csv('Base_Dados/Magnetita/' + ds_mag[i], sep=';')

    for j in range(len(df['2-THETA'])):
        for k in range(len(theta)): 
            if df['2-THETA'][j] == theta[k]:
                data_mag[i][k] = df['2-THETA'][j]

# Goetita

filepath_goetita = 'C:/Users/Marcos Tassan/Documents/Mariana/rdx_17_05_2022/rdx_17_05_2022/Base_Dados/Goetita'
ds_goe = os.listdir(filepath_goetita)
tam_goe = len(ds_goe)

data_goe = np.zeros((15,3), dtype=np.float64)
#np.set_printoptions(threshold=sys.maxsize)

for i in range(0, tam_goe):
    df = pd.read_csv('Base_Dados/Goetita/' + ds_goe[i], sep=';')

    for j in range(len(df['2-THETA'])):
        for k in range(len(theta)): 
            if df['2-THETA'][j] == theta[k]:
                data_goe[i][k] = df['2-THETA'][j]      

# Calcita

filepath_calcita = 'C:/Users/Marcos Tassan/Documents/Mariana/rdx_17_05_2022/rdx_17_05_2022/Base_Dados/Calcita'
ds_cal = os.listdir(filepath_calcita)
tam_cal = len(ds_cal)

data_cal = np.zeros((15,3), dtype=np.float64)
#np.set_printoptions(threshold=sys.maxsize)

for i in range(0, tam_cal):
    df = pd.read_csv('Base_Dados/Calcita/' + ds_cal[i], sep=';')

    for j in range(len(df['2-THETA'])):
        for k in range(len(theta)): 
            if df['2-THETA'][j] == theta[k]:
                data_cal[i][k] = df['2-THETA'][j] 