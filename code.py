fk = open("dec_of_ind.txt","r")
fc = open("cipher.txt","r")
fw = open("res.txt","w")

arrk = fk.read().split("\n")
arrc = fc.read().split("\n")

arrc = list(map(int,arrc))

for n in arrc:
    print(arrk[n-1][0])
    fw.write(arrk[n-1][0])
# print(arrk)
