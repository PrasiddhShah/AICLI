from functions import get_file_content

print(get_file_content("calculator","lorem.txt"))
print("-"*50)
print(get_file_content("calculator", "main.py"))
print("-"*50)
print(get_file_content("calculator", "pkg/calculator.py"))
print("-"*50)
print(get_file_content("calculator", "/bin/cat"))
print("-"*50)
print(get_file_content("calculator", "pkg/does_not_exist.py"))