def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        
        if char.isupper():
            encrypted_message += chr((ord(char) + shift - 65) % 26 + 65)
        
        elif char.islower():
            encrypted_message += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            
            encrypted_message += char
    return encrypted_message

def decrypt(message, shift):
    decrypted_message = ""
    for char in message:
        if char.isupper():
            decrypted_message += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            decrypted_message += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted_message += char
    return decrypted_message

def main():
    choice = input("Would you like to (E)ncrypt or (D)ecrypt? ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))
    
    if choice == 'e':
        print("Encrypted message:", encrypt(message, shift))
    elif choice == 'd':
        print("Decrypted message:", decrypt(message, shift))
    else:
        print("Invalid choice. Please select 'E' for encrypt or 'D' for decrypt.")

if __name__ == "__main__":
    main()
