
not_compres_text = "WWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"

compres_text = "9W3B24W1B14W"


def compres_rle(text):

    
    result = ''
    pred_simbol = ''
    index = 1
    for char in text:
        if char != pred_simbol:
            if pred_simbol:
                result += str(index) + pred_simbol
            index = 1
            pred_simbol = char
        else:
            index += 1
    else:
        result += str(index)+pred_simbol
    return result


def decompress_text(text):

    result = ''
    index = ''
    for char in text:
        if char.isdigit():
            index += char
        else:
            result += char*int(index)
            index = ''
    return result


print(compres_rle(not_compres_text))

print(decompress_text(compres_text))
