import sys

EXIT_FAILURE = 1

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def pall(self):
        for value in reversed(self.stack):
            print(value)

def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def main(filename):
    stack = Stack()
    line_number = 0
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                line_number += 1
                parts = line.split()
                if not parts:
                    continue
                opcode = parts[0]
                
                if opcode == "push":
                    if len(parts) != 2 or not is_integer(parts[1]):
                        print(f"L{line_number}: usage: push integer")
                        sys.exit(EXIT_FAILURE)
                    stack.push(int(parts[1]))
                elif opcode == "pall":
                    stack.pall()
                else:
                    print(f"L{line_number}: unknown instruction {opcode}")
                    sys.exit(EXIT_FAILURE)
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        sys.exit(EXIT_FAILURE)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: monty <file>")
        sys.exit(EXIT_FAILURE)
    
    main(sys.argv[1])
