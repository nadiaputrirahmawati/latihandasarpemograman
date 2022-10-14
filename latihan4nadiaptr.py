#deskripsi
# tulis variabel harga barang 
#tulis variabel nama barang 
#tulis variabel persen harga 
#input nama barang 
#input harga barang 
#menghitung harga barang 
#harga barang* persen / 100 
#print harga barang beserta nama barang 

from ast import Break


while("true"):
    nama_barang = input("\nMasukan nama barang :")
    harga_barang1 = int(input("\nMasukan harga barang :"))
    persen = int(input("masukan persen barang : " ))
    harga_keuntungan1 = int(harga_barang1)*persen/100
    harga_jual = int(harga_barang1) + harga_keuntungan1
    print(nama_barang, 'dijual dengan harga :',harga_jual)

    apakahlanjut = input ('apakah ingin input barang lain ? Y lanjut : ')
    if (apakahlanjut != 'Y') :
        Break



persen = 10 

total = harga_barang1+harga_barang2+harga_barang3

hargapersen = int(total*10/100)

print("\nharga barang setelah di persenkan:",hargapersen)

print("\nTotal harga keuntungan:", total + hargapersen)


