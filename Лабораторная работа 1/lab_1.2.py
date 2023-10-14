# TODO Найдите количество книг, которое можно разместить на дискете
V = 1.44
pages = 100
string = 50
symbols = 25
symbol_size = 4
book_size = (pages*string*symbols*symbol_size)/1024**2
book_in_diskette = int(V//book_size)
print("Количество книг, помещающихся на дискету:", book_in_diskette)
