import pandas as pd
import os

def convert(real, predict):
    new_df = pd.DataFrame(columns = ['Real Grade', 'Predicted Grade'])
    prediction = list()
    i = 0
    # Grab the real values from the original data set
    realvalue = real['Grade class 1: 90+  0:90-'].to_list()
    for line in predict:
        if (float(line.rstrip()) > 0):
            prediction.append(1)
        elif (float(line.rstrip()) < 0):
            prediction.append(0)
        i += 1

    df = pd.DataFrame({'Real Grade':realvalue, 'Predicted Grade': prediction})

    return df

def sspa(df):
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    for i in range(len(df)):
        row= df.loc[i]
        if row['Real Grade'] == 1:
            if row['Predicted Grade'] == 1:
                tp = tp + 1
            else:
                fn = fn + 1
        else:
            if row['Predicted Grade'] == 0:
                tn = tn + 1
            else:
                fp = fp + 1
    sensitivity = tp/(tp+fn)
    specificity = tn/(tn+fp)
    precision = tp/(tp+fp)
    accuracy = (tp + tn)/(tp + fp + fn + tn)

    return tp,tn,fp,fn,sensitivity, specificity, precision, accuracy

if __name__ == "__main__":
    # Grab the output file and convert
    predict = open('./SVMParts/predictions/prediction_set1.txt', 'r')
    realvalue = pd.read_excel('set1.xlsx', engine='openpyxl')

    converted = convert(realvalue, predict)
    print(sspa(converted))
