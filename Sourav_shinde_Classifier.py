import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn import neighbors
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import f1_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn import svm
#from sklearn. import SVC
import sys

def knn(students_data):
    X = students_data[['Major/Area of Study', 'CGPA/ percentage', 'Areas of interest', 'Have you worked core Java',
                         'Programming Language Known other than Java (one major)',
                      'Have you worked on MySQL or Oracle database', 'Have you studied OOP Concepts',
                       'Rate your written communication skills [1-10]', 'Rate your verbal communication skills [1-10]',
                      'Male', 'Fourth-year', 'Second-year', 'Third-year']]
    y = students_data["eligible"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)

    sc = StandardScaler()
    X_train_std = sc.fit_transform(X_train)
    X_test_std = sc.transform(X_test)
    clf = neighbors.KNeighborsClassifier()
    clf.fit(X_train_std, y_train)
   # print(clf)
    y_except = y_test
    y_pred = clf.predict(X_test)
    print(metrics.classification_report(y_except, y_pred))

    print(f1_score(y_except, y_pred))


def logistic(students_data):
    X = students_data.drop("eligible", axis=1)
    y = students_data["eligible"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

    sc = StandardScaler()
    X_train_std = sc.fit_transform(X_train)
    X_test_std = sc.transform(X_test)
    logmodel = LogisticRegression()

    logmodel.fit(X_train_std, y_train)
    predictions = logmodel.predict(X_test_std)
    classification_report(y_test, predictions)
    confusion_matrix(y_test, predictions)
    accuracy_score(y_test, predictions)
    print((f1_score(y_test, predictions)*100))

def svm(students_data):
    X = students_data.drop("eligible", axis=1)
    y = students_data["eligible"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)
    sc = StandardScaler()
    X_train_std = sc.fit_transform(X_train)
    X_test_std = sc.transform(X_test)
    classifier = svm.SVC(kernel='linear', gamma='auto', C=2)
    classifier.fit(X_train_std, y_train)
    y_predict = classifier.predict(X_test_std)
    print(f1_score(y_test, y_predict))



if __name__ == "__main__":
    students_data = pd.read_csv(sys.argv[1])
    students_data.head(10)
    students_data.drop("link to Linkedin profile", axis=1, inplace=True)
    students_data.drop("Certifications/Achievement/ Research papers", axis=1, inplace=True)
    students_data.drop("Link to updated Resume (Google/ One Drive link preferred)", axis=1, inplace=True)
    students_data.head()

    gender = pd.get_dummies(students_data['Gender'], drop_first=True)
    students_data=pd.concat([students_data,gender],axis=1)
    students_data.head()
    students_data.drop('Gender', axis=1, inplace=True)
    label = pd.get_dummies(students_data['Label'])
    label.head()
    students_data = pd.concat([students_data, label], axis=1)
    students_data.head()
    students_data.drop(['Label', 'ineligible'], axis=1)
    year = pd.get_dummies(students_data["Which-year are you studying in?"], drop_first=True)
    year.head()
    students_data = pd.concat([students_data, year], axis=1)
    students_data.drop('Which-year are you studying in?', axis=1, inplace=True)

    label_encoder = preprocessing.LabelEncoder()
    students_data['Major/Area of Study'] = label_encoder.fit_transform(students_data['Major/Area of Study'])
    students_data['Areas of interest'] = label_encoder.fit_transform(students_data['Areas of interest'])
    students_data['Have you worked core Java'] = label_encoder.fit_transform(students_data['Have you worked core Java'])
    students_data['Programming Language Known other than Java (one major)'] = label_encoder.fit_transform(students_data['Programming Language Known other than Java (one major)'])
    students_data['Have you worked on MySQL or Oracle database'] = label_encoder.fit_transform(students_data['Have you worked on MySQL or Oracle database'])
    students_data['Have you studied OOP Concepts'] = label_encoder.fit_transform(students_data['Have you studied OOP Concepts'])
    students_data.head()
    students_data.drop(
        ["State", "First Name", "Last Name", "Zip Code", "DOB [DD/MM/YYYY]", "Email Address", "Contact Number",
         "Emergency Contact Number", "Course Type", "Current Employment Status"], axis=1, inplace=True)
    students_data.head()
    students_data.drop(["City", "Age", "College name", "University Name", "How Did You Hear About This Internship?"],
                       axis=1, inplace=True)
    students_data.drop(["Degree", "Expected Graduation-year", "ineligible", "Label"], axis=1, inplace=True)
    #knn(students_data)

    logistic(students_data)
    #svm(students_data)
   # svm(students_data)



















