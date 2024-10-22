floppy_size_mb = 1.44
book_sheets = 100
numbers_of_lines = 50
symbols_on_line = 25
byte_per_symbol = 4

book_size = symbols_on_line * numbers_of_lines * book_sheets * byte_per_symbol
byte_floppy_size = floppy_size_mb * 1024**2

count_books = int(byte_floppy_size / book_size)

print("Количество книг, помещающихся на дискету:", count_books)
