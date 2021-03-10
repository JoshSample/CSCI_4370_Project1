# Data Mining Project 1 Follow Up
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
        YesYes = (len(Yesdf.loc[Yesdf[attrib] == 1])+1)/(totalYes+2)
        YesNo = (len(Yesdf.loc[Yesdf[attrib] == 0])+1)/(totalYes+2)
        NoYes = (len(Nodf.loc[Nodf[attrib] == 1])+1)/(totalNo+2)
        NoNo = (len(Nodf.loc[Nodf[attrib] == 0])+1)/(totalNo+2)

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
    new_df = pd.DataFrame(columns = ['Real Grade', 'Predicted Grade'])
    attributes = list(df.columns)
    attributes = attributes[2:]
    matchYes = 0
    # Go through each row and calculate probabilities
    for i in range(len(df)):
        row= df.loc[i]
        yes_prob = 1.0
        no_prob = 1.0
        for att in attributes:
            if row[att] == 1:
                yes_prob = yes_prob * attrib_dict["YesYes"+att]
                no_prob = no_prob * attrib_dict["NoYes"+att]
            else:
                yes_prob = yes_prob * attrib_dict["YesNo"+att]
                no_prob = no_prob * attrib_dict["NoNo"+att]

        class1 = yes_prob * probYes
        class2 = no_prob * probNo
        prediction = int()
        if class1 > class2:
            prediction = 1
        elif class2 > class1:
            prediction = 0
        else:
            prediction = -1
        
        new_df = new_df.append({'Real Grade': row['Grade class 1: 90+  0:90-'], 'Predicted Grade': prediction}, ignore_index = True)
        if row['Grade class 1: 90+  0:90-'] == prediction:
            matchYes += 1

    correctness = matchYes/len(df) 
    print(correctness)  
    return new_df

# What needs to happen here is that you take four of the five sets
# and combine them into a training set use the left over as testing set
# Here is the ten dataset sets (5 train, 5 test) that need to be created
# TESTING     TRAINING (COMBINE THESE)
#   1               2-3-4-5
#   2               1-3-4-5
#   3               1-2-4-5
#   4               1-2-3-5
#   5               1-2-3-4

# After this is done SAVE THEM off to excel files BECAUSE we need to run them with 
# SVM, after this just like we did normally for the first project

# AFTER THIS IS DONE AND WE have a predicted and a true for these excel file for each 
# of these (we'll have five in total)

# Compare the true & predicted to each other to find the truePositive, trueNegative, etc.
# EXAMPLE ON HOW IT WORKS:
# TRUE      PREDICTED
# 1             1           True Positive
# 1             0           False Negative
# 0             1           False Positive
# 0             0           True Negative

# Once we have these now we calculate the values:
# sensitivity = Ture Positive/Positive
# specificity = True Negative/Negative
# precision = True Positive/(True Positive + False Positive)
# accuracy = (True Positives + True Negatives)/(True Positives + False Positives + False Negatives + True Negatives)
# for accuracy the value in denominator is just how many rows are in the excel file lol

# ONTO SVM:
# SVM gives precision & sensisitvy & accuracy, we'll have to calculate
# specificity
# Which means converting the output file from an svm run into 1 and 0's
# and then just doing the calcualtions
# Sorry Kat that exam problem has come back from the dead

if __name__ == "__main__":
    # Load in the whole dataset
    trainingDataset = pd.read_excel('Full Wine Data.xlsx', engine='openpyxl')

    # Get the overall totals from the dataset
    (totalYes, totalNo, total, probYes, probNo) = getTotals(trainingDataset)

    # Find what attributes contribute and/or detract from 90+
    attrib_dict = findAttributes(trainingDataset, totalYes, totalNo)
    
    # Load testing dataset
    testingDataset = pd.read_excel('Full Wine Data.xlsx', engine='openpyxl')

    # Predict accuracy & write to file
    new_df = predict_grade(testingDataset, probYes, probNo, attrib_dict)
    new_df.to_excel("output.xlsx")