word = input("Введите слово: ")
if str(word) == "".join(reversed(word)) :
    print("Слово полидром")
else:
    print("Слово не полидром")