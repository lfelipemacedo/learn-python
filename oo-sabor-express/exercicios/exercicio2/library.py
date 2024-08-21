from book import Book

hp_prisioner_azkaban =  Book("Harry Potter and The Prisoner of Azkaban", 'J K Rowling', 2004)
a_game_of_thrones =  Book("A Game of Thrones", 'Gorge R R Martin', 1996)

a_game_of_thrones.lendBook()
print(hp_prisioner_azkaban.__str__())
print(a_game_of_thrones.__str__())

available_books = Book.check_availability(2004)

for book in available_books:
    print(f'{book.__str__()}')