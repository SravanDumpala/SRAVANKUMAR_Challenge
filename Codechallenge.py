import re
import sys

def isValidCardNumber(sequence):
    regexPattern='^([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$'
    match = re.match(regexPattern,sequence)
    if match == None:
        print("Invalid")
        return
    for group in match.groups():
        if group[0] * 4 == group:
            print("Invalid")
            return
    # Check for consecutive numbers
    if not re.search(r"(.)(-?\1){3,}",sequence):
        print("Valid")
    else:
        print("Invalid")

n=int(sys.stdin.readline())
inputStrngs = sys.stdin.readlines()
for inputStr in inputStrngs:
    inputStr = inputStr.rstrip('\n')
    isValidCardNumber(inputStr)
