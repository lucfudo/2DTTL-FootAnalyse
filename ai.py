import pandas as pd
import numpy as np
import sklearn
from sklearn import svm
from sklearn import linear_model
from sklearn.model_selection import train_test_split


def remove_useless_columns(data):
    del data['Club']
    # del data['Wage']
    # del data['Position']
    # del data['Preferred Foot']
    del data['Release Clause']
    # del data['Value']
    # del data['Nationality']
    # del data['Work Rate']
    return data


data = pd.read_csv("./data/data_ai_subset.csv", sep=";", index_col=0)
data = data.dropna()

remove_useless_columns(data)
features_data = pd.get_dummies(data, columns=['Wage', 'Position', 'Preferred Foot',
                                              'Value', 'Nationality', 'Work Rate'])
features_data = sklearn.utils.shuffle(features_data)

y = features_data['Price'].values
del features_data['Price']
X = features_data.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# clf = svm.SVC()
# clf.fit(X_train, y_train)
# print("Précision de :", int(clf.score(X_test, y_test)*100), "%")

reg = linear_model.LassoLars(max_iter=15, alpha=.1)
# reg = linear_model.Ridge(alpha=.5)
reg.fit(X_train, y_train)
print("Précision de :", int(reg.score(X_test, y_test)*100), "%")
# for X, y in zip(X_test, y_test):
#     print(f"Model: {reg.predict([X])[0]}, Actual: {y}")
