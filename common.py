def ltrs(filename, mychar):
    f = open(filename, 'r')
    count = 0;
    run = True 
    while run:
        letters = f.read(1)
        letters = letters.lower()
        if letters == "":
            break 
        else:
            if letters == mychar: 
                count = count + 1
    return(count)
import string
abc = list(string.ascii_lowercase)
abc_count = []
for i in abc: 
    n = ltrs("constituton.txt",i) 
    abc_count.append(n)
m = max(abc_count)
l = abc_count.index(m)
print (abc[l])
    
    

#make a list with the alphabet 
#make a list that stores the value of each letter    
#Make a loop that counts how many of each letter there is
#define the maximum value
#Find the letter at the maximum value
#Print your results 

