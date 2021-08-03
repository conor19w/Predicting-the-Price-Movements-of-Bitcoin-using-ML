import pandas as pd
from joblib import dump, load
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
X=[]
z=[]

name="Bot1"  ##name of model we want to make
train="trainAv6minutestype2" ##which csv file we are training on
file=f'{train}.csv' ## read file from location need to change to directory of traintype2
data= pd.read_csv(file,sep=",")
X=data.drop({"z","Close"},axis=1) ##remove labels and closing price prevent data leakage
y=data["z"] ##store labels to check accuracy later

print(file)
TS=.001 ##How much of data to use in training, whats left will be used for testing
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test =train_test_split(X,y,train_size=TS,shuffle=True) ##split dataset into training and testing sets & the labels

##Imports for classifiers
from sklearn import tree, neighbors
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier


DT=1 ##turn on to create a Decision tree from the training data
if DT:
    model=tree.DecisionTreeClassifier(criterion='entropy')
    model.fit(X_train, y_train)     ##Fit model to training data
    dump(model, f'{name}.joblib')  ##Save model to current directory


SVM=0  ##turn on to create a Support vector Machine from the training data
if SVM:
    model = SVC()
    model.fit(X_train, y_train)     ##Fit model to training data
    dump(model, f'{name}.joblib')  ##Save model to current directory

NN=0  ##turn on to create a Neural Network from the training data
if NN:
    model = MLPClassifier(activation='relu',solver='adam',hidden_layer_sizes=(8,150))
    model.fit(X_train, y_train)     ##Fit model to training data
    dump(model, f'{name}.joblib')   ##Save model to current directory


NearestN=0  ##turn on to use Nearest neighboursto classify the training data
if NearestN:
    n_neighbors = 15  ##how many neighbours to compare to
    model = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors)
    model.fit(X_train, y_train)     ##Fit model to training data
    dump(model, f'{name}.joblib')   ##Save model to current directory

RF=0  ##turn on to create a Random Forest from the training data
if RF:
    model = RandomForestClassifier()
    model.fit(X_train, y_train)     ##Fit model to training data
    dump(model, f'{name}.joblib')   ##Save model to current directory


z_pred=model.predict(X_test) ## predict labels for test set
print("Accuracy: ",accuracy_score(y_pred=z_pred,y_true=y_test))  ##Print the Accuracy of the labels

day1=pd.read_csv(f'C:/Users/conor/Desktop/Final year project/Output/{train}.csv',sep=",")
day1X=day1.drop({"z","Close"},axis=1)
#day1y=day1["z"]
priceD1=day1["Close"]
day1_pred=pd.Series(model.predict(day1X),name="z_pred") ##predict on unshuffled data
result1=pd.concat([priceD1,day1_pred],axis=1) ##concatenate the price with corresponding predictions
day1=result1
#CloseD1= day1["Close"]
CloseD1=priceD1
#CloseD1= load('recentClose.joblib')
Day1_pred=day1["z_pred"]
Profit=0
currentPosition=-99
positionPrice=0
totalinvestment=0
tradeNO=0
profitgraph=[]  ## for graphing the profit

##Evaluate the profit of the model
for i in range(len(day1_pred)):
    if currentPosition==-99 and Day1_pred[i]==0:
        positionPrice=CloseD1[i]
        currentPosition=0
        tradeNO+=1
    elif currentPosition == -99 and Day1_pred[i] == 1:
        positionPrice = CloseD1[i]
        currentPosition = 1
        tradeNO += 1
    elif currentPosition==1 and Day1_pred[i]==0:
        Profit+=CloseD1[i]-positionPrice ##This will be positive if the price went up
        totalinvestment += abs(CloseD1[i] - positionPrice)
        positionPrice=CloseD1[i]
        profitgraph.append(Profit)
        currentPosition=0
        tradeNO += 1
    elif currentPosition == 0 and Day1_pred[i] == 1:
        Profit += positionPrice - CloseD1[i] ##This will be positive if the price went down
        totalinvestment += abs(positionPrice - CloseD1[i])
        positionPrice = CloseD1[i]
        profitgraph.append(Profit)
        currentPosition = 1
        tradeNO += 1
print(name)
print("Profit: ",Profit)
print("PV: ",(Profit/tradeNO)*100/50000) ##50000 max price of a bitcoin at the time


plt.plot(profitgraph,label="Profit",color="red")
plt.ylabel('Dollars')
plt.xlabel('Number of Trades')
plt.legend(loc=2)
plt.show()





## Below is used to run 10000 times and save the best model
'''
highestPV=(Profit/tradeNO)*100/60000

##Find best PV valued SVM:
for i in range(10000):
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=TS, shuffle=True)

    from sklearn.svm import SVC
    if SVM:
        model = SVC()
        model.fit(X_train, y_train)
    elif DT:
        model = tree.DecisionTreeClassifier(criterion='entropy')
        model.fit(X_train, y_train)
    elif NearestN:
        n_neighbors = 15
        model = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors)
        model.fit(X_train, y_train)

    elif NN:
        model = MLPClassifier(activation='relu', solver='adam', hidden_layer_sizes=(8,200))
        model.fit(X_train, y_train)
    elif RF:
        model = RandomForestClassifier(bootstrap=True,class_weight="balanced_subsample",max_features=None)
        model.fit(X_train, y_train)


    day1 = pd.read_csv(f'C:/Users/conor/Desktop/Final year project/Output/{train}.csv', sep=",")

    day1X = day1.drop({"z", "Close"}, axis=1)
    day1y = day1["z"]

    day1_pred = pd.Series(model.predict(day1X), name="z_pred")
    priceD1 = day1["Close"]

    result1 = pd.concat([priceD1, day1y, day1_pred], axis=1)

    day1 = result1
    CloseD1 = day1["Close"]
    # CloseD1= load('recentClose.joblib')
    Day1_pred = day1["z_pred"]
    Profit = 0
    currentPosition = -99
    positionPrice = 0
    totalinvestment = 0
    tradeNO = 0
    
    for j in range(len(day1_pred)):
        if currentPosition == -99 and Day1_pred[j] == 0:
            positionPrice = CloseD1[j]
            currentPosition = 0
            tradeNO += 1
        elif currentPosition == -99 and Day1_pred[j] == 1:
            positionPrice = CloseD1[j]
            currentPosition = 1
            tradeNO += 1
        elif currentPosition == 1 and Day1_pred[j] == 0:
            Profit += CloseD1[j] - positionPrice  ##This will be positive if the price went up
            totalinvestment += abs(CloseD1[j] - positionPrice)
            positionPrice = CloseD1[j]
            currentPosition = 0
            tradeNO += 1
        elif currentPosition == 0 and Day1_pred[j] == 1:
            Profit += positionPrice - CloseD1[j]  ##This will be positive if the price went down
            totalinvestment += abs(positionPrice - CloseD1[j])
            positionPrice = CloseD1[j]
            currentPosition = 1
            tradeNO += 1
    #print((Profit / tradeNO) * 100 / CloseD1[len(day1_pred)-1])
    if ((Profit/tradeNO)*100/60000)>highestPV:
        highestPV=(Profit/tradeNO)*100/60000
        dump(model, f'{name}.joblib')
        print(highestPV)

##100084
'''