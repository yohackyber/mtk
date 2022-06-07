print("==============================================================")
print("Program Python MTK Bab Menentukan Bilangan Terkecil & Terbesar")
print("==============================================================")
print("Author:Suryo Saputro")
print("==============================================================")

n = int(input("\nMasukan Jumlah Bilangan = "))
bil = []
tot = 0
for x in range(n):
    m=x+1
    a = int(input("Bilangan ke %d = "%m))
    bil.append(a)
    tot += bil[x]
    rata2 = tot / n

print("===========================Hasilnya===========================")
print("\nBilangan Terkecil : %d" %min(bil))
print("Bilangan Terbesar : %d" %max(bil))
print("Nilai Rata-rata   : %0.2f" %rata2)

print("Makannya Kalo Pas Pelajaran MTK Jangan Turu")