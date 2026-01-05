from functions import write_file
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
print("-"*50)
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
print("-"*50)
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))