# Data Mining Project 1
# By Makenzie Spurling, Josh Sample, and Kathryn Villarreal

import pandas as pd

def getTotals(df):
    # Create seperate dataframes of 90+ and 90-
    dfYes = df.loc[df['Grade class 1: 90+  0:90-'] == 1]
    dfNo = df.loc[df['Grade class 1: 90+  0:90-'] == 0]
    # Get the total number of entries
    total = len(df)
    # Get the total of 90+
    totalYes = len(dfYes)
    # Get the total of 90-
    totalNo = len(dfNo)
    # Find the probablities of 90+ and 90-
    probYes = (totalYes+1)/(total+2)
    probNo = (totalNo+1)/(total+2)
    return totalYes, totalNo, total, probYes, probNo

def findAttributes(df, totalYes, totalNo):
    # Parsing through each possible attribute for the wine (each column)
    # Collect the amount of 1s and 0s corresponding to each attribute and if it is a 90+ or 90-
    # Basically find which attributes are seen more with 90+ and 90- and make a list or dictionary 
    #   of the attributes
    attrib_dict = dict()
    attributes = list(df.columns)
    attributes = attributes[2:]
    Yesdf = df.loc[df['Grade class 1: 90+  0:90-'] == 1]
    Nodf = df.loc[df['Grade class 1: 90+  0:90-'] == 0]

    for attrib in attributes:
        YesYes = round((len(Yesdf.loc[Yesdf[attrib] == 1])+1)/(totalYes+2), 4)
        YesNo = round((len(Yesdf.loc[Yesdf[attrib] == 0])+1)/(totalYes+2), 4)
        NoYes = round((len(Nodf.loc[Nodf[attrib] == 1])+1)/(totalNo+2), 4)
        NoNo = round((len(Nodf.loc[Nodf[attrib] == 0])+1)/(totalNo+2), 4)

        attrib_dict["YesYes" + attrib] = YesYes
        attrib_dict["YesNo" + attrib] = YesNo
        attrib_dict["NoYes" + attrib] = NoYes
        attrib_dict["NoNo" + attrib] = NoNo

    return attrib_dict

def predict_grade(df, probYes, probNo, attrib_dict):
    # Loop through each entry
    #   Make X based on the 0s and 1s in the entry
    #   Example: X = (
    #                  ACCENTS = 0
    #                  ACIDITY = 1
    #                  ...
    #                  WONDERFUL = 0
    #                  YOUNG = 0)
    #   So since ACCENTS = 0 get the YesNoACCENTS and the NoNoACCENTS
    #       and ACIDITY = 1 get YesYesACIDITY and NoYesACIDITY

    # Multiply all the 90+ probibilities together and then multiply it by the probablity of yes
    # Multiply all the 90- probibilities together and then multiply it by the probablity of no
    # whichever is the highest is the predicted result
    prediction_dict = dict()
    attributes = list(df.columns)
    names = attributes[0]
    attributes = attributes[2:]
    yes_prob = 1.0
    no_prob = 1.0
    matchYes = 0
    matchNo = 0
    # Go through each row and 
    for i in range(len(df)):
        row= df.loc[i]
        for att in attributes:
            if row[att] == 1:
                yes_prob *= attrib_dict["YesYes"+att]
                no_prob *= attrib_dict["YesNo"+att]
            else:
                yes_prob *= attrib_dict["NoYes"+att]
                no_prob *= attrib_dict["NoNo"+att]

        class1 = yes_prob * probYes
        class2 = no_prob * probNo
        prediction = int()
        if class1 > class2:
            prediction = 1
        elif class2 > class1:
            prediction = 0
        else:
            prediction = -1

        if row['Grade class 1: 90+  0:90-'] == prediction:
            prediction_dict[row[names]] = [row['Grade class 1: 90+  0:90-'], prediction, 1]
            matchYes += 1
        else:
            prediction_dict[row[names]] = [row['Grade class 1: 90+  0:90-'], prediction, 0]
            matchNo += 1

    correctness = matchYes/len(df)
    print(correctness)    
    return prediction_dict

if __name__ == "__main__":
    # Load in the training dataset
    trainingDataset = pd.read_excel('Training dataset.xlsx', engine='openpyxl')
    # Get the overall totals from the dataset
    (totalYes, totalNo, total, probYes, probNo) = getTotals(trainingDataset)
    # Find what attributes contribute and/or detract from 90+
    attrib_dict = findAttributes(trainingDataset, totalYes, totalNo)
    
    testingDataset = pd.read_excel('Testing dataset.xlsx', engine='openpyxl')

    prediction_dict = predict_grade(testingDataset, probYes, probNo, attrib_dict)

    # Compare the predicted results to the actual data and find the accuracy of our method

    # Convert to SVM format 
    # Run training and testing data through SVM.exe
    # Compare the SVM accuracy to our accuracy