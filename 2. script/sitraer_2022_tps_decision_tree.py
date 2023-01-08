# -*- coding: utf-8 -*-
"""sitraer_2022_TPS_Decision Tree.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f4Tj73qhhvl-DFobrhzqscFyqNMVQxbS

#Machine Learning Applied in the Evaluation of Airport Projects# 
#SITRAER 2022#

Universidade Federal de Pernambuco (UFPE)

Data: Agosto / 2022

Autores:
*   Ítalo Guedes - italo.guedes@ufpe.br
*   Max Andrade - max.andrade@ufpe.br 
*   Cleber Zanchettin - cz@cin.ufpe.br

#Importação das bibliotecas
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
import seaborn as sns

"""#Importação do Dataset (Excel)"""

df = pd.read_csv('/content/sample_data/DATASET_TPS_.csv', delimiter=';')
df.head()

"""#Visualização dos Dados"""

sns.pairplot(df, hue='status')
plt.show()

sns.pairplot(df, hue='status', kind='kde')
plt.show()

"""#Separando *inputs* e *outputs*"""

X = df.drop('status', axis=1)
y = df.status
X

"""#Normalizando os Dados"""

from sklearn.preprocessing import MinMaxScaler
minmax = MinMaxScaler()
X_norm = minmax.fit_transform(X)
X_norm

"""#Implementando o algoritmo KNN"""

from sklearn.tree import DecisionTreeClassifier

"""#Configurando o classificador Decision Tree (profundidade, nº de folhas)"""

dt = DecisionTreeClassifier (max_depth=3, max_leaf_nodes=4)

print(dt.get_depth())
print(dt.get_n_leaves())

"""#Separando conjunto de treino e teste"""

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#criando variáveis (treino e teste)
X_train, X_test, y_train, y_test = train_test_split(X_norm, y, train_size=2/3)

"""#Avaliando a acurácia do algoritmo Decision Tree"""

dt.fit(X_train, y_train)

accuracy_score(y_test, dt.predict(X_test))

resultado_dt = dt.predict(X_test)

print(classification_report(y_test, resultado_dt))

"""#Avaliando o classificador (a partir de um novo projeto)"""

novo_projeto = [[5.00, 8.00, 20.00, 20.00]]
X_new = minmax.transform(novo_projeto)
X_new

dt.predict(X_new)