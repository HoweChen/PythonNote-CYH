symbols = '$¢£¥€¤'
codes_one = []

for symbol in symbols:
    codes_one.append(ord(symbol))

print(codes_one)

codes_two = []
codes_two = [ord(symbol) for symbol in symbols]
print(codes_two)
