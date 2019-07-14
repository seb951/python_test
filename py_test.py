
setwd("/Users/jerry/Dropbox/CSBQ/workshop/python")

#I'm running python3 in Rstudio type exit to exit and go back to R
library(reticulate)
reticulate::repl_python()

###hello
print("Hello from Python!")
my_dna = "ACTG" # a string
print(my_dna)

###length
dna_len = len(my_dna2)
print(dna_len) # a number

###replace
protein = "vlspldktnv"
protein_replace = protein.replace("v", "y")
# replace valine with tyrosine
print(protein_replace)


###print positions three to five
print(protein[3:5])
print(protein[0:6])
print(protein[2:])

#this is a list
apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"] 
apes[0][0:5]


###count (returns a number) more using regexpr
valine_count = protein.count('v')
lsp_count = protein.count('lsp')
tryptophan_count = protein.count('w')
print("valines: " + str(valine_count))
print("lsp: " + str(lsp_count))
print("tryptophans: " + str(tryptophan_count))

###find position
print(protein.find('l')) 
print(protein.find('kt')) 
print(protein.find('w'))

###options on strings
dir(protein)
help(protein.capitalize)

###
dna="ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
dna2 = dna.replace("A","t")
dna2 = dna2.replace("C","g")
dna2 = dna2.replace("G","c")
dna2 = dna2.replace("T","a")
dna2 = dna2.upper()
print(dna2)


#Working with files
my_file = open("dna.txt")
my_dna_temp = my_file.read()
my_dna = my_dna_temp.rstrip("GCCTGT\n")
my_dna = my_file.read().rstrip("\n")
dna_length = len(my_dna)
print("sequence is " + my_dna +  " and length is " + str(dna_length))

##writing to file "w" or "a" or "r" arguments
my_file = open("out.txt", "w")
my_file.write("Hello world\n")
my_file.write("abc" + "def\n")
my_file.close()

#try reading this file with multiple lines now to create a list
my_file = open("out.txt")
out = my_file.read().rsplit("\n")


#lists
apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
conserved_sites = [24, 56, 132]
last_ape = apes[-1] #last ape

ranks = ["kingdom","phylum", "class", "order", "family"]
lower_ranks = ranks[2:5]

#append to list and cat (extend to append a list)
apes.append("Pan paniscus")
monkeys = ["Papio ursinus", "Macaca mulatta"]
primates = monkeys + apes
apes.extend(monkeys)
print("after sorting : " + str(ranks)) #can only cat str to str.

#reverse and sort
apes.sort()
apes.reverse()

#loops
apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]    
for ape in apes:
    name_length = len(ape)
    first_letter = ape[0]
    print(ape + " is an ape. Its name starts with " + first_letter)
    print("Its name has " + str(name_length) + " letters")

#iterate over a file
# first store a list of lines in the file
file = open("gen.fasta")
all_lines = file.readlines()

# print the lengths
for line in all_lines:

    print("The length is " + str(len(line)))

for line in all_lines:
    print(line)
    


#
#The file input.txt contains a number of DNA sequences, one per line. 
#Each sequence starts with the same 14 base pair fragment – a sequencing adapter 
#that should have been removed. Write a program that will 
#(a) trim this adapter and write the cleaned sequences to a new file and 
#(b) print the length of each sequence to the screen.
file = open("input.txt")
all_lines = file.readlines()

###number 0 to 6
for number in range(len(all_lines)):  

    file_temp = all_lines[number]
    file_temp_r = file_temp.replace("ATTCGATTATAAGC","")
    
    #
    #print(number)
    #print(len(file_temp_r))
    #print(file_temp_r)
    
    #write.file
    my_file = open("out.txt" + str(number), "w")
    my_file.write(file_temp_r)
    my_file.close()



#regular expression
print(r"\t\n")
print("\t\n")

dna = "ATCGCGAATTCAC"
if re.search(r"GAATTC", dna):
    print("restriction site found!")
re.search(r"GAA(T|A)TC", dna) #either A or T
re.search(r"GAA[ACTG]TC", dna) #any in bracket
re.search(r"GAA.TC", dna) # any character
re.search(r"GA(A)?TTC", dna) #A or not
m = re.search(r"GA*TTC", dna) #any nb of A....

#show me where it matched.
m.group() 


#GA{2,4}T means G, followed by between 2 and 4 As, followed by T. S

###complex example
^AUG[AUGC]{30,1000}A{5,10}$

#Reading the pattern from left to right, it will match:
#an AUG start codon at the beginning of the sequence
#followed by between 30 and 1000 bases which can be A, U, G or C
#followed by a poly-A tail of between 5 and 10 bases at the end of the sequence


#complex example 2
scientific_name = "Homo sapiens" 

m = re.search("(.+) (.+)", scientific_name) 

if m: 
    genus = m.group(1) 
    species = m.group(2) 
    print("genus is " + genus + ", species is " + species)


#more than one hit
dna = "CTGCATTATATCGTACGAAATTATACGCGCG" 
result = re.findall(r"[AT]{6,}", dna)  #section with more than 6 A or T. 
print(result)

#split based on regexpr
dna = "ACTNGCATRGCTACGTYACGATSCGAWTCG"
runs = re.split(r"[^ATGC]", dna)
print(runs)












#float
float_string3 = "%f" % (1.237)

#dictionnaries
print("%(value)s %(value)s %(value)s !" % {"value":"SPAM"})


###lists:
my_list3 = ["a", 1, "Python", 5]
my_list2 = ["a", "b", "c"]
m3 = my_list3 + my_list2
m4 = [4,24,1,2,3]
m4.sort()
m4

#slice list
m4[1:2]


###Tuples (immutable)
my_tuple = (1, 2, 3, 4, 5)

#dictionnaries (hash table: immutable)
my_dict = {"name":"Mike", "address":"123 Happy Way"}
my_other_dict = {"one":1, "two":2, "three":3}
my_dict["name"]
"name" in my_dict


#if
var1 = 1
var2 = 3
if var1 > var2:
    print("That's ok")
elif 1 <= var2 <= 5:
    print("I'd still pay that...")
else:
    print("ouin ouin")
        
        
#packages
pip install numpy
