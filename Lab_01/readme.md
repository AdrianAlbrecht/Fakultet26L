# Lab 01 - wprowadzenie do testowania z Python unittest

Pakiet `unittest` to standardowa biblioteka Pythona służąca do tworzenia i uruchamiania testów jednostkowych.

[Dokumentacja](https://docs.python.org/3/library/unittest.html)

## Organizacja projektu

Dobrą praktyką jest organizowanie kodu w sposób, który oddziela kod produkcyjny od testów:

```
project_root/
    src/                    # Kod źródłowy aplikacji
        __init__.py
        example.py          # Przykładowy moduł
    tests/                  # Testy jednostkowe
        __init__.py
        test_example.py     # Testy dla example.py
```

## Przykładowy projekt

Stwórzmy przykładowy projekt, który demonstruje użycie unittest. Naszym przykładem będzie prosta klasa Person z metodami do zarządzania danymi osobowymi.


Kod źródłowy _(src/person.py)_
```python
class Person:
    def __init__(self, first_name, last_name, age = None):
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
        if self.age is None:
            raise ValueError("Age is not set")
        self.age += 1
        return self.age
```

A teraz testy _(tests/test_person.py)_:

```python
import unittest
from src.person import Person


class TestPerson(unittest.TestCase):
    def setUp(self):
        #Ten kod jest wykonywany przed każdym testem
        self.person = Person("Jan", "Kowalski", 30)

    def test_get_full_name(self):
        #Sprawdzamy, czy metoda get_full_name zwraca poprawną wartość
        self.assertEqual(self.person.get_full_name(), "Jan Kowalski")

    def test_is_adult_true(self):
        #Sprawdzamy, czy metoda is_adult zwraca True dla osoby pełnoletniej
        self.assertTrue(self.person.is_adult())

    def test_is_adult_false(self):
        #Sprawdzamy, czy metoda is_adult zwraca False dla osoby niepełnoletniej
        young_person = Person("Anna", "Nowak",15)
        self.assertFalse(young_person.is_adult())

    def test_is_adult_no_age(self):
        #Sprawdzamy, czy metoda is_adult zgłasza wyjątek, gdy age nie jest ustawiony
        person_no_age = Person("Piotr","Wiśniewski")
        with self.assertRaises(ValueError):
            person_no_age.is_adult()

    def test_celebrate_birthday(self):
        #Sprawdzamy, czy metoda celebrate_birthday zwiększa wiek o 1
        old_age = self.person.age
        new_age = self.person.celebrate_birthday()
        self.assertEqual(new_age, old_age + 1)
        self.assertEqual(self.person.age, old_age + 1)

    def tearDown(self):
        #Ten kod jest wykonywany po każdym teście
        pass


if __name__ == "__main__":
    unittest.main()    
```

### Metody setUp i tearDown
1. `setUp()`- metoda wywoływana przed każdym testem, służy do przygotowania środowiska testowego
2. `tearDown()`- metoda wywoływana po każdym teście, służy do czyszczenia po testach

### Uruchamianie testów

Aby uruchomić testy, możesz skorzystać z kilku metod:

1. Uruchomienie pojedynczego pliku testowego:
```
python -m unittest tests/test_person.py
```
2. Uruchomienie wszystkich testów w katalogu:
```
python -m unittest discover -s tests
```
3. Uruchomienie testów z określonym wzorcem nazwy:
```
python -m unittest discover -s tests -p "test_*.py"
```


### Najważniejsze metody unittest

Poniżej znajdziesz objaśnienie najważniejszych metod z modułu unittest, które będą przydatne do rozwiązania zadań:

1. `assertEqual(a, b)`- sprawdza, czy a == b
2. `assertNotEqual(a, b)`- sprawdza, czy a != b
3. `assertTrue(x)`- sprawdza, czy bool(x) is True
4. `assertFalse(x)`- sprawdza, czy bool(x) is False
5. `assertIs(a, b)`- sprawdza, czy a is b
6. `assertIsNot(a, b)`- sprawdza, czy a is not b
7. `assertIsNone(x)`- sprawdza, czy x is None
8. `assertIsNotNone(x)`- sprawdza, czy x is not None
9. `assertIn(a, b)`- sprawdza, czy a in b
10. `assertNotIn(a, b)`- sprawdza, czy a not in b
11. `assertIsInstance(a, b)`- sprawdza, czy isinstance(a, b)
12. `assertNotIsInstance(a, b)`- sprawdza, czy not isinstance(a, b)
13. `assertRaises(exception, callable, *args, **kwargs)`- sprawdza, czy wywołanie funkcji zgłasza określony wyjątek
14. `assertAlmostEqual(a, b)`- sprawdza, czy a ~ b (przydatne dla liczb zmiennoprzecinkowych)

Oczywiśnie nie są to wszystkie dostępne metody, ale te najczęściej używane.

## Zadania

Zadanie 1

Stwórz klasę `Calculator` z metodami do podstawowych operacji matematycznych: `add`, `subtract`, `multiply` i `divide`. Następnie napisz testy jednostkowe sprawdzające poprawność działania każdej z tych metod. Pamiętaj o przetestowaniu przypadku dzielenia przez zero.

Zadanie 2

Napisz funkcję `validate_email`, która sprawdza czy podany ciąg znaków jest poprawnym adresem email. Funkcja powinna zwracać True dla poprawnych adresów i False dla niepoprawnych. Następnie napisz testy jednostkowe, które sprawdzą różne przypadki: poprawne adresy, adresy bez znaku @, adresy bez domeny, itd.

Zadanie 3

Stwórz klasę `StringManipulator` z metodami: `reverse_string`, `count_words` i `capitalize_words`. Napisz testy jednostkowe sprawdzające działanie tych metod dla różnych przypadków, w tym dla pustego ciągu znaków oraz ciągów zawierających znaki specjalne.

Zadanie 4

Zaimplementuj funkcję `fibonacci`, która zwraca n-ty wyraz ciągu Fibonacciego. Napisz testy jednostkowe sprawdzające poprawność działania tej funkcji dla różnych wartości n, w tym dla n=0, n=1 oraz dużych wartości n.

Zadanie 5

Napisz klasę `ShoppingCart` symulującą koszyk zakupowy z metodami `add_item`, `remove_item`, `get_total` i `clear`. Utwórz komplet testów jednostkowych sprawdzających poprawność działania koszyka w różnych scenariuszach użycia.

Zadanie 6

Stwórz funkcję `find_most_frequent_word`, która przyjmuje tekst i zwraca najczęściej występujące w nim słowo. Napisz testy jednostkowe sprawdzające działanie funkcji dla różnych tekstów, w tym dla pustego tekstu, tekstu z jednym słowem oraz tekstów zawierających słowa o takiej samej częstotliwości.

Zadanie 7

Zaimplementuj klasę `TemperatureConverter` z metodami do konwersji między różnymi skalami temperatury: `celsius_to_fahrenheit`, `fahrenheit_to_celsius`, `celsius_to_kelvin` i `kelvin_to_celsius`. Napisz testy jednostkowe sprawdzające poprawność konwersji dla różnych wartości temperatur, w tym dla temperatury zera absolutnego.

Zadanie 8

Stwórz klasę `BankAccount` symulującą konto bankowe z metodami `deposit`, `withdraw` i `get_balance`. Zaimplementuj mechanizm wyjątków dla operacji niedozwolonych (np. wypłata większej kwoty niż dostępna na koncie). Napisz testy jednostkowe sprawdzające poprawne działanie konta oraz obsługę wyjątków.

Zadanie 9

Napisz funkcję `is_palindrome`, która sprawdza czy podany ciąg znaków jest palindromem (czyta się tak samo od przodu i od tyłu). Funkcja powinna ignorować wielkość liter i znaki niealfanumeryczne. Utwórz zestaw testów jednostkowych sprawdzających różne przypadki.

Zadanie 10

Zaimplementuj klasę `TodoList` do zarządzania listą zadań z metodami `add_task`, `complete_task`, `get_active_tasks` i `get_completed_tasks`. Napisz testy jednostkowe sprawdzające poprawność działania wszystkich metod.