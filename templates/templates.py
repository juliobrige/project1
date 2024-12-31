import sys
import os

sys.path.append(os.path.abspath(os.curdir))


from model.password import Password
from views.password_views import FernetHasher


action = input('Digite 1 para salvar uma nova senha ou 2 para ver uma senha: ')


match action:
    case '1':

        if len(Password.get()) == 0:
            key, path = FernetHasher.create_key(archive=True)
            print('Sua chave foi salva com sucesso, salve com cuidado.')
            print(f'Chave: {key.decode("utf-8")}')
        if __path__:
            print("Chave salva no arquivo, lembre-se de remover o arquivo apos o tranferir.")
            print(f'Caminho: {path}')

        else :
            key = input ('Digite sua chave usada para a criptografia, use sempre a mesma senha')

            domain = input('Dominio:')
            password = input('senha:')
            fernet_user = FernetHasher(key)
            p1 = Password(domain=domain, password=fernet_user.encrypt(password).decode('utf-8'))
            p1.save()

    
    case '2':
        password = Password.get()
        if password:
            print(f'Sua senha salva é: {password}')
        else:
            print('Nenhuma senha salva encontrada.')

    case _: 
        print("Opção inválida.")
