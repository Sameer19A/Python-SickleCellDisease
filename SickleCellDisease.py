#Task 25
#Compulsory Task 1

#Disease ia a dictionary containing the SLC's and their DNA codons
Disease = {'ATT':'I','ATC':'I','ATA':'I',
           'CTT':'L','CTC':'L','CTA':'L','CTG':'L','TTA':'L','TTG':'L',
           'GTT':'V','GTC':'V','GTA':'V','GTG':'V',
           'TTT':'F','TTC':'F',
           'ATG':'M'}

def translate(Sequence):
    Seq_Len = len(Sequence)
    if Seq_Len%3 == 0: #if the len of the seq is divisible by 3
        num = 3
    elif Seq_Len%2 == 0:
        num = 2

    multiple = int(len(Sequence)/num)
    #print(multiple)
    for n in range(0,multiple):
        Start_Index = num*n
        End_Index = num*(n+1)
        Codon = Sequence[Start_Index:End_Index]  # slice the string according to the Start and end index, which should always differ by num
        #print(Codon)
        if Codon in DNA_Seq:
            #if Codon in Sequence:
            print(Disease[Codon],end="")      #prints the value (amino acid SLC code) of the Sequence i.e. I,L,V,F,M  
        else:
            print("The DNA codon", Codon," does not exist in database")


#Compulsory Task 2
def mutate():
    InputDNA = open('DNA.txt','r')          #open DNA.txt for reading
    NormalDNA = open('NormalDNA.txt','w')   #open NormalDNA.txt for reading
    MutatedDNA = open('MutatedDNA.txt','w') #open MutatedDNA.txt for reading
    for line in InputDNA:
        #NormalDNA.write(line)   #write the line to the normal DNA file.
        length = len(line)
        
        for i in range(0,length):
            CharN = line[i]
            CharM = line[i]
            if CharN == 'a':
                CharN = CharN.upper() #replace the small letter 'a' with capital 'A'
                #print(CharN)
                CharM = 'T'
                
            NormalDNA.write(CharN)  # Write to output file using CharN because CharN holds each character including the Uppercase character
            MutatedDNA.write(CharM)

    InputDNA.close()
    NormalDNA.close()
    MutatedDNA.close()

    
#function calling
DNA_Seq = input("Please enter the DNA sequence:\t")
translate(DNA_Seq)      #call the translate function
mutate()                #call the mutate function - not using arguments because we not returning anything.


