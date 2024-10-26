# TODO Найдите количество книг, которое можно разместить на дискете
symbol_size = 4
symbol_in_string = 25
string_on_page = 50
pages_in_book = 100
book_size = symbol_size * symbol_in_string * string_on_page * pages_in_book
disk_size_in_bytes = 1.44 * 1024 * 1024
books_on_disk = disk_size_in_bytes / book_size
print("Количество книг, помещающихся на дискету:", int(books_on_disk))
