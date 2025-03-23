# qa_python
test_add_new_book_add_two_books - проверка добавления двух книг с валидным названием
test_add_new_book_add_same_book_twice - проверка добавления двух одинаковых книг ( запись не повторяется)
test_add_new_book_invalid_name_length- проверка добавления книги с невалидным названием (книга не добавляется)
test_set_book_genre_for_existing_book - проверка присваивания жанра существующей книги
test_set_book_genre_invalid_genre - проверка присваивания жанра не из списка self.genre (жанр не выводится)
test_get_book_genre_existing_genre_set - проверка вывода жанра книги из self.genre
test_get_book_genre_non_existing_book - проверка вывода жанра для несуществующей книги
test_get_books_with_specific_genre - проверка вывода книг с определенным валидным жанром
test_get_books_with_specific_genre_invalid_genre - проверка вывода книг с определенным невалидным жанром
test_get_book_genre_genre_set -проверка вывода книг валидного жанра
test_get_book_genre_no_genre_set - проверка вывода книг без жанра
test_get_books_for_children_positive -проверка вывода книг для детей (позитивный, валидные жанры)
test_get_books_for_children_add_genre_age_rating - проверка вывода вниг для детей (негативный, с невалиндными жанрами)
test_add_book_in_favorites - проверка добавления книги в список избранное
test_add_book_in_favorites_add_same_book_twice - проверка добавления двух одинаковых книг в список избранное( запись не повторяется)
test_delete_book_from_favorites - проверка удаления книги из списка избранное
test_delete_book_from_favorites_not_in_favorites - проверка удаления книги из списка избранное , если книга ранее не была в этом списке
test_get_list_of_favorites_books - проверка вывода списка избранное с добавленными книгами
test_get_list_of_favorites_books_no_books_in_list - проверка вывода списка избранное, если не добавлена ни одна книга

