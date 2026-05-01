import hashlib

# Aap yahan apna password/text change kar sakte hain
text = "1111vijaygumthal"

print(f"--- Hashes for: {text} ---")

# MD5 (Common, but weak)
md5_hash = hashlib.md5(text.encode()).hexdigest()
print(f"MD5    : {md5_hash}")

# SHA-1 (Old standard)
sha1_hash = hashlib.sha1(text.encode()).hexdigest()
print(f"SHA-1  : {sha1_hash}")

# SHA-256 (Current industry standard)
sha256_hash = hashlib.sha256(text.encode()).hexdigest()
print(f"SHA-256: {sha256_hash}")

# SHA-512 (Very secure, long hash)
sha512_hash = hashlib.sha512(text.encode()).hexdigest()
print(f"SHA-512: {sha512_hash}")