import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix,accuracy_score,f1_score
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
data= pd.read_csv('C:/Users/conor/Desktop/Final year project/Output/traintype1.csv',sep=",") ## change to file location, traintype1 included in python scripts folder
X=data.drop({"z","Close"},axis=1)
z=data['z']
X_train,X_test,z_train,z_test =train_test_split(X,z,train_size=.3)

##Nearest Neighbours
nearest=neighbors.KNeighborsClassifier(n_neighbors=15)
nearest.fit(X_train,z_train)
##Support vector machine
svclassifier=SVC()
svclassifier.fit(X_train,z_train)
##Neural Network
NN=MLPClassifier(activation='relu',solver='adam',hidden_layer_sizes=(6,300))
NN.fit(X_train,z_train)
##Decision Tree
DT=tree.DecisionTreeClassifier(criterion='entropy')
DT.fit(X_train,z_train)
RF = RandomForestClassifier(bootstrap=True,class_weight="balanced_subsample")#,max_features=None)
RF.fit(X_train, z_train)

z_pred_nearest=nearest.predict(X_test)
z_pred_SVM = svclassifier.predict(X_test)
z_pred_NN = NN.predict(X_test)
z_pred_DT = DT.predict(X_test)
z_pred_RF = RF.predict(X_test)

Accuracy_nearest=accuracy_score(y_pred=z_pred_nearest,y_true=z_test)
Accuracy_SVM=accuracy_score(y_pred=z_pred_SVM,y_true=z_test)
Accuracy_NN=accuracy_score(y_pred=z_pred_NN,y_true=z_test)
Accuracy_DT=accuracy_score(y_pred=z_pred_DT,y_true=z_test)
Accuracy_RF=accuracy_score(y_pred=z_pred_RF,y_true=z_test)
print("Nearest N Acc: ",Accuracy_nearest)
print("SVM Acc: ",Accuracy_SVM)
print("NN Acc: ",Accuracy_NN)
print("DT Acc: ",Accuracy_DT)
print("RF Acc: ",Accuracy_RF)
##Confusion matrices
print("Nearest Neighbour: ",confusion_matrix(y_true=z_test, y_pred=z_pred_nearest))
print("SVM: ",confusion_matrix(y_true=z_test, y_pred=z_pred_SVM))
print("Neural Network: ",confusion_matrix(y_true=z_test,y_pred= z_pred_NN))
print("Decision Tree: ",confusion_matrix(y_true=z_test,y_pred= z_pred_DT))
print("Random Forest: ",confusion_matrix(y_true=z_test,y_pred= z_pred_RF))

##Graph Results
objects = ('Nearest Neighbours', 'SVM', 'Neural Network', 'Decision Tree','Random Forest')
y_pos = np.arange(len(objects))
plt.yticks(y_pos, objects)
plt.xlabel('Accuracy %')
plt.title('ML Algorithms')
performance = [Accuracy_nearest,Accuracy_SVM,Accuracy_NN,Accuracy_DT,Accuracy_RF]
plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.show()
