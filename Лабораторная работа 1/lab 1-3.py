# TODO Найдите количество книг, которое можно разместить на дискете


disket = 1.44
listy = 100
stroki = 50
simvols = 25
code = 4

book = code*simvols*stroki*listy
book = book/1024

kolvo = 1.44*1024/book
kolvo=round(kolvo)
print("Количество книг, помещающихся на дискету:", kolvo)