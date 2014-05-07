import re
def double(s):
    m=re.match(r"(.*)\1$",s)
    if m == None:
        return None
    return m.group(1)
    