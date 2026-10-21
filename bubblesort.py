data = [5, 60, 10, 20, 30, 70, 55, 12]
n = len(data)

for i in range(n - 1):
  swapped = False  # Penanda apakah ada pertukaran di putaran ini
  for j in range(n - 1 - i):
    if data[j] > data[j + 1]:
      data[j], data[j + 1] = data[j + 1], data[j]
      swapped = True  # Terjadi pertukaran

  print(f"Pass ke-{i+1}:", data)

  # Jika dalam satu putaran penuh tidak ada satupun pertukaran, berarti data sudah urut
  if not swapped:
    print(
        f"Data sudah terurut sepenuhnya pada Pass ke-{i+1}, perulangan dihentikan"
        " lebih awal."
    )
    break