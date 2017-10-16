DNAinput = input ('Enter your DNA sequence: ') #allows user to input DNA sequence as argument

G_num = DNAinput.count("G") #Declare G_num as the variable for the number of Gs in the sequence
g_num = DNAinput.count("g") #Declare g_num as the variable for the number of gs in the sequence
C_num = DNAinput.count("C") #Declare C_num as the variable for the number of Cs in the sequence
c_num = DNAinput.count("C") #Declare c_num as the variable for the number of cs in the sequence
seq_len = len (DNAinput) #count the number of nucleotides in the sequence

GC = (((G_num + C_num + c_num + g_num)/seq_len)*100) #Calculating the GC percentage in the sequence
GC_round = round (GC, 2) #Rounded GC percentage to 2 decimal places

print ("GC percent= ", GC_round, "%") #print GC percentage
