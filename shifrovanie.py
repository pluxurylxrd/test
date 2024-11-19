def shfr(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def ushfr(a, b):
    if b == 0:
        return 1, 0
    else:
        x1, y1 = ushfr(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
    return x, y


def generate_keys():
    p = 114689
    q = 157733
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 53567
    d = ushfr(e, phi)[0] % phi
    return (e, n), (d, n)


def encrypt(text, pub_key):
    e, n = pub_key
    encrypted_message = [str(pow(ord(char), e, n)) for char in text]
    return ' '.join(encrypted_message)


def decrypt(text, priv_key):
    d, n = priv_key
    encrypted_numbers = text.split(' ')
    decrypted_message = ''.join([chr(pow(int(num), d, n)) for num in encrypted_numbers])
    return decrypted_message

public_key = None  # (e, n)
private_key = None  # (d, n)

public_key, private_key = generate_keys() if public_key is None else (public_key, private_key)

message = "я купил москвич"

print(f"Публичный ключ: {public_key}")
print(f"Приватный ключ: {private_key}")
print(f"Исходное сообщение: {message}")

encrypted = encrypt(message, public_key)
print(f"Зашифрованное сообщение: {encrypted}")

decrypted = decrypt(encrypted, private_key)
print(f"Расшифрованное сообщение: {decrypted}")
