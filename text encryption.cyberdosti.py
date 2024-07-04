def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26
            code = ord(char) + shift_amount
            if char.islower():
                if code > ord('z'):
                    code -= 26
                encrypted_message += chr(code)
            elif char.isupper():
                if code > ord('Z'):
                    code -= 26
                encrypted_message += chr(code)
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message, shift):
    return encrypt(message, -shift)

def main():
    print("Secret Message Encryption and Decryption Tool")
    choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? ")

    if choice.upper() == 'E':
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift number: "))
        encrypted_message = encrypt(message, shift)
        print("Encrypted message:", encrypted_message)
    elif choice.upper() == 'D':
        message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift number: "))
        decrypted_message = decrypt(message, shift)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice, please select either 'E' or 'D'.")

if __name__ == "__main__":
    main()
