matkom = {"Faiq", "Alya", "Aisyah", "Asa"}
strukdat = {"Bagus", "Aisyah", "Faiq", "Alya", "Gabriel", "Lionel", "Diva", "Lukman"}
algoritma = {"Faza", "Cinda", "Lukman", "Diva"}
basdat = {"Karin", "Atta", "Lukman", "Khayla", "Bagus", "Raka"}

total_mahasiswa = strukdat.union(algoritma)
print(f"Total mahasiswa yang hadir di setidaknya salah satu kelas: {len(total_mahasiswa)}")

