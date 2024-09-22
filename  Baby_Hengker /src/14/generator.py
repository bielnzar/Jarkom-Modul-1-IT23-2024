import os
from PIL import Image

def decode_image_reversed(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = img.load()

    binary_message = ""
    for i in range(img.width):
        for j in range(img.height):
            r, g, b = pixels[i, j]
            
            r_bin = format(r, '08b')
            binary_message += r_bin[-1]

    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i + 8]
        char = chr(int(byte, 2))
        
        if message.endswith("EOF"):
            break
        message += char

    message = message.replace("EOF", "")

    reversed_message = message[::-1]
    return reversed_message

def find_messages_in_images(folder_path):

    image_files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))])
    
    files_with_messages = []
    all_messages = []

    for image_file in image_files:
        full_path = os.path.join(folder_path, image_file)
        try:
            decoded_message = decode_image_reversed(full_path)
            if decoded_message.strip():
                files_with_messages.append(image_file)
                all_messages.append(decoded_message)
                print(f"Pesan ditemukan dalam file: {image_file}")
                print(f"Pesan terdekode: {decoded_message}")
            else:
                print(f"Tidak ada pesan dalam file: {image_file}")
        except Exception as e:
            print(f"Error saat memproses file {image_file}: {str(e)}")
    
    print("\nNama-nama file yang memiliki pesan (Berurut abjad):")
    for file in files_with_messages:
        print(file)
    
    print("\nSemua pesan yang ditemukan (Berurut sesuai file):")
    for message in all_messages:
        print(message)

folder_path = "/home/bosmuda/Documents/jarkomprak/1/stego/images"
find_messages_in_images(folder_path)