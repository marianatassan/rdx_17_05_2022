import numpy as np; import os; import pandas as pd; import pickle
from sklearn.tree import DecisionTreeClassifier

np.random.seed(1)

X = []
Y = []

# Hematita

filepath_hematita = 'Base_Dados/Hematita/'
ds_hem = os.listdir(filepath_hematita)

hem_feature_amostra = []

for i in range(15):
  df = pd.read_csv(filepath_hematita + ds_hem[i], sep=';')

  for m in range(10):
    hem_feature_amostra.append(df['INTENSITY'][m])
  hem_feature_amostra.append(len(df['INTENSITY']))

  X.append(hem_feature_amostra)
  hem_feature_amostra = []

  Y.append('0')

# Magnetita

filepath_magnetita = 'Base_Dados/Magnetita/'
ds_mag = os.listdir(filepath_magnetita)

mag_feature_amostra = []

for i in range(15):
    df = pd.read_csv(filepath_magnetita + ds_mag[i], sep=';')

    for m in range(10):
      mag_feature_amostra.append(df['INTENSITY'][m])
    mag_feature_amostra.append(len(df['INTENSITY']))

    X.append(mag_feature_amostra)
    mag_feature_amostra = []

    Y.append('1')
  
# Goetita

filepath_goetita = 'Base_Dados/Goetita/'
ds_goe = os.listdir(filepath_goetita)

goe_feature_amostra = []

for i in range(15):
    df = pd.read_csv(filepath_goetita + ds_goe[i], sep=';')
  
    for m in range(10):
      goe_feature_amostra.append(df['INTENSITY'][m])
    goe_feature_amostra.append(len(df['INTENSITY']))  

    X.append(goe_feature_amostra)
    goe_feature_amostra = []

    Y.append('2')

# Calcita

filepath_calcita = 'Base_Dados/Calcita/'
ds_cal = os.listdir(filepath_calcita)

cal_feature_amostra = []

for i in range(15):
    df = pd.read_csv(filepath_calcita + ds_cal[i], sep=';')

    for m in range(10):
      cal_feature_amostra.append(df['INTENSITY'][m])
    cal_feature_amostra.append(len(df['INTENSITY']))

    X.append(cal_feature_amostra)
    cal_feature_amostra = []

    Y.append('3')
  
# print('\n', X)
# print('\n', Y)

arvore_tipo_substancia = DecisionTreeClassifier(criterion='entropy')
arvore_tipo_substancia.fit(X, Y)
importancia = arvore_tipo_substancia.feature_importances_

for i,v in enumerate(importancia):
	print('Feature: %0d, Score: %.5f' % (i,v))