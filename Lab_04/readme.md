# Lab 04 - analiza statyczna, wyrażenia regularne
### (flake8, pylint, black, vulture)

## 1. Czym jest analiza statyczna kodu?

**Analiza statyczna (static code analysis)** to technika sprawdzania jakości kodu **bez jego uruchamiania**.

Program analizujący kod sprawdza m.in.:

* błędy składniowe
* nieużywany kod
* problemy stylistyczne
* potencjalne błędy logiczne
* niezgodność ze standardami kodowania
* problemy z bezpieczeństwem

Analiza odbywa się **bez wykonywania programu**, dlatego nazywa się ją **statyczną**.

---

### Analiza statyczna vs dynamiczna

| Rodzaj             | Na czym polega                           |
| ------------------ | ---------------------------------------- |
| analiza statyczna  | analiza kodu źródłowego bez uruchamiania |
| analiza dynamiczna | analiza podczas działania programu       |

Przykłady bibliotek:

**Analiza statyczna**

```
flake8
pylint
vulture
black
```

**Analiza dynamiczna**

```
unittest
pytest
coverage
```

---

## 2. Dlaczego analiza statyczna jest ważna w testowaniu?

W procesie testowania analiza statyczna pozwala wykryć błędy **zanim powstaną testy lub zanim kod zostanie uruchomiony**.

Korzyści:

* wykrywanie błędów bardzo wcześnie
* spójny styl kodu
* łatwiejsze utrzymanie projektu
* mniej błędów logicznych
* lepsza czytelność kodu

Dlatego analiza statyczna jest często elementem:

* **CI/CD**
* **Code Review**
* **Quality Gates**

---

## 3. Wyrażenia regularne (Regular Expressions)

### Czym są wyrażenia regularne?

**Wyrażenia regularne (regex)** to specjalny język służący do **wyszukiwania i dopasowywania wzorców w tekście**.

W Pythonie są obsługiwane przez moduł:

```python
import re
```

---

### Przykład zastosowania regex

Załóżmy, że chcemy sprawdzić czy tekst zawiera email.

```python
import re

pattern = r"\w+@\w+\.\w+"

text = "kontakt@test.pl"

if re.match(pattern, text):
    print("Poprawny email")
```

---

### Najważniejsze elementy regex

| symbol | znaczenie        |
| ------ | ---------------- |
| `.`    | dowolny znak     |
| `\d`   | cyfra            |
| `\w`   | litera lub cyfra |
| `+`    | jeden lub więcej |
| `*`    | zero lub więcej  |
| `?`    | opcjonalny       |
| `^`    | początek tekstu  |
| `$`    | koniec tekstu    |

---

### Przykład dopasowania numeru telefonu

```python
pattern = r"\d{3}-\d{3}-\d{3}"
```

dopasuje

```
123-456-789
```

---

### Regex w testach jednostkowych

Regex często używa się w testach np. do walidacji danych.

```python
import unittest
import re

def is_email(text):
    return bool(re.match(r"\w+@\w+\.\w+", text))


class TestEmail(unittest.TestCase):

    def test_email(self):
        self.assertTrue(is_email("test@test.com"))

    def test_invalid_email(self):
        self.assertFalse(is_email("test.com"))
```

---

## 4. flake8

### Czym jest flake8?

Flake8 to popularne narzędzie do analizy statycznej kodu Python, które łączy w sobie kilka narzędzi: PyFlakes (wykrywanie błędów logicznych), pycodestyle (sprawdzanie zgodności z PEP 8) oraz McCabe (mierzenie złożoności cyklomatycznej).

[Dokumentacja](https://flake8.pycqa.org/en/latest/)

**Flake8** sprawdza:

* błędy składniowe
* styl kodu (PEP8)
* nieużywane zmienne
* nieczytelny kod

flake8 łączy trzy narzędzia:

```
PyFlakes – błędy w kodzie
pycodestyle – styl PEP8
mccabe – złożoność kodu
```

---

### Instalacja

```bash
pip install flake8
```

---

### Uruchomienie

Sprawdzenie pliku:

```bash
flake8 program.py
```

Sprawdzenie całego projektu:

```bash
flake8 moj_projekt/
```

Z określonymi regułami:

```bash
flake8 --select E111,E121--max-line-length=120 plik.py
```

Reguły (typowe błędy wykrywane przez flake8):
- E101: Wcięcia zawierają mieszankę spacji i tabulatorów
- E111: Wcięcia nie są wielokrotnością 4 spacji
- E501: Linia za długa (przekracza domyślne 79 znaków)
- F401: Zaimportowany moduł, ale nieużywany
- F841: Zmienna zdefiniowana, ale nieużywana

Wiecej kodów błędów:
- https://flake8.pycqa.org/en/latest/user/error-codes.html
- https://pycodestyle.pycqa.org/en/latest/intro.html#error-codes

---

### Przykład błędu

Kod:

```python
def add(a,b):
    return a+b
```

flake8 zgłosi:

```
E231 missing whitespace after ','
```

Poprawna wersja:

```python
def add(a, b):
    return a + b
```

---

### Integracja z testami

flake8 często uruchamia się **przed testami**.

Przykład w pipeline:

```
flake8
pytest
coverage
```

---

### Konfiguracja
Można skonfigurować flake8 tworząc plik setup.cfg lub .flake8 w głównym katalogu projektu:

```yml
[flake8]
max-line-length = 100
exclude = .git,__pycache__,build,dist, .venv
ignore = E203,W503
```

## 5. pylint

### Czym jest pylint?

**pylint** to bardziej zaawansowane narzędzie analizy statycznej niż flake8. Pomaga wykrywać błędy, egzekwować standardy kodowania i szukać potencjalnych problemów. Ocenia kod w skali od 0 do 10, gdzie 10 oznacza kod idealny.

[Dokumentacja](https://docs.pylint.org/)

Sprawdza:

* styl kodu
* błędy logiczne
* problemy projektowe
* brak dokumentacji
* nazewnictwo

---

### Instalacja

```bash
pip install pylint
```

---

### Uruchomienie

```bash
pylint program.py
```

### Generowanie raportu

```bash
pylint --reports=y plik.py
```

### Filtrowanie według kategorii

```bash
pylint --disable=C,R plik.py
```

### Typowe komunikaty pylint
- C: Konwencje (style kodowania)
- R: Refaktoring (sugestie ulepszeń)
- W:Ostrzeżenia (potencjalne problemy)
- E: Błędy (definite problems)
- F: Błędy krytyczne (uniemożliwiające dalszą analizę)

### Przykłady:
- C0111: Brak docstringa
- W0611: Nieużywany import
- E1101: Odwołanie do nieistniejącego atrybutu
- R0903: Zbyt mało metod publicznych

[Lista błędów](https://pylint.readthedocs.io/en/stable/user_guide/messages/messages_overview.html)

---

### Przykład ostrzeżenia

Kod:

```python
x = 10
```

pylint:

```
C0103: Variable name "x" doesn't conform to snake_case
```

---

### Punktacja

pylint przyznaje ocenę:

```
Your code has been rated at 8.50/10
```

Często w projektach wymaga się np.:

```
minimum 8/10
```

---

### Konfiguracja

Możesz skonfigurować pylint tworząc plik .pylintrc w katalogu projektu:

```yaml
[MESSAGES CONTROL]
disable=C0111,W0611
[FORMAT]
max-line-length=100
```

Ewentualnie w pliku setup.cfg

```yaml
[pylint]
max-line-length = 100
disable = C0111,W0611,R0903
ignore = migrations, .venv
[pylint.FORMAT]
max-line-length = 100
[pylint.MESSAGES CONTROL]
disable = C0111,W0611
[pylint.SIMILARITIES]
min-similarity-lines = 7
ignore-comments = yes
ignore-docstrings = yes
```

## 6. black

### Czym jest black?

**Black** to automatyczny **formatter kodu Python**. Jego głównym zadaniem jest formatowanie kodu Python według określonych zasad, co eliminuje dyskusje na temat stylu w
zespołach programistycznych. Black jest nazywany “bezkompromisowym formatem kodu” ponieważ oferuje bardzo niewiele opcji konfiguracyjnych, wymuszając spójny styl.

Jego celem jest:

> automatyczne formatowanie kodu w jednolity sposób.

Programista **nie decyduje o stylu**, black robi to automatycznie.

---

### Instalacja

```bash
pip install black
```

---

### Formatowanie pliku

```bash
black program.py
```

Formatowanie projektu:

```bash
black katalog/
```

Sprawdzenie, które pliki zostałyby zmodyfikowane bez faktycznego ich formatowania:

```bash
black --check nazwa_pliku.py
black --diff nazwa_pliku.py
```

---

### Przykład

Kod przed:

```python
def add( a,b ):return a+b
```

Po użyciu black:

```python
def add(a, b):
    return a + b
```

---

### Dlaczego black jest ważny?

Zalety:

* brak sporów o styl kodu
* spójny kod w zespole
* szybsze code review

---

### Konfiguracja

Mimo, że Black ma niewiele opcji konfiguracyjnych, możesz ustawić podstawowe parametry w pliku pyproject.toml:

```yaml
[tool.black]
line-length=88
target-version=['py312']
include='\.pyi?$'
exclude='''
/(
      \.eggs
    | \.git
    | \.hg
    | \.mypy_cache
    | \.tox
    | \.venv
    | _build
    | buck-out
    | build
    | dist
)/
'''
```
Można dodać ustawienia w setup.cfg jednak twórcy modułu tego nie zalecają:
```yaml
[tool:black]
line-length= 100
target-version= py312
include= \.pyi?$
exclude= /(\.eggs|\.git|\.hg|\.mypy_cache|\.tox|\.venv|_build|buck-out|build|dist)/
```

## 7. vulture

### Czym jest vulture?

**vulture** wykrywa **martwy kod (dead code)** w Pythonie.  Analizuje statycznie pliki źródłowe, identyfikując nieużywane klasy, funkcje, zmienne i importy, które mogą
zostać bezpiecznie usunięte, poprawiając czytelność i utrzymanie kodu.

Czyli:

* nieużywane funkcje
* nieużywane zmienne
* nieużywane klasy

---

### Instalacja

```bash
pip install vulture
```

---

### Uruchomienie

Aby przeanalizować pojedynczy plik:

```bash
vulture sciezka/do/pliku.py
```

Aby przeanalizować cały katalog rekurencyjnie:

```bash
vulture sciezka/do/katalogu/
```

---

### Przykład

Kod:

```python
def used_function():
    return 1

def unused_function():
    return 2
```

vulture zgłosi:

```
unused_function is unused
```

Rozważmy plik przyklad.py z następującą zawartością:

```python
import os
import sys
import json # nieużywany import


def funkcja_uzywana():
    return "Ta funkcja jest używana"

def funkcja_nieuzywana():
    return "Ta funkcja nie jest nigdzie wywoływana"


STALA_NIEUZYWANA = 100


class KlasaUzywana:
    def __init__(self):
        self.atrybut = "używany"

class KlasaNieuzywana:
    def __init__(self):
        self.atrybut = "nieużywany"


wynik = funkcja_uzywana()
instancja = KlasaUzywana()
```

Po uruchomieniu:

```bash
vulture przyklad.py
```

Otrzymamy wynik podobny do:

```text
przyklad.py:3: unused import 'json' (90% confidence)
przyklad.py:6: unused function 'funkcja_nieuzywana' (60% confidence)
przyklad.py:9: unused variable 'STALA_NIEUZYWANA' (60% confidence)
przyklad.py:14: unused class 'KlasaNieuzywana' (60% confidence)
```
---

### Zaawansowane użycie

Vulture pozwala na dostosowanie minimalnego poziomu pewności:

```bash
vulture --min-confidence 80 sciezka/do/pliku.py
```

Wykluczenie określonych typów martwego kodu:

```bash
vulture --exclude-vars sciezka/do/pliku.py
```

Zapisanie wyników do pliku:

```bash
vulture sciezka/do/pliku.py > martwy_kod.txt
```

Pliki whitelisty

Można tworzyć pliki whitelisty, aby ignorować określone elementy. Na przykład whitelist.py:

```python
# funkcja_nieuzywana # vulture: ignore
```
I uruchomić:

```bash
vulture przyklad.py whitelist.py
```

Analiza wielu plików

```bash
vulture pierwszy.py drugi.py trzeci.py
```

Lub za pomocą wildcard:

```bash
vulture *.py
```

### Ustawienia w pliku pyproject.toml

```yaml
[tool.vulture]
min_confidence = 50
exclude = [".venv/"]
```

### Dlaczego martwy kod jest problemem?

Martwy kod:

* utrudnia czytanie projektu
* zwiększa rozmiar kodu
* może wprowadzać w błąd programistów

---

## 8. Typowy workflow jakości kodu

W profesjonalnym projekcie Python często stosuje się pipeline:

```
black → flake8 → pylint → vulture → tests
```

czyli:

1. **black** – formatowanie kodu
2. **flake8** – sprawdzanie stylu
3. **pylint** – analiza jakości
4. **vulture** – wykrywanie martwego kodu
5. **unittest / pytest** – testy

---

## 9. Przykładowy pipeline projektu Python

```
project/
│
├── src/
│   └── calculator.py
│
├── tests/
│   └── test_calculator.py
│
└── requirements.txt
```

Polecenia:

```
black .
flake8 .
pylint src
vulture src
pytest
```

---

## 10. Podsumowanie

**Analiza statyczna** pozwala wykrywać błędy w kodzie **bez jego uruchamiania**, co znacząco poprawia jakość oprogramowania.

Najważniejsze narzędzia w Pythonie:

| narzędzie | funkcja                        |
| --------- | ------------------------------ |
| flake8    | analiza stylu i błędów         |
| pylint    | zaawansowana analiza jakości   |
| black     | automatyczne formatowanie kodu |
| vulture   | wykrywanie martwego kodu       |

W połączeniu z **testami jednostkowymi (unittest / pytest)** stanowią podstawę nowoczesnego procesu **zapewniania jakości oprogramowania**.


# Zadania

## flake8, pylint, black, vuture

Na bazie kodów w folderze `codes` dokonaj analizy statycznej kodu za pomocą modułu flake8, pylint, black, vulture.
- (opcjonalnie) Skonfiguruj akcje w ramach Github Action. Przykładowe działania są w repozytorium w folderze `actions`.
- (opcjonalnie) Osoby używające konstrukcję type hinting mogą również moduł [mypy](https://mypy.readthedocs.io/en/stable)

Proponowane kody do analizy dla podanych narzędzi:
- flake8 -> Kody do analizy: biblioteka.py, person.py
- pylint -> Kody do analizy: produkt.py, vehicle.py 
- black -> Kody do analizy: inventory.py, animal.py 
- vulture -> Kody do analizy: wszystkie :)

## Wyrażenia regularne
Postępuj według poniższych etapów przez proces tworzenia klasy PeselValidator zgodnie z metodyką Test-Driven Development (TDD) przy użyciu biblioteki unittest w Pythonie. Klasa
będzie zawierać metody statyczne do walidacji numerów PESEL, wykorzystując wyrażenia regularne gdzie to możliwe.

### Etap 1: Przygotowanie projektu
1. Utwórz nowy katalog na projekt o nazwie pesel_validator.
2. Wewnątrztego katalogu utwórz dwa pliki: pesel_validator.py i test_pesel_validator.py.
3. Otwórz plik pesel_validator.py i zadeklaruj pustą klasę PeselValidator.
4. Otwórz plik test_pesel_validator.py i zaimportuj moduł unittest oraz klasę PeselValidator.

### Etap 2: Test podstawowej walidacji formatu PESEL
1. Wpliku test_pesel_validator.py utwórz klasę testową TestPeselValidator dziedzi
czącą po unittest.TestCase.
2. Napisz test test_pesel_format sprawdzający czy metoda validate_format istnieje i poprawnie weryfikuje, że PESEL składa się dokładnie z 11 cyfr.
3. Uruchom test, który powinien nie przejść (czerwony etap TDD).
4. Zaimplementuj metodę statyczną validate_format w klasie PeselValidator, która sprawdza format PESEL za pomocą wyrażenia regularnego.
5. Uruchom test ponownie, powinien teraz przejść (zielony etap TDD).

###  Etap 3: Test walidacji cyfr kontrolnych
1. Dodaj test test_check_digit sprawdzający poprawność cyfry kontrolnej PESEL.
2. Uruchom test, który powinien nie przejść.
3. Zaimplementuj metodę statyczną validate_check_digit w klasie PeselValidator, która weryfikuje poprawność cyfry kontrolnej.
4. Uruchom test ponownie, powinien teraz przejść.

### Etap 4: Test walidacji daty urodzenia
1. Dodaj test test_birth_date sprawdzający czy data urodzenia zakodowana w PESEL jest prawidłowa.
2. Uruchom test, który powinien nie przejść.
3. Zaimplementuj metodę statyczną validate_birth_date w klasie PeselValidator, która dekoduje i weryfikuje datę urodzenia.
4. Uruchom test ponownie, powinien teraz przejść.

### Etap 5: Test walidacji płci
1. Dodaj test test_gender sprawdzający czy metoda do określenia płci działa poprawnie.
2. Uruchom test, który powinien nie przejść.
3. Zaimplementuj metodę statyczną get_gender w klasie PeselValidator, która określa płeć na podstawie numeru PESEL.
4. Uruchom test ponownie, powinien teraz przejść.

### Etap 6: Test walidacji kompletnej
1. Dodaj test test_is_valid sprawdzający główną metodę is_valid, która powinna wykorzystywać wszystkie wcześniejsze metody walidacji.
2. Uruchom test, który powinien nie przejść.
3. Zaimplementuj metodę statyczną is_valid w klasie PeselValidator, która przeprowadza pełną walidację numeru PESEL.
4. Uruchom test ponownie, powinien teraz przejść.

### Etap 7: Refaktoryzacja
1. Przejrzyj kod pod kątem możliwych usprawnień, eliminacji powtórzeń i poprawy czytel
ności.
2. Wprowadź niezbędne zmiany refaktoryzacyjne, upewniając się, że wszystkie testy nadal przechodzą.

### Etap 8: Testy przypadków brzegowych
1. Dodaj testy dla szczególnych przypadków (np. numery PESEL z różnych stuleci, PESEL z datą 29 lutego w roku przestępnym itp.).
2. Uruchom testy i popraw implementację tam, gdzie to konieczne.

### Etap 9: Dokumentacja
1. Dodaj dokumentację (docstring) do każdej metody klasy PeselValidator.
2. Uruchom testy, aby upewnić się, że dodanie dokumentacji nie wpłynęło na funkcjonalność.

### Etap 10: Finalizacja
1. Uruchom pełny zestaw testów, aby upewnić się, że wszystko działa poprawnie.
2. Zaimplementuj prosty program demonstracyjny pokazujący użycie klasy PeselValidator.

