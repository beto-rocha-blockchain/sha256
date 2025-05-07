import hashlib

def hash_string(input_string):
    sha = hashlib.sha256()
    sha.update(input_string.encode('utf-8'))
    return sha.hexdigest()

if __name__ == "__main__":
    user_input = input("Digite uma string para gerar o hash SHA-256: ")
    hash_result = hash_string(user_input)
    print(f"Hash gerado: {hash_result}")
