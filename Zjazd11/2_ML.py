import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

df = pd.read_csv('dane.csv', comment='#')
print(df.head().to_string())
print(df.target.value_counts())

X = df.iloc[:, :-1]
y = df.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print('\Part1 pojedyncze algorytmy')
print('\nLogistic Regression')
model = LogisticRegression()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))

print('\nKNN')
model = KNeighborsClassifier()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))

results1 = []
for k in range(1, 50):
    model = KNeighborsClassifier(n_neighbors=k) # , weights='distance')
    model.fit(X_train, y_train)
    results1.append(model.score(X_test, y_test))

plt.title('KNN')
plt.plot(range(1, 50), results1)
plt.show()

results2 = []
for k in range(1, 50):
    model = KNeighborsClassifier(n_neighbors=k, weights='distance')
    model.fit(X_train, y_train)
    results2.append(model.score(X_test, y_test))

plt.title('KNN - distance')
plt.plot(range(1, 50), results2)
plt.show()