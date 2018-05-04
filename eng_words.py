expression = 'I want to work for you'
print(expression)
expression = expression.replace(' ', '')  # удаляем проблемы
vowels = set("aeiouyAEIOUY")
word_set = set(expression)
print(word_set.difference(vowels))
