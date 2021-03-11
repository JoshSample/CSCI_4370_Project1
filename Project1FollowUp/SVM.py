import pandas as pd

# if you want to, just the program to convert the prediction to the 0 and 1 format and then compare the prediction to the actual to get accuracy measures.

def convert(dfr, dfp):
   new_df = pd.DataFrame(columns = ['Real Grade', 'Predicted Grade'])
   # Grab the real values from the original data set
   realvalue = dfr.loc[df['Grade class 1: 90+  0:90-']]
   # Concatenate it with the unconverted 
   conv = concat([realvalue, dfp], join = 'outer', axis = 1)
   attributes = list(conv.columns)
   attributes = attributes[2:]
   for i in range(len(conv)):
       row= conv.loc[i]
       for att in attributes:
           if (row[att] > 0):
               prediction = 1
           elif (BLANK < 0):
               prediction = 0
           new_df = new_df.append({'Real Grade': row['Grade class 1: 90+  0:90-'], 'Predicted Grade': prediction}, ignore_index = True)

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
    # need to read the input file
    realvalue = pd.read_exel('real.xlsx', engine='openpyxl')

    converted = convert(realvalue, output)
    (tp,tn,fp,fn,sensitivity, specificity, precision, accuracy) = sspa(converted)
