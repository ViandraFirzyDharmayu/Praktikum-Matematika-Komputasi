def cek_sistem_alarm(sensor_mendeteksi, alarm_berbunyi):
  """
  Mengecek validitas sistem alarm menggunakan inferensi logika (p -> q).
  Sistem gagal jika sensor mendeteksi gerakan (p=True) tetapi alarm tidak berbunyi (q=False).
  """
  # Aturan inferensi: Jika p benar dan q salah, maka sistem gagal.
  # Ini adalah satu-satunya kondisi di mana implikasi (p -> q) bernilai False.
  if sensor_mendeteksi and not alarm_berbunyi:
    hasil = "Sistem gagal."
  else:
    hasil = "Sistem berfungsi dengan baik."

  print(f"Sensor mendeteksi gerakan: {sensor_mendeteksi}, Alarm berbunyi: {alarm_berbunyi}, Hasil: {hasil}")

# --- Studi Kasus ---
print("=== Analisis Sistem Alarm Keamanan ===")

# Kasus 1: Aturan dilanggar (Inferensi Gagal)
# Sensor mendeteksi gerakan, TAPI alarm tidak berbunyi.
cek_sistem_alarm(True, False)

# Kasus 2: Aturan dipatuhi (Inferensi Valid)
# Sensor mendeteksi gerakan, DAN alarm berbunyi.
cek_sistem_alarm(True, True)

# Kasus 3: Aturan tidak relevan (Inferensi Valid)
# Sensor tidak mendeteksi gerakan, dan alarm tidak berbunyi.
cek_sistem_alarm(False, False)

# Kasus 4: Aturan tidak dilanggar (Inferensi Valid)
# Sensor tidak mendeteksi gerakan, tetapi alarm berbunyi (misal: alarm manual).
cek_sistem_alarm(False, True)

print("====================================")