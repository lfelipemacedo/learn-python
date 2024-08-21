from book import Book

def main():
    hp_prisioner_azkaban =  Book("Harry Potter and The Prisoner of Azkaban", 'J K Rowling', 2004)
    a_game_of_thrones =  Book("A Game of Thrones", 'Gorge R R Martin', 1996)

    print(hp_prisioner_azkaban.__str__())
    print(a_game_of_thrones.__str__())

if __name__ == '__main__':
    main()