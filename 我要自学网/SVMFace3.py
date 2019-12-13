#-*- coding:utf-8 -*-
from __future__ import print_function#解决python2中的print问题
from time import time#记录每段处理花费的时间
import logging#记录进展的状况
import matplotlib.pyplot as plt
from  sklearn.model_selection import train_test_split#分割数据集
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.datasets import fetch_lfw_people#用来下载数据
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import PCA
from sklearn.svm import SVC#支持向量机

print(__doc__)#输出文件开头注释的内容
logging.basicConfig(level=logging.INFO,format='%(asctime)s%(message)s')#INFO是指日志按照预处理进行 asctime指进展时间 message指进展内容
lfw_people=fetch_lfw_people(min_faces_per_person=70,resize=0.6)#下载并导入数据
n_samples,h,w=lfw_people.images.shape
#print(lfw_people)
#print(n_samples)#样本大小
# print(h)#图片的多少
# print(w)#维度
X=lfw_people.data#数据矩阵
#print(X)#
n_features=X.shape[1]#维度大小
#print(n_features)
Y=lfw_people.target#不同人的身份
target_names=lfw_people.target_names#特征向量的类别名 也就是对应的人名
n_class=target_names.shape[0]#有几个人要区分识别
# print(Y)
# print(target_names)
# print(n_class)

X_train,X_test,Y_train,Y_test=train_test_split(#train_test_split是sklearn自带的一种划分数据的函数
    X,Y,test_size=0.65,random_state=49
)#训练集 测试集 训练集的label 测试集的label
# print(X_train)
# print(X_test)
# print(Y_train)
# print(Y_test)

#PCA降维
n_components=150#设置一个参数来进行降维炒作
print("Extracting the top %d eigenfaces from %d faces"
      % (n_components, X_train.shape[0]))
t0=time()
pca=PCA(n_components=n_components,svd_solver='randomized',
        whiten=True).fit(X_train)#降维并建立训练集模型
print("done in %0.3fs" % (time() - t0))#该过程花费多少时间

#print(pca)
eigenfaces=pca.components_.reshape((n_components,h,w))#人脸上的一些特征值
print("Projecting the input data on the eigenfaces orthonormal basis")
t0=time()
X_train_pca=pca.transform(X_train)#训练集转低维训练集
X_test_pca=pca.transform(X_test)#测试集转低维测试集
print("done in %0.3fs" % (time() - t0))

print("Fitting the classifier to the training set")
t0=time()
param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5],
              'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }#gamma特征函数来建立不同的比例的核函数 对分类的精度来对比尝试来组成的精度
clf=GridSearchCV(SVC(kernel='rbf',class_weight='balanced'),
                 param_grid,cv=5)#rbf用来处理图像的特征点,class_weight权重 param_grid核函数
#print("clf:",clf)
clf=clf.fit(X_train_pca,Y_train)#高维度建模
print("done in %0.3fs" % (time() - t0))
print("Best estimator found by grid search:")
print(clf.best_estimator_)
#进行预测和真实值之间的比较
print("Predicting people's names on the test set")
t0=time()
Y_pred=clf.predict(X_test_pca)
print("done in %0.3fs" % (time() - t0))

print(classification_report(Y_test, Y_pred, target_names=target_names))
print(confusion_matrix(Y_test, Y_pred, labels=range(n_class)))

def plot_gallery(images,titles,h,w,n_row=3,n_col=4):
    """Helper function to plot a gallery of portraits"""
    plt.figure(figsize=(1.8 * n_col,2.4 * n_row))
    plt.subplots_adjust(bottom=0,left=.01,right=.99,top=.90,hspace=.35)
    for i in range(n_row * n_col):
        plt.subplot(n_row,n_col,i+1)
        plt.imshow(images[i].reshape((h,w)),cmap=plt.cm.gray)
        plt.title(titles[i], size=12)
        plt.xticks(())
        plt.yticks(())

def title(Y_pred,Y_test,target_names,i):
    pred_name = target_names[Y_pred[i]].rsplit(' ', 1)[-1]
    true_name = target_names[Y_test[i]].rsplit(' ', 1)[-1]
    return 'predicted: %s\ntrue:      %s' % (pred_name, true_name)
prediction_titles = [title(Y_pred, Y_test, target_names, i)
                     for i in range(Y_pred.shape[0])]
plot_gallery(X_test,prediction_titles,h,w)

eigenface_titles=["eigenface %d" % i for i in range(eigenfaces.shape[0])]
plot_gallery(eigenfaces,eigenface_titles,h,w)
plt.show()