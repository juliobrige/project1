from datetime import datetime
from pathlib import Path

class BaseModel:
    BASE_DIR = Path(__file__).resolve().parent.parent
    DB_DIR = BASE_DIR / 'db'

    def save(self):
        table_path = Path(self.DB_DIR / f'{self.__class__.__name__}.txt')

        if not table_path.exists():
            table_path.touch()

        with open(table_path, 'a') as arq:
            arq.write("|".join(list(map(str, self.__dict__.values()))))  
            arq.write('\n')

    @classmethod
    def get(cls):
        table_path = Path(cls.DB_DIR / f'{cls.__name__}.txt')

        if not table_path.exists():
            table_path.touch()

        result = []

        with open(table_path, 'r') as arq:
            lines = arq.readlines()

           
            for line in lines:
                
                values = line.strip().split('|')

                attribute_dict = {attr: value for attr, value in zip(vars(cls()).keys(), values)}

               
                result.append(attribute_dict)

        return result


class Password(BaseModel):
    def __init__(self, domain=None, password=None, expire=False):
        self.domain = domain
        self.password = password
        self.create_at = datetime.now().isoformat()  #
        self.expire = expire


p1 = Password(domain='JulioBenjamimB', password='1234')


p1.save()

passwords = Password.get()

for password in passwords:
    print(password)
