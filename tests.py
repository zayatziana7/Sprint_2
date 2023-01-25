from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_cant_add_book_twice(self):
        collector = BooksCollector()
        book_name = 'Эпичная книга'

        collector.add_new_book(name=book_name)
        collector.add_new_book(name=book_name)

        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_cant_set_rating_for_not_added_book(self):
        collector = BooksCollector()
        not_added_book_name = 'Книга, которая не была добавлена'

        collector.set_book_rating(name=not_added_book_name, rating=1)

        assert collector.get_book_rating(name=not_added_book_name) is None

    def test_set_book_rating_cant_set_rating_below_minimum(self):
        collector = BooksCollector()
        book_name = 'Книга с невероятно низким рейтингом'

        collector.add_new_book(name=book_name)
        collector.set_book_rating(name=book_name, rating=0)

        assert collector.get_book_rating(name=book_name) == 1

    def test_set_book_rating_cant_set_rating_above_maximum(self):
        collector = BooksCollector()
        book_name = 'Книга с невероятно высоким рейтингом'

        collector.add_new_book(name=book_name)
        collector.set_book_rating(name=book_name, rating=11)

        assert collector.get_book_rating(name=book_name) == 1

    def test_get_book_rating_not_added_book_has_no_rating(self):
        collector = BooksCollector()
        not_added_book_name = 'Книга, которая не была добавлена'

        assert collector.get_book_rating(name=not_added_book_name) is None

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        book_name = 'Самая любимая книга'

        collector.add_new_book(name=book_name)
        collector.add_book_in_favorites(name=book_name)

        assert collector.get_list_of_favorites_books()[0] == book_name

    def test_add_book_in_favorites_cant_add_to_favorites_not_added_book(self):
        collector = BooksCollector()
        book_name = 'Самая любимая книга'

        collector.add_book_in_favorites(name=book_name)

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        book_name = 'Самая любимая книга, которую придется удалить'

        collector.add_new_book(name=book_name)
        collector.add_book_in_favorites(name=book_name)
        collector.delete_book_from_favorites(name=book_name)

        assert len(collector.get_list_of_favorites_books()) == 0

