def tambah ():
    print("\t1. oenjumlahan")
    a = int(input("\tMasukan nilai x= "))
    b = int(input("\tMasukan nilai y= "))
    c = a+b
    print ("\tx+y=",c)
    tanya ()
def kurang ():
    print("\t2. pengurangan")
    a = int(input("\tMasukan nilai x= "))
    b = int(input("\tMasukan nilai y= "))
    c = a-b
    print ("\tx-y=",c)
    tanya ()
def bagi ():
    print("\t3. pembagian")
    a = int(input("\tMasukan nilai x= "))
    b = int(input("\tMasukan nilai y= "))
    c = a/b
    print ("\tx/y=",c)
    tanya ()
def kali ():
    print("\t4. perkalian")
    a = int(input("\tMasukan nilai x= "))
    b = int(input("\tMasukan nilai y= "))
    c = x*y
    print ("\tx*y=",c)
    tanya ()

def tanya():
    tanya = input("\n\tKembali ke menu kalkulator (Y/T)? ")
    if tanya == "Y":
        menu()
    elif tanya == "T":
        exit
    else:
        print ("\n\tSalah input............!!!")
def pilihan() :
    print("\n\t======================================")
    print("\tProgram kalkulator sederhana")
    print("==========================================")
    print("\t1.Penjumlahan")
    print("\t2.Pengurangan")
    print("\t3.Pembagian")
    print("\t4.Perkalian")
    print("==========================================")
    print("Silahkan pilih 1-4")
    print(" ")
    pil = input("Masukan pilihan 1 ")
    if pil == '1':
        tambah()
    elif pil == '2':
        kurang()
    elif pil == '3':
        bagi()
    elif pil == '4':
        kali()
    else:
        print("Maaf, input yang andamasukan salah")
        print("Coba ulangi kembali...")
        tanya()
