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

decoded_message_reversed = decode_image_reversed("filename.extantion")
print(f"Pesan terbalik yang diambil: {decoded_message_reversed}")
