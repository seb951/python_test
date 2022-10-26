##set wd
import os
os.chdir("/Users/jerry/Documents/protocols_documentation/python")


###learning dictionnaries...
dna = "AATGATGAACGAC" 
bases = ['A','T','G','C'] 
all_counts = {} 
for base1 in bases: 
    for base2 in bases: 
        dinucleotide = base1 + base2 
        count = dna.count(dinucleotide) 
        if count > 0: 
            all_counts[dinucleotide] = count


###iterate
for dinucleotide in all_counts.keys():
    if all_counts.get(dinucleotide) == 2:
        print(dinucleotide)


###iterate over items
for dinucleotide, count in all_counts.items():
    if count == 2:
        print(str(dinucleotide)+str(count))



###
gencode = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

###

fasta = open("adh.fasta") #open a fasta file

count = 0 #counter set at 0
sep = '' #separator
#number 0 to 6
for line in fasta: #read line by line
    count = count + 1 #add to counter
    line2 = line.rsplit()[0] #strip the \n
    if count % 2 == 1: #action for sequence name
        my_file = open("out_test/protein" + str(count) + ".fasta", "w") #write a new file
        my_file.write(line2 + '\n') #add to file
    if count % 2 == 0: #action for sequence.
        protein = [] #empty list
        for n in range(len(line2)): #iterate over the range of characters
            if n % 3 == 0: #every 3rd character 
                codon = line2[(n-3):n] #triplets
                aa = gencode.get(codon,"X") #get info from dictionnary, X if not there.
                protein.append(aa) #append to list
        protein = seperator.join(protein) #cat to a string    
        my_file = open("out_test/protein" + str(count-1) + ".fasta",  "a") #append to file 
        my_file.write(protein + '\n') # write it up.

        
    
    
    os.system(command)
