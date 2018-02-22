def urlifyString(string,length):
    if len(string)<=length:
        return string.replace(' ','%20')
    return string[:length].replace(' ','%20')

print urlifyString('asd fffg    ',6) # asd%20ff , O(1)