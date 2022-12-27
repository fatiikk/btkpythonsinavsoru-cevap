```doyadaki her satırı 1 cümle olarak kabul edin
1 cümledeki ortanca kelimeyi alın ters çevirin cümleye geri ekleyin ve output.txt dosyasına yazdırın
çift sayıda kelime varsa ortancadan 1 öncesini çevirsin```



import os

filename = "asdasd.txt"

with open(filename, "r") as f:
  lines = f.readlines()

output_filename = "output.txt"
with open(output_filename, "w") as f:

  for line in lines:
    
    sentences = line.split(".")
    
    for sentence in sentences:
     
      words = sentence.split()
    
      if len(words) % 2 == 0:
        middle_index = len(words) // 2 - 1
      else:
        middle_index = len(words) // 2
      middle_word = words[middle_index]
    
      reversed_middle_word = middle_word[::-1]
     
      words[middle_index] = reversed_middle_word
      
      new_sentence = " ".join(words)
     
      f.write(new_sentence)
      
      f.write("\n")
      
with open(output_filename, "r") as f:
  output = f.read()

print(output)
