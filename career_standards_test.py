import numpy as np

def CST(data):
    data[1] = np.floor((data['H'] - 1500) / 150).clip(0, 10)
    data[2] = np.floor(((data['H'] / data['AB']) - 0.275)/0.005).clip(0,9)
    data[3] = np.ceil((data['H'] / data['AB']) - 0.3).clip(0,1)
    data[4] = np.floor((data['R'] - 900) / 100).clip(0, 8)
    data[5] = np.ceil(((data['R'] / data['G']) - 0.500)).clip(0,1)
    data[6] = np.ceil(((data['R'] / data['G']) - 0.644)).clip(0,1)
    data[7] = np.floor((data['RBI'] - 800) / 100).clip(0, 8)
    data[8] = np.ceil(((data['RBI'] / data['G']) - 0.500)).clip(0,1)
    data[9] = np.ceil(((data['RBI'] / data['G']) - 0.600)).clip(0,1)
    data[10] = np.floor((((data['H'] + 2*data['2B'] + 3*data['3B'] + 4*data['HR'])/data['AB']) - 0.3)/0.025).clip(0,10)
    data[11] = np.floor((((data['H'] + data['BB'] + data['HBP'])/(data['AB'] + data['BB'] + data['HBP'] + data['SF'])) - 0.3)/0.01).clip(0,10)
    data[12] = np.floor(data['HR'] / 200)
    data[13] = np.ceil(((data['HR'] / data['H']) - 0.1)).clip(0,1)
    data[14] = np.ceil(((data['HR'] / data['H']) - 0.2)).clip(0,1)
    data[15] = np.floor(((data['2B'] + data['3B'] + data['HR']) - 300) / 200).clip(0, 5)
    data[16] = np.floor((data['BB'] - 300) / 200).clip(0, 5)
    data[17] = np.floor(data['SB'] / 100).clip(0, 5)
    
    data['CST'] = data[1]
    for i in range(16):
        data['CST'] += data[i + 2]
    data['CST'] = data['CST'].fillna(0)
    
    data = data.drop([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] , axis = 1)
    
    return data