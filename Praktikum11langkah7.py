def cek_segitiga_siku_siku(sudut1, sudut2, sudut3):
  """
  Mengecek apakah sebuah segitiga adalah siku-siku berdasarkan Aksioma dan Corollary.
  """
  # Langkah 1: Validasi berdasarkan Aksioma
  # Aksioma: Total sudut dalam segitiga adalah 180 derajat.
  # Jika aksioma tidak terpenuhi, maka bangun tersebut bukan segitiga.
  if sudut1 + sudut2 + sudut3 != 180:
    kesimpulan = "Ini bukan segitiga yang valid."
    print(f"Sudut 1: {sudut1}, Sudut 2: {sudut2}, Sudut 3: {sudut3}, Kesimpulan: {kesimpulan}")
    return

  # Langkah 2: Pengecekan berdasarkan Corollary
  # Corollary: Jika segitiga memiliki sudut 90 derajat, maka itu adalah segitiga siku-siku.
  if sudut1 == 90 or sudut2 == 90 or sudut3 == 90:
    # Kesimpulan ini mengafirmasi Teorema
    kesimpulan = "Ini adalah segitiga siku-siku."
  else:
    kesimpulan = "Ini bukan segitiga siku-siku."

  print(f"Sudut 1: {sudut1}, Sudut 2: {sudut2}, Sudut 3: {sudut3}, Kesimpulan: {kesimpulan}")


# --- Definisi Konsep Geometri ---
print("=== Studi Kasus: Aksioma, Teorema, Lemma, dan Corollary ===")
print("Aksioma: Total sudut dalam segitiga adalah 180 derajat.")
print("Teorema: Dalam segitiga siku-siku, salah satu sudutnya adalah 90 derajat.")
print("Lemma: Sudut di seberang sisi terpanjang dalam segitiga siku-siku adalah 90 derajat.")
print("Corollary: Jika segitiga memiliki sudut 90 derajat, maka itu adalah segitiga siku-siku.")
print("-" * 60)

# --- Uji Coba Fungsi ---
# Kasus 1: Segitiga siku-siku
cek_segitiga_siku_siku(90, 60, 30)

# Kasus 2: Bukan segitiga siku-siku (tapi segitiga valid)
cek_segitiga_siku_siku(60, 60, 60)

# Kasus 3: Bukan segitiga yang valid (total sudut bukan 180)
cek_segitiga_siku_siku(90, 45, 40)