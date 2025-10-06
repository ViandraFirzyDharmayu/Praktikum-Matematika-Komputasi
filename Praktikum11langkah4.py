def cek_sinkronisasi_perangkat(status_p, status_q):
  """
  Mengecek sinkronisasi dua perangkat berdasarkan logika bikondisional.
  Jaringan dianggap berfungsi jika kedua perangkat sama-sama menyala atau sama-sama mati.
  """
  # Logika bikondisional: (p AND q) OR (NOT p AND NOT q)
  # Dalam Python, untuk boolean, ini ekuivalen dengan (p == q)
  sinkron = (status_p == status_q)

  if sinkron:
    hasil = "Perangkat berfungsi dengan baik."
  else:
    hasil = "Perangkat tidak sinkron."

  print(f"Perangkat A: {status_p}, Perangkat B: {status_q}, Hasil: {hasil}")

# --- Studi Kasus ---
print("=== Analisis Sinkronisasi Perangkat Jaringan ===")

# Kasus 1: Salah satu perangkat mati
cek_sinkronisasi_perangkat(True, False)

# Kasus 2: Kedua perangkat menyala
cek_sinkronisasi_perangkat(True, True)

# Kasus 3: Salah satu perangkat mati (kebalikan dari kasus 1)
cek_sinkronisasi_perangkat(False, True)

# Kasus 4: Kedua perangkat mati
cek_sinkronisasi_perangkat(False, False)

print("==============================================")