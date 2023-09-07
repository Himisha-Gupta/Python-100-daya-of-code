
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_case_name1 = name1.lower()
lower_case_name2 = name2.lower()
conc_name = lower_case_name1+lower_case_name2
print(conc_name)

nl = conc_name.count("l")
no = conc_name.count("o")
nv = conc_name.count("v")
ne = conc_name.count("e")

love= str(nl+no+nv+ne)
print(love)

nt = conc_name.count("t")
nr = conc_name.count("r")
nu = conc_name.count("u")
nee = conc_name.count("e")

true = str(nt+nr+nu+nee)
print(true)

print("Love Score = " +love +true)
