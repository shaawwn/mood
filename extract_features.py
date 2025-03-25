import librosa
import numpy as np
import csv


# extract basic audio features and records to a csv
'''
tangible and measurable elements rms, zcsr, mfccs, and so on
[artist,track,rms_mean,rms_std,zcr_mean,zcr_std,peak_amp,dynamic_range,ber,spectral_centroid,spectral_bandwidth,
mfcc_mean, mfcc_std,mfcc_1,mfcc_2,mfcc_3,mfcc_4,mfcc_5,mfcc_6,mfcc_7,mfcc_8,mfcc_9,mfcc_10,mfcc_11,mfcc_12,mfcc_13]


'''

csv_path = './data/custom.csv'
melodic_file = './audio/melodic.mp3'
ambient_file = './audio/ambient.mp3'
FRAME_SIZE = 1024
HOP_SIZE=512

def extract_basic_features(signal, sr):
    '''
    get rms_mean,rms_std,zcr_mean,zcr_std,peak_amp,dynamic_range
    '''
    features =[]

    # rms
    rms = librosa.feature.rms(y=signal)
    rms_mean = rms.mean()
    rms_std = rms.std()
    features.append(rms_mean)
    features.append(rms_std)

    # zcr
    zcr = librosa.feature.zero_crossing_rate(y=signal)
    zcr_mean = zcr.mean()
    zcr_std = zcr.std()
    features.append(zcr_mean)
    features.append(zcr_std)

    #amp
    peak_amp = np.max(np.abs(signal))
    features.append(peak_amp)

    #dynamic range
    dynamic_range = rms.max() - rms.min()
    features.append(dynamic_range)

    print(features)
    return features


def extract_ber(signal, sr):
    return True

def extract_spectral_centroid(signal, sr):
    return True

def extract_mfcss(signal, sr):
    return True


with open(csv_path, 'a', newline='') as f:
    writer = csv.writer(f)

    # for now, add ph values for artist/track

    melodic,sr = librosa.load(melodic_file)
    ambient,_ = librosa.load(ambient_file)


    mel_features = extract_basic_features(melodic, sr)
    amb_features = extract_basic_features(ambient, sr)

    # writer.writerow(['_', 'melodic'] + mel_features)
    # writer.writerow(['_', 'ambient'] + amb_features)
    # writer.writerow(['new', 'row', 'of', 'values'])




print("Hello feature extraction")