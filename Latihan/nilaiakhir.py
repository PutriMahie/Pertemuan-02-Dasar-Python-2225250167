tugas = float(input("Masukkan nilai tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

nilai_akhir = (tugas * 0.3) + (uts * 0.3) + (uas * 0.4)

print("Nilai akhir:", round(nilai_akhir, 2))

if nilai_akhir >= 85:
    grade = "A"
elif nilai_akhir >= 70:
    grade = "B"
elif nilai_akhir >= 55:
    grade = "C"
else:
    grade = "D"

print("Grade:", grade)
