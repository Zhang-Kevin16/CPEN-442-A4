import sys
import hashlib

if len(sys.argv) != 3:
    print("Usage: python3 patch.py PATH_TO_EXECUTABLE NEW_PASSWORD")

path = sys.argv[1]
new_password = sys.argv[2]
new_hash = hashlib.sha1(new_password.encode("ascii")).digest()
print(new_hash.hex())
hash_offset = 0x1d3e9

new_path = path.split(".exe")
new_path = new_path[0]+".{}.exe".format(new_password)
print(new_path)

data = b''
with open(path, "rb") as f:
    data = f.read()

with open(new_path, "wb") as f:
    f.write(data)
    f.seek(hash_offset)
    f.write(new_hash)

