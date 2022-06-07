print("===========================================")
print("Program Python MTK Bab Luas & Volume Tabung")
print("===========================================")
print("Author:Suryo Saputro")
print("===========================================")

pi    = 22/7
jari   = float(input("Masukan Jari-jarinya  : "))
tinggi = float(input("Masukan Tinggginya    : "))
volume = pi*jari*jari*tinggi
luas   = 2*pi*jari*(jari+tinggi)

print("=================Hasilnya=================")
print("Volume Tabung         =","{:.2f}".format(volume))
print("Luas Permukaan Tabung =","{:.2f}".format(luas)) 
print("Makannya Kalo Pas Pelajaran MTK Jangan Turu")