nama = []
umur = []

sumOfData = int(raw_input("Berapa banyak data yang mau dimasukkan? "))

for value in range(0, sumOfData):
    input_nama = raw_input("Silahkan masukkan nama ke {}? ".format(value))
    input_umur = int(raw_input("Silahkan masukkan umur ke {}? ".format(value)))

    nama.append(input_nama)
    umur.append(input_umur)

for index in range(0, len(nama)):
    print("Nama {} umur {}".format(nama[index], umur[index]))
