```kullanıcıdan aldığı inputa göre yukarıdaki şekli oluşturan bir kod yazın```




def print_baklava(size):
  for i in range(size):
    print("*" * (i + 1))
  for i in range(size - 1, 0, -1):
    print("*" * i)

# Örnek kullanım
A = int(input("Kaç satır dilim istediğiniz yazınız: "))
print_baklava(A)
