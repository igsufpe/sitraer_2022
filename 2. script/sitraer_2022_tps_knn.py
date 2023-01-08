# -*- coding: utf-8 -*-
"""sitraer_2022_TPS_KNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R01CgQvTnE9eZQk1pj54Sf67yTwabq1X

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
import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import seaborn as sns
from mlxtend.plotting import plot_learning_curves

"""#Importação do Dataset (Excel)"""

df = pd.read_csv('/content/sample_data/DATASET_TPS_.csv', delimiter=';')
df.head()

"""#Visualização dos Dados"""

sns.pairplot(df)
plt.show()

"""#Pré-processamento *inputs*"""

X = df.drop('status', axis=1)
y = df.status
X

"""#Separando *inputs* e *outputs*"""

from sklearn.preprocessing import MinMaxScaler

normalizador = MinMaxScaler()
X_norm = normalizador.fit_transform(X)
X_norm

"""#Implementando o algoritmo KNN"""

from sklearn.neighbors import KNeighborsClassifier

"""#Treinando o classificador KNN"""

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_norm, y)

"""#Separando conjunto de treino e teste"""

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

#criando variáveis
X_train, X_test, y_train, y_test = train_test_split(X_norm, y, train_size=2/3)

"""#Avaliando a acurácia do algoritmo KNN"""

# Setup arrays to store train and test accuracies
neighbors = np.arange(1, 10)
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))

# Loop over different values of k
for i, k in enumerate(neighbors):
    # Setup a k-NN Classifier with k neighbors: knn
    knn = KNeighborsClassifier(n_neighbors=k)

    # Fit the classifier to the training data
    knn.fit(X_train, y_train)
    
    #Compute accuracy on the training set
    train_accuracy[i] = knn.score(X_train, y_train)

    #Compute accuracy on the testing set
    test_accuracy[i] = knn.score(X_test, y_test)

# Generate plot
plt.title('k-NN: Variação de k-vizinhos')
plt.plot(neighbors, test_accuracy, label = 'Acurácia Teste')
plt.plot(neighbors, train_accuracy, label = 'Acurácia Treino')
plt.legend()
plt.xlabel('Número de k-vizinhos')
plt.ylabel('Acurária')
plt.show()

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

accuracy_score(y_test, knn.predict(X_test))

resultado_knn = knn.predict(X_test)

print(classification_report(y_test, resultado_knn))

"""#Avaliando o classificador (a partir de um novo projeto)"""

novo_projeto = [[2.00, 3.00, 20.00, 3.00]]
normalizador.transform(novo_projeto)
X_new = normalizador.transform(novo_projeto)
X_new

knn.predict(X_new)