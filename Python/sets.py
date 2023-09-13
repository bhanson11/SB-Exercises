lemon = {'sour', 'yellow', 'fruit', 'bumpy'}
banana = {'fruit', 'smooth', 'sweet', 'yellow'}
orange = ['fruit', 'bumpy', 'orange', 'sweet']

lemon | banana
# {'bumpy', 'fruit', 'smooth', 'sour', 'sweet', 'yellow}

lemon & banana
# {'fruit', 'yellow'}

lemon - banana
# {'bumpy', 'sour'}

banana - lemon
# {'smooth', 'sweet'}

lemon ^ banana
# {'bumpy', 'smooth', 'sour', 'sweet'}


# for adj in banana | lemon | set(orange):
#     print(adj)
