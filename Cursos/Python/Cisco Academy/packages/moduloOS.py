### CRIAR DIRETÓRIOS - mkdir
# import os

# os.mkdir('my_first_directory')
# print(os.listdir())

### CRIAR DIRETÓRIOS RECURSIVOS - makedirs
# import os

# os.makedirs("my_first_directory/my_second_directory")
# os.chdir("my_first_directory")
# print(os.listdir())

### LOCALIZA A PASTA DE TRABALHO ATUAL - getcwd
# import os

# os.makedirs("my_first_directory/my_second_directory")
# os.chdir("my_first_directory")
# print(os.getcwd())
# os.chdir("my_second_directory")
# print(os.getcwd())

### DELETAR DIRETÓRIOS VAZIOS - rmdir
# import os

# os.mkdir("my_first_directory")
# print(os.listdir())
# os.rmdir("my_first_directory")
# print(os.listdir())

### DELETAR DIRETÓRIOS E SUBDIRETÓRIOS - removedirs
import os

os.makedirs("my_first_directory/my_second_directory")
print(os.listdir())
os.removedirs("my_first_directory/my_second_directory")
print(os.listdir())

##### 4.5.1.1