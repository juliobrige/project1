import string
import secrets
import hashlib
import base64
from pathlib import Path

class FernetHasher:
    # Conjunto de caracteres para a string aleatória
    RANDOM_STRING_CHARS = string.ascii_lowercase + string.ascii_uppercase
    BASE_DIR = Path(__file__).resolve().parent.parent # Ajustado para ir apenas um nível acima
    KEY_DIR = BASE_DIR / 'keys'

    @classmethod
    def _get_random_string(cls, length=25):
        random_string = ''.join(secrets.choice(cls.RANDOM_STRING_CHARS) for _ in range(length))
        return random_string

    @classmethod
    def create_key(cls, archive=False):
        # Gerar string aleatória
        value = cls._get_random_string()
        print("String gerada:", value)

        # Gerar hash e codificar em base64
        hasher = hashlib.sha256(value.encode('utf-8'))
        key = base64.b64encode(hasher.digest()).decode('utf-8')  # Converte para string

        # Arquivar a chave, se solicitado
        if archive:
            file_path = cls.archive_key(key)
            return key, file_path

        print("Chave gerada:", key)
        return key, None

    @classmethod
    def archive_key(cls, key):
        # Verificar e criar o diretório se necessário
        cls.KEY_DIR.mkdir(parents=True, exist_ok=True)

        # Gerar nome de arquivo único
        file_name = cls.KEY_DIR / 'key.txt'
        counter = 1
        while file_name.exists():
            file_name = cls.KEY_DIR / f'key_{counter:05d}.txt'  # Cria nomes como key_00001.txt, key_00002.txt, etc.
            counter += 1

        # Salvar a chave no arquivo
        with open(file_name, 'w') as arq:
            arq.write(key)
        print(f"Chave salva em: {file_name}")

        return file_name

# Chamando os métodos da classe
key, file_path = FernetHasher.create_key(archive=True)

if file_path:
    print(f"A chave foi salva em: {file_path}")
else:
    print("A chave não foi arquivada.")
