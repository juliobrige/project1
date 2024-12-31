import string
import secrets
import hashlib
import base64
from pathlib import Path
from cryptography.fernet import Fernet

class FernetHasher:

    RANDOM_STRING_CHARS = string.ascii_lowercase + string.ascii_uppercase
    BASE_DIR = Path(__file__).resolve().parent.parent 
    KEY_DIR = BASE_DIR / 'keys'

    def __init__(self, key):
        if not isinstance(key, bytes):
            key = key.encode()

       
        if len(key) != 32:
            raise ValueError("A chave deve ter exatamente 32 bytes.")
        
        self.fernet = Fernet(base64.urlsafe_b64encode(key))

    @classmethod
    def _get_random_string(cls, length=25):
        random_string = ''.join(secrets.choice(cls.RANDOM_STRING_CHARS) for _ in range(length))
        return random_string

    @classmethod
    def create_key(cls, archive=False):

        value = cls._get_random_string()
        print("String gerada:", value)

        hasher = hashlib.sha256(value.encode('utf-8'))
        key = base64.urlsafe_b64encode(hasher.digest())[:32] 
        key = key.decode('utf-8') 

        if archive:
            file_path = cls.archive_key(key)
            return key, file_path

        print("Chave gerada:", key)
        return key, None

    @classmethod
    def archive_key(cls, key):
        cls.KEY_DIR.mkdir(parents=True, exist_ok=True)

      
        file_name = cls.KEY_DIR / 'key.txt'
        counter = 1
        while file_name.exists():
            file_name = cls.KEY_DIR / f'key_{counter:05d}.txt'  
            counter += 1

    
        with open(file_name, 'w') as arq:
            arq.write(key)
        print(f"Chave salva em: {file_name}")

        return file_name

    def encrypt(self, value):
        if not isinstance(value, bytes):
            value = value.encode()
        return self.fernet.encrypt(value)


key, file_path = FernetHasher.create_key(archive=True)

if file_path:
    print(f"A chave foi salva em: {file_path}")
else:
    print("A chave não foi arquivada.")


fernet_instance = FernetHasher('A8TkHavaqk6r81NmOzu7UJDGh82Tt+F8uMvePiYIRYc='.encode()[:32])
encrypted_value = fernet_instance.encrypt('Minha senha')
print("Valor criptografado:", encrypted_value)
