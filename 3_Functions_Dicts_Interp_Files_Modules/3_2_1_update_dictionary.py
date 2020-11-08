def update_dictionary(d, key, value):
    if key in d.keys():
        a = d[key]
        a.append(value)
        d[key] = a
    elif key*2 in d.keys():
        a = d[key*2]
        a.append(value)
        d[key*2] = a
    else:
        d[2*key] = [value]