from random import choice

def get_file_lines(filename):
    
    in_file = open(filename, "r")
    lines = in_file.readlines()
    in_file.close()
    return lines 

def lines_printed_backwards(lines_list):
    lines_list.reverse()
    lines_length = len(lines_list)
    for i in range(lines_length):
        line = lines_list[i]
        line_num = lines_length - i
        print(f"{line_num} {line}")

def lines_printed_random(lines_list):
    for line in lines_list:
        print(choice(lines_list))

 for line in open('poem.txt'):
    
    if line.startswith('I') or line.startswith('You'): 
       print(line)

poem_lines = get_file_lines('poem.txt')
lines_printed_backwards(poem_lines)

