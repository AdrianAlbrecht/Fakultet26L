# Lab 03 - TDD w unittest

> Przypomnienie - [konwencja nazw](
https://piojas.pl/wp-content/uploads/2025/03/nazwy_plikow.pdf)

## Wprowadzenie

## 1. Czym jest TDD (Test-Driven Development)?

**TDD (Test-Driven Development)** to metodologia wytwarzania oprogramowania polegająca na tym, że **najpierw pisze się testy, a dopiero potem kod implementujący funkcjonalność**.

Czyli zamiast:

1. napisać funkcję
2. przetestować ją

robimy odwrotnie:

1. **piszemy test opisujący oczekiwane zachowanie**
2. uruchamiamy test → **test musi się nie powieść**
3. piszemy **minimalny kod**, który sprawi że test przejdzie
4. **refaktoryzujemy kod**

---

### Klasyczny cykl TDD: Red → Green → Refactor

1. **RED** – piszesz test, który **nie przechodzi**
2. **GREEN** – piszesz minimalny kod, który **przechodzi test**
3. **REFACTOR** – poprawiasz kod, ale **testy nadal muszą przechodzić**

Schemat:

```
napisz test → test fail → napisz kod → test pass → refactor
```

---

### Przykład idei TDD

Chcemy napisać funkcję `add(a, b)`.

#### Krok 1 – piszemy test

```python
def test_add():
    assert add(2, 3) == 5
```

Test nie przejdzie, bo funkcja jeszcze nie istnieje.

---

#### Krok 2 – minimalna implementacja

```python
def add(a, b):
    return a + b
```

Teraz test przechodzi.

---

#### Krok 3 – refaktoryzacja

Jeśli kod jest już dobry — nic nie zmieniamy.
Jeśli nie — poprawiamy strukturę.

---

## 2. Czym jest `unittest` w Pythonie?

`unittest` to **wbudowany framework do testów jednostkowych w Pythonie**.

Pozwala:

* tworzyć **klasy testowe**
* uruchamiać **testy automatycznie**
* sprawdzać wyniki przy pomocy **asercji**

Jest odpowiednikiem:

* **JUnit** w Javie
* **NUnit** w C#
* **pytest** jest nowocześniejszą alternatywą w Pythonie

Import:

```python
import unittest
```

---

## 3. Czym jest TDD w `unittest`?

**TDD w unittest oznacza stosowanie podejścia test-first przy użyciu frameworka unittest.**

Czyli:

1. najpierw piszesz **test w unittest**
2. uruchamiasz go → **fail**
3. piszesz implementację
4. test przechodzi

---

## 4. Przykład TDD w Python `unittest`

### Plik z testami

`test_math.py`

```python
import unittest
from math_utils import add

class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == "__main__":
    unittest.main()
```

---

### Uruchomienie testu

```
python test_math.py
```

Na początku dostaniesz błąd:

```
ModuleNotFoundError: No module named 'math_utils'
```

czyli **RED**.

---

### Implementacja

`math_utils.py`

```python
def add(a, b):
    return a + b
```

---

### Ponowne uruchomienie

```
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```

Czyli **GREEN**.

---

## 5. Najważniejsze metody asercji w `unittest`

Najczęściej używane:

| metoda                 | sprawdza                    |
| ---------------------- | --------------------------- |
| `assertEqual(a, b)`    | czy wartości są równe       |
| `assertNotEqual(a, b)` | czy wartości są różne       |
| `assertTrue(x)`        | czy wyrażenie jest True     |
| `assertFalse(x)`       | czy wyrażenie jest False    |
| `assertIsNone(x)`      | czy wartość to None         |
| `assertIn(a, b)`       | czy element jest w kolekcji |
| `assertRaises()`       | czy funkcja rzuca wyjątek   |

---

### Przykład sprawdzania wyjątku

```python
def divide(a, b):
    return a / b
```

Test:

```python
def test_divide_by_zero(self):
    with self.assertRaises(ZeroDivisionError):
        divide(5, 0)
```

---

## 6. Struktura projektu w TDD

Typowa struktura:

```
project/
│
├── math_utils.py
├── test_math_utils.py
```

albo bardziej profesjonalnie:

```
project/
│
├── src/
│   └── math_utils.py
│
├── tests/
│   └── test_math_utils.py
```

---

## 7. Zalety TDD

- kod jest **bardziej niezawodny**
- mniej błędów w produkcji
- kod jest **łatwiejszy do refaktoryzacji**
- projekt ma **automatyczną dokumentację zachowania**

---

## 8. Wady TDD

- pisanie testów zajmuje czas
- trudniejsze przy projektach eksploracyjnych
- wymaga **dyscypliny programisty**

---

## 9. Związek TDD z testami jednostkowymi

TDD prawie zawsze wykorzystuje **testy jednostkowe (unit tests)**.

Test jednostkowy sprawdza:

> najmniejszą testowalną część programu (np. funkcję lub metodę)

Przykład jednostki:

```
funkcja
metoda klasy
pojedynczy moduł
```

---

## 10. Jednozdaniowa definicja 

**TDD (Test-Driven Development)** to technika programowania polegająca na tworzeniu testów jednostkowych przed implementacją kodu i rozwijaniu oprogramowania w cyklu **Red → Green → Refactor**.

## Zadania

### 1. Zadanie łatwiejsze

W tym ćwiczeniu będziemy tworzyć klasę Trip zgodnie z zasadami Test-Driven Development (TDD), wykorzystując bibliotekę unittest w Pythonie.

#### Specyfikacja klasy Trip

Klasa Trip powinna:
1. Mieć konstruktor przyjmujący dwa argumenty: destination i duration
2. Posiadać dwie metody:
    - calculate_cost()- obliczającą koszt wycieczki
    - add_participant(participant)- dodającą uczestnika wycieczki

#### Kroki ćwiczenia (zgodnie z cyklem TDD: Red, Green, Refactor)

##### Etap 1: Testy dla konstruktora klasy
1. Utwórz plik test_trip.py.
2. Zaimportuj moduł unittest i moduł, w którym będzie znajdować się klasa Trip.
3. Stwórz klasę testową TestTripInitialization dziedziczącą po unittest.TestCase.
4. Napisz test sprawdzający, czy obiekt klasy Trip jest tworzony poprawnie z parametrami
“Paris” jako destination i 7 jako duration.
5. Napisz test sprawdzający, czy atrybuty destination i duration są poprawnie przypi
sywane.
6. Uruchom testy- powinny zakończyć się niepowodzeniem (faza Red).

##### Etap 2: Implementacja konstruktora klasy
1. Utwórz plik trip.py.
2. Zaimplementuj klasę Trip z konstruktorem przyjmującym parametry destination i
duration.
3. Uruchom testy- powinny zakończyć się powodzeniem (faza Green).

##### Etap 3: Testy dla metody calculate_cost()
1. Dodaj do klasy testowej nową metodę testującą test_calculate_cost.
2. Napisz test sprawdzający, czy metoda zwraca poprawny koszt dla wycieczki do “Paris”
na 7 dni (oczekiwany wynik: 700).
3. Napisz test sprawdzający, czy metoda zwraca poprawny koszt dla wycieczki do “Rome”
na 5 dni (oczekiwany wynik: 500).
4. Uruchom testy- powinny zakończyć się niepowodzeniem (faza Red).

##### Etap 4: Implementacja metody calculate_cost()
1. Dodaj do klasy Trip metodę calculate_cost(), która oblicza koszt wycieczki jako 100
jednostek za dzień.
2. Uruchom testy- powinny zakończyć się powodzeniem (faza Green).

##### Etap 5: Testy dla metody add_participant()
1. Dodaj do klasy testowej nową metodę testującą test_add_participant.
2. Napisz test sprawdzający, czy po dodaniu uczestnika “John” znajduje się on na liście
uczestników wycieczki.
3. Napisz test sprawdzający, czy po dodaniu kilku uczestników (“John”, “Alice”, “Bob”)
wszyscy znajdują się na liście.
4. Napisz test sprawdzający, czy próba dodania uczestnika o pustym imieniu (““) wywołuje
wyjątek ValueError z odpowiednim komunikatem.
5. Uruchom testy- powinny zakończyć się niepowodzeniem (faza Red).

##### Etap 6: Implementacja metody add_participant()
1. Dodaj do klasy Trip atrybut participants inicjalizowany jako pusta lista w konstruk
torze.
2. Zaimplementuj metodę add_participant(participant), która:
    - Sprawdza czy przekazany parametr nie jest pusty, jeśli jest- rzuca wyjątek ValueError z komunikatem “Participant name cannot be empty”
    - Dodaje uczestnika do listy participants
3. Uruchom testy- powinny zakończyć się powodzeniem (faza Green).

##### Etap 7: Refaktoryzacja
1. Przejrzyj kod klasy Trip i testy, zastanów się nad możliwymi usprawnieniami.
2. Przeprowadź refaktoryzację kodu, np. wprowadzając walidację typów lub dodając doku
mentację.
3. Upewnij się, że wszystkie testy nadal przechodzą po refaktoryzacji.

##### Etap 8: Dodatkowe testy brzegowe
1. Dodaj test sprawdzający zachowanie metody calculate_cost() dla wycieczki o długości
0 dni.
2. Dodaj test sprawdzający, czy po dodaniu tego samego uczestnika kilka razy, pojawia się
on odpowiednią ilość razy na liście.
3. Uruchom testy i dostosuj implementację, jeśli to konieczne.

##### Etap 9: Uruchomienie wszystkich testów
1. Uruchom wszystkie testy za pomocą komendy w terminalu.
2. Upewnij się, że wszystkie testy kończą się powodzeniem.

#### Wartości testowe
- Testy pozytywne:
    - Destination: “Paris”, Duration: 7, Oczekiwany koszt: 700
    - Destination: “Rome”, Duration: 5, Oczekiwany koszt: 500
    - Dodanie uczestnika “John” do wycieczki
    - Dodanie uczestników [“John”, “Alice”, “Bob”] do wycieczki
- Testy negatywne:
    - Destination: ““, Duration: 0, Oczekiwany koszt: 0
    - Dodanie tego samego uczestnika (“John”) kilkukrotnie
- Test wyjątku:
    - Dodanie uczestnika o pustym imieniu (““) powinno wywołać ValueError z komunikatem”Participant name cannot be empty”

### 2. Zadanie trudniejsze

Wtymćwiczeniu będziemy tworzyć klasę Sport zgodnie z zasadami Test-Driven Development (TDD), wykorzystując bibliotekę unittest w Pythonie. Dodatkowo zastosujemy właściwości
(properties) do walidacji i kontroli dostępu do atrybutów.

#### Specyfikacja rozszerzonej klasy Sport
Klasa Sport powinna:
1. Mieć konstruktor przyjmujący dwa argumenty: name i duration
2. Używać właściwości (properties) do weryfikacji:
    - name- musi być niepustym łańcuchem znaków
    - duration- musi być liczbą całkowitą większą od zera
3. Posiadać dwie metody:
    - calculate_calories()- obliczającą spalane kalorie podczas aktywności
    - add_equipment(equipment)- dodającą sprzęt potrzebny do uprawiania sportu

#### Kroki ćwiczenia (zgodnie z cyklem TDD: Red, Green, Refactor)

##### Etap 1: Testy dla konstruktora klasy
1. Utwórz plik test_sport.py.
2. Zaimportuj moduł unittest i moduł, w którym będzie znajdować się klasa Sport.
3. Stwórz klasę testową TestSportInitialization dziedziczącą po unittest.TestCase.
4. Napisz test sprawdzający, czy obiekt klasy Sport jest tworzony poprawnie z parametrami “Running” jako name i 30 jako duration.
5. Napisz test sprawdzający, czy atrybuty name i duration są poprawnie przypisywane.
6. Uruchom testy- powinny zakończyć się niepowodzeniem (faza Red).

##### Etap 2: Testy dla walidacji właściwości (properties)
1. Dodaj do klasy testowej metody testujące walidację właściwości name:
    - Test sprawdzający, czy próba ustawienia pustego łańcucha znaków jako name wywołuje ValueError.
    - Test sprawdzający, czy próba ustawienia liczby jako name wywołuje TypeError.
2. Dodaj do klasy testowej metody testujące walidację właściwości duration:
    - Test sprawdzający, czy próba ustawienia wartości 0 jako duration wywołuje
    ValueError.
    - Test sprawdzający, czy próba ustawienia wartości ujemnej (-5) jako duration wywołuje ValueError.
    - Test sprawdzający, czy próba ustawienia łańcucha znaków jako duration wywołuje TypeError.
3. Uruchom testy- powinny zakończyć się niepowodzeniem (faza Red).

##### Etap 3: Implementacja konstruktora i właściwości (properties)
1. Utwórz plik sport.py.
2. Zaimplementuj klasę Sport z prywatnym atrybutem _name i _duration.
3. Zaimplementuj właściwość name używając dekoratora @property dla gettera i @name.setter dla settera.
4. W setterze dla name dodaj walidację:
    - Sprawdzenie, czy wartość jest łańcuchem znaków- jeśli nie, rzuć TypeError z ko
    munikatem “Name must be a string”
    - Sprawdzenie, czy łańcuch znaków nie jest pusty- jeśli jest, rzuć ValueError z komunikatem “Name cannot be empty”
5. Zaimplementuj właściwość duration używając dekoratora @property dla gettera i @duration.setter dla settera.
6. W setterze dla duration dodaj walidację:
    - Sprawdzenie, czy wartość jest liczbą całkowitą- jeśli nie, rzuć TypeError z komunikatem “Duration must be an integer”
    - Sprawdzenie, czy wartość jest większa od zera- jeśli nie, rzuć ValueError z komunikatem “Duration must be greater than 0”
7. Zaimplementuj konstruktor, który używa tych setterów do ustawienia wartości.
8. Uruchom testy- powinny zakończyć się powodzeniem (faza Green).

##### Etap 4: Testy dla metody calculate_calories()
1. Dodaj do klasy testowej nową metodę testującą test_calculate_calories.
2. Napisz test sprawdzający, czy metoda zwraca poprawne kalorie dla aktywności “Running”
przez 30 minut (oczekiwany wynik: 300).
3. Napisz test sprawdzający, czy metoda zwraca poprawne kalorie dla aktywności “Swim
ming” przez 45 minut (oczekiwany wynik: 450).
4. Uruchom testy- powinny zakończyć się niepowodzeniem (faza Red).

##### Etap 5: Implementacja metody calculate_calories()
1. Dodaj do klasy Sport metodę calculate_calories(), która oblicza kalorie jako 10
jednostek za minutę.
2. Uruchom testy- powinny zakończyć się powodzeniem (faza Green).

##### Etap 6: Testy dla właściwości i metody equipment
1. Dodaj do klasy testowej nową metodę testującą test_equipment_property.
2. Napisz test sprawdzający, czy właściwość equipment początkowo zwraca pustą listę.
3. Napisz test sprawdzający, czy próba bezpośredniego modyfikowania właściwości
equipment nie wpływa na wewnętrzną listę (sprawdź czy zwracana jest kopia).
4. Uruchom testy- powinny zakończyć się niepowodzeniem (faza Red).

##### Etap 7: Implementacja właściwości equipment
1. Dodaj do klasy Sport prywatny atrybut _equipment inicjalizowany jako pusta lista w
konstruktorze.
2. Zaimplementuj właściwość equipment używając dekoratora @property, która zwraca
kopię listy _equipment (aby uniemożliwić bezpośrednią modyfikację).
3. Uruchom testy- powinny zakończyć się powodzeniem (faza Green).

##### Etap 8: Testy dla metody add_equipment()
1. Dodaj do klasy testowej nową metodę testującą test_add_equipment.
2. Napisz test sprawdzający, czy po dodaniu sprzętu “Shoes” znajduje się on na liście
sprzętu sportowego.
3. Napisz test sprawdzający, czy po dodaniu kilku elementów sprzętu (“Shoes”, “Shorts”,
“Watch”) wszystkie znajdują się na liście.
4. Napisz test sprawdzający, czy próba dodania sprzętu o pustej nazwie (““) wywołuje
wyjątek ValueError z odpowiednim komunikatem.
5. Napisz test sprawdzający, czy próba dodania sprzętu, który nie jest łańcuchem znaków
(np. liczby), wywołuje wyjątek TypeError.
6. Uruchom testy- powinny zakończyć się niepowodzeniem (faza Red).

##### Etap 9: Implementacja metody add_equipment()
1. Zaimplementuj metodę add_equipment(equipment), która:
    - Sprawdza czy przekazany parametr jest łańcuchem znaków, jeśli nie- rzuca wyjątek
    TypeError z komunikatem “Equipment name must be a string”
    - Sprawdza czy przekazany parametr nie jest pusty, jeśli jest- rzuca wyjątek
    ValueError z komunikatem “Equipment name cannot be empty”
    - Dodaje sprzęt do listy _equipment
2. Uruchom testy- powinny zakończyć się powodzeniem (faza Green).

##### Etap 10: Refaktoryzacja
1. Przejrzyj kod klasy Sport i testy, zastanów się nad możliwymi usprawnieniami.
2. Przeprowadź refaktoryzację kodu, np. wprowadzając dodatkowe właściwości lub metody
pomocnicze.
3. Upewnij się, że wszystkie testy nadal przechodzą po refaktoryzacji.

##### Etap 11: Dodatkowa właściwość calories_per_minute
1. Dodaj do klasy testowej nową metodę testującą test_calories_per_minute_property.
2. Napisz test sprawdzający, czy domyślna wartość calories_per_minute wynosi 10.
3. Napisz test sprawdzający, czy można ustawić nową wartość calories_per_minute na 15.
4. Napisz test sprawdzający, czy próba ustawienia wartości 0 lub wartości ujemnej jako
calories_per_minute wywołuje wyjątek ValueError.
5. Napisz test sprawdzający, czy próba ustawienia łańcucha znaków jako calories_per_minute
wywołuje wyjątek TypeError.
6. Uruchom testy- powinny zakończyć się niepowodzeniem (faza Red).

##### Etap 12: Implementacja właściwości calories_per_minute
1. Dodaj do klasy Sport prywatny atrybut __calories_per_minute inicjalizowany jako 10 w konstruktorze.
2. Zaimplementuj właściwość calories_per_minute używając dekoratora @property dla
gettera i @calories_per_minute.setter dla settera.
3. W setterze dla calories_per_minute dodaj walidację:
    - Sprawdzenie, czy wartość jest liczbą- jeśli nie, rzuć TypeError z komunikatem
    “Calories per minute must be a number”
    - Sprawdzenie, czy wartość jest większa od zera- jeśli nie, rzuć ValueError z komunikatem “Calories per minute must be greater than 0”
4. Zaktualizuj metodę calculate_calories(), aby używała właściwości calories_per_minute zamiast stałej wartości 10.
5. Uruchom testy- powinny zakończyć się powodzeniem (faza Green).

##### Etap 13: Dodatkowe testy
1. Dodaj test sprawdzający, czy zmiana calories_per_minute wpływa na wynik metody
calculate_calories().
2. Dodaj test sprawdzający, czy po dodaniu tego samego sprzętu kilka razy, pojawia się on
odpowiednią ilość razy na liście.
3. Uruchom testy i dostosuj implementację, jeśli to konieczne.

##### Etap 14: Uruchomienie wszystkich testów
1. Uruchom wszystkie testy za pomocą komendy w terminalu.
2. Upewnij się, że wszystkie testy kończą się powodzeniem.

#### Wartości testowe
- Testy pozytywne:
    - Name: “Running”, Duration: 30, Calories per minute: 10, Oczekiwane kalorie: 300
    - Name: “Swimming”, Duration: 45, Calories per minute: 15, Oczekiwane kalorie: 675
    - Dodanie sprzętu “Shoes” do aktywności sportowej
    - Dodanie sprzętu [“Shoes”, “Shorts”, “Watch”] do aktywności sportowej
- Testy negatywne (powinny wywołać wyjątki):
    - Name: ““, Duration: 30- oczekiwany ValueError
    - Name: “Running”, Duration: 0- oczekiwany ValueError
    - Name: “Running”, Duration:-5- oczekiwany ValueError
    - Name: 123, Duration: 30- oczekiwany TypeError
    - Name: “Running”, Duration: “half hour”- oczekiwany TypeError
    - Name: “Running”, Duration: 30, Calories per minute: 0- oczekiwany ValueError
    - Name: “Running”, Duration: 30, Calories per minute:-5- oczekiwany ValueError
    - Name: “Running”, Duration: 30, Calories per minute: “high”- oczekiwany TypeError
- Testy wyjątków:
    - Dodanie sprzętu o pustej nazwie (““) powinno wywołać ValueError z komunikatem ”Equipment name cannot be empty”
    - Dodanie sprzętu niebędącego łańcuchem znaków (np. liczby 123) powinno wywołać TypeError z komunikatem “Equipment name must be a string”