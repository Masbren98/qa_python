from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_same_book_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_invalid_name_length(self):
        collector = BooksCollector()
        collector.add_new_book('Жизнь и удивительные приключения Робинзона Крузо, моряка из Йорка, прожившего двадцать восемь лет')
        assert 'Жизнь и удивительные приключения Робинзона Крузо, моряка из Йорка, прожившего двадцать восемь лет' not in collector.get_books_genre()

    def test_set_book_genre_for_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Злой город')
        collector.set_book_genre('Злой город', 'Ужасы')
        assert collector.get_book_genre('Злой город') == 'Ужасы'

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Злой город')
        collector.set_book_genre('Злой город', 'Артхауз')
        assert collector.get_book_genre('Злой город') == ''

    def test_get_book_genre_existing_genre_set(self):
        collector = BooksCollector()
        collector.add_new_book('Город')
        collector.set_book_genre('Город', 'Комедии')
        assert collector.get_book_genre('Город') == 'Комедии'

    def test_get_book_genre_non_existing_book(self):
        collector = BooksCollector()
        assert collector.get_book_genre('Неизвестный') is None

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Город')
        collector.set_book_genre('Город', 'Комедии')
        collector.add_new_book('Деревня')
        collector.set_book_genre('Деревня', 'Комедии')
        comedies = collector.get_books_with_specific_genre('Комедии')
        assert 'Город' in comedies
        assert 'Деревня' in comedies
        assert len(comedies) == 2

    def test_get_books_with_specific_genre_invalid_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Город')
        collector.set_book_genre('Город', 'Комедии')
        books = collector.get_books_with_specific_genre('Артхауз')
        assert books == []

    def test_get_book_genre_genre_set(self):
        collector = BooksCollector()
        collector.add_new_book('Город')
        collector.set_book_genre('Город', 'Комедии')
        assert collector.get_book_genre('Город') == 'Комедии'

    def test_get_book_genre_no_genre_set(self):
        collector = BooksCollector()
        collector.add_new_book('Город')
        assert collector.get_book_genre('Город') == ''

    def test_get_books_for_children_positive(self):
        collector = BooksCollector()
        collector.add_new_book('Незнайка')
        collector.set_book_genre('Незнайка', 'Комедии')
        collector.add_new_book('Рататуй')
        collector.set_book_genre('Рататуй', 'Мультфильмы')
        books_for_children = collector.get_books_for_children()
        assert 'Незнайка' in books_for_children
        assert 'Рататуй' in books_for_children
        assert len(books_for_children) == 2

    def test_get_books_for_children_add_genre_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Злой город')
        collector.set_book_genre('Злой город', 'Ужасы')
        collector.add_new_book('Поймай меня')
        collector.set_book_genre('Поймай меня', 'Детективы')
        books_for_children = collector.get_books_for_children()
        assert 'Злой город' not in books_for_children
        assert 'Поймай меня' not in books_for_children
        assert len(books_for_children) == 0

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Рататуй')
        collector.add_book_in_favorites('Рататуй')
        favorites = collector.get_list_of_favorites_books()
        assert 'Рататуй' in favorites

    def test_add_book_in_favorites_add_same_book_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Рататуй')
        collector.add_book_in_favorites('Рататуй')
        collector.add_book_in_favorites('Рататуй')
        favorites = collector.get_list_of_favorites_books()
        assert 'Рататуй' in favorites
        assert len(favorites) == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Рататуй')
        collector.add_book_in_favorites('Рататуй')
        collector.add_new_book('Незнайка')
        collector.add_book_in_favorites('Незнайка')
        favorites = collector.get_list_of_favorites_books()
        collector.delete_book_from_favorites('Рататуй')
        assert 'Незнайка' in favorites
        assert 'Рататуй' not in favorites

    def test_delete_book_from_favorites_not_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Рататуй')
        collector.delete_book_from_favorites('Рататуй')
        favorites = collector.get_list_of_favorites_books()
        assert 'Рататуй' not in favorites

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Рататуй')
        collector.add_new_book('Незнайка')
        collector.add_book_in_favorites('Рататуй')
        favorites = collector.get_list_of_favorites_books()
        assert favorites == ['Рататуй']

    def test_get_list_of_favorites_books_no_books_in_list(self):
        collector = BooksCollector()
        favorites = collector.get_list_of_favorites_books()
        assert favorites == []
