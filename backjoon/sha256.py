# SHA-256 : 10930
import hashlib

plain_text = input()
result = hashlib.sha256(plain_text.encode())

print(result.hexdigest())