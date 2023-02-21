def oxford_comma(items):
    if(len(items) == 1):
        return items[0]
    elif(len(items) == 2):
        return f"{items[0]} and {items[1]}"
    elif(len(items) > 2):
        sentence = ", ".join(items[0:-1])
        sentence = sentence + f", and {items[-1]}"
        return sentence
    else:
        return "Invalid argument"
    return None
