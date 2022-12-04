def caesar_encrypt(plainText, step):
 outText = []
 cryptText = []
    
 uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
 lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for eachLetter in plainText:
  if eachLetter in uppercase:
   index = uppercase.index(eachLetter)
   crypting = (index + step) % 26
   cryptText.append(crypting)
   newLetter = uppercase[crypting]
   outText.append(newLetter)
  elif eachLetter in lowercase:
   index = lowercase.index(eachLetter)
   crypting = (index + step) % 26
   cryptText.append(crypting)
   newLetter = lowercase[crypting]
   outText.append(newLetter)
return outText
a = input("Enter the text:")
code = caesar_encrypt(a , 5)
print(a)
print(code)
print()
