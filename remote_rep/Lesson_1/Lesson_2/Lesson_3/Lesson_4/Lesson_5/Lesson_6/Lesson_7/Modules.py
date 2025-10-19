# Чтобы установить любой модуль - нам нужна команда pip install <module_name>
# Репозиторий для всех сторонних модулей питона - pypi.org
import random # Модуль рандомных функцих
import sys
from mymodule import asist



print(sys.platform)

print(random.randint(0,5))
print(random.randrange(6,8)) #рандрендж до невключительно

users=['Aleks','Antont','Sergey']
print(random.choice(users))

b='text'

asist('text')