# Author: Mei-Ren Ke, An-Ting Hsieh
# Update: 2022/08/18 by Mei-Ren

import pandas as pd
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

# 1. 處理資料集，並分割成訓練和測試檔
dataset = pd.read_csv('svm_train_final.csv')
X = dataset.iloc[0:6876, 0:45]
Y = dataset.loc[:, ['ans']]

X_train, X_test, y_train, y_test = train_test_split(X, Y, stratify=Y, test_size=0.3)

# Important to scale
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# 2. 用訓練集（X_train和y_train）訓練model
clf = SVC(probability=True)
clf.fit(X_train, y_train.values.ravel())
pred = clf.predict(X_test)

# 3. 輸入測試矩陣，該矩陣是colorgram_output.py的輸出結果
C = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0897, 0.13319999999999999, 0, 0, 0.0351, 0, 0, 0, 0, 0.4212, 0, 0, 0, 0.32089999999999996, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
C = sc.transform([C])
pre1 = clf.predict(C)
print(pre1)
print('______________________________________________________')

# 4. print model的準確率等等
print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))
