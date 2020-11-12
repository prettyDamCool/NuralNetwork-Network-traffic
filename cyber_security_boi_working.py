# -*- coding: utf-8 -*-
"""cyber_security_boi_working.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NX5BlSSR847fnISvddpd2nb0i1q2qip6
"""

import pandas as pd 
from sklearn.model_selection import train_test_split



# names of tables 
column_names = ["proto", "service", "state", "sbytes", "smean", "dinpkt", "dur", "ct_srv_src", "response_body_len", "ct_state_ttl", 'ct_dst_ltm','ct_src_dport_ltm', 'ct_dst_sport_ltm'
                , 'ct_dst_src_ltm', 'dload', 'sloss', 'dloss', 'sinpkt', 'sjit', 'swin', "attack_cat",]



data = pd.read_csv("UNSW_NB15_training-set-ERS4M.csv", header=None, names=column_names, na_values=['NA'],
sep =',', low_memory=False, encoding="utf-8")


# read data  
data.head()

y = data.attack_cat
#x = data.drop('attack_cat',axis=1)

#phas data
data.isna().sum()
attack_vector = pd.DataFrame(data.attack_cat.value_counts()).rename(columns={'traffic_type':'counts'})
attack_vector['percent'] = data.attack_cat.value_counts() / len(data) * 100
print(attack_vector)

print(data.groupby('attack_cat').size())

from sklearn.preprocessing import LabelEncoder #encodes data types
lb_encoder = LabelEncoder()
data['proto'] = lb_encoder.fit_transform(data['proto'])
data['service'] = lb_encoder.fit_transform(data['service'])
data['state'] = lb_encoder.fit_transform(data['state'])
data['sbytes'] = lb_encoder.fit_transform(data['sbytes'])
data['smean'] = lb_encoder.fit_transform(data['smean'])
data['dinpkt'] = lb_encoder.fit_transform(data['dinpkt'])
data['dur'] = lb_encoder.fit_transform(data['dur'])
data['ct_srv_src'] = lb_encoder.fit_transform(data['ct_srv_src'])
data['response_body_len'] = lb_encoder.fit_transform(data['response_body_len'])
data.fillna(data.mean(), inplace=True)

data['attack_cat'] = lb_encoder.fit_transform(data['attack_cat'].astype(str))
data['ct_state_ttl'] = lb_encoder.fit_transform(data['ct_state_ttl'])
data['ct_dst_ltm'] = lb_encoder.fit_transform(data['ct_dst_ltm'])
data['ct_src_dport_ltm'] = lb_encoder.fit_transform(data['ct_src_dport_ltm'])
data['ct_dst_sport_ltm'] = lb_encoder.fit_transform(data['ct_dst_sport_ltm'])
data['ct_dst_src_ltm'] = lb_encoder.fit_transform(data['ct_dst_src_ltm'])

data['dload'] = lb_encoder.fit_transform(data['dload'])
data['sloss'] = lb_encoder.fit_transform(data['sloss'])
data['dloss'] = lb_encoder.fit_transform(data['dloss'])
data['sinpkt'] = lb_encoder.fit_transform(data['sinpkt'])
data['dinpkt'] = lb_encoder.fit_transform(data['dinpkt'])
data['sjit'] = lb_encoder.fit_transform(data['sjit'])
data['swin'] = lb_encoder.fit_transform(data['swin'])
#ata['stcpb'] = lb_encoder.fit_transform(data['stcpb'])
#data['dtcpb'] = lb_encoder.fit_transform(data['dtcpb'])
#data['dwin'] = lb_encoder.fit_transform(data['dwin'])

"""test data"""

data_train = pd.read_csv("UNSW_NB15_testing-set-ERS4M.csv", header=None, names=column_names, na_values=['NA'],
sep =',', low_memory=False, encoding="utf-8-sig")
ytrain = data_train.attack_cat
data_train['proto'] = lb_encoder.fit_transform(data_train['proto'])
data_train['service'] = lb_encoder.fit_transform(data_train['service'])
data_train['state'] = lb_encoder.fit_transform(data_train['state'])
data_train['sbytes'] = lb_encoder.fit_transform(data_train['sbytes'])
data_train['smean'] = lb_encoder.fit_transform(data_train['smean'])
data_train['dinpkt'] = lb_encoder.fit_transform(data_train['dinpkt'])
data_train['dur'] = lb_encoder.fit_transform(data_train['dur'])
data_train['ct_srv_src'] = lb_encoder.fit_transform(data_train['ct_srv_src'])
data_train['response_body_len'] = lb_encoder.fit_transform(data_train['response_body_len'])
data_train.fillna(data_train.mean(), inplace=True)

data_train['attack_cat'] = lb_encoder.fit_transform(data_train['attack_cat'].astype(str))
data_train['ct_state_ttl'] = lb_encoder.fit_transform(data_train['ct_state_ttl'])
data_train['ct_dst_ltm'] = lb_encoder.fit_transform(data_train['ct_dst_ltm'])
data_train['ct_src_dport_ltm'] = lb_encoder.fit_transform(data_train['ct_src_dport_ltm'])
data_train['ct_dst_sport_ltm'] = lb_encoder.fit_transform(data_train['ct_dst_sport_ltm'])
data_train['ct_dst_src_ltm'] = lb_encoder.fit_transform(data_train['ct_dst_src_ltm'])

data_train['dload'] = lb_encoder.fit_transform(data_train['dload'])
data_train['sloss'] = lb_encoder.fit_transform(data_train['sloss'])
data_train['dloss'] = lb_encoder.fit_transform(data_train['dloss'])
data_train['sinpkt'] = lb_encoder.fit_transform(data_train['sinpkt'])
data_train['dinpkt'] = lb_encoder.fit_transform(data_train['dinpkt'])
data_train['sjit'] = lb_encoder.fit_transform(data_train['sjit'])
data_train['swin'] = lb_encoder.fit_transform(data_train['swin'])

train_array = data_train.values

train_array = data_train.values
array = data.values

x = array[:, 0:20]
Y = array[:, 20]
Xtrain = train_array[:, 0:20]
Ytrain = train_array[:, 20]
n_classes = array[:,0:1]

from sklearn.metrics import roc_curve, auc
from sklearn import datasets
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import LinearSVC
from sklearn.preprocessing import label_binarize
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

from sklearn.neural_network import MLPClassifier
from sklearn import metrics

clf = MLPClassifier(solver ='adam',alpha=1, activation='relu',
                     hidden_layer_sizes=(75,75,25,75,75), random_state=1)
clf.fit(x,Y)
prediction  = clf.predict(Xtrain)
print ("accuracy:", metrics.accuracy_score(Ytrain,prediction))
#metrics.log_loss(x)
