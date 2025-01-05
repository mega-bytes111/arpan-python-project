# Caesar Cipher project..

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# encryption convert plain text to cipher text
def encryption(plain_text,shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)#(x+n)%26
            new_position = (position+shift_key)%26
            cipher_text+=alphabet[new_position]
        else:
            cipher_text+=char    
    print(f"Here's the text after encryption : {cipher_text}")
# decryption convert cipher text to plain text
def decryption(cipher_text,shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            position = alphabet.index(char)#(x-n)%26
            x = position-shift_key
            if x<0:
                x+=26
            new_position = x%26    
            plain_text+=alphabet[new_position]
        else:#may be that char is not in alphabet then simply add it..
            plain_text+=char
    print(f"Here's the text after decryption : {plain_text}")
wanna_end = False   
while not wanna_end:
    what_to_do = input("Type 'encrypt' for encryption,type 'decrypt' for decryption :\n")
    text = input("Type Your Message :\n").lower()
    shift = int(input("Enter shift key:\n"))

    if what_to_do=="encrypt":
        encryption(plain_text=text,shift_key=shift)

    elif what_to_do=="decrypt":
        decryption(cipher_text=text,shift_key=shift)

    play_again = input("Enter 'yes' for continue,otherwise 'no' :\n")
    if play_again=='no':
        wanna_end = True
else:
    print("Have a nice day,Good Bye !!")            