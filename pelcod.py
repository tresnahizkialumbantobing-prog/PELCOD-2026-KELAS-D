nama = "Renatha"
nilai_tugas = 100
nilai_kuis = 100
nilai_ujian = 90
kehadiran = 100

nilai_akhir =  (nilai_tugas * 30 / 100) + (nilai_kuis * 20 / 100) + (nilai_ujian * 50 / 100)

if kehadiran < 75:
   status = "Tidak lulus"
elif nilai_akhir >= 85 and kehadiran >= 80:
   status = "Lulus dengan predikat A"
elif nilai_akhir >= 75 and kehadiran >= 80:
   status = "Lulus dengan predikat B"
elif nilai_akhir >= 65 and kehadiran >= 75:
   status = "Lulus dengan predikat C"
else:
     status = "Tidak lulus"

print()
print("=====HASIL PENILAIAN=====")
print("Nama         :" , nama)
print("Nilai_akhir  :" , nilai_akhir)
print("Kehadiran   :", kehadiran, "%")
print("Status      :", status)