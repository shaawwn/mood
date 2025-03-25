import pandas as pd




training_file = './data/train.csv'

df = pd.read_csv(training_file)

print(df.info())