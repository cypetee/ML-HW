# Load libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation
from sklearn import tree
import matplotlib.pyplot as plt

col_names = ['ID #','Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape', 'Marginal Adhesion', 'Single Epithelial', 'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli', 'Mitosis','Class']
# load dataset
DataTrain = pd.read_excel(r'C:\Users\twg\Desktop\NoRowTrain.xlsx', header=None, names=col_names)
DataTest = pd.read_excel(r'C:\Users\twg\Desktop\NoRowTest.xlsx', header=None, names=col_names)
DataValid = pd.read_excel(r'C:\Users\twg\Desktop\NoRowValidation.xlsx', header=None, names=col_names)

#split dataset in features and target variable
feature_cols = ['Clump Thickness', 'Uniformity of Cell Size', 'Uniformity of Cell Shape', 'Marginal Adhesion', 'Single Epithelial', 'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli', 'Mitosis']
X_train = DataTrain[feature_cols] # Features
y_train = DataTrain.Class # Target variable
X_test = DataTrain[feature_cols] # Features
y_test = DataTrain.Class # Target variable
# Split dataset into training set and test set

# Create Decision Tree classifer object with depth of tree
clf = DecisionTreeClassifier(max_depth=(3))

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)


# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))


plt.figure(figsize=(12,12))  # set plot size (denoted in inches)
tree.plot_tree(clf, fontsize=10)


