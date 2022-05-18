import numpy as np
import os

np.random.seed(1)

theta = np.linspace(10, 90, num=8001)

# Hematita

filepath_hematita = 'C:/Users/Marcos Tassan/Documents/Mariana/rdx_17_05_2022/rdx_17_05_2022/Base_Dados/Hematita'
ds_hem = os.listdir(filepath_hematita)
tam_hem = len(ds_hem)

data_hem = np.zeros((14,3), dtype=np.float64)

for i in range(0, tam_hem):
    with open('Base_Dados/Hematita/' + ds_hem[i], 'r', encoding='utf-8') as dir:
        content = dir.read()
        
        lines = content.split('\n')
                
        lines = lines[1:]
        
        for line in lines:
            fragments = line.split(';')

            print(fragments[0])
        print('\n')
    print('\n')            
          
# Magnetita

filepath_magnetita = 'C:/Users/Marcos Tassan/Documents/Mariana/rdx_17_05_2022/rdx_17_05_2022/Base_Dados/Magnetita'
ds_mag = os.listdir(filepath_magnetita)
tam_mag = len(ds_mag)

data_mag = np.zeros((14,3), dtype=np.float64)

for i in range(0, tam_mag):
    with open('Base_Dados/Magnetita/' + ds_mag[i], 'r', encoding='utf-8') as dir:
        content = dir.read()
        
        lines = content.split('\n')
                
        lines = lines[1:]
        
        for line in lines:
            fragments = line.split(';')

            print(fragments[0])
        print('\n')
    print('\n') 

# Goetita

filepath_goetita = 'C:/Users/Marcos Tassan/Documents/Mariana/rdx_17_05_2022/rdx_17_05_2022/Base_Dados/Goetita'
ds_goe = os.listdir(filepath_goetita)
tam_goe = len(ds_goe)

data_goe = np.zeros((14,3), dtype=np.float64)

for i in range(0, tam_goe):
    with open('Base_Dados/Goetita/' + ds_goe[i], 'r', encoding='utf-8') as dir:
        content = dir.read()
        
        lines = content.split('\n')
                
        lines = lines[1:]
        
        for line in lines:
            fragments = line.split(';')

            print(fragments[0])
        print('\n')
    print('\n')       

# Calcita

filepath_calcita = 'C:/Users/Marcos Tassan/Documents/Mariana/rdx_17_05_2022/rdx_17_05_2022/Base_Dados/Calcita'
ds_cal = os.listdir(filepath_calcita)
tam_cal = len(ds_cal)

data_cal = np.zeros((14,3), dtype=np.float64)

for i in range(0, tam_cal):
    with open('Base_Dados/Calcita/' + ds_cal[i], 'r', encoding='utf-8') as dir:
        content = dir.read()
        
        lines = content.split('\n')
                
        lines = lines[1:]
        
        for line in lines:
            fragments = line.split(';')

            print(fragments[0])
        print('\n')
    print('\n')