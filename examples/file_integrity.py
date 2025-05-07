import hashlib
import os

def hash_file(file_path):
    if not os.path.exists(file_path):
        return "Arquivo não encontrado."

    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

if __name__ == "__main__":
    path = input("Caminho do arquivo: ")
    result = hash_file(path)
    print(f"SHA-256: {result}")
