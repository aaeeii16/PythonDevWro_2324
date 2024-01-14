import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from sklearn.svm import SVC  #clasifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

X, y = make_circles(n_samples=1000, factor=0.5, noise=0.3)

plt.scatter(x=X[:, 0], y=X[:, 1], c=y)
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print('\nSVC')
model = SVC(kernel='poly', degree=10)
model.fit(X_train, y_train)
print(model.score(X_test, y_test))
print(pd.DataFrame(confusion_matrix(y_test, model.predict(X_test))))