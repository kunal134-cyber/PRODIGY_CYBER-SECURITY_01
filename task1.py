def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Shift within alphabet range
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char  # Keep other characters as is
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)  # Decryption is reverse of encryption

# Main Program
def main():
    print("Caesar Cipher Program ")
    choice = input("Type 'E' to encrypt or 'D' to decrypt: ").strip().upper()

    if choice not in ('E', 'D'):
        print("Invalid choice. Please enter 'E' or 'D'.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift value (0-25): "))
    except ValueError:
        print("Shift value must be an integer.")
        return

    if choice == 'E':
        result = caesar_encrypt(message, shift)
        print(f" Encrypted message: {result}")
    else:
        result = caesar_decrypt(message, shift)
        print(f" Decrypted message: {result}")

if __name__ == "__main__":
    main()
