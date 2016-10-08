import pandas as pd

train = pd.read_csv('pouttransfer')
dataclean = train.dropna(axis=1, thresh=int(len(train)*0.8))
dataclean = dataclean[dataclean['class'].notnull()]
dataclean.to_csv('poutclean')