from random import choice

def get_file_lines(filename):
    
    in_file = open(filename, "r")
    lines = in_file.readlines()
    in_file.close()
    return lines 
