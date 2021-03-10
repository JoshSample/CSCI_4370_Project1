with open('Project1FollowUp/SVMParts/set5.txt', 'r', encoding='utf-8-sig') as reader, open('Project1FollowUp/SVMParts/set5_svm.txt', 'w') as writer:
    for line in reader:
        words = line.split(',')
        if (words[0] == '0'):
            writer.write('-1  ')
            j = 1
            for i in words:
                writer.write(str(j) + ':' + i +' ')
                j+=1
        elif (words[0] == '1'):
            writer.write('1  ')
            j = 1
            for i in words:
                writer.write(str(j) + ':' + i +' ')
                j+=1
            
