import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

df = pd.read_csv('iris.csv')
print(df['class'].value_counts())

species = {
    'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2
}
df['class_value'] = df['class'].map(species) #nowa kolumna z danymi numerycznymi
print(df['class_value'].value_counts())

sample = np.array([5.6, 3.2, 5.2, 1.45])

sns.scatterplot(data=df, x="sepallength", y="sepalwidth", hue='class')
plt.scatter(x=5.6, y=3.2, c='r')
plt.show()

sns.scatterplot(data=df, x="petallength", y="petalwidth", hue='class')
plt.scatter(x=5.2, y=1.45, c='r')
plt.show()

X = df.iloc[:,    :4   ]  # wszystkie wiersze i 2 pierwsze kolumny - 4 cechy
y = df.class_value
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
model = KNeighborsClassifier(n_neighbors=5)   #, weights='distance')
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))

# recznie
df['distance'] = (df.sepallength - sample[0]) ** 2  +  (df.sepalwidth - sample[1]) ** 2  +\
    (df.petallength - sample[2]) ** 2  +  (df.petalwidth - sample[3]) ** 2
print(df.sort_values('distance').to_string())

results = []
for k in range(1, 50):
    model = KNeighborsClassifier(n_neighbors=k) # , weights='distance')
    model.fit(X_train, y_train)
    results.append(model.score(X_test, y_test))

# plt.scatter(x=range(1, 50), y=results) # wykres punktowy
plt.plot(range(1, 50), results, 'b')   # linia ciągła
plt.show()

