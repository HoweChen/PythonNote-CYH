import array

symbols = '$¢£¥€¤'
symbols_tuple = tuple(ord(symbol) for symbol in symbols)

# (ord(symbol) for symbol in symbols) actually returns a generator
# tuple() accept one argument which could be an iterable object, generator is
# an interable object, so it could be used in tuple(). Also, when there is
# only one argument needed in the function call, the outside () of
# (ord(symbol) for symbol in symbols) could be ignored

print(symbols_tuple)

symbols_array = array.array('I', (ord(symbol) for symbol in symbols))
print(symbols_array)
