import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

PLOT_LABEL_FONT_SIZE = 25

def getColors(n):
  COLORS = []
  cm = plt.cm.get_cmap('hsv', n)
  for i in np.arange(n):
    COLORS.append(cm(i))
  return COLORS

def dict_sort(my_dict):
  keys = []
  values = []
  my_dict = sorted(my_dict.items(), key=lambda x:x[1], reverse=True)
  for k, v in my_dict:
    keys.append(k)
    values.append(v)
  return (keys,values)

pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 12)
df = pd.read_csv('vgsales.csv', escapechar='`', low_memory=False)

df = df.replace({None: 'unknown'})
df = df.replace({np.NaN: 'unknown'})
print(df)

breed_count = pd.value_counts(df['Genre'].values, sort=True)
breed_count_keys, breed_count_values = dict_sort(dict(breed_count))
TOP_breed = len(breed_count_keys)
plt.figure(figsize=(20,10))
plt.title('Жанры', fontsize=PLOT_LABEL_FONT_SIZE)
plt.bar(np.arange(TOP_breed), breed_count_values, color=getColors(TOP_breed)) #метод построения гистаграмм
plt.xticks(np.arange(TOP_breed), breed_count_keys, rotation=90, fontsize=PLOT_LABEL_FONT_SIZE)
plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
plt.ylabel('Количество игр в жанре', fontsize=PLOT_LABEL_FONT_SIZE)
#plt.show()

breed_count = pd.value_counts(df['Publisher'].values, sort=True)
breed_count_keys, breed_count_values = dict_sort(dict(breed_count))
print(range(len(breed_count_keys)))
del breed_count_values[50:579]
del breed_count_keys[50:579]
TOP_breed = len(breed_count_keys)
plt.figure(figsize=(20,10))
plt.title('Издатель', fontsize=PLOT_LABEL_FONT_SIZE)
plt.bar(np.arange(TOP_breed), breed_count_values, color=getColors(TOP_breed)) #метод построения гистаграмм
plt.xticks(np.arange(TOP_breed), breed_count_keys, rotation=90, fontsize=PLOT_LABEL_FONT_SIZE)
plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
plt.ylabel('Количество игр в издании', fontsize=PLOT_LABEL_FONT_SIZE)
#plt.show()

breed_count = pd.value_counts(df['Publisher'].values, sort=True)
breed_count_keys, breed_count_values = dict_sort(dict(breed_count))
print(range(len(breed_count_keys)))
del breed_count_values[0:50]
del breed_count_keys[0:50]
del breed_count_values[50:579]
del breed_count_keys[50:579]
TOP_breed = len(breed_count_keys)
plt.figure(figsize=(20,10))
plt.title('Издатель', fontsize=PLOT_LABEL_FONT_SIZE)
plt.bar(np.arange(TOP_breed), breed_count_values, color=getColors(TOP_breed)) #метод построения гистаграмм
plt.xticks(np.arange(TOP_breed), breed_count_keys, rotation=90, fontsize=PLOT_LABEL_FONT_SIZE)
plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
plt.ylabel('Количество игр в издании', fontsize=PLOT_LABEL_FONT_SIZE)
#plt.show()

breed_count = pd.value_counts(df['Platform'].values, sort=True)
breed_count_keys, breed_count_values = dict_sort(dict(breed_count))
TOP_breed = len(breed_count_keys)
plt.figure(figsize=(20,10))
plt.title('Платформы', fontsize=PLOT_LABEL_FONT_SIZE)
plt.bar(np.arange(TOP_breed), breed_count_values, color=getColors(TOP_breed)) #метод построения гистаграмм
plt.xticks(np.arange(TOP_breed), breed_count_keys, rotation=90, fontsize=PLOT_LABEL_FONT_SIZE)
plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
plt.ylabel('Количество игр на платформе', fontsize=PLOT_LABEL_FONT_SIZE)
#plt.show()

breed_count = pd.value_counts(df['Year'].values, sort=True)
breed_count_keys, breed_count_values = dict_sort(dict(breed_count))
del breed_count_values[20]
del breed_count_keys[20]
TOP_breed = len(breed_count_keys)
plt.figure(figsize=(20,10))
plt.title('Год издания', fontsize=PLOT_LABEL_FONT_SIZE)
plt.bar(np.arange(TOP_breed), breed_count_values, color=getColors(TOP_breed)) #метод построения гистаграмм
plt.xticks(np.arange(TOP_breed), breed_count_keys, rotation=90, fontsize=PLOT_LABEL_FONT_SIZE)
plt.yticks(fontsize=PLOT_LABEL_FONT_SIZE)
plt.ylabel('Количество игр изданных в год', fontsize=PLOT_LABEL_FONT_SIZE)
plt.show()

