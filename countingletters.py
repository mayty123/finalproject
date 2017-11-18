#Open the text file 
#Read File 
#Split File 
#Count Letters
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
    print(count)

while True: 
    choice = input ("What letter are you looking for in the file?: ")
    mychar = int(input("Enter the letter you are looking for: "))
ltrs(filename= "constituton.txt" ,mychar = "t")