import string, secrets

class FernetHasher:
    # Conjunto de caracteres para a string aleatória
    RANDOM_STRING_CHARS = string.ascii_lowercase + string.ascii_uppercase

    @classmethod
    def _get_random_string(cls):
        random_string = ''  # Definir uma variável para armazenar a string aleatória
        for i in range(25):
            random_string += secrets.choice(cls.RANDOM_STRING_CHARS)  # Acrescentar um caractere aleatório
        print(random_string)  # Imprimir a string final após o loop

# Chamando o método da classe
FernetHasher._get_random_string()
