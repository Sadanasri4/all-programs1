from PIL import Image
import numpy as np

def load_image(image_path):
    # Load image from the given path
    img = Image.open(r"C:\Users\sadan\OneDrive\Desktop\codsoft\pixel\example.jpg"  # Absolute path
)
    return img

def image_to_array(img):
    return np.array(img, dtype=np.uint8)  # Ensure the array is of type uint8

def encrypt_image(pixel_array, key):
    encrypted_array = (pixel_array.astype(np.int16) + key) % 256  # Convert to int16 to avoid overflow
    return encrypted_array.astype(np.uint8)  # Convert back to uint8

def decrypt_image(encrypted_array, key):
    decrypted_array = (encrypted_array.astype(np.int16) - key) % 256  # Convert to int16 to avoid overflow
    return decrypted_array.astype(np.uint8)  # Convert back to uint8

def array_to_image(pixel_array):
    return Image.fromarray(pixel_array)

def save_image(img, output_path):
    img.save(output_path)

def main(image_path, key, output_encrypted_path, output_decrypted_path):
    img = load_image(image_path)
    pixel_array = image_to_array(img)

    # Encrypt the image
    encrypted_array = encrypt_image(pixel_array, key)
    encrypted_img = array_to_image(encrypted_array)
    save_image(encrypted_img, output_encrypted_path)

    # Decrypt the image
    decrypted_array = decrypt_image(encrypted_array, key)
    decrypted_img = array_to_image(decrypted_array)
    save_image(decrypted_img, output_decrypted_path)

    print(f"Encrypted image saved at {output_encrypted_path}")
    print(f"Decrypted image saved at {output_decrypted_path}")

# Example Usage
if __name__ == "__main__":
    image_path = r"C:\Users\sadan\OneDrive\Desktop\codsoft\pixel\example.jpg"  # Replace with the correct image file name
    key = 50  # Simple integer key for encryption/decryption
    output_encrypted_path = r"C:\Users\sadan\OneDrive\Desktop\codsoft\pixel\encrypted_image.png"
    output_decrypted_path = r"C:\Users\sadan\OneDrive\Desktop\codsoft\pixel\decrypted_image.png"
    main(image_path, key, output_encrypted_path, output_decrypted_path)
