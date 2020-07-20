import os

print(os.name)

#print(os.environ)
print(os.getcwd())

print(os.listdir())

os.chdir('aulas')
print(os.getcwd())

os.mkdir('aula modulo os')
print(os.listdir())

os.removedirs('aula modulo os')
print(os.listdir())
