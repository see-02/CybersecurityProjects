import bcrypt

def string_hash(input_string):
    salt = bcrypt.gensalt()
    encoded = input_string.encode('utf-8')
    hashed_string = bcrypt.hashpw(encoded, salt)
    return hashed_string

hashed1 = string_hash("_password-123_")
print(f"\'_password-123_\' \t-->Hash Function-->\t {hashed1}")
