#Billy Lu, GC Percent HW with user input DNA sequence

DNA = input ('Enter your DNA sequence (can be upper or lower case): ') #allows user to input DNA sequence as argument

# changed the DNA sequence into all upper case letters
DNAinput = DNA.upper()

G_num = DNAinput.count("G") #Declare G_num as the variable for the number of Gs in the sequence
C_num = DNAinput.count("C") #Declare C_num as the variable for the number of Cs in the sequence

seq_len = len (DNAinput) #count the number of nucleotides in the sequence

GC = (((G_num + C_num)/seq_len)*100) #Calculating the GC percentage in the sequence
GC_round = round (GC, 2) #Rounded GC percentage to 2 decimal places

print ("Your DNA sequence is ", DNAinput) #prints out the user DNA sequence in all capital letters
print ("GC percent= ", GC_round, "%") #print GC percentage
