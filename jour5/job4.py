def decaler_message(message, decalage):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  resultat = ''
  
  for c in message:
    if c.isalpha():
      c_decale = alphabet[(alphabet.index(c.lower()) + decalage) % 26]
      if c.isupper():
        c_decale = c_decale.upper()
      resultat += c_decale
    else:
      resultat += c
  return resultat

message = input('Entrez un message : ')
decalage = int(input('Entrez un décalage : '))

print(decaler_message(message, decalage))
