import librosa
import numpy as np
import csv
import os
import shutil


# extract basic audio features and records to a csv
'''
tangible and measurable elements rms, zcsr, mfccs, and so on
[artist,track,rms_mean,rms_std,zcr_mean,zcr_std,peak_amp,dynamic_range,ber,spectral_centroid,spectral_bandwidth,
mfcc_mean, mfcc_std,mfcc_1,mfcc_2,mfcc_3,mfcc_4,mfcc_5,mfcc_6,mfcc_7,mfcc_8,mfcc_9,mfcc_10,mfcc_11,mfcc_12,mfcc_13]


'''



# hardcode in files to process
melodic_file = './audio/melodic.mp3'
ambient_file = './audio/ambient.mp3'


# run script to process files from folders
UNPROCESSED_DIR = './audio/unprocessed'
PROCESSED_DIR = './audio/processed'

CSV_PATH = './data/custom.csv'

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



def extract_audio_features(file):
    '''
    extract all the audio featrures from the given files
    '''

    with open(CSV_PATH, 'a', newline='') as f:
        writer = csv.writer(f)

        # for now, add ph values for artist/track
        signal, sr = librosa.load(file)

        # OK
        base_features = extract_basic_features(signal,sr)
        print(file, base_features, "\n")

        # Add additional features



        # Write features to CSV
        # writer.writerow(['_', 'melodic'] + mel_features)
        # writer.writerow(['_', 'ambient'] + amb_features)
        # writer.writerow(['new', 'row', 'of', 'values'])



# uncomment whichever one needs to be done


# hardcoded files
files = [melodic_file, ambient_file]
# for file in files:
#     extract_audio_features(file)


# files from directory
for filename in os.listdir(UNPROCESSED_DIR):
    filepath = os.path.join(UNPROCESSED_DIR, filename)
    print(filename)

    # features = extract_audio_features(filepath)

    # after extraction, move to processed folder
    # shutil.move(filepath, os.path.join(PROCESSED_DIR, filename))


