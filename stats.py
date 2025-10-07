def word_count(string):
    words = string.split()
    return len(words)

def symbol_count(string):
    symbol_dict = {}
    for char in string:
        if char in symbol_dict:
            symbol_dict[char] += 1
        else:
            symbol_dict[char] = 1
    return symbol_dict

def sort_symbols(symbol_dict): 
    symbol_list = []
    for key in symbol_dict:
        symbol_list.append({"char": key, "num": symbol_dict[key]})
    symbol_list.sort(reverse=True, key=sort_symbols_on)
    return symbol_list

def sort_symbols_on(items):
    return items["num"]