import re

def regexStripFunc(text, regexText=' '):
    regexChecker = re.compile(rf"[^{regexText}]", re.IGNORECASE)
    return(''.join(regexChecker.findall(text)))


print(regexStripFunc('Hello, my name is Hubert. My stomach is growling.', 'my'))

