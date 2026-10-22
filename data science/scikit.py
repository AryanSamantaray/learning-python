from sklearn import tree
#height,weight,shoe size
X = [
    [170, 68, 9], [162, 57, 7], [183, 82, 11], [175, 73, 10], [158, 52, 6],
    [178, 76, 10], [166, 61, 8], [188, 91, 12], [155, 49, 6], [172, 70, 9],
    [181, 79, 11], [164, 59, 7], [176, 74, 10], [160, 54, 6], [185, 86, 12],
    [168, 64, 8], [173, 72, 9], [157, 51, 6], [190, 94, 13], [163, 56, 7],
    [179, 77, 10], [169, 66, 8], [182, 83, 11], [161, 55, 7], [174, 71, 9],
    [186, 88, 12], [159, 53, 6], [177, 75, 10], [167, 63, 8], [184, 85, 11],
]
Y = [
    'male', 'female', 'male', 'male', 'female', 'male', 'female', 'male', 'female', 'female',
    'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female', 'male', 'female',
    'male', 'female', 'male', 'female', 'male', 'male', 'female', 'male', 'female', 'male',
]
clf=tree.DecisionTreeClassifier()
clf=clf.fit(X,Y)
prediction=clf.predict([[170, 42, 7]])
print(prediction)