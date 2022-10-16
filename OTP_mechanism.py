import onetimepad

msg = input("Enter your Secret Message : ")
cipher = onetimepad.encrypt(msg, 'random')
print("Cipher text is ")
print(cipher)
print("Plain text is ")
msg = onetimepad.decrypt(cipher, 'random')

print(msg)
