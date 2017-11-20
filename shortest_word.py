#Find the shortest word in a given string and ouput its length.
s = ("bitcoin take over the world maybe who knows perhaps")

def find_short(s):
    var = s.split(" ")
    l = len(min(var, key = len))
    return l

print find_short(s)
