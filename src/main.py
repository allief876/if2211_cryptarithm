# NIM: 13519221
# Nama: Allief Nuriman
# Tanggal: Rabu, 27 Januari 2021

# Program CryptharithmCalc
# Membaca input dari suatu file, yang
# menyatakan suatu cryptharithm, kemudian
# mengeluarkan persoalan & solusi, waktu
# eksekusi program (Tidak termasuk waktu
# pembacaan file input), dan jumlah total
# tes yang dilakukan untuk menemukan
# substitusi angka yang benar untuk setiap
# huruf

from time import perf_counter

def next_permutation(L):
    n = len(L)
    # Step 1: find rightmost position i such that L[i] < L[i+1]
    i = n - 2
    while i >= 0 and L[i] >= L[i+1]:
        i -= 1
    if i == -1:
        return False
    # Step 2: find rightmost position j to the right of i such that L[j] > L[i]
    j = i + 1
    while j < n and L[j] > L[i]:
        j += 1
    j -= 1
    # Step 3: swap L[i] and L[j]
    L[i], L[j] = L[j], L[i]
    # Step 4: reverse everything to the right of i
    left = i + 1
    right = n - 1
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
    return True

def getVal(arrAbj,arrVal,x):
    ketemu = False
    i = 0
    if (x == '+'):
        return 0
    while (not (ketemu)):
        if (arrAbj[i] == x):
            ketemu = True
        else:
            i = i + 1
    return arrVal[i]

def test(arrAbj,arrVal,cc): # Fungsi ini digunakan untuk melakukan testing apakah sudah benar solusinya
    i = 0
    global sum2
    sum1 = 0 # Jumlah antara operan-operan
    sum2 = 0 # Jumlah hasil

    for i in range(len(cc)-2):
        for j in range(len(cc[i])):
            if (cc[i][len(cc[i])-1] == '+' and cc[i][j] != '+'):
                sum1 = sum1 + getVal(arrAbj,arrVal,cc[i][j])*(10**(len(cc[i])-2-j))
            else:
                sum1 = sum1 + getVal(arrAbj,arrVal,cc[i][j])*(10**(len(cc[i])-1-j))

    i = i + 2

    for j in range(len(cc[i])):
        sum2 = sum2 + getVal(arrAbj,arrVal,cc[i][j])*(10**(len(cc[i])-1-j))
    return (sum1 == sum2)

def hurufpertamanol(arrAbj,arrVal,cc):
    i = 0
    while (i < len(cc)):
        if (cc[i][0] == '-'):
            i = i + 1
        else:
            if (getVal(arrAbj,arrVal,cc[i][0]) == 0):
                return True
            i = i + 1
    return False


def printjumlahTiapOp(arrAbj,arrVal,cc):
    for i in range(len(cc)):
        sum = 0
        if (cc[i][0] == '-'):
            print(cc[i])
            outfile.write(str(cc[i]))
            outfile.write("\n")
        elif (cc[i][len(cc[i])-1] == '+'):
            for j in range(len(cc[i])-1):
                if (cc[i][j] != '+'):
                    sum = sum + getVal(arrAbj,arrVal,cc[i][j])*(10**(len(cc[i])-2-j))
            print(sum,end='')
            outfile.write(str(sum)+"+")
            outfile.write("\n")
            print("+")
        elif (i != len(cc)-1):
            for j in range(len(cc[i])):
                sum = sum + getVal(arrAbj,arrVal,cc[i][j])*(10**(len(cc[i])-1-j))
            print(sum)
            outfile.write(str(sum))
            outfile.write("\n")
        else:
            print(sum2)
            outfile.write(str(sum2))
            outfile.write("\n")
            outfile.write("\n")
        
# ALGORITMA
print("Untuk keluar, tulis exit")
print("Masukkan nama file: ",end='')
filename = input()

while (filename != "exit"): # Filename valid & bukan tanda keluar
    arrAbjad = [] # Dipakai untuk menyimpan alfabet
    arrVal = [0,1,2,3,4,5,6,7,8,9] # Indeks arrAbjad menunjuk ke sini, ini yang akan dipermutasikan
    berkas = open(filename,'r') # Buka file testing untuk read-only, asumsikan file valid & berisi input yang diharapkan
    cc = berkas.read().splitlines() # Baca baris pertama (operan pertama)

    # Masukkan cc ke arrAbjad
    for i in range(len(cc)):
        if (cc[i][0] != '-'):
            for j in range(len(cc[i])):
                unik = True
                k = 0
                while (k < len(arrAbjad) and unik):
                    if (arrAbjad[k] == cc[i][j]):
                        unik = False
                    else:
                        k = k + 1
                if (unik and cc[i][j] != '+'):
                    arrAbjad.append(cc[i][j])

    t1_start = perf_counter()
    
    for i in range(len(cc)):
        print(cc[i])

    totalaksi = 1
    
    Found = False
    while (next_permutation(arrVal) and not (Found)):
        if (test(arrAbjad,arrVal,cc)):
            if (not (hurufpertamanol(arrAbjad,arrVal,cc))):
                Found = True
        totalaksi = totalaksi + 1

    t1_stop = perf_counter()

    outfile = open("output.txt",'w')

    if (not Found):
        print("Tidak ditemukan kombinasi yang memenuhi")
        outfile.write("Tidak ditemukan kombinasi yang memenuhi")
        outfile.write("\n")
    else:
        print()
        printjumlahTiapOp(arrAbjad,arrVal,cc)
        print()
    
    print("Waktu pencarian (dalam sekon) adalah ",end='')
    outfile.write("Waktu pencarian (dalam sekon) adalah "+str(t1_stop-t1_start))
    outfile.write("\n")
    outfile.write("Jumlah tes yang dilakukan adalah "+str(totalaksi))
    outfile.write("\n")
    outfile.close()
    print(t1_stop-t1_start)
    print("Jumlah tes yang dilakukan adalah ",end='')
    print(totalaksi)
    print()

    berkas.close()
    outfile.close()

    print("Untuk keluar, tulis exit")
    print("Masukkan nama file: ",end='')
    filename = input()