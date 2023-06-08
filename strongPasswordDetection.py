import re

# Password requirements
# At least 8 characters long.
# Both upper and lowercase characters.
# At least one digit

strongPasswordRegex = re.compile(r'''(
    (\w{8,})
    )''', re.VERBOSE)

lowerCaseDetection = re.compile(r"[a-z]")
upperCaseDetection = re.compile(r"[A-Z]")
numericDetection = re.compile(r"[0-9]")

def strongPasswordDetection(password):
    if strongPasswordRegex.search(password) == None:
        return print('Password needs to be at least 8 characters long.')
    elif (lowerCaseDetection.search(password) == None or 
          upperCaseDetection.search(password) == None):
        return print('Password needs to contain uppercase and lowercase characters.')
    elif numericDetection.search(password) == None:
        return print('Password must contain a number.')
    return print('Password accepted.')

strongPasswordDetection('HELLOOO5oOOO')