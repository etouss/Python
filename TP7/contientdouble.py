import re
def contientdouble(s):
    m=re.match(r".*(.+)\1.*",s)
    if m == None:
        return None
    return m.group(1)
    