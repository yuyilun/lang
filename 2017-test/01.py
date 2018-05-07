# -*- coding: utf-8 -*-
"""
Created on Sun Apr 02 13:26:32 2017

@author: xyd-yuyilun
"""
#导入pandas 与 numpy 工具包
import pandas as pd
import numpy as np
#创建特征列表
column_names=['Sample code number','Clump Thickness','Uniformity of Cell Size','Uniformity of Cell Shape','Marginal Adhesion','Single Epithelial Cell Size','Bare Nuclei','Bland Chromatin','Normal Nucleoli','Mitoses','Class']
#shiyong padnas.read_csv hanshuconghulianwangduquzhidingshuju
data=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data',names=column_names)

#将？替换为标准缺失值表示
data=data.replace(to_replace='?',value=np.nan)
#丢弃带有缺失值的数据（只要有一个维度有缺失）
data=data.dropna(how='any')
#输出data的数据和维度
data.shape
#使用sklearn.cross_valiation里的tran_test_split模块用于分割数据
from sklearn.cross_validation import train_test_split
#随机采样25%的数据用于测试，剩下的75%用于构建训练集合
X_train,X_test,y_train,y_test=train_test_split(data[column_names[1:10]],data[column_names[10]],test_size=0.25,random_state=33)
#查验训练样本的数量和类别分布
y_train.value_counts()
y_test.value_counts()
#从sklearn.preprocessing导入StandardScaler
from sklearn.preprocessing import StandardScaler
#从
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
#标准化数据，保证每个维度的特征数据方差为了1，均值为0，使得预测结果不会被某些维度过大的特征值而主导
ss=StandardScaler()
X_train=ss.fit_transform(X_train)
X_test=ss.transform(X_test)

#初始化
lr=LogisticRegression()
sgdc=SGDClassifier()

#调用log**中的fit函数、模块用来训练模型参数
lr.fit(X_train,y_train)
#使用训练好的模型lr对X_test进行预测，结果存储在变量lr_y_predict中
lr_y_predict=lr.predict(X_test)
#调用SGDC***中的fit函数、模块用来训练模型参数
sgdc.fit(X_train,y_train)
#使用训练好的模型sgdc对x-test进行预测，结果存储在变量中
sgdc_y_predict=sgdc.predict(X_test)

from sklearn.metrics import classification_report
print 'Accuracy of LR Classifier:',lr.score(X_test,y_test)
print classification_report(y_test,lr_y_predict,target_names=['Benign','Malignant'])
 

print 'Accuracy of SGD Classifier:',sgdc.score(X_test,y_test)
print classification_report(y_test,sgdc_y_predict,target_names=['Benign','Malignant'])
 




