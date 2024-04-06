
import os
# write in file
with open('my_file.txt', 'w') as file:
    file.write('Hello my friend hope you are doing great!\n')
    file.write("Me, i'm well\n")
    file.write('I miss you\n')
    
    print(file)
    
# reading file
    
read_file = open('my_file.txt', 'r')
result= read_file.read()
print(result)

#modifying my_file.txt in append mode
append_file = open('my_file.txt', 'a+')
append_file.write('Do you like this session of python\n')
append_file.write('for me i like python with all my things\n')
append_file.write('Because it has big value this day\n')
append_file = open('my_file.txt', 'r')
read_append_file = append_file.read() # reading appended file
print(append_file)
print(read_append_file)

# Error Handling
# try and except
try:
  
  path_of_file = open("my_file.txt")
  result_of_try = path_of_file.read()
  print(result_of_try)
except FileNotFoundError :
  print("File not found")
  
except PermissionError:
    print("you don't allowed to open this file")
