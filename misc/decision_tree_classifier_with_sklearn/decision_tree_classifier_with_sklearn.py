"""Decision Tree Classifier with Iris dataset"""

import random
from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
from sklearn import tree

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


iris = datasets.load_iris()
x = iris.data
y = iris.target

# split to 80% training, 20% validation
random.seed(0)
train_idx = random.sample([i for i in range(len(x))], int(0.8 * len(x)))
validation_idx = [i for i in range(len(x)) if not i in train_idx]
print(f"traing dataset is {train_idx}")
print(f"testing dataset is {validation_idx}")

# train and validation idx cover the full range of possible idx [0, 149]
print(sorted(train_idx + validation_idx) == [i for i in range(len(x))])

# 'train' for traing dataset
# x_train for training features(SL, SW, PL, PW)
# y_train for training labels(species)
x_train, y_train = x[train_idx], y[train_idx]

# 'validation' for testing dataset
# x_validation for testing features(SL, SW, PL, PW)
# y_validation for testing labels(species)
x_validation, y_validation = x[validation_idx], y[validation_idx]

data1 = pd.DataFrame(
    data=np.c_[iris["data"], iris["target"]],
    columns=iris["feature_names"] + ["species"],
)

data1.head()

clf = DecisionTreeClassifier(criterion="gini", random_state=0)

model = clf.fit(x_train, y_train)

text_representation = tree.export_text(clf)
fig = plt.figure(figsize=(25, 20))
_ = tree.plot_tree(
    clf,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True,
)

# try it out with some random data
observation = [[5, 4, 3, 2]]

# Predict observation's class
model.predict(observation)
# ['setosa','versicolor','virginica']

# View predicted class probabilities for the three classes
model.predict_proba(observation)
# ['setosa','versicolor','virginica']


# Let's look at some predictions for the input training data:
for i, obs in enumerate(x_train):

    # print(model.predict_proba(obs.reshape(1,-1)))
    pred = model.predict(obs.reshape(1, -1))
    print(
        f"({i})".ljust(5)
        + " | "
        + "".join("{}: {} | ".format(*k) for k in zip(data1.columns[:4], obs))
        + f"species: {y_train[i]} | "
        + f"prediction: {pred[0]} | "
        # + f'predict_proba: {model.predict_proba(obs.reshape(1,-1))} | '
        + (
            "(Correct)".ljust(len("Incorrect"))
            if y_train[i] == pred
            else "(Incorrect)"
        )
    )

# Notably, all leaves of the decision classifier tree show Gini impurity of 0,
# so all predictions using the training data are correct

# how does the model do for the validation data set?
for i, obs in enumerate(x_validation):
    pred = model.predict(obs.reshape(1, -1))
    print(
        f"({i})".ljust(5)
        + " | "
        + "".join("{}: {} | ".format(*k) for k in zip(data1.columns[:4], obs))
        + f"species: {y_validation[i]} | "
        + f"prediction: {pred[0]} | "
        + (
            "(Correct)".ljust(len("Incorrect"))
            if y_validation[i] == pred
            else "(Incorrect)"
        )
    )

# So the example our model predict as incorrect is :
# sepal length (cm): 6.0 | sepal width (cm): 2.2 | petal length (cm): 5.0
#   | petal width (cm): 1.5 | species: 2 | prediction: 1 | (Incorrect)
print(
    "For species 2 in training dataset:\n mean "
    + "\n mean ".join(
        "{:19}: {}".format(*_)
        for _ in [
            (
                label,
                data1.iloc[train_idx].loc[data1["species"] == 2][label].mean(),
            )
            for label in data1.columns[:4]
        ]
    ).ljust(25)
)
print(
    " stdev "
    + "\n stdev ".join(
        "{:18}: {}".format(*_)
        for _ in [
            (
                label,
                data1.iloc[train_idx].loc[data1["species"] == 2][label].std(),
            )
            for label in data1.columns[:4]
        ]
    ).ljust(25)
)

# mean -/+ 2 sigma covers 95% of the population

# sepal length
minSL = round(6.625641025641025 - 2 * (0.6463329550618013), 2)
maxSL = round(6.625641025641025 + 2 * (0.6463329550618013), 2)
print("\nsepal length (cm): 6.0")
print(f"95% of sepal length is in {minSL} to {maxSL}")

# sepal width
minSW = round(3.0230769230769226 - 2 * (0.30989093027058345), 2)
maxSW = round(3.0230769230769226 + 2 * (0.30989093027058345), 2)
print("\n!!sepal width (cm): 2.2")
print(f"95% of sepal width is in {minSW} to {maxSW}")

# petal length
minPL = round(5.592307692307692 - 2 * (0.5814612334385697), 2)
maxPL = round(5.592307692307692 + 2 * (0.5814612334385697), 2)
print("\npetal length (cm): 5.0")
print(f"95% of petal length is in {minPL} to {maxPL}")

# petal width
minPW = round(2.0205128205128196 - 2 * (0.2647535966452055), 2)
maxPW = round(2.0205128205128196 + 2 * (0.2647535966452055), 2)
print("\npetal width (cm): 1.5")
print(f"95% of petal width is in {minPW} to {maxPW}")

# Note that the failing case has:
#     - sepal width 2.2 cm
# So this is an outlier case, and comparing in the decision tree printout we can
# see the misclassification happens exactly at the test of sepal width <= 3.1 cm

# 1 sigma, 2 sigma, 3 sigma 'rule'
# 68–95–99.7 rule
# integral of bell curve from -1*sigma to +1*sigma = 0.68
# integral of bell curve from -2*sigma to +2*sigma = 0.95
# integral of bell curve from -3*sigma to +3*sigma = 0.997
