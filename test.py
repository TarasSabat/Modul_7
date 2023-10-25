def encode(data):
    if not data:
        return []
    
    current = data[0]
    count = 1
    
    for i in range(1, len(data)): # for i in data):
        if data[i] == current:      # if i == current:
            count += 1
        else:
            break

    if count > 1:
        return [current, count] + encode(data[count:])
    else:
        return [current, count] + encode(data[count:])


print(encode(["X", "X", "X", "X", "X", "Z", "X", "Y", "Y", "Y", "Y", "Z", "Z"]))

