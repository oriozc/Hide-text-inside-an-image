
with open('image.jpg', 'ab') as f:
    f.write(b"hello world")


with open('image.jpg', 'rb') as f:
    content = f.read()
    offset = content.index(bytes.fromhex('FFD9'))   # finding the offset of FFD9 (every jpg file ends with FFD9)
    f.seek(offset + 2)  # the secret data is stored 2 bytes after the calculated offset
    print(f.read())