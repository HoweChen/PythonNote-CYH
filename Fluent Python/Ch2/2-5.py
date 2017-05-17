import array

symbols = '$¢£¥€¤'
symbols_tuple = tuple(ord(symbol) for symbol in symbols)

print(symbols_tuple)

symbols_array = array.array('I', (ord(symbol) for symbol in symbols))
print(symbols_array)
