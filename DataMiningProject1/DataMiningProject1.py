# Data Mining Project 1
# By Makenzie Spurling, Josh Sample, and Kathryn Villarreal

import pandas as pd

# This opens the training set and the testing set and stores it in a variable
trainingDataset = pd.read_excel('Training dataset.xlsx', engine='openpyxl')
testingDataset = pd.read_excel('Testing dataset.xlsx', engine='openpyxl')

#row = testingDataset.iloc[1, 1:].array
#print(row)


# Counts up yes/nos (1/0s) in class label
# and calculates the yes/no probabilites
yesCount = 0
noCount = 0

for item in trainingDataset['Grade class 1: 90+  0:90-']:
    if item == 0:
        yesCount += 1
    else:
        noCount += 1

total = yesCount + noCount;
yesProb = yesCount / total;
noProb = noCount / total;

print(total, yesProb, noProb)

# Class is 90+/90- (1/0)
# Do a count of how many 1's & 0's in Class save it off <---------------------------|
# Divide that by total and save it off                                              |
#                                                                                   |
# Will then need to go to testing data and grab one line                            |
# Section the line off and then run probabilites for the label                      |
# EXAMPLE from training data (just a couple bc it has like 30 lmao):                |
# ACCENTS   ACIDITY <- Labels we need to section                                    |
#    0         0    <- grab all 0's the labels from TRAINING DATASET                |
#                       then count which ones correspond to a 1(90+) or a 0(90-)    |
#                       in the grade class and divide them by the count we did in --|
# Once that is done we'll have probabilites for each label
# Multiply the yes probabilites with themselves and no probabilies with themselves
# then multiply that by the TOTAL PROBABILITY ON LINE 9 THAT WE SAVED OFF
# which ever is higher is what the sample belongs to
# repeat for the rest of testing data

# Basic design (yes there will be errors bc we have no variables)
# DONE FOR EACH TESTING VARIABLE
if (testingLabel == 0): 
    # Loop through training dataset & find all 0's
    # correspond to 90+ & 90-
    plusCount += 1
    minusCount += 1

    # Divide counts by yes & no from line 8
    totalZeroLabelCount
else:
    # Do the same from the first label except checking for 1
    plusCount += 1
    minusCount += 1

    # Divide counts by yes & no from line 8
    totalOneLabelCount

    # Then multiply all the totalZeroLabelCounts (may want to use an array?)
    # & totalOneLabelCounts then multiply those by their respecitve line 9
    # and based on which is bigger classify it and save it off in the excel

    # ONCE THAT IS DONE FOR EVERY TESTING DATA
    # Take the real grade from testing data and the predicited
    # put them in a new dataset (Maybe??)

    # Will also need to go through the predicited and real grade and do another 
    # line 26-line 33 for finding which are the correct then divide that value by
    # total wine and save that off