# Lab 07 - techniki testowania

## 1. Czym są techniki testowania?

**Techniki testowania** to metody służące do **projektowania przypadków testowych**, czyli określania:

* jakie dane wejściowe należy użyć,
* jakie scenariusze sprawdzić,
* jakie wyniki są oczekiwane.

Innymi słowy:

> Techniki testowania pomagają zdecydować **co dokładnie należy przetestować**.

Bez technik testowania testy często są:

* przypadkowe
* niekompletne
* niesystematyczne

---

## 2. Podział technik testowania

Techniki testowania dzieli się najczęściej na trzy grupy:

| grupa                            | opis                                   |
| -------------------------------- | -------------------------------------- |
| techniki czarnoskrzynkowe        | testowanie bez znajomości kodu         |
| techniki białoskrzynkowe         | testowanie na podstawie struktury kodu |
| techniki oparte na doświadczeniu | testy bazujące na wiedzy testera       |

---

## 3. Techniki czarnoskrzynkowe (Black-Box Testing)

### Czym jest testowanie czarnoskrzynkowe?

Testowanie **czarnoskrzynkowe** polega na sprawdzaniu programu **bez znajomości jego wewnętrznej implementacji**.

Tester zna tylko:

* dane wejściowe
* oczekiwane wyniki

Nie analizuje:

* kodu źródłowego
* algorytmów

Program traktowany jest jak **„czarna skrzynka”**.

---

#### Przykład funkcji

```python
def discount(price):
    if price > 100:
        return price * 0.9
    return price
```

Tester nie patrzy na kod, tylko na zachowanie funkcji.

---

## 3.1. Podział na klasy równoważności

### Czym jest partycjonowanie klas równoważności?

Technika polega na podzieleniu danych wejściowych na **grupy (klasy)**, które powinny zachowywać się podobnie.

Zamiast testować **każdą wartość**, testujemy **reprezentantów klas**.

---

#### Przykład

Program przyjmuje wiek:

```
0 – 17  → dziecko
18 – 64 → dorosły
65+     → senior
```

Klasy równoważności:

| klasa   | przykład |
| ------- | -------- |
| dziecko | 10       |
| dorosły | 30       |
| senior  | 70       |

---

#### Test w Python

```python
import unittest

def age_group(age):
    if age < 18:
        return "child"
    elif age < 65:
        return "adult"
    else:
        return "senior"


class TestAge(unittest.TestCase):

    def test_child(self):
        self.assertEqual(age_group(10), "child")

    def test_adult(self):
        self.assertEqual(age_group(30), "adult")

    def test_senior(self):
        self.assertEqual(age_group(70), "senior")
```

---

## 3.2. Analiza wartości brzegowych

### Czym jest analiza wartości brzegowych?

Błędy często pojawiają się **na granicach zakresów danych**.

Dlatego testuje się wartości:

```
tuż przed granicą
na granicy
tuż po granicy
```

---

### Przykład

Zakres:

```
18–65
```

Testujemy:

```
17
18
19
64
65
66
```

---

#### Python

```python
class TestAgeBoundaries(unittest.TestCase):

    def test_boundary(self):
        self.assertEqual(age_group(17), "child")
        self.assertEqual(age_group(18), "adult")
        self.assertEqual(age_group(65), "senior")
```

---

## 3.3. Tablice decyzyjne

### Czym są tablice decyzyjne?

Tablica decyzyjna opisuje **różne kombinacje warunków i odpowiadające im akcje**.

Stosuje się ją przy:

* złożonych warunkach
* wielu kombinacjach danych

---

### Przykład

Warunki:

```
czy klient premium
czy wartość zamówienia > 100
```

Tabela:

| premium | >100 | rabat |
| ------- | ---- | ----- |
| tak     | tak  | 20%   |
| tak     | nie  | 10%   |
| nie     | tak  | 5%    |
| nie     | nie  | 0     |

---

### Python

```python
def discount(premium, amount):
    if premium and amount > 100:
        return 0.2
    if premium:
        return 0.1
    if amount > 100:
        return 0.05
    return 0
```

Test:

```python
class TestDiscount(unittest.TestCase):

    def test_cases(self):
        self.assertEqual(discount(True, 200), 0.2)
        self.assertEqual(discount(True, 50), 0.1)
        self.assertEqual(discount(False, 200), 0.05)
        self.assertEqual(discount(False, 50), 0)
```

---

## 4. Techniki białoskrzynkowe (White-Box Testing)

### Czym jest testowanie białoskrzynkowe?

Testowanie **białoskrzynkowe** polega na analizie **wewnętrznej struktury programu**.

Tester zna:

* kod źródłowy
* strukturę programu
* ścieżki wykonania

---

#### Cel

Sprawdzenie:

* wszystkich gałęzi kodu
* wszystkich warunków
* wszystkich ścieżek programu

---

## 4.1. Pokrycie instrukcji (Statement Coverage)

Technika polega na sprawdzeniu czy **każda linia kodu została wykonana**.

Przykład:

```python
def check(x):
    if x > 0:
        return "positive"
    return "negative"
```

Test:

```python
check(5)
```

pokrycie:

```
50%
```

Bo gałąź `negative` nie została wykonana.

---

## 4.2. Pokrycie gałęzi (Branch Coverage)

Sprawdza czy **wszystkie możliwe gałęzie programu zostały wykonane**.

Przykład:

```python
if x > 0:
    ...
else:
    ...
```

Testy:

```
x = 5
x = -1
```

---

## 4.2. Analiza ścieżek

**Analiza ścieżek (path testing)** to technika testowania białoskrzynkowego polegająca na projektowaniu testów tak, aby **przejść przez wszystkie możliwe ścieżki wykonania programu**.

Ścieżka programu to:

> sekwencja instrukcji wykonywanych od początku do końca funkcji lub fragmentu kodu.

Tester analizuje **strukturę kodu**, aby określić wszystkie możliwe drogi przejścia przez program.

---

### 4.2.1. Czym jest ścieżka wykonania programu?

Ścieżka to **konkretna kombinacja warunków logicznych**, która prowadzi do wykonania określonych instrukcji.

#### Przykład kodu

```python
def check(x):
    if x > 0:
        return "positive"
    else:
        return "negative"
```

Możliwe ścieżki:

| ścieżka | warunek |
| ------- | ------- |
| 1       | x > 0   |
| 2       | x ≤ 0   |

Aby pokryć wszystkie ścieżki, potrzebujemy dwóch testów.

---

### 4.2.2. Bardziej złożony przykład

```python
def classify_number(x):
    if x > 0:
        if x % 2 == 0:
            return "positive even"
        else:
            return "positive odd"
    else:
        return "non-positive"
```

Możliwe ścieżki:

| ścieżka | warunki              |
| ------- | -------------------- |
| 1       | x > 0 AND x % 2 == 0 |
| 2       | x > 0 AND x % 2 != 0 |
| 3       | x ≤ 0                |

---

### 4.2.3. Projektowanie testów dla ścieżek

Testy w Pythonie:

```python
import unittest

class TestClassify(unittest.TestCase):

    def test_positive_even(self):
        self.assertEqual(classify_number(4), "positive even")

    def test_positive_odd(self):
        self.assertEqual(classify_number(3), "positive odd")

    def test_non_positive(self):
        self.assertEqual(classify_number(-1), "non-positive")
```

Każdy test pokrywa **inną ścieżkę programu**.

---

### 4.2.4. Graf przepływu sterowania (Control Flow Graph)

W analizie ścieżek często tworzy się **graf przepływu sterowania (CFG)**.

W grafie:

* wierzchołki = instrukcje programu
* krawędzie = możliwe przejścia

Przykład:

```
start
  |
if x > 0
 /     \
T       F
|       |
if even |
 /   \  |
T     F |
|     | |
end   end
```

Na podstawie grafu można określić **liczbę ścieżek do przetestowania**.

---

### 4.2.5. Złożoność cyklomatyczna (Cyclomatic Complexity)

Analiza ścieżek często wykorzystuje pojęcie **złożoności cyklomatycznej**.

Została wprowadzona przez **Thomas J. McCabe**.

Złożoność cyklomatyczna określa:

> minimalną liczbę testów potrzebnych do pokrycia wszystkich niezależnych ścieżek programu.

---

#### Wzór

[
V(G) = E - N + 2
]

gdzie:

* **E** – liczba krawędzi grafu
* **N** – liczba wierzchołków grafu

W praktyce często stosuje się prostszą zasadę:

```
złożoność = liczba warunków + 1
```

---

#### Przykład

```python
if a > 0:
    ...
if b > 0:
    ...
```

Mamy dwa warunki.

Złożoność:

```
2 + 1 = 3
```

Potrzeba **minimum 3 testów**, aby pokryć wszystkie niezależne ścieżki.

---

### 4.2.6. Problem eksplozji ścieżek

W dużych programach liczba ścieżek rośnie **bardzo szybko**.

Przykład:

```
3 warunki → 8 ścieżek
5 warunków → 32 ścieżki
10 warunków → 1024 ścieżki
```

Dlatego w praktyce:

* testuje się **najważniejsze ścieżki**
* stosuje się **pokrycie gałęzi zamiast pełnego path coverage**

---

### 4.2.7. Analiza ścieżek w praktyce

Analiza ścieżek jest szczególnie przydatna dla:

* algorytmów
* funkcji z wieloma warunkami
* kodu krytycznego
* walidacji danych

---

#### Przykład funkcji z wieloma warunkami

```python
def login(user, password):
    if user == "admin":
        if password == "123":
            return "login success"
        else:
            return "wrong password"
    return "unknown user"
```

Możliwe ścieżki:

| ścieżka | scenariusz               |
| ------- | ------------------------ |
| 1       | admin + correct password |
| 2       | admin + wrong password   |
| 3       | unknown user             |

---

#### Testy

```python
class TestLogin(unittest.TestCase):

    def test_success(self):
        self.assertEqual(login("admin", "123"), "login success")

    def test_wrong_password(self):
        self.assertEqual(login("admin", "abc"), "wrong password")

    def test_unknown_user(self):
        self.assertEqual(login("user", "123"), "unknown user")
```

---

### 4.2.8. Analiza ścieżek a pokrycie kodu

Analiza ścieżek jest powiązana z metrykami pokrycia kodu:

| technika           | co sprawdza       |
| ------------------ | ----------------- |
| statement coverage | wszystkie linie   |
| branch coverage    | wszystkie gałęzie |
| path coverage      | wszystkie ścieżki |

Relacja:

```
path coverage > branch coverage > statement coverage
```
czyli:

* pokrycie ścieżek jest **najbardziej wymagające**.

## 5. Techniki oparte na doświadczeniu

## Czym są techniki oparte na doświadczeniu?

Są to techniki wykorzystujące:

* intuicję testera
* wiedzę o błędach
* doświadczenie z podobnych systemów

---

## 5.1. Testowanie eksploracyjne

Tester:

* poznaje system
* jednocześnie projektuje testy
* analizuje zachowanie programu

---

## 5.2. Zgadywanie błędów (Error Guessing)

Tester przewiduje gdzie mogą wystąpić błędy.

Przykłady:

* dzielenie przez zero
* puste dane
* bardzo duże liczby
* niepoprawne typy

---

#### Python

```python
class TestDivide(unittest.TestCase):

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            5 / 0
```

---

## 6. Zastosowanie technik w praktyce

Dobrze zaprojektowane testy zwykle łączą kilka technik.

Przykład:

Test funkcji:

```python
def sqrt(x):
    if x < 0:
        raise ValueError
    return x ** 0.5
```

Można zastosować:

| technika            | przykład            |
| ------------------- | ------------------- |
| klasy równoważności | x < 0, x = 0, x > 0 |
| wartości brzegowe   | -1, 0, 1            |
| error guessing      | bardzo duże liczby  |

---

#### Test

```python
class TestSqrt(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(sqrt(0), 0)

    def test_positive(self):
        self.assertEqual(sqrt(4), 2)

    def test_negative(self):
        with self.assertRaises(ValueError):
            sqrt(-1)
```

---

## 7. Podsumowanie

Techniki testowania pozwalają **systematycznie projektować przypadki testowe**.

Najważniejsze z nich to:

### Techniki czarnoskrzynkowe

* klasy równoważności
* wartości brzegowe
* tablice decyzyjne

### Techniki białoskrzynkowe

* pokrycie instrukcji
* pokrycie gałęzi
* analiza ścieżek

### Techniki oparte na doświadczeniu

* testowanie eksploracyjne
* zgadywanie błędów

Ich stosowanie prowadzi do:

* lepszych testów
* większego pokrycia kodu
* wyższej jakości oprogramowania.

## Zadanie

Bazując na przykładzie w pliku `przyklad.pdf` załączonego do plików zajęć wykonaj:
- Projekt pól (i ew. właściwości) w klasie
- Projekt metod w klasie
- Projekt różnych technik testowania dla podanej klasy (do wyboru przez studenta, proponowane: testowanie klas równoważności, analiza watości brzegowych, tablica decyzyjna)

Zaprojektuj klasę `CashRegister` (pol. kasa fiskalna), która ma symulować działanie kasy fiskalnej w sklepie. Kasa będzie posiadać mechanizmy sprzedaży, zwrotów, generowania raportów oraz zmiany statusu kasy w zależności od różnych warunków.

**Wymagania funkcjonalne**:
1. Kasa ma posiadać stan gotówki, który nie może być ujemny
2. Kasa ma mieć możliwość rejestrowania sprzedaży i zwrotów towarów
3. Kasa może mieć jeden z czterech statusów: ACTIVE, MAINTENANCE, LOCKED, CLOSED (pol.
AKTYWNA, KONSERWACJA, ZABLOKOWANA, ZAMKNIĘTA)
4. Kasa generuje różne rodzaje raportów w zależności od typu operacji:
    - raport dzienny: zestawienie wszystkich transakcji z danego dnia
    - raport okresowy: zestawienie z wybranego okresu (od-do)
    - raport podatkowy: wyliczenie należnego podatku VAT według stawek
5. Możliwa jest zmiana statusu kasy według określonych reguł
6. Jeśli przez 24 godziny nie będzie żadnych operacji, kasa przechodzi w stan KONSERWACJA
7. Kasa może zostać ZABLOKOWANA w przypadku trzech nieudanych prób otwarcia szuflady
8. Kasa może zostać ZAMKNIĘTA tylko przez uprawnionego serwisanta i po wygenerowaniu raportu
zamknięcia dnia
9. Rejestrowanie sprzedaży i zwrotów jest możliwe tylko dla kas o statusie AKTYWNA


**Wymagania niefunkcjonalne**:
1. Pokrycie kodu z gałęziami: 90%
2. Zgodność ze stylem PEP8