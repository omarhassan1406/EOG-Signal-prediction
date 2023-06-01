import os
import numpy as np
import re

path = '3-class'
def Data_Preparation(path):
    all_signals = []
    for sig in os.listdir(path):
        dir = os.path.join(path , sig)
        bol = 0
        temp_signal = []
        lables = ''
        lable = re.split('\d+', sig)
        lable = lable[0]
        if lable == 'asagi':
            lables = 'down'
            bol = 1
        elif lable == 'kirp':
            lables = 'blink'
            bol = 1
        elif lable == 'sag':
            lables = 'right'
            bol = 1
        elif lable == 'sol':
            lables = 'left'
            bol = 1
        elif lable == 'yukari':
            lables = 'up'
            bol = 1
        if bol == 1:
            signal = open( '%s'%dir , 'r')
            lines = signal.readlines()
            for i in range(len(lines) - 1):
                L = lines[i + 1]
                temp_signal.append(int(L))
            all_signals.append([temp_signal , lables])


    #concatinating horizontal and vertical signals
    All_Signal = []
    for i in range(len(all_signals)):
        if i%2 == 0:
            for j in range(250):
                all_signals[i][0].append(all_signals[i + 1][0][j])
            All_Signal.append([all_signals[i][0] , all_signals[i][1]])
    return All_Signal



def Data_Preparation_gui(path1 , path2):
    all_signal = []
    signal_h = open( path1 , 'r')
    signal_v = open(path2 , 'r')
    lines_h = signal_h.readlines()
    for i in range(len(lines_h) - 1):
        L = lines_h[i + 1]
        all_signal.append(int(L))
    lines_v = signal_v.readlines()
    for i in range(len(lines_v) - 1):
        L = lines_v[i + 1]
        all_signal.append(int(L))

    return all_signal


# up = 0
# down = 0
# right = 0
# left =0
# blink = 0

# for i in all_signals:
#     if i[1] =='up':
#         up+=1
#     elif i[1] =='down':
#         down+=1
#     elif i[1] =='right':
#         right+=1
#     elif i[1] =='left':
#         left+=1
#     elif i[1] =='blink':
#         blink+=1
#
# print('Number of Documents in each Class')
# print("Up = " + str (up/2))
# print("Down = " + str (down/2))
# print("Right = " + str (right/2))
# print("Left = " + str (left/2))
# print("blink = " + str (blink/2))
#
# up = down = blink = left = right = 0
#
# Train_data = []
# Test_data = []
#
# for signal in All_Signal:
#     if signal[1] == 'up' and up < 5:
#         Test_data.append(signal)
#         up +=1
#     elif signal[1] == 'down' and down < 5:
#         Test_data.append(signal)
#         down+=1
#     elif signal[1] == 'right' and right < 5:
#         Test_data.append(signal)
#         right += 1
#     elif signal[1] == 'left' and left < 5:
#         Test_data.append(signal)
#         left += 1
#     elif signal[1] == 'blink' and blink < 5:
#         Test_data.append(signal)
#         blink += 1
#     else:
#         Train_data.append(signal)
#

# print()
# print('Length of Training Data (75%) = ' + str(len(Train_data)))
# print('Length og Testing Data (25%) = ' + str(len(Test_data)))

# np.save('Train_data.npy' , (Train_data))
# np.save('Test_data.npy' , (Test_data))

