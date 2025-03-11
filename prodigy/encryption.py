def caesar_cipher(text, shift, encrypt=True):
    result = ""
    
    for char in text:
        if char.isalpha():
            shift_amount = shift if encrypt else -shift
            ascii_offset = 65 if char.isupper() else 97
            shifted_char = chr((ord(char) - ascii_offset + shift_amount) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char

    return result

def main():
    print("Caesar Cipher Program")
    
    # Input text to encrypt or decrypt
    text = input("Enter the text: ")
    
    # Input shift value
    shift = int(input("Enter the shift value: "))
    
    # Choose encryption or decryption
    choice = input("Type 'e' for encryption or 'd' for decryption: ").lower()
    
    if choice == 'e':
        encrypted_text = caesar_cipher(text, shift, encrypt=True)
        print(f"Encrypted text: {encrypted_text}")
    elif choice == 'd':
        decrypted_text = caesar_cipher(text, shift, encrypt=False)
        print(f"Decrypted text: {decrypted_text}")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
