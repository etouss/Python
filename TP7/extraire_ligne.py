import re
def extraire_ligne(s):
    m = re.match("(.*),(.*),(.*),(.*)",s)
    return (m.group(1),m.group(2),m.group(3),m.group(4))