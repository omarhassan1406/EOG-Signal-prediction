from Data import Data_Preparation_gui
from Preprocessing import Signal_preprocessing_gui
from Feature_Extraction import Feature_Extraction_gui
from Classification import Classification_gui
import pickle
import numpy as np

path = 'Test'
def Model_main(path1 , path2):
    move = ''
    Data = Data_Preparation_gui(path1 , path2)
    F_signal_h , F_signal_v = Signal_preprocessing_gui(Data)
    Filtered_signal = ([F_signal_h , F_signal_v ])
    Signal_Features = Feature_Extraction_gui(Filtered_signal)
    Signal_Features = ([Signal_Features])
    Test_data  = Classification_gui(Signal_Features)
    Model = pickle.load(open('Random_forest_2.sav' , 'rb'))
    prediction_Lable = Model.predict(Test_data)
    if prediction_Lable == 0:
        move = 'Up'
    elif prediction_Lable == 1:
        move = 'Down'
    elif prediction_Lable == 2:
        move = 'Right'
    elif prediction_Lable == 3:
        move = 'Left'
    elif prediction_Lable == 4:
        move = 'Blink'
    return move


