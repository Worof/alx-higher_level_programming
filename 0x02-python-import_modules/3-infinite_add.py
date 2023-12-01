#!/usr/bin/python3
import sys

def main():
    total = sum(int(arg) for arg in sys.argv[1:])  # Sum all arguments excluding the script name
    print(total)

if __name__ == "__main__":
    main()
