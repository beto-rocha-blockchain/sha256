## 🔐 SHA-256

Este repositório é dedicado ao estudo do algoritmo de hash SHA-256. Ele apresenta exemplos práticos em Python que demonstram como aplicar SHA-256 para:

- Gerar hashes de strings
- Verificar integridade de arquivos
- Entender o papel do SHA-256 na blockchain

## 🧪 Requisitos

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 📂 Estrutura

- examples/hash_string.py: Gera o hash SHA-256 de qualquer string.

- examples/file_integrity.py: Gera e compara hashes de arquivos.

- docs/SHA256_basics.md: Explicação teórica sobre o funcionamento do SHA-256.

## 📚 Referências

- Documentação hashlib

- Funções de hash no contexto da blockchain

## ✅ Rodar os scripts

Para gerar o hash de uma string:

```bash
python examples/hash_string.py
```

Para gerar o hash de um arquivo (ex: um .txt):

```bash
python examples/file_integrity.py
```
