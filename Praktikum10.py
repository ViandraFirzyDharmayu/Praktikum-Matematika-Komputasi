def opbiconditional(work_hours, is_late):
    # Karyawan mendapatkan bonus jika bekerja lebih dari 8 jam dan tidak terlambat
    return (work_hours > 8) == (not is_late)

# Studi kasus
work_hours = 9 # Jam kerja lebih dari 8
is_late = False # Tidak terlambat

# Penerapan 
result = opbiconditional(work_hours, is_late)
if result:
    print("Karyawan layak mendapatkan bonus.")
else:
    print("Karyawan tidak layak mendapatkan bonus.")

def opinferensi(is_raining):
    # Jika hujan, maka tanah basah
    if is_raining:
        return "Tanah basah"
    else:
        return "Tanah kering"
    
# Studi kasus
is_raining = True # Hujan turun

# Penerapan 
result = opinferensi(is_raining)
print(f"Hasil inferensi: {result}")

def opargumen(nilai):
    # Argumen: Jika nilai lebih dari 70, maka lulus
    if nilai > 70:
        return "Lulus"
    else:
        return "Tidak lulus"
    
# Studi kasus
nilai = 85 # nilai lebih dari 70

# Penerapan
result = opargumen(nilai)
print(f"Hasil argumen: {result}")

# Aksioma: Setiap angka genap dapat dibagi 2
def opaksioma(n):
    return n % 2 == 0

# Lemma: Bilangan genap adalah kelipatan dari 2
def oplema(n):
    return opaksioma(n)

# Teorema: Jumlah dua bilangan genap adalah bilangan genap
def opteorema(a, b):
    return opaksioma(a + b)

# Corollary: Jika dua bilangan ganjil dijumlahkan, maka hasilnya adalah bilangan genap
def opcorollary(a, b):
    return opaksioma(a + b)

# Studi kasus
a = 4 # Bilangan genap
b = 6 # Bilangan genap

# Penerapan 
print(f"Aksioma: {a} adalah bilangan genap? {opaksioma(a)}")
print(f"Lemma: {b} adalah kelipatan 2? {oplema (b)}")
print(f"Teorema: Jumlah {a} dan {b} adalah bilangan genap? {opteorema(a, b)}")

# Contoh bilangan ganjil
c = 3 # Bilangan ganjil
d = 5 # Bilangan ganjil
print(f"Corollary: Jumlah {c} dan {d} adalah bilangan genap? {opcorollary(c, d)}")

if __name__ == "__main__":
    opbiconditional()
    opinferensi()
    opargumen()
    opaksioma()
    oplema()
    opteorema()
    opcorollary()
  


