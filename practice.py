import hashlib

md5_hash = hashlib.md5()
md5_hash.update(b"DgSable@123")
hex_digest = md5_hash.hexdigest()
print("MD5 Hash : ",hex_digest)

sha1_hash = hashlib.sha1()
sha1_hash.update(b"DgSable@123")
sha1hex_digest = sha1_hash.hexdigest()
print("SHA1 Hash : ",sha1hex_digest)


sha256_hash = hashlib.sha256()
sha256_hash.update(b"DgSable@123")
sha256hex_digest = sha256_hash.hexdigest()
print("SHA256 Hash : ",sha256hex_digest)

sha512_hash = hashlib.sha512()
sha512_hash.update(b"DgSable@123")
sha512hex_digest = sha512_hash.hexdigest()
print("SHA512 Hash : ",sha512hex_digest)

sha3_512_hash = hashlib.sha3_512()
sha3_512_hash.update(b"DgSable@123")
sha3_512hex_digest = sha3_512_hash.hexdigest()
print("SHA3_512 Hash : ",sha3_512hex_digest)

blake2b_hash = hashlib.blake2b()
blake2b_hash.update(b"Hello, World!")
hex_digest = blake2b_hash.hexdigest()
print("Blake2b Hash:", hex_digest)

blake2s_hash = hashlib.blake2s()
blake2s_hash.update(b"Hello, World!")
hex_digest = blake2s_hash.hexdigest()
print("Blake2s Hash:", hex_digest)

