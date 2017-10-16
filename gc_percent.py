seq = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT" #set seq as the variable for the sequence string
print ("DNA sequence= ", seq) #print out the DNA sequence

G_num = seq.count("G") #Declare G_num as the variable for the number of Gs in the sequence
C_num = seq.count("C") #Declare C_num as the variable for the number of Cs in the sequence
seq_len = len (seq) #count the number of nucleotides in the sequence

GC = (((G_num + C_num)/seq_len)*100) #Calculating the GC percentage in the sequence
GC_round = round (GC, 2) #Rounded GC percentage to 2 decimal places

print ("GC percent= ", GC_round, "%") #print GC percentage
