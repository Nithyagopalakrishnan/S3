from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
iris=load_iris()
x=iris.data
y=iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)
c_knn=KNeighborsClassifier(n_neighbors=3)
c_knn.fit(x_train,y_train)
y_pred=c_knn.predict(x_test)
print("Accuracy:",metrics.accuracy_score(y_test,y_pred))
print("Enter the sample code")
a=float(input("Enter sepal length in cm :"))
b=float(input("Enter sepal width in cm :"))
c=float(input("Enter petal length in cm :"))
d=float(input("Enter petal width in cm :"))
sample = [[a,b,c,d]]
pred = c_knn.predict(sample) # c_knn is now defined and trained
print(pred)
pred_v = [iris.target_names[p] for p in pred]
print(pred_v)
