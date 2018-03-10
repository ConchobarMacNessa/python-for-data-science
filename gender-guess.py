from sklearn import tree, neighbors, linear_model, naive_bayes, ensemble

# define classifiers
clf = tree.DecisionTreeClassifier()
neigh = neighbors.KNeighborsClassifier(n_neighbors=3)
logist = linear_model.LogisticRegression()
gnb = naive_bayes.GaussianNB()
rfc = ensemble.RandomForestClassifier(n_estimators=2)

classifiers = [clf, neigh, logist, gnb, rfc]

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female', 'female', 'male', 'male']

# ...and train them on our data
testCase = [[156, 53, 38], [178, 82, 48]]

for case in classifiers:
    case = case.fit(X,Y)
    prediction = case.predict(testCase)
    print(prediction)