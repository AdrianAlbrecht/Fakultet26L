# Lab 06 - pokrycie kodu (moduł coverage) 

## 1. Czym jest pokrycie kodu?

**Pokrycie kodu (code coverage)** to miara określająca **jaka część kodu programu została wykonana podczas uruchamiania testów**.

Innymi słowy:

> Pokrycie kodu pokazuje, które fragmenty programu zostały sprawdzone przez testy, a które nigdy nie zostały uruchomione.

---

### Przykład

Mamy funkcję:

```python
def check_number(x):
    if x > 0:
        return "positive"
    else:
        return "negative"
```

Jeśli testujemy tylko:

```python
check_number(5)
```

to:

* gałąź `x > 0` została wykonana
* gałąź `else` **nie została przetestowana**

Pokrycie kodu wynosi więc **50% tej funkcji**.

---

## 2. Dlaczego pokrycie kodu jest ważne?

Pokrycie kodu pozwala:

* sprawdzić **czy testy obejmują cały program**
* wykryć **fragmenty kodu bez testów**
* poprawić **jakość testów**
* zmniejszyć ryzyko błędów w produkcji

---

### Problem bez pokrycia kodu

Możemy mieć wiele testów, ale:

* testują tylko część programu
* pomijają ważne scenariusze

Pokrycie kodu pomaga to wykryć.

---

## 3. Rodzaje pokrycia kodu

Istnieje kilka typów pokrycia.

---

### 1. Line Coverage (pokrycie linii)

Sprawdza **ile linii kodu zostało wykonanych**.

Przykład:

```python
if x > 0:
    return 1
else:
    return -1
```

Jeśli test wykona tylko pierwszą gałąź:

```
line coverage = 50%
```

---

### 2. Branch Coverage (pokrycie gałęzi)

Sprawdza **czy wszystkie możliwe ścieżki programu zostały wykonane**.

Np.

```python
if x > 0:
    ...
else:
    ...
```

Dla pełnego pokrycia trzeba przetestować:

```
x > 0
x <= 0
```

---

### 3. Function Coverage

Sprawdza czy **każda funkcja została wywołana**.

---

### 4. Condition Coverage

Sprawdza czy **wszystkie warunki logiczne zostały sprawdzone**.

Np.

```python
if a > 0 and b > 0:
```

musimy przetestować różne kombinacje:

```
a > 0, b > 0
a > 0, b <= 0
a <= 0, b > 0
```

---

## 4. Moduł `coverage` w Pythonie

W Pythonie najpopularniejszym narzędziem do mierzenia pokrycia kodu jest **coverage.py**.

Pozwala:

* mierzyć pokrycie testów
* generować raporty
* wskazywać nieprzetestowane linie kodu

---

### Instalacja

```bash
pip install coverage
```

---

## 5. Przykład projektu

Struktura projektu:

```
project/
│
├── calculator.py
└── test_calculator.py
```

---

### Plik programu

`calculator.py`

```python
def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b
```

---

### Testy jednostkowe

`test_calculator.py`

```python
import unittest
from calculator import add, divide


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)


if __name__ == "__main__":
    unittest.main()
```

---

## 6. Uruchamianie pokrycia kodu

Zamiast uruchamiać testy normalnie:

```bash
python test_calculator.py
```

uruchamiamy je przez `coverage`.

---

### Krok 1 – uruchomienie testów

```bash
coverage run -m unittest test_calculator.py
```

---

### Krok 2 – raport

```bash
coverage report
```

Przykładowy wynik:

```
Name              Stmts   Miss  Cover
-------------------------------------
calculator.py         6      1   83%
test_calculator.py    8      0  100%
-------------------------------------
TOTAL                14      1   93%
```

---

### Interpretacja

```
Stmts – liczba linii kodu
Miss – ile linii nie zostało wykonanych
Cover – procent pokrycia
```

---

## 7. Raport HTML

Najbardziej czytelny raport można wygenerować w HTML.

```bash
coverage html
```

Powstanie folder:

```
htmlcov/
```

Otwieramy plik:

```
htmlcov/index.html
```

---

Raport pokazuje:

* linie wykonane (zielone)
* linie niewykonane (czerwone)

To bardzo pomaga znaleźć **brakujące testy**.

---

## 8. Poprawa pokrycia kodu

W poprzednim przykładzie nie przetestowaliśmy:

```
raise ValueError("Division by zero")
```

Dodajemy test.

---

### Nowy test

```python
def test_divide_by_zero(self):
    with self.assertRaises(ValueError):
        divide(5, 0)
```

---

Po ponownym uruchomieniu:

```
coverage run -m unittest
coverage report
```

możemy dostać:

```
calculator.py 100%
```

---

## 9. Automatyzacja pokrycia kodu

W projektach często stosuje się:

```
black
flake8
pylint
tests
coverage
```

Przykład:

```bash
coverage run -m unittest
coverage report
coverage html
```

---

## 10. Minimalny próg pokrycia

W wielu projektach ustala się **minimalne pokrycie testami**, np.

```
80%
90%
95%
```

Jeśli pokrycie jest niższe:

```
build fails
```

---

Można to wymusić:

```bash
coverage report --fail-under=80
```

Jeśli pokrycie < 80%:

```
command exits with error
```

---

## 11. Typowy workflow testowania w Pythonie

W profesjonalnym projekcie proces wygląda często tak:

```
1. formatowanie kodu → black
2. analiza statyczna → flake8
3. analiza jakości → pylint
4. martwy kod → vulture
5. testy jednostkowe → unittest / pytest
6. pokrycie kodu → coverage
```

---

## 12. Ograniczenia pokrycia kodu

Wysokie pokrycie **nie oznacza idealnych testów**.

Przykład:

```python
def add(a, b):
    return a + b
```

Test:

```python
add(2, 3)
```

pokrycie:

```
100%
```

ale test:

* nie sprawdza błędów
* nie sprawdza wartości ujemnych
* nie sprawdza typów

Dlatego pokrycie kodu **nie zastępuje dobrych testów**.

---

## 13. Podsumowanie

**Pokrycie kodu (code coverage)** to miara określająca jaka część programu została wykonana podczas testów.

W Pythonie najczęściej używa się narzędzia **coverage.py**, które:

* mierzy wykonanie kodu
* generuje raporty
* wskazuje nieprzetestowane fragmenty

Pokrycie kodu pomaga:

* zwiększyć jakość testów
* wykryć brakujące scenariusze
* poprawić niezawodność oprogramowania.

---

## 14. Przydatne komendy

1. Instalacja:

    ```bash
    pip install coverage
    ```

2. Aby uruchomić testy z pomiarem pokrycia, używamy narzędzia coverage:

    ```bash
    coverage run-m unittest test_calculator.py
    ```
    lub

    ```bash
    coverage run-m unittest discover-s tests
    ```

    lub (łącznie z gałęziami)

    ```bash
    coverage run-m--branch unittest discover-s tests
    ```

3. Sprawdźmy raport pokrycia:

    ```bash
    coverage report-m
    ```

    Możemy również wygenerować HTML-owy raport, który będzie bardziej czytelny:

    ```bash
    coverage html
    ```
    
4. `coverage` oferuje wiele przydatnych opcji:
    - `coverage run --branch` - mierzy pokrycie gałęzi (sprawdza, czy wykonane zostały
    różne ścieżki w instrukcjach warunkowych)
    - `coverage run --source=modul1,modul2`- mierzy pokrycie tylko wybranych modułów
    - `coverage run --omit="*/tests/*,*/venv/*"`- pomija określone pliki/katalogi

## 15. Przykładowy Github Action

```yaml
name: Python tests

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest
    defaults:
      run:
        working-directory: ./lab06
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'
      - name: Install dependencies
        run: |
          pip install coverage
      - name: Run tests with coverage
        run: |
          coverage run -m --branch unittest discover -s tests
          coverage report -m
          coverage html
      - name: Upload coverage report as artifact
        uses: actions/upload-artifact@v4
        with:
          name: coverage-report
          path: lab06/htmlcov
```

## Zadania

1. Przeanalizuj zawartość folderów dodanych do folderu tego laba sprawdzając pokrycie kodu za pomocą modułu coverage:
    - analiza zadania z kalkulatorem
    - moduł utils.py i testy do niego
    - moduł book_manager.py i testy do niego
    - O ile to możliwe, zapewnij 100% pokrycia.
2. (Opcjonalnie) Skonfiguruj Github Action w celu wygenerowania i pobrania raportu przykładowa zawartość znajduje się w pliku `.github\workflows\main.yml`
