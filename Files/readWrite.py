import sys

try:
    file = open('654.txt', 'r')

    for f in file:
        print(f)

except FileNotFoundError:
    print("File not found exception")
except:
    print("Unexpected error:", sys.exc_info()[0])