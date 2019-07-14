
reticulate::repl_python()


my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT" 

length = len(my_dna) 
a_count = my_dna.count('A') 
t_count = my_dna.count('T') 
at_content = (a_count + t_count) / length 

print("AT content is " + str(at_content))

#define a function (with default)
def get_at_content(dna,sig_figs=2): 
    length = len(dna) 
    a_count = dna.upper().count('A') 
    t_count = dna.upper().count('T') 
    at_content = (a_count + t_count) / length 
    return round(at_content,sig_figs)

#and run it
x=get_at_content("ATGACTGGACCATT")

#check it (assert a test suite)
assert get_at_content("A") == 1
assert get_at_content("G") == 0
assert get_at_content("ATGC") == 0.5
assert get_at_content("ATGCN") == 0.5 #fails, but can add "dna = dna.replace('N', '')" to function to fix it.
