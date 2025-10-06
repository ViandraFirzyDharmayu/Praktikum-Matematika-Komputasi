def cek_validitas_argumen(proyek_tepat_waktu, klien_puas, perusahaan_terima_bonus):
  """
  Mengecek validitas argumen bisnis menggunakan Silogisme Hipotetis.
  Premis 1: Jika proyek tepat waktu (p), maka klien puas (q).
  Premis 2: Jika klien puas (q), maka perusahaan dapat bonus (r).
  Kesimpulan: Jika proyek tepat waktu (p), maka perusahaan dapat bonus (r).
  """
  # Mengubah premis ke bentuk logika: (A -> B) sama dengan (NOT A OR B)
  premis_1_valid = not proyek_tepat_waktu or klien_puas
  premis_2_valid = not klien_puas or perusahaan_terima_bonus

  # Argumen dianggap valid jika kedua premisnya benar untuk kasus yang terjadi.
  if premis_1_valid and premis_2_valid:
    kesimpulan = "Perusahaan menerima bonus."
  else:
    kesimpulan = "Tidak ada bonus."

  print(f"Proyek selesai tepat waktu: {proyek_tepat_waktu}, Klien puas: {klien_puas}, Perusahaan menerima bonus: {perusahaan_terima_bonus}, Kesimpulan: {kesimpulan}")

# --- Studi Kasus ---
print("=== Analisis Argumen Proses Bisnis ===")

# Kasus 1: Rantai logika putus di tengah (premis 1 gagal)
# Proyek selesai tepat waktu, TAPI klien tidak puas.
cek_validitas_argumen(True, False, False)

# Kasus 2: Semua premis terpenuhi
# Proyek selesai tepat waktu, klien puas, DAN perusahaan menerima bonus.
cek_validitas_argumen(True, True, True)

# Kasus 3: Rantai logika putus di akhir (premis 2 gagal)
# Proyek selesai tepat waktu, klien puas, TAPI perusahaan tidak dapat bonus.
cek_validitas_argumen(True, True, False)

# Kasus 4: Kondisi awal tidak terpenuhi
# Proyek tidak selesai tepat waktu, sehingga argumen tidak relevan, namun rantai tidak terputus.
cek_validitas_argumen(False, False, False)

print("====================================")