
reticulate::repl_python()
#The file input.txt contains a number of DNA sequences, one per line. 
#Each sequence starts with the same 14 base pair fragment – a sequencing adapter 
#that should have been removed. Write a program that will 
#(a) trim this adapter and write the cleaned sequences to a new file and 
#(b) print the length of each sequence to the screen.
file = open("input.txt")
all_lines = file.readlines()

#number 0 to 6
for number in range(len(all_lines)):  
    #loop iteration
    file_temp = all_lines[number]
    file_temp_r = file_temp.replace("ATTCGATTATAAGC","")
    
    #various print statement
    #print(number)
    #print(len(file_temp_r))
    #print(file_temp_r)
    
    #mkdir 
    if number==0:
        os.system("mkdir out_test")
    
    #write.file
    my_file = open("out_test/out.txt" + str(number), "w")
    my_file.write(file_temp_r)
    my_file.close()
    
    #create a shell command and run it.
    command = "wc out_test/out.txt" + str(number) + " >out_test/wc" + str(number)
    os.system(command)
    



####
import os

file = open("input.txt")

all_lines = file.readlines()

#number 0 to 6
for number in range(len(all_lines)):  
    command = "wc out.txt >wc" + str(number)
    print(command)
    
    os.system(command)







#PERCENTAGE OF AMINO ACID RESIDUES, PART ONE
Write a function that takes two arguments – a protein sequence and an amino acid residue code
– and returns the percentage of the protein that the amino acid makes up. Use the following 
assertions to test your function:

#define a function (with default)
def aa(protein,aa): 
    PRO = protein.upper() #upper case protein
    AA = aa.upper() #upper case amino
    length = len(PRO)  #length protein
    percenta = PRO.count(AA) / length  * 100 #count AA divided by length protein.
    return round(percenta)


assert aa("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert aa("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert aa("msrslllrfllfllllpplp", "L") == 50
assert aa("MSRSLLLRFLLFLLLLPPLP", "Y") == 0


#iterate over a file line by line....a
count = 0
#
fasta =  open("file.fasta", "r")
for aline in fasta:
    a = aline.rsplit()[0]
    if len(a) > 4:
        print(a + " The length is:" + str(len(a)))
    elif len(a) < 4:
        print(a)
    count = count + 1


#iterate over a file line by line....a
count = 0
fasta =  open("file.fasta", "r")
for line in fasta:
    count = count + 1
    seq_head = line.rsplit()[0]
    print(seq_head)
    if len(seq_head) > 4:
        my_file = open("out_test/out_seq" + str(count), "w")
        my_file.write(seq_head)
    if count % 2 == 1:
        my_file = open("out_test/out_header_seq" + str(count), "w")
        my_file.write(seq_head + "\n")
    if count % 2 == 0:
        my_file = open("out_test/out_header_seq" + str(count-1), "a")
        my_file.write(seq_head + "\n")
    if len(seq_head) < 4:
        my_file = open("out_test/out_header" + str(count), "w")
        my_file.write(seq_head)
    my_file.close()
    

accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for acc in accs:
    if acc.startswith('a') and not acc.endswith('6'):
        print(acc)

