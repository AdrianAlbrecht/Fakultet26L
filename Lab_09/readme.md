# Lab 09 - moduł pytest-bdd; Gherkin; Docstring

## 1. Czym jest BDD (Behavior Driven Development)?

**BDD (Behavior Driven Development)** to podejście do tworzenia oprogramowania polegające na opisywaniu funkcjonalności systemu **z punktu widzenia zachowania aplikacji**.

Testy opisują **jak system powinien się zachowywać**, zamiast skupiać się wyłącznie na implementacji.

Kluczowa idea BDD:

> testy są jednocześnie dokumentacją działania systemu.

---

## 2. Charakterystyka BDD

BDD zakłada współpracę pomiędzy:

* programistami
* testerami
* analitykami biznesowymi
* klientami

Scenariusze są zapisywane w formie **czytelnej dla człowieka**, dzięki czemu mogą być rozumiane również przez osoby nietechniczne.

---

## 3. Czym jest `pytest-bdd`?

`pytest-bdd` to rozszerzenie frameworka `pytest`, które umożliwia pisanie testów w stylu **BDD**.

Pozwala:

* definiować scenariusze testowe w języku **Gherkin**
* powiązać je z implementacją w Pythonie
* uruchamiać je przy pomocy `pytest`

Instalacja:

```bash
pip install pytest-bdd
```

---

## 4. Język Gherkin

**Gherkin** to język opisu scenariuszy testowych używany w BDD.

Scenariusze zapisuje się w plikach:

```
.feature
```

Język Gherkin wykorzystuje zestaw słów kluczowych:

| słowo    | znaczenie                     |
| -------- | ----------------------------- |
| Feature  | opis funkcjonalności          |
| Scenario | pojedynczy scenariusz testowy |
| Given    | stan początkowy               |
| When     | akcja użytkownika             |
| Then     | oczekiwany rezultat           |
| And      | dodatkowy krok                |

---

## 5. Przykład scenariusza Gherkin

Plik `calculator.feature`

```
Feature: Calculator

  Scenario: Adding two numbers
    Given the calculator is running
    When I add 2 and 3
    Then the result should be 5
```

Opis:

| element  | znaczenie                |
| -------- | ------------------------ |
| Feature  | opisywana funkcjonalność |
| Scenario | przypadek testowy        |
| Given    | przygotowanie testu      |
| When     | wykonanie akcji          |
| Then     | weryfikacja wyniku       |

---

### Podstawowe słowa kluczowe

Gherkin używa zestawu słów kluczowych, które nadają strukturę scenariuszom:

**Feature**
```feature
Feature: Online Shopping Cart
    As a customer
    I want to manage items in my shopping cart
    So that I can purchase products online
```
Każdy plik zaczyna się od słowa `Feature`, po którym następuje nazwa funkcjonalności. Poniżej można umieścić opis w formacie:
- _As a [rola]_ - określa kto będzie korzystał z funkcjonalności
- _I want [akcja]_ - określa co użytkownik chce zrobić
- _So that [wartość biznesowa]_ - określa dlaczego ta funkcjonalność jest potrzebna

**Background**
```feature
Background:
    Given I am logged in as a customer
    And I have an empty shopping cart
```
`Background` pozwala zdefiniować wspólne warunki początkowe dla wszystkich scenariuszy w pliku. Jest to jak setup wykonywany przed każdym scenariuszem.

#### Struktura kroków (Steps)
Kroki składają się z trzech głównych typów:

**Given (warunki początkowe)**
```feature
Given I am on the home page
And I have selected English as my language
And the database contains test data
```
`Given` określa stan początkowy systemu. Może zawierać:
- Stan użytkownika (zalogowany, gość)
- Stan danych (baza danych, pliki)
- Stan aplikacji (otwarta strona, załadowane dane)

**When (akcje)**
```feature
When I click the "Login" button
And I enter "user@example.com" in the email field
And I press Enter
```
`When` opisuje akcje wykonywane przez użytkownika lub system. Powinien zawierać:
- Konkretne interakcje (kliknięcia, wpisywanie tekstu)
- Wywołania API
- Zdarzenia systemowe

**Then (oczekiwane rezultaty)**
```feature
Then I should see a welcome message
And the cart badge should show "3 items"
But I should not see error messages
```

`Then` określa oczekiwane rezultaty. Może sprawdzać:
- Widoczność elementów
- Wartości na stronie
- Stan systemu
- Otrzymane dane

#### Dodatkowe słowa kluczowe

**And/But**
```feature
Given I am logged in
And I have premium account
But my subscription expires tomorrow
```
`And` oraz `But` służą do łączenia wielu kroków tego samego typu, poprawiając czytelność.

**Komentarze**
```feature
# Ten scenariusz testuje funkcję logowania
Scenario: Successful login
    # Uwaga: email musi być aktywny
    Given I am on the login page
```
Komentarze zaczynają się od znaku `#` i są ignorowane podczas wykonania.

**Tagi**
```feature
@smoke @critical
Feature: Login functionality

@wip @manual
Scenario: Password recovery
```
`Tagi` zaczynające się od `@` pozwalają na kategoryzację i filtrowanie scenariuszy. Można ich używać do:
- Oznaczania priorytetów (`@critical`, `@low-priority`)
- Grupowania testów (`@smoke`, `@regression`)
- Wskazywania stanu prac (`@wip`, `@todo`)

## 6. Integracja z pytest

Scenariusze z pliku `.feature` są powiązane z kodem Python.

Przykład:

```python
from pytest_bdd import scenario

@scenario("calculator.feature", "Adding two numbers")
def test_addition():
    pass
```

Funkcja `scenario` łączy scenariusz z pliku Gherkin z testem w Pythonie.

---

## 7. Implementacja kroków (steps)

Każdy krok scenariusza musi mieć implementację w Pythonie.

---

### Given

```python
from pytest_bdd import given

@given("the calculator is running")
def calculator():
    return {}
```

---

### When

```python
from pytest_bdd import when

@when("I add 2 and 3")
def add(calculator):
    calculator["result"] = 2 + 3
```

---

### Then

```python
from pytest_bdd import then

@then("the result should be 5")
def check_result(calculator):
    assert calculator["result"] == 5
```

---

## 8. Parametryzacja scenariuszy

Gherkin umożliwia przekazywanie parametrów.

Przykład:

```
Scenario: Adding numbers
  Given the calculator is running
  When I add 4 and 6
  Then the result should be 10
```

Implementacja:

```python
from pytest_bdd import when, parsers

@when(parsers.parse("I add {a:d} and {b:d}"))
def add_numbers(calculator, a, b):
    calculator["result"] = a + b
```

---

## 9. Scenario Outline

Gherkin umożliwia również testowanie wielu danych.

```
Scenario Outline: Adding numbers
  Given the calculator is running
  When I add <a> and <b>
  Then the result should be <result>

Examples:
  | a | b | result |
  | 2 | 3 | 5 |
  | 4 | 5 | 9 |
```

---

## 10. Dobre praktyki

**Używaj języka naturalnego**

```feature
# Dobre
When I add a product to cart
# Złe
When I click_button("add_to_cart_button")
```

Gherkin ma być czytelny dla interesariuszy biznesowych. Unikaj technicznych szczegółów implementacji.

**Jeden scenariusz- jeden cel**
```feature
# Dobre
Scenario: Successfully adding item to cart
    Given I am viewing a product
    When I click "Add toCart"
    Then the product is added to mycart

# Złe (testuje zbyt wiele)
Scenario: Shopping process
    Given I am viewing a product
    When I click "Add to Cart"
    And I go to checkout
    And I enter payment details
    And I confirm order
    Then I receive order confirmation
```

Każdy scenariusz powinien testować jedną funkcjonalność.

**Unikaj szczegółów implementacji**
```feature
# Dobre
Given I am logged in as admin

# Złe
Given I open browser
And I navigate to "http://localhost:3000"
And I enter "admin" in field "username"
And I enter "password123" in field "password"
And I click button "Login"
```
Skup się na intencji, nie na szczegółach technicznych.

**Używaj tabeli danych**
```feature
Scenario: Creating multiple users
    Given the following users exist:
    | name   | email             |role   |
    | Alice  | alice@test.com    | admin |
    | Bob    | bob@test.com      |user   |
```
Tabele ułatwiają przedstawienie większej ilości danych w czytelny sposób.

### Docstring w Gherkin

**Docstring** w Gherkin to blok tekstu przekazywany do kroku testowego.

Jest zapisany między trzema cudzysłowami:

```
"""
tekst
"""
```

Używa się go do przekazywania:

* długich tekstów
* JSON
* XML
* zapytań SQL
* danych konfiguracyjnych

---

#### Przykład Docstring

Scenariusz:

```feature
Scenario: Process message
  Given the message
  """
  Hello world
  """
  When the system processes the message
  Then the message should be stored
```

---

#### Obsługa Docstring w Pythonie

```python
from pytest_bdd import given

@given("the message")
def message(docstring):
    return docstring
```

`docstring` zawiera tekst z bloku.

---

#### Przykład z JSON

Scenariusz:

```feature
Scenario: Process JSON
  Given the JSON message
  """
  {
    "user": "admin",
    "role": "administrator"
  }
  """
  When the system reads the message
  Then the role should be administrator
```

Python:

```python
import json
from pytest_bdd import given

@given("the JSON message")
def json_message(docstring):
    return json.loads(docstring)
```

---

## 11. Zalety BDD

Najważniejsze zalety podejścia BDD:

| zaleta        | opis                                       |
| ------------- | ------------------------------------------ |
| czytelność    | scenariusze zrozumiałe dla biznesu         |
| dokumentacja  | testy dokumentują zachowanie systemu       |
| współpraca    | ułatwia komunikację w zespole              |
| automatyzacja | scenariusze można uruchamiać automatycznie |

---

## 12. Różnica między BDD a TDD

| cecha        | TDD           | BDD                |
| ------------ | ------------- | ------------------ |
| fokus        | implementacja | zachowanie systemu |
| język testów | techniczny    | biznesowy          |
| odbiorcy     | programiści   | cały zespół        |

---

## 13. Przykładowy projekt BDD

Struktura projektu:

```
project/

├── src/
│   ├── calculator.py
│
├── tests/
│   ├── test_calculator.py
│   └── calculator.feature
```

---

## 14. Uruchomienie testów

Testy uruchamia się tak samo jak zwykły `pytest`:

```bash
pytest
```

Framework automatycznie:

* wczyta pliki `.feature`
* powiąże kroki z implementacją
* wykona scenariusze.

---

## 15. Podsumowanie

`pytest-bdd` to rozszerzenie `pytest`, które umożliwia tworzenie testów w stylu **Behavior Driven Development**.

Najważniejsze elementy tego podejścia to:

* **Gherkin** – język opisu scenariuszy testowych
* **Scenariusze Given-When-Then**
* **Docstring** – sposób przekazywania większych bloków danych do testów

Dzięki temu testy są:

* bardziej czytelne
* bliższe wymaganiom biznesowym
* jednocześnie dokumentacją systemu.

# Ale halo... to trzeba umieć angielski...

Na szczęście nie — **Gherkin można pisać po polsku** i jest to oficjalnie wspierane przez standard Gherkin. W praktyce oznacza to, że słowa kluczowe takie jak `Feature`, `Scenario`, `Given`, `When`, `Then` mają swoje **lokalne odpowiedniki w wielu językach**, w tym w polskim.

---

## Gherkin w języku polskim

Aby używać języka polskiego w pliku `.feature`, należy na początku pliku wskazać język:

```feature
# language: pl
```

Dzięki temu parser Gherkina wie, że powinien używać **polskich słów kluczowych**.

---

## Polskie słowa kluczowe Gherkin

| angielski | polski     |
| --------- | ---------- |
| Feature   | Właściwość |
| Scenario  | Scenariusz |
| Given     | Zakładając |
| When      | Jeżeli     |
| Then      | Wtedy      |
| And       | Oraz       |
| But       | Ale        |

Czasami spotyka się również alternatywy:

| angielski | alternatywa |
| --------- | ----------- |
| Given     | Mając       |
| When      | Gdy         |
| Then      | Wtedy       |

---

## Przykład scenariusza po polsku

Plik `kalkulator.feature`

```feature
# language: pl

Właściwość: Kalkulator

  Scenariusz: Dodawanie dwóch liczb
    Zakładając że kalkulator jest uruchomiony
    Jeżeli dodam 2 i 3
    Wtedy wynik powinien być 5
```

Taki plik będzie poprawnie interpretowany przez narzędzia BDD (np. `pytest-bdd`).

---

## Implementacja kroków w Pythonie

Kroki w Pythonie **muszą dokładnie odpowiadać tekstowi w scenariuszu**.

```python
from pytest_bdd import given, when, then

@given("że kalkulator jest uruchomiony")
def kalkulator():
    return {}

@when("dodam 2 i 3")
def dodawanie(kalkulator):
    kalkulator["wynik"] = 2 + 3

@then("wynik powinien być 5")
def sprawdz_wynik(kalkulator):
    assert kalkulator["wynik"] == 5
```

---

## Parametry w polskim Gherkin

Można również używać parametrów.

### Scenariusz

```feature
# language: pl

Scenariusz: Dodawanie liczb
  Zakładając że kalkulator jest uruchomiony
  Jeżeli dodam 4 i 6
  Wtedy wynik powinien być 10
```

### Python

```python
from pytest_bdd import when, parsers

@when(parsers.parse("dodam {a:d} i {b:d}"))
def dodaj(kalkulator, a, b):
    kalkulator["wynik"] = a + b
```

---

## Czy warto pisać Gherkin po polsku?

To zależy od kontekstu projektu.

### Zalety

* scenariusze są bardziej zrozumiałe dla klientów
* łatwiejsza komunikacja z biznesem
* dobre w projektach lokalnych

---

### Wady

* większość dokumentacji jest po angielsku
* trudniejsza współpraca w międzynarodowych zespołach
* część narzędzi i przykładów używa tylko angielskiego

---

## Praktyka w branży

W praktyce:

| środowisko              | język Gherkin           |
| ----------------------- | ----------------------- |
| projekty międzynarodowe | angielski               |
| projekty lokalne        | czasem lokalny język    |
| projekty open-source    | prawie zawsze angielski |

Dlatego najczęściej stosuje się **angielski**, nawet w polskich zespołach.

---

## Dobra praktyka

Często stosuje się kompromis:

* **Gherkin po angielsku**
* **komentarze i dokumentacja po polsku**

Przykład:

```feature
Feature: Calculator

  Scenario: Add two numbers
    Given the calculator is running
    When I add 2 and 3
    Then the result should be 5
```

---

## Podsumowanie

Gherkin można pisać w języku polskim, używając dyrektywy:

```
# language: pl
```

oraz polskich odpowiedników słów kluczowych, takich jak:

* **Właściwość**
* **Scenariusz**
* **Zakładając**
* **Jeżeli**
* **Wtedy**

Jednak w praktyce branżowej najczęściej stosuje się **język angielski**, aby ułatwić współpracę w zespołach międzynarodowych.

# Przykłady projektowe

- po angielsku  ====>   folder `eng`
- po polsku     ====>   folder `pl`

# Zadanie

## Struktura projektu

Najpierw utworzymy strukturę katalogów:

    project/
    ├── src/
    │   └── cash_register.py
    ├── tests/
    │   ├── __init__.py
    |   ├── features/
    |   │   └── cash_register.feature
    │   └── step_defs/
    │       ├── __init__.py
    │       └── test_cash_register_steps.py
    └── requirements.txt

## Krok 1: Instalacja zależności

W pliku `requirements.txt` dodaj:

    pytest
    pytest-bdd

Zainstaluj zależności:

``` bash
pip install -r requirements.txt
```

## Krok 2: Tworzenie klasy kasy fiskalnej

W pliku `src/cash_register.py` utworzymy prostą klasę:

``` python
class CashRegister:
    def __init__(self):
        self.total = 0.0
        self.items = []
        self.tax_rate = 0.23

    def add_item(self, name, price):
        if price <= 0:
            raise ValueError("Price must be greater than zero")
        self.items.append({"name": name, "price": price})
        self.total += price

    def apply_discount(self, percentage):
        if percentage < 0 or percentage > 100:
            raise ValueError("Discount must be between 0 and 100")
        discount_amount = self.total * (percentage / 100)
        self.total -= discount_amount
        return discount_amount

    def calculate_total_with_tax(self):
        tax_amount = self.total * self.tax_rate
        return self.total + tax_amount

    def get_receipt(self):
        receipt_lines = ["=== RECEIPT ==="]
        for item in self.items:
            receipt_lines.append(f"{item['name']}: ${item['price']:.2f}")
        receipt_lines.append(f"Subtotal: ${self.total:.2f}")
        receipt_lines.append(f"Tax ({self.tax_rate * 100}%): ${self.total * self.tax_rate:.2f}")
        receipt_lines.append(f"Total: ${self.calculate_total_with_tax():.2f}")
        receipt_lines.append("===============")
        return "\n".join(receipt_lines)

    def clear(self):
        self.total = 0.0
        self.items = []
```

## Krok 3: Definiowanie scenariuszy w Gherkin

W pliku `features/cash_register.feature` opisujemy scenariusze w języku
Gherkin:

``` gherkin
Feature: Cash Register Operations
  As a cashier
  I want to use a cash register
  So that I can process customer purchases

  Background:
    Given a new cash register

  Scenario: Add single item to cash register
    When I add item "Coffee" with price 5.99
    Then the total should be 5.99
    And the receipt should contain "Coffee: $5.99"

  Scenario: Add multiple items to cash register
    When I add item "Coffee" with price 5.99
    And I add item "Sandwich" with price 7.50
    Then the total should be 13.49
    And the receipt should contain "Coffee: $5.99"
    And the receipt should contain "Sandwich: $7.50"

  Scenario: Apply discount to purchase
    Given I add item "Book" with price 30.00
    When I apply a 10 percent discount
    Then the total should be 27.00
    And the discount amount should be 3.00

  Scenario: Calculate total with tax
    Given I add item "Book" with price 100.00
    When I calculate the total with tax
    Then the final amount should be 123.00

  Scenario: Handle invalid price
    When I try to add item "Invalid" with price -5.00
    Then I should get a price error message

  Scenario: Handle invalid discount
    Given I add item "Book" with price 100.00
    When I try to apply a 150 percent discount
    Then I should get a discount error message
```

## Krok 4: Implementacja kroków testowych

W pliku `tests/step_defs/test_cash_register_steps.py` implementujemy
kroki:

``` python
from pytest_bdd import scenarios, given, when, then, parsers
import pytest
from src.cash_register import CashRegister

# Load scenarios from the feature file
scenarios('../features/cash_register.feature')

# Fixtures
@pytest.fixture
def cash_register():
    return CashRegister()

@pytest.fixture
def test_context():
    """Context to store test-specific values"""
    return {}

# Given steps
@given("a new cash register")
def new_cash_register(cash_register):
    """Create a new cash register instance."""
    return cash_register

@given(parsers.parse('I add item "{name}" with price {price:f}'))
def given_add_item(cash_register, name, price):
    """Add an item to the cash register."""
    cash_register.add_item(name, price)

# When steps
@when(parsers.parse('I add item "{name}" with price {price:f}'))
def when_add_item(cash_register, name, price):
    """Add an item to the cash register."""
    cash_register.add_item(name, price)

@when(parsers.parse('I apply a {percentage:d} percent discount'))
def apply_discount(cash_register, test_context, percentage):
    """Apply a discount percentage."""
    test_context['discount_amount'] = cash_register.apply_discount(percentage)

@when('I calculate the total with tax')
def calculate_with_tax(cash_register, test_context):
    """Calculate the total with tax."""
    test_context['final_amount'] = cash_register.calculate_total_with_tax()

@when(parsers.parse('I try to add item "{name}" with price {price:f}'))
def try_add_invalid_item(cash_register, test_context, name, price):
    """Try to add an item with an invalid price."""
    with pytest.raises(ValueError) as excinfo:
        cash_register.add_item(name, price)
    test_context['error_message'] = str(excinfo.value)

@when(parsers.parse('I try to apply a {percentage:d} percent discount'))
def try_apply_invalid_discount(cash_register, test_context, percentage):
    """Try to apply an invalid discount."""
    with pytest.raises(ValueError) as excinfo:
        cash_register.apply_discount(percentage)
    test_context['error_message'] = str(excinfo.value)

# Then steps
@then(parsers.parse('the total should be {expected:f}'))
def check_total(cash_register, expected):
    """Verify the total amount."""
    assert cash_register.total == pytest.approx(expected, 0.01)

@then(parsers.parse('the receipt should contain "{expected_text}"'))
def check_receipt_content(cash_register, expected_text):
    """Verify receipt contains expected text."""
    receipt = cash_register.get_receipt()
    assert expected_text in receipt

@then(parsers.parse('the discount amount should be {expected:f}'))
def check_discount_amount(test_context, expected):
    """Verify the discount amount."""
    assert 'discount_amount' in test_context, "Discount was not applied in the test"
    assert test_context['discount_amount'] == pytest.approx(expected, 0.01)

@then(parsers.parse('the final amount should be {expected:f}'))
def check_final_amount(test_context, expected):
    """Verify the final amount with tax."""
    assert 'final_amount' in test_context, "Total with tax was not calculated in the test"
    assert test_context['final_amount'] == pytest.approx(expected, 0.01)

@then('I should get a price error message')
def check_price_error(test_context):
    """Verify the price error message is received."""
    assert 'error_message' in test_context, "No error was caught in the test"
    assert "Price must be greater than zero" in test_context['error_message']

@then('I should get a discount error message')
def check_discount_error(test_context):
    """Verify the discount error message is received."""
    assert 'error_message' in test_context, "No error was caught in the test"
    assert "Discount must be between 0 and 100" in test_context['error_message']
```

## Krok 5: Uruchamianie testów

Aby uruchomić testy, wykonaj w głównym katalogu projektu:

``` bash
pytest -v
```

Możesz również uruchomić testy z bardziej szczegółowym raportem:

``` bash
pytest -v --gherkin-terminal-reporter
```

## Krok 6: Uzupełnienie scenariusza o tabelkę

Dopisz na końcu pliku `features/cash_register.feature`:

``` gherkin
  Scenario Outline: Apply various discounts and calculate total with tax
    Given I add item "<item_name>" with price <price>
    When I apply a <discount> percent discount
    And I calculate the discounted total with tax
    Then the final amount after discount and tax should be <expected_total>

    Examples:
      | item_name    | price  | discount | expected_total |
      | Laptop       | 1000.00 | 20      | 984.00        |
      | TV           | 500.00  | 10      | 553.50        |
      | Phone        | 300.00  | 15      | 313.05        |
      | Headphones   | 80.00   | 5       | 93.48         |
      | Tablet       | 250.00  | 0       | 307.50        |
```

## Krok 7: Dodaj testy

W pliku `tests/step_defs/test_cash_register_steps.py` dodaj:

``` python
@when('I calculate the discounted total with tax')
def calculate_discounted_total_with_tax(cash_register, test_context):
    """Calculate the total with tax after discount has been applied."""
    test_context['final_discounted_amount'] = cash_register.calculate_total_with_tax()


@then(parsers.parse('the final amount after discount and tax should be {expected:f}'))
def check_final_discounted_amount(test_context, expected):
    """Verify the final amount after discount and tax."""
    assert 'final_discounted_amount' in test_context, "Discounted total with tax was not calculated in the test"
    assert test_context['final_discounted_amount'] == pytest.approx(expected, 0.01)
```

## Inny przykład do samodzielnej analizy (konto bankowe)

- <https://pytest-with-eric.com/bdd/pytest-bdd/#What-You%E2%80%99ll-Learn>

## Symulator telefonu na kartę

``` gherkin
# prepaid_phone.feature

Feature: Prepaid phone functionality
    As a prepaid phone user
    I want to manage my phone balance and make calls
    So that I can use my phone services effectively

    Background:
        Given a prepaid phone with number "555-123-4567"

    Scenario: Make a call with sufficient balance
        Given the phone has a balance of $10.00
        When I make a call that costs $2.50
        Then the call should be successful
        And the remaining balance should be $7.50

    Scenario: Attempt to make a call with insufficient balance
        Given the phone has a balance of $1.00
        When I attempt to make a call that costs $2.50
        Then the call should be rejected
        And the remaining balance should be $1.00

    Scenario: Top up the phone balance
        Given the phone has a balance of $5.00
        When I add $15.00 to the balance
        Then the new balance should be $20.00

    Scenario: Check call history
        Given the phone has a balance of $20.00
        And I have made the following calls:
            | number       | duration | cost  |
            | 555-987-6543 | 5 min    | $2.50 |
            | 555-234-5678 | 3 min    | $1.50 |
        When I check my call history
        Then I should see 2 calls in the history
        And the total cost should be $4.00

    Scenario Outline: Different call rates
        Given the phone has a balance of $10.00
        When I make a <duration> minute call to <type> number
        Then the call cost should be $<cost>
        And the remaining balance should be $<remaining>

        Examples:
            | duration | type          | cost | remaining |
            | 2        | local         | 0.40 | 9.60      |
            | 5        | international | 5.00 | 5.00      |
            | 3        | mobile        | 0.90 | 9.10      |

    Scenario: Multiple top-ups with different amounts
        Given the phone has a balance of $0.00
        When I add the following amounts:
            | amount |
            | $5.00  |
            | $10.00 |
            | $2.50  |
        Then the final balance should be $17.50

    Scenario: Check balance limits
        Given the phone has a balance of $95.00
        When I add $10.00 to the balance
        Then the operation should be rejected with message "Maximum balance limit of $100.00 exceeded"
        And the balance should remain $95.00

    Scenario: Send SMS message
        Given the phone has a balance of $5.00
        When I send an SMS message
        Then the SMS should be sent successfully
        And the remaining balance should be $4.80

    Scenario: Multiple operations in sequence
        Given the phone has a balance of $20.00
        When I perform the following operations:
            | operation | detail        | amount |
            | call      | 5 min local   | $1.00  |
            | sms       | 1 message     | $0.20  |
            | topup     | add credit    | $5.00  |
            | call      | 3 min mobile  | $0.90  |
        Then the final balance should be $22.90
```

``` python
# prepaid_phone.py

from datetime import datetime


class CallRecord:
    def __init__(self, number, duration, cost, timestamp=None):
        self.number = number
        self.duration = duration
        self.cost = float(cost)
        self.timestamp = timestamp or datetime.now()


class PrepaidPhone:
    # Define call rates for different types
    CALL_RATES = {
        'local': 0.20,  # $0.20 per minute
        'mobile': 0.30,  # $0.30 per minute
        'international': 1.00  # $1.00 per minute
    }

    SMS_COST = 0.20  # $0.20 per SMS
    MAX_BALANCE = 100.00  # Maximum allowed balance

    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.balance = 0.0
        self.call_history = []
        self.sms_count = 0

    def add_credit(self, amount):
        """
        Add credit to the phone balance
        Returns True if successful, False if operation would exceed maximum balance
        """
        amount = float(amount)

        if self.balance + amount > self.MAX_BALANCE:
            return False

        self.balance += amount
        # Round to 2 decimal places to avoid floating point precision issues
        self.balance = round(self.balance, 2)
        return True

    def make_call(self, destination_number, duration, call_type='local'):
        """
        Attempt to make a call
        Returns True if successful, False if insufficient balance
        """
        # Calculate call cost based on duration and type
        duration_minutes = float(duration)
        rate = self.CALL_RATES.get(call_type, self.CALL_RATES['local'])
        cost = duration_minutes * rate
        # Round cost to 2 decimal places
        cost = round(cost, 2)

        if self.balance >= cost:
            # Deduct the cost and record the call
            self.balance -= cost
            self.balance = round(self.balance, 2)
            call_record = CallRecord(destination_number, duration, cost)
            self.call_history.append(call_record)
            return True

        return False

    def send_sms(self):
        """
        Attempt to send an SMS
        Returns True if successful, False if insufficient balance
        """
        if self.balance >= self.SMS_COST:
            self.balance -= self.SMS_COST
            self.balance = round(self.balance, 2)
            self.sms_count += 1
            return True

        return False

    def get_balance(self):
        """Return current balance"""
        return self.balance

    def get_call_history(self):
        """Return list of all calls made"""
        return self.call_history

    def get_total_call_cost(self):
        """Calculate total cost of all calls"""
        total = sum(call.cost for call in self.call_history)
        return round(total, 2)

    def attempt_call_with_cost(self, cost):
        """
        Attempt to make a call with a specific cost (for testing purposes)
        Returns True if successful, False if insufficient balance
        """
        cost = float(cost)

        if self.balance >= cost:
            self.balance -= cost
            self.balance = round(self.balance, 2)
            call_record = CallRecord("unknown", 0, cost)
            self.call_history.append(call_record)
            return True

        return False

    def add_call_to_history(self, number, duration, cost):
        """
        Add a call record to history (for testing purposes)
        """
        call_record = CallRecord(number, duration, cost)
        self.call_history.append(call_record)
        # Deduct from balance to simulate actual call
        self.balance -= float(cost)
        self.balance = round(self.balance, 2)

    def perform_operations(self, operations):
        """
        Perform a sequence of operations and return final balance
        """
        for operation in operations:
            op_type = operation['operation']
            amount = float(operation['amount'])

            if op_type == 'call':
                # For simplicity, we use the amount as cost directly
                self.attempt_call_with_cost(amount)
            elif op_type == 'sms':
                self.send_sms()
            elif op_type == 'topup':
                self.add_credit(amount)

        return self.balance
```