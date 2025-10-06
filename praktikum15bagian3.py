matkom = {"Faiq", "Alya", "Aisyah", "Asa"}
strukdat = {"Bagus", "Aisyah", "Faiq", "Alya", "Gabriel", "Lionel", "Diva", "Lukman"}
algoritma = {"Faza", "Cinda", "Lukman", "Diva"}

mahasiswa_kedua_kelas = strukdat.intersection(algoritma)
print(f"Mahasiswa yang hadir di kedua kelas: {mahasiswa_kedua_kelas}")

mahasiswa_satu_kelas = strukdat.symmetric_difference(algoritma)
print(f"Mahasiswa yang hanya hadir di salah satu kelas: {mahasiswa_satu_kelas}")

total_mahasiswa = strukdat.union(algoritma)
print(f"Total mahasiswa yang hadir di setidaknya salah satu kelas: {len(total_mahasiswa)}")

matkom_subset_strukdat = matkom.issubset(strukdat)
if matkom_subset_strukdat:
    print("Semua maasiswa yang hadir di Matematika Komputasi juga hadir di Struktur Data.")
else:
    print("Tidak semua mahasiswa yang hadir di Matematika Komputasi hadir di Struktur Data.")

if len(matkom) == len(strukdat):
    print("Jumlah mahasiswa yang hadir di kedua kelas sama.")
else:
    print("Jumlah mahasiswa yang hadir di kedua kelas berbeda.")

    