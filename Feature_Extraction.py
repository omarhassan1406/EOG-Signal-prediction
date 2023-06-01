import numpy as np
from scipy.signal import find_peaks
import scipy.integrate as integrate
from statsmodels.tsa.ar_model import AutoReg
from pywt import wavedec
import pywt
import matplotlib.pyplot as plt

#Train

#MORPHOLOGICAL FEATURES
Data = np.load('Preprocessing_train2.npy' , allow_pickle=True)


def Feature_Extraction(signal):
    I_h = integrate.simpson(signal[0])
    I_v = integrate.simpson(signal[1])
    peaks_h,_ = find_peaks(signal[0])
    peaks_v, _ = find_peaks(signal[1])
    Y_h= []
    Y_v =[]
    for i in range(len(peaks_h)-1):
        L = peaks_h[i]
        Y_h.append(signal[0][L])
    for i in range(len(peaks_v)-1):
        L = peaks_v[i]
        Y_v.append(signal[1][L])
    peak_value_h = max(Y_h)
    peak_value_v = max(Y_v)

    feature_1_h = peak_value_h
    feature_2_h = I_h

    feature_1_v = peak_value_v
    feature_2_v = I_v

    model_h = AutoReg(signal[0] , lags = 4)
    model_fit_h = model_h.fit()
    feature_3_h = model_fit_h.params

    model_v = AutoReg(signal[1], lags=4)
    model_fit_v = model_v.fit()
    feature_3_v = model_fit_v.params

    coff_h = wavedec(signal[0], 'db1', level=4)
    feature_4_h =  pywt.waverec([coff_h[0] , coff_h[1]] ,  'db1')



    coff_v = wavedec(signal[1], 'db1', level=4)
    feature_4_v = pywt.waverec([coff_v[0],coff_v[1]], 'db1')


    signal_features = ([feature_1_h , feature_2_h , feature_3_h , feature_4_h , feature_1_v , feature_2_v , feature_3_v , feature_4_v , signal[2]])
    return signal_features

def Feature_Extraction_gui(signal):
    I_h = integrate.simpson(signal[0])
    I_v = integrate.simpson(signal[1])
    peaks_h,_ = find_peaks(signal[0])
    peaks_v, _ = find_peaks(signal[1])
    Y_h= []
    Y_v =[]
    for i in range(len(peaks_h)-1):
        L = peaks_h[i]
        Y_h.append(signal[0][L])
    for i in range(len(peaks_v)-1):
        L = peaks_v[i]
        Y_v.append(signal[1][L])
    peak_value_h = max(Y_h)
    peak_value_v = max(Y_v)

    feature_1_h = peak_value_h
    feature_2_h = I_h

    feature_1_v = peak_value_v
    feature_2_v = I_v

    model_h = AutoReg(signal[0] , lags = 4)
    model_fit_h = model_h.fit()
    feature_3_h = model_fit_h.params

    model_v = AutoReg(signal[1], lags=4)
    model_fit_v = model_v.fit()
    feature_3_v = model_fit_v.params

    coff_h = wavedec(signal[0], 'db1', level=4)
    feature_4_h =  pywt.waverec([coff_h[0] , coff_h[1]] ,  'db1')



    coff_v = wavedec(signal[1], 'db1', level=4)
    feature_4_v = pywt.waverec([coff_v[0],coff_v[1]], 'db1')


    signal_features = ([feature_1_h , feature_2_h , feature_3_h , feature_4_h , feature_1_v , feature_2_v , feature_3_v , feature_4_v])
    return signal_features


#Train
# All_signal_features_train = []
# for signal in Data:
#     signal_features = Feature_Extraction(signal)
#     All_signal_features_train.append(signal_features)
# np.save('Train_All_features2.npy' , All_signal_features_train)
#

# Test
# All_signal_features_test = []
# Data = np.load('Preprocessing_test2.npy' , allow_pickle=True)

# for signal in Data:
#     signal_features = Feature_Extraction(signal)
#     All_signal_features_test.append(signal_features)
# np.save('Test_All_features2.npy' , All_signal_features_test)




