# Lab 08 - moduł pytest

## 1. Czym jest `pytest`?

**`pytest`** to jeden z najpopularniejszych frameworków do testowania w Pythonie, służący do tworzenia i uruchamiania **testów jednostkowych oraz integracyjnych**.

[Dokumentacja](https://docs.pytest.org/)

Framework ten jest alternatywą dla wbudowanego modułu:

* `unittest`

Jednak w wielu projektach Pythonowych `pytest` jest preferowany, ponieważ:

* ma prostszą składnię
* wymaga mniej kodu
* oferuje wiele dodatkowych funkcji
* łatwo rozszerza się przez pluginy

---

## 2. Instalacja `pytest`

Instalacja przy użyciu `pip`:

```bash
pip install pytest
```

Sprawdzenie instalacji:

```bash
pytest --version
```

---

## 3. Podstawowa idea działania `pytest`

W przeciwieństwie do `unittest`, w `pytest` **testy mogą być zwykłymi funkcjami**, a nie metodami klas.

Najprostszy test wygląda tak:

```python
def test_addition():
    assert 2 + 2 == 4
```

Framework automatycznie:

* znajdzie test
* uruchomi go
* sprawdzi asercję

---

## 4. Struktura projektu z pytest

Typowa struktura projektu:

```
project/
└── src/
│   └── calculator.py
│
└── tests/
    └── test_calculator.py
```

Zasady wykrywania testów:

| element | reguła                 |
| ------- | ---------------------- |
| plik    | zaczyna się od `test_` |
| funkcja | zaczyna się od `test_` |
| klasa   | zaczyna się od `Test`  |

---

## 5. Przykład programu

Plik `calculator.py`

```python
def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b
```

---

## 6. Testy w `pytest`

Plik `test_calculator.py`

```python
from calculator import add, divide


def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(6, 3) == 2
```

---

## 7. Uruchamianie testów

Aby uruchomić testy:

```bash
pytest
```

Przykładowy wynik:

```
==================== test session starts ====================
collected 2 items

test_calculator.py ..                                [100%]

===================== 2 passed =============================
```

---

## 8. Testowanie wyjątków

W `pytest` wyjątki testuje się przy pomocy `pytest.raises`.

Przykład:

```python
import pytest
from calculator import divide


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)
```

---

## 9. Parametryzacja testów

Jedną z największych zalet `pytest` jest **parametryzacja testów**.

Pozwala testować funkcję na wielu danych wejściowych.

---

### Przykład

```python
import pytest
from calculator import add


@pytest.mark.parametrize("a,b,result", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (10, 5, 15)
])
def test_add(a, b, result):
    assert add(a, b) == result
```

Framework wykona **4 testy**.

---

## 10. Fixtures

Fixtures to mechanizm przygotowywania **danych lub środowiska testowego**.

Pozwalają uniknąć powtarzania kodu.

---

### Przykład

```python
import pytest

@pytest.fixture
def sample_data():
    return [1, 2, 3]
```

Test:

```python
def test_sum(sample_data):
    assert sum(sample_data) == 6
```

`pytest` automatycznie wstrzyknie fixture.

---

## 11. Setup i teardown

Fixtures mogą też przygotowywać i sprzątać środowisko.

```python
@pytest.fixture
def database():
    db = connect_database()
    yield db
    db.close()
```

`yield` oznacza:

```
setup → test → teardown
```

---

## 12. Markery w pytest

Markery pozwalają oznaczać testy.

Przykład:

```python
@pytest.mark.slow
def test_big_calculation():
    ...
```

Uruchomienie tylko szybkich testów:

```bash
pytest -m "not slow"
```

---

## 13. Pomijanie testów

Test można pominąć:

```python
import pytest

@pytest.mark.skip
def test_old_feature():
    ...
```

Lub warunkowo:

```python
@pytest.mark.skipif(sys.platform == "win32")
def test_linux_feature():
    ...
```

---

## 14. Testy oczekujące na poprawkę

Można oznaczyć test jako **oczekiwanie na poprawkę błędu**:

```python
@pytest.mark.xfail
def test_bug():
    assert broken_function() == 5
```

Jeśli test nie przejdzie – nie psuje builda.

---

## 15. Integracja z pokryciem kodu

`pytest` bardzo dobrze współpracuje z `coverage`.

Instalacja pluginu:

```bash
pip install pytest-cov
```

Uruchomienie:

```bash
pytest --cov
```

Raport:

```
Name           Stmts   Miss  Cover
-----------------------------------
calculator.py     10      1   90%
```

---

## 16. Najważniejsze zalety pytest

| zaleta          | opis                           |
| --------------- | ------------------------------ |
| prosta składnia | testy jako funkcje             |
| mniej kodu      | brak klas i boilerplate        |
| parametryzacja  | testowanie wielu danych        |
| fixtures        | łatwe przygotowanie środowiska |
| pluginy         | ogromny ekosystem              |
| integracja z CI | bardzo popularny w DevOps      |

---

## 17. `pytest` vs `unittest`

| cecha          | unittest             | pytest             |
| -------------- | -------------------- | ------------------ |
| składnia       | bardziej rozbudowana | prostsza           |
| asercje        | metody klasy         | zwykłe `assert`    |
| parametryzacja | trudniejsza          | bardzo prosta      |
| fixtures       | ograniczone          | bardzo rozbudowane |
| popularność    | standard Python      | standard branżowy  |

---

## 18. Typowy workflow testowania w Pythonie

W wielu projektach pipeline wygląda tak:

```
black
flake8
pylint
vulture
pytest
coverage
```

Czyli:

1. formatowanie kodu
2. analiza statyczna
3. testy
4. pomiar pokrycia kodu

---

## 19. Podsumowanie

`pytest` to nowoczesny framework testowy w Pythonie umożliwiający łatwe tworzenie i uruchamianie testów.

Jego główne cechy to:

* prostota użycia
* duża elastyczność
* możliwość parametryzacji testów
* mechanizm fixtures
* integracja z narzędziami analizy jakości kodu.

Dzięki temu `pytest` jest obecnie **jednym z najczęściej używanych narzędzi testowych w projektach Pythonowych**.

## 20. Przykładowy projekt

Stwórzmy przykładowy projekt, który demonstruje użycie pytest. Naszym przykładem będzie prosta klasa Person z metodami do zarządzania danymi osobowymi.

### Kod źródłowy (src/person.py)

```python
class Person:
    def __init__(self, first_name, last_name, age=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_adult(self):
        if self.age is None:
            raise ValueError("Age is not set")
        return self.age >= 18

    def celebrate_birthday(self):
        if self.ageis None:
            raise ValueError("Ageisnotset")
        self.age+= 1
        return self.age
```

### Testy(tests/test_person.py)

```python
import pytest
from src.person import Person

#Fixture- odpowiednik setUp w unittest

@pytest.fixture
def person():
    return Person("Jan","Kowalski", 30)

def test_get_full_name(person):
    #Sprawdzamy, czy metoda get_full_name zwraca poprawną wartość
    assert person.get_full_name()== "Jan Kowalski"

def test_is_adult_true(person):
    #Sprawdzamy, czy metoda is_adult zwraca True dla osoby pełnoletniej
    assert person.is_adult()== True

def test_is_adult_false():
    #Sprawdzamy, czy metoda is_adult zwraca False dla osoby niepełnoletniej
    young_person = Person("Anna", "Nowak",15)
    assert young_person.is_adult()== False

def test_is_adult_no_age():
    #Sprawdzamy, czy metoda is_adult zgłasza wyjątek, gdy age nie jest ustawiony
    person_no_age= Person("Piotr","Wiśniewski")
    with pytest.raises(ValueError):
        person_no_age.is_adult()

def test_celebrate_birthday(person):
    #Sprawdzamy, czy metoda celebrate_birthday zwiększa wiek o 1
    old_age = person.age
    new_age = person.celebrate_birthday()
    assert new_age == old_age + 1
    assert person.age == old_age + 1
```

### Uruchamianie testów

Aby uruchomić te testy z pytest, możesz skorzystać z kilku metod:

1. Uruchomienie wszystkich testów:
```bash
pytest
```
2. Uruchomienie określonego pliku testowego:
```bash
pytest tests/test_person.py
```
3. Uruchomienie testów z określonym wzorcem nazwy:
```bash
pytest tests/test_*.py
```
4. Uruchomienie testów z wyświetlaniem szczegółowych informacji:
```bash
pytest-v
```
5. Uruchomienie określonego testu:
```bash
pytest tests/test_person.py::test_get_full_name
```

## Zadania

> Wszystkie kody podane w poleceniach są przykładowe, można zrealizować to inaczej.

**Zad 1.** Napisz testy jednostkowe dla prostej funkcji kalkulującej cenę po rabacie. Funcja przyjmuje dwa argumenty: cenę podstawową (price) oraz wartość rabatu w procentach (discount). Funkcja zwraca cenę po rabacie.

```python
def calculate_discounted_price(price, discount):
    """
    Calculate price after applying discount.

    Args:
        price (float): Base price
        discount (float): Discount as percentage (0-100)

    Returns:
        float: Price after discount
    """
    if not isinstance(price, (int, float)) or price< 0 :
        raise ValueError("Price must be a non-negative number")

    if not isinstance(discount, (int,float)) or discount < 0 or discount> 100 :
        raise ValueError("Discount must be a number between 0 and 100")

    discounted_price =price *( 1 - discount/ 100 )
    return round(discounted_price, 2 )
```

Napisz komplet testów jednostkowych używając pytest, które przetestują:
1. Poprawność obliczania ceny po rabacie dla różnych scenariuszy
2. Obsługę nieprawidłowych danych wejściowych


3. Zaokrąglanie wyników do dwóch miejsc po przecinku

**Zad 2.** Załóżmy, że mamy klasęShoppingCartreprezentującą koszyk zakupowy, który umożliwia dodawanie produktów, zliczanie ich wartości oraz usuwanie produktów.

```python
class Product:
    def __init__(self,id, name, price):
        self.id = id
        self.name =name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.products= {}

    def add_product(self, product, quantity= 1 ):
        if quantity <= 0 :
            raise ValueError("Quantity must be positive")
        if product.id in self.products:
            self.products[product.id]["quantity"] += quantity
        else :
            self.products[product.id]= {
                "product": product,
                "quantity": quantity
            }

    def remove_product(self, product_id, quantity= 1 ):
        if product_id not in self.products:
            raise ValueError("Product not in cart")
        if quantity <= 0 :
            raise ValueError("Quantity must be positive")
        if self.products[product_id]["quantity"]<= quantity:
            del self.products[product_id]
        else :
            self.products[product_id]["quantity"] -= quantity

    def get_total_price(self):
        total =sum(item["product"].price *item["quantity"]
                    for item in self.products.values())
        return round(total, 2 )

    def get_product_count(self):
        return sum(item["quantity"] for item in self.products.values())
```
Napisz testy dla tej klasy wykorzystując fixture’y oraz parametryzację testów. Testy powinny
sprawdzać:

1. Dodawanie produktów (pojedynczych i wielu sztuk)
2. Usuwanie produktów (pojedynczych i wielu sztuk)
3. Obliczanie całkowitej wartości koszyka
4. Zliczanie liczby produktów w koszyku
5. Obsługę błędów (np. próba usunięcia produktu, którego nie ma w koszyku)

**Zad 3.** Poniżej znajduje się klasaLibraryManager, która zarządza biblioteką książek. Klasa umożliwia dodawanie książek, wypożyczanie ich, wyszukiwanie oraz generowanie statystyk. Twoim zadaniem jest napisanie kompletu testów jednostkowych dla tej klasy.

```python
class Book:
    def __init__(self, book_id, title, author, publication_year, genre):
        self.book_id =book_id
        self.title = title
        self.author =author
        self.publication_year = publication_year
        self.genre = genre
        self.is_borrowed =False
        self.borrow_count = 0

    def __str__(self):
        return f"{self.title}by {self.author} ({self.publication_year})"


class LibraryManager:
    def __init__(self):
        self.books = {}
        self.borrowed_books ={}


    def add_book(self, book):
        """
        Add a book to the library

        Args:
        book (Book): Book to add

        Returns:
        bool: True if book was added, False if book with same ID already exists
        """
        if not isinstance(book, Book):
            raise TypeError("Object must be of type Book")
        if book.book_id in self.books:
            return False
        self.books[book.book_id]= book
        return True

    def get_book(self, book_id):
        """
        Get a book by its ID

        Args:
        book_id: ID of the book to get

        Returns:
        Book or None: Book if found, None otherwise
        """
        return self.books.get(book_id)

    def remove_book(self, book_id):
        """
        Remove a book from the library


        Args:
        book_id: ID of the book to remove

        Returns:
        bool: True if book was removed, False if book wasn't in the library
        """
        if book_id not in self.books:
            return False
        if self.books[book_id].is_borrowed:
            raise ValueError("Cannot remove a borrowed book")
        del self.books[book_id]
        return True

    def borrow_book(self, book_id, borrower_id):
        """
        Borrow a book

        Args:
        book_id: ID of the book to borrow
        borrower_id: ID of the borrower

        Returns:
        bool: True if book was borrowed, False otherwise
        """
        if book_id not in self.books:
            raise ValueError("Book not found in library")
        book =self.books[book_id]
        if book.is_borrowed:
            return False
        book.is_borrowed =True
        book.borrow_count += 1
        if borrower_id not in self.borrowed_books:
            self.borrowed_books[borrower_id] = []
        self.borrowed_books[borrower_id].append(book_id)
        return True

    def return_book(self, book_id, borrower_id):
        """
        Return a borrowed book

        Args:
        book_id: ID of the book to return
        borrower_id: ID of the borrower

        Returns:
        bool: True if book was returned, False otherwise
        """
        if book_id not in self.books:
            raise ValueError("Book not found in library")
        if borrower_id not in self.borrowed_books or book_id not in self.borrowed_books[borrower_id]:
            raise ValueError("Book was not borrowed by this borrower")
        book =self.books[book_id]
        if not book.is_borrowed:
            return False
        book.is_borrowed =False
        self.borrowed_books[borrower_id].remove(book_id)
        # Clean up empty borrower entries
        if not self.borrowed_books[borrower_id]:
            del self.borrowed_books[borrower_id]
        return True

    def search_books(self, criteria):
        """
        Search for books based on criteria

        Args:
        criteria (dict): Dictionary with search criteria
        (title, author, year_from, year_to, genre)

        Returns:
        list: List of books matching criteria
        """
        results = []

        for book in self.books.values():
            matches =True
            if 'title' in criteria and criteria['title'].lower() not in book.title.lower():
                matches =False
            if 'author' in criteria and criteria['author'].lower() not in book.author.lower():
                matches =False
            if 'year_from' in criteria and book.publication_year <criteria['year_from']:
                matches =False
            if 'year_to' in criteria and book.publication_year > criteria['year_to']:
                matches =False
            if 'genre' in criteria and book.genre != criteria['genre']:
                matches =False
            if 'available_only' in criteria and criteria['available_only'] and book.is_borrowed:
                matches =False
            if matches:
                results.append(book)
        return results

    def get_statistics(self):
        """
        Get library statistics

        Returns:
        dict: Dictionary with statistics
        """
        total_books =len(self.books)
        borrowed_count = sum( 1 for book in self.books.values() if book.is_borrowed)
        available_count =total_books - borrowed_count
        # Count books by genre
        genres = {}
        for book in self.books.values():
            if book.genre not in genres:
                genres[book.genre] = 0
            genres[book.genre] += 1
        # Find most popular books (by borrow count)
        popular_books = sorted(
            self.books.values(),
            key= lambda book: book.borrow_count,
            reverse=True
        )[: 5 ] # Top 5
        return {
            "total_books": total_books,
            "available_books": available_count,
            "borrowed_books": borrowed_count,
            "borrowers_count":len(self.borrowed_books),
            "genres": genres,
            "popular_books": popular_books
        }
```
Napisz komplet testów jednostkowych, które dokładnie przetestują klasęLibraryManager. Testy powinny:

1. Sprawdzać poprawność dodawania, usuwania i pobierania książek
2.Testować proces wypożyczania i zwracania książek
3.Weryfikować funkcjonalność wyszukiwania książek według różnych kryteriów
4. Sprawdzać generowanie statystyk biblioteki
5.Wykorzystywać parametryzację do testowania różnych scenariuszy
6. Używać fixture do konfiguracji wspólnych elementów testów
7.Testować obsługę błędów (np. próba usunięcia wypożyczonej książki)
8. Sprawdzać zachowanie metod w przypadku nieprawidłowych danych wejściowych
