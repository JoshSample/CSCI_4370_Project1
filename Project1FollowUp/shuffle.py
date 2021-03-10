import pandas as pd

def shuffle(ds):
    # Shuffle the dataset
    # then split data into 5 equal parts
    df = ds.sample(frac = 1)
    splitsNum = int(len(df) / 5)
    set1 = df.iloc[0:splitsNum]
    set2 = df.iloc[splitsNum+1:splitsNum*2]
    set3 = df.iloc[splitsNum*2+1:splitsNum*3]
    set4 = df.iloc[splitsNum*3+1:splitsNum*4]
    set5 = df.iloc[splitsNum*4+1:splitsNum*5]
    return set1, set2, set3, set4, set5

if __name__ == "__main__":
    # Load in the whole dataset
    trainingDataset = pd.read_excel('Full Wine Data.xlsx', engine='openpyxl')
    # Shuffle rows and split into 5 sets, output to excel
    (set1, set2, set3, set4, set5) = shuffle(trainingDataset)
    set1.to_excel("set1.xlsx")
    set2.to_excel("set2.xlsx")
    set3.to_excel("set3.xlsx")
    set4.to_excel("set4.xlsx")
    set5.to_excel("set5.xlsx")
