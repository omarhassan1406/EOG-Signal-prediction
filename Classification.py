from sklearn.naive_bayes import MultinomialNB
import numpy as np
from sklearn import metrics
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier

all_features = np.load('Train_All_features2.npy' , allow_pickle=True)
test_all_features = np.load('Test_All_features2.npy' , allow_pickle=True)

np.random.shuffle(all_features)
def Classification(all_features):
  max_peak_h = []
  area_under_curve_h = []
  autoreg_features_h = []
  wavelet_coff_h = []
  max_peak_v = []
  area_under_curve_v = []
  autoreg_features_v = []
  wavelet_coff_v =[]
  labels=[]

  for feature in all_features:
    max_peak_h.append(feature[0])
    area_under_curve_h.append(feature[1])
    autoreg_features_h.append(feature[2])
    wavelet_coff_h.append(feature[3])
    max_peak_v.append(feature[4])
    area_under_curve_v.append(feature[5])
    autoreg_features_v.append(feature[6])
    wavelet_coff_v.append(feature[7])
    labels.append(feature[8])



  Train_data = []

  for i in range(len(all_features)):
    vector = []
    vector.append(max_peak_h[i])
    vector.append(area_under_curve_h[i])
    for j in range(len(autoreg_features_h[i])):
      vector.append(autoreg_features_h[i][j])
    for j in range(len(wavelet_coff_h[i])):
      vector.append(wavelet_coff_h[i][j])
    vector.append(max_peak_v[i])
    vector.append(area_under_curve_v[i])
    for j in range(len(autoreg_features_v[i])):
      vector.append(autoreg_features_v[i][j])
    for j in range(len(wavelet_coff_v[i])):
      vector.append(wavelet_coff_v[i][j])

    Train_data.append(vector)
  # Train_data = np.array(Train_data)
  # Train_data =Train_data.reshape(-1 , (len(autoreg_features_h[0] +len(autoreg_features_v[0])+4)))


  Labels = []
  for i in labels:
    if i == 'up':
      Labels.append(0)
    elif i == 'down':
      Labels.append(1)
    elif i == 'right':
      Labels.append(2)
    elif i == 'left':
      Labels.append(3)
    elif i == 'blink':
      Labels.append(4)
  return Train_data , Labels


def Classification_gui(all_features):
  max_peak_h = []
  area_under_curve_h = []
  autoreg_features_h = []
  wavelet_coff_h = []
  max_peak_v = []
  area_under_curve_v = []
  autoreg_features_v = []
  wavelet_coff_v =[]

  for feature in all_features:
    max_peak_h.append(feature[0])
    area_under_curve_h.append(feature[1])
    autoreg_features_h.append(feature[2])
    wavelet_coff_h.append(feature[3])
    max_peak_v.append(feature[4])
    area_under_curve_v.append(feature[5])
    autoreg_features_v.append(feature[6])
    wavelet_coff_v.append(feature[7])



  Train_data = []

  for i in range(len(all_features)):
    vector = []
    vector.append(max_peak_h[i])
    vector.append(area_under_curve_h[i])
    for j in range(len(autoreg_features_h[i])):
      vector.append(autoreg_features_h[i][j])
    for j in range(len(wavelet_coff_h[i])):
      vector.append(wavelet_coff_h[i][j])
    vector.append(max_peak_v[i])
    vector.append(area_under_curve_v[i])
    for j in range(len(autoreg_features_v[i])):
      vector.append(autoreg_features_v[i][j])
    for j in range(len(wavelet_coff_v[i])):
      vector.append(wavelet_coff_v[i][j])

    Train_data.append(vector)
  # Train_data = np.array(Train_data)
  # Train_data =Train_data.reshape(-1 , (len(autoreg_features_h[0] +len(autoreg_features_v[0])+4)))

  return Train_data
# Train_data , Labels = Classification(all_features)
# Test_data , labels = Classification(test_all_features)



# model = SVC(C=1, kernel='linear')
# model.fit(Train_data,Labels)
# ypred = model.predict(Test_data)
# Accuracy = metrics.accuracy_score(labels,ypred)
# print("SVM Accuracy = " + str(Accuracy))

# model2 = linear_model.LogisticRegression(C=1.5)
# model2.fit(Train_data,Labels)
# y2_predict = model2.predict(Test_data)
# Accuracy2 = metrics.accuracy_score(labels,y2_predict)
# print("Logistic Accuracy = " + str(Accuracy2))

# model3 = RandomForestClassifier()
# model3.fit(Train_data,Labels)
# model3 = pickle.load(open('Random_forest_2.sav' , 'rb'))
# y3_predict = model3.predict(Test_data)
# Accuracy3 = metrics.accuracy_score(labels,y3_predict)
# print("Random Forest Accuracy = " + str(Accuracy3*100))




