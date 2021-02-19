with open('testing_set.txt', 'r') as reader, open('new_testing_set.txt', 'w') as writer:
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
            
