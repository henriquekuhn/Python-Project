alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt_msg(message, encrypt_key):
    encrypt_msg = ""
    number = 0
    for letter in message:
        if letter == ' ':
            encrypt_msg += ' '
        elif letter in alphabet:
            shift = int(alphabet.index(letter))+int(encrypt_key)
            print(shift)
            print(int(alphabet.index(letter)))
            if shift > len(alphabet):
                shift = shift - len(alphabet)
                print(shift)
            encrypt_msg += alphabet[shift]
        else:
            encrypt_msg += letter
        number += 1
    print(encrypt_msg)


def decrypt_msg(message, decrypt_key):
    decrypt_msg = ""
    number = 0
    for letter in message:
        if letter == ' ':
            decrypt_msg += ' '
        elif letter in alphabet:
            shift = int(alphabet.index(letter))-int(decrypt_key)
            print(shift)
            print(len(alphabet))
            decrypt_msg += alphabet[shift]
        else:
            decrypt_msg += letter

        number += 1
    print(decrypt_msg)

if __name__ == "__main__":
    print("Welcome to Encrypt Decrypt Script")
    run_script = True
    while run_script:
        choice = input("Type 'e' to ENCRYPT or 'd' to DECRYPT: ")
        if choice == 'e':
            encrypt_key = input("chose a encrypt key number: ")
            encrypt_msg(input("Enter your message: "), encrypt_key)
        else:
            decrypt_key = input("chose a decrypt key number: ")
            decrypt_msg(input("Enter your message: "), decrypt_key)
        continue_script = input(f"Type 'y' if you want to continue: ")
        if continue_script != 'y':
            run_script = False