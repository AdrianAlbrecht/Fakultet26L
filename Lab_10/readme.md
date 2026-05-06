# Lab 10 - Analiza wartości brzegowych

## 1. Czym jest analiza wartości brzegowych?

**Analiza wartości brzegowych (Boundary Value Analysis, BVA)** to technika testowania polegająca na sprawdzaniu danych **na granicach zakresów dopuszczalnych wartości**.

Opiera się ona na obserwacji, że:

> większość błędów w programach pojawia się w pobliżu granic zakresów danych.

Dlatego zamiast testować wiele wartości wewnątrz zakresu, skupiamy się na wartościach **przed granicą, na granicy i tuż za granicą**.

---

## 2. Dlaczego błędy pojawiają się na granicach?

Błędy często wynikają z:

* błędów w operatorach (`<`, `<=`, `>`, `>=`)
* błędów off-by-one
* złej obsługi minimalnych lub maksymalnych wartości
* błędów indeksowania tablic
* problemów z typami danych

Przykładowy błąd:

```python
if x > 10
```

zamiast

```python
if x >= 10
```

---

## 3. Zasada wyboru wartości brzegowych

Dla zakresu:

```
min ≤ x ≤ max
```

testujemy zwykle:

```
min - 1
min
min + 1
max - 1
max
max + 1
```

---

## 4. Przykład zakresu

Załóżmy, że funkcja przyjmuje wiek:

```
18–65
```

Testowane wartości:

| wartość | znaczenie               |
| ------- | ----------------------- |
| 17      | poniżej zakresu         |
| 18      | dolna granica           |
| 19      | tuż nad granicą         |
| 64      | tuż przed górną granicą |
| 65      | górna granica           |
| 66      | powyżej zakresu         |

---

## 5. Przykład funkcji w Pythonie

```python
def age_category(age):
    if age < 18:
        return "minor"
    elif age <= 65:
        return "adult"
    else:
        return "senior"
```

---

## 6. Testy jednostkowe (unittest)

```python
import unittest

class TestAgeCategory(unittest.TestCase):

    def test_boundary_values(self):
        self.assertEqual(age_category(17), "minor")
        self.assertEqual(age_category(18), "adult")
        self.assertEqual(age_category(19), "adult")
        self.assertEqual(age_category(65), "adult")
        self.assertEqual(age_category(66), "senior")
```

---

## 7. Analiza wartości brzegowych dla tablic

Granice pojawiają się również przy pracy z tablicami.

Dla tablicy o długości `n` indeksy to:

```
0 ... n-1
```

Testujemy:

```
-1
0
1
n-2
n-1
n
```

---

### Przykład funkcji

```python
def get_element(arr, index):
    return arr[index]
```

Testy:

```python
class TestArray(unittest.TestCase):

    def test_boundaries(self):
        arr = [10, 20, 30]

        self.assertEqual(get_element(arr, 0), 10)
        self.assertEqual(get_element(arr, 2), 30)

        with self.assertRaises(IndexError):
            get_element(arr, -1)

        with self.assertRaises(IndexError):
            get_element(arr, 3)
```

---

## 8. Analiza wartości brzegowych dla długości danych

Często testuje się długość:

* tekstu
* listy
* hasła

Przykład: hasło musi mieć **8–16 znaków**.

Testy:

```
7
8
9
15
16
17
```

---

### Python

```python
def valid_password(pwd):
    return 8 <= len(pwd) <= 16
```

Test:

```python
class TestPassword(unittest.TestCase):

    def test_boundaries(self):
        self.assertFalse(valid_password("1234567"))
        self.assertTrue(valid_password("12345678"))
        self.assertTrue(valid_password("123456789"))
        self.assertTrue(valid_password("1234567890123456"))
        self.assertFalse(valid_password("12345678901234567"))
```

---

## 9. Analiza wartości brzegowych a klasy równoważności

Te dwie techniki często stosuje się razem.

### Klasy równoważności

Dzielą dane na grupy.

Przykład:

```
x < 0
0 ≤ x ≤ 100
x > 100
```

### Analiza wartości brzegowych

Testuje granice tych klas:

```
-1
0
1
99
100
101
```

---

## 10. Rozszerzona analiza wartości brzegowych

Istnieje również **robust boundary value analysis**.

Oprócz wartości w zakresie testuje również:

```
min - 1
max + 1
```

czyli wartości **niepoprawne**.

---

## 11. Zalety techniki

Najważniejsze zalety analizy wartości brzegowych:

| zaleta                     | opis                          |
| -------------------------- | ----------------------------- |
| skuteczność                | wykrywa wiele błędów          |
| mała liczba testów         | niewiele przypadków testowych |
| prostota                   | łatwa do zastosowania         |
| dobra dla walidacji danych | szczególnie przy formularzach |

---

## 12. Ograniczenia techniki

Technika nie wykrywa wszystkich błędów.

Ograniczenia:

* nie testuje wszystkich ścieżek programu
* zakłada, że błędy są przy granicach
* nie sprawdza złożonych kombinacji warunków

Dlatego często łączy się ją z:

* klasami równoważności
* analizą ścieżek
* tablicami decyzyjnymi

---

## 13. Podsumowanie

**Analiza wartości brzegowych** to technika testowania polegająca na sprawdzaniu zachowania programu dla danych znajdujących się **na granicach zakresów wejściowych**.

Najczęściej testuje się wartości:

```
min - 1
min
min + 1
max - 1
max
max + 1
```

Technika ta jest szczególnie skuteczna przy testowaniu:

* walidacji danych
* zakresów liczbowych
* indeksów tablic
* długości danych.

# Zadania

## Ćwiczenie 1: System naliczania rabatów w sklepie internetowym

Testujesz moduł e-commerce obliczający wysokość rabatu na podstawie
wartości koszyka. System przyjmuje wartość zakupów w złotych (0-5000 zł)
i zwraca procent rabatu zgodnie z poniższą tabelą:

| Wartość koszyka (zł) | Rabat (%) |
|----------------------|-----------|
| 0 - 99               | 0         |
| 100 - 299            | 5         |
| 300 - 699            | 10        |
| 700 - 1499           | 15        |
| 1500 - 2999          | 20        |
| 3000 - 5000          | 25        |

Używając dwupunktowej analizy wartości brzegowych, zaprojektuj przypadki
testowe sprawdzające poprawność działania modułu. Dla każdej wartości
testowej określ oczekiwany rabat.

Następnie rozszerz zestaw testów do trójpunktowej analizy wartości
brzegowych. Założenie: system przyjmuje tylko liczby całkowite
reprezentujące złotówki.

## Ćwiczenie 2: Kalkulator opłat parkingowych

Testujesz system parkingowy obliczający opłatę za postój na podstawie
liczby minut. System przyjmuje czas postoju (0-720 minut) i zwraca
opłatę według cennika:

| Czas postoju (min) | Opłata (zł) |
|--------------------|-------------|
| 0 - 30             | 0           |
| 31 - 60            | 3           |
| 61 - 120           | 6           |
| 121 - 240          | 12          |
| 241 - 480          | 20          |
| 481 - 720          | 30          |

Aplikacja dostępna jest przez API REST przyjmujące parametr czasu w
minutach. Zaprojektuj zestaw testów używając dwupunktowej analizy
wartości brzegowych, określając dla każdego przypadku testowego
oczekiwaną opłatę.

Jakie dodatkowe przypadki testowe należy uwzględnić przy zastosowaniu
trzypunktowej analizy wartości brzegowych?

## Ćwiczenie 3: Walidator siły hasła

Testujesz moduł oceniający siłę hasła na podstawie jego długości. System
przyjmuje długość hasła (1-30 znaków) i zwraca ocenę:

| Długość hasła | Ocena siły      |
|---------------|-----------------|
| 1 - 5         | Bardzo słabe    |
| 6 - 8         | Słabe           |
| 9 - 12        | Średnie         |
| 13 - 16       | Silne           |
| 17 - 20       | Bardzo silne    |
| 21 - 30       | Wyjątkowo silne |

Zaprojektuj przypadki testowe używając dwupunktowej analizy wartości
brzegowych. Dla każdego przypadku określ oczekiwaną ocenę siły hasła.

Rozważ także testowanie wartości spoza dozwolonego zakresu. Jakie
przypadki testowe dodałbyś, aby sprawdzić obsługę błędnych danych
wejściowych?

## Ćwiczenie 4: System obliczania uprawnień emerytalnych

Rozważ następującą specyfikację systemu sprawdzającego uprawnienia
emerytalne:

System weryfikuje prawo do emerytury na podstawie wieku pracownika W
oraz stażu pracy S. Pracownik ma prawo do emerytury, gdy spełniony jest
jeden z warunków: wiek wynosi co najmniej 65 lat LUB suma wieku i stażu
pracy wynosi co najmniej 85 (zasada 85). System przyjmuje wiek w
zakresie 18-75 lat oraz staż pracy w zakresie 0-60 lat.

Zaprojektuj przypadki testowe stosując dwupunktową analizę wartości
brzegowych. Zwróć uwagę, że musisz analizować wartości brzegowe dla
dwóch niezależnych warunków oraz ich kombinacji.

Jakie problemy w tej specyfikacji możesz zidentyfikować? Rozważ
przypadki, gdy osoba zaczęła pracę w bardzo młodym wieku lub gdy suma
wieku i stażu przekracza realnie możliwe wartości.

## Ćwiczenie 5: Kalkulator zniżek lotniczych dla rodzin

System linii lotniczych oblicza zniżkę rodzinną według następującej
specyfikacji:

Zniżka jest przyznawana rodzinom na podstawie liczby dorosłych D (18+
lat) i liczby dzieci N (0-17 lat). Zniżka wynosi 15%, gdy D = 2 i N ≥ 2,
lub gdy D = 1 i N ≥ 3. W pozostałych przypadkach zniżka wynosi 0%.
System akceptuje D w zakresie 1-4 oraz N w zakresie 0-8. Dodatkowo,
całkowita liczba osób (D + N) nie może przekroczyć 9.

Zaprojektuj testy używając analizy wartości brzegowych, uwzględniając
ograniczenie na sumę D + N. Rozważ, które kombinacje wartości są
nierealne lub niemożliwe do przetestowania.

Czy specyfikacja jest kompletna? Jakie przypadki graniczne związane z
definicją rodziny mogą powodować problemy interpretacyjne?

## Ćwiczenie 6: System walidacji transakcji bankowych

Analizujesz system weryfikujący transakcje kartą płatniczą:

System sprawdza poprawność transakcji na podstawie: kwoty transakcji K
(1-50000 zł), dostępnego salda S (0-100000 zł) oraz dziennego limitu
pozostałego do wykorzystania L (0-20000 zł). Transakcja jest
akceptowana, gdy K ≤ S ORAZ K ≤ L. System dodatkowo sprawdza, czy K nie
przekracza 30% wartości S dla transakcji powyżej 5000 zł (zabezpieczenie
przed wyczyszczeniem konta).

Zaprojektuj przypadki testowe dla tego systemu, analizując wartości
brzegowe dla wszystkich trzech parametrów oraz ich wzajemnych
zależności. Zwróć szczególną uwagę na punkt przełączenia zasady 30%.

Jakie sytuacje graniczne nie są jasno zdefiniowane w specyfikacji?
Rozważ przypadki, gdy wiele warunków jest na granicy jednocześnie.

## Ćwiczenie 7: Algorytm dopasowania kierowców w aplikacji taxi

System dopasowuje kierowcę do pasażera według specyfikacji:

Algorytm bierze pod uwagę: odległość kierowcy od pasażera O (0-25 km),
ocenę kierowcy R (1.0-5.0 z krokiem 0.1) oraz czas oczekiwania kierowcy
na zlecenie T (0-120 minut). Kierowca jest dopasowany, gdy spełnia
warunek: (O ≤ 5 ORAZ R ≥ 4.0) LUB (O ≤ 10 ORAZ R ≥ 4.5 ORAZ T ≥ 30) LUB
(O ≤ 15 ORAZ T ≥ 60).

Zaprojektuj kompleksowy zestaw testów analizując wartości brzegowe dla
złożonych warunków logicznych. Określ, które kombinacje parametrów są
najbardziej krytyczne dla jakości usługi.

Czy potrafisz zidentyfikować scenariusze, w których specyfikacja może
prowadzić do nieintuicyjnych lub niesprawiedliwych dopasowań?

## Ćwiczenie 8: System oceny ryzyka kredytowego

Rozważ specyfikację modułu oceny zdolności kredytowej:

System oblicza kategorię ryzyka na podstawie: miesięcznego dochodu D
(1000-50000 zł), wieku kredytobiorcy W (18-70 lat) oraz wnioskowanej
kwoty kredytu K (5000-500000 zł). Ryzyko jest NISKIE gdy: D ≥ 5000 ORAZ
K/D ≤ 48 ORAZ W ≤ 60. Ryzyko jest WYSOKIE gdy: D \< 3000 LUB K/D \> 72
LUB W \> 65. W pozostałych przypadkach ryzyko jest ŚREDNIE. Dodatkowo,
system odrzuca wnioski, gdzie okres spłaty (obliczany jako K/D/12)
przekroczyłby wiek 75 lat.

Zaprojektuj przypadki testowe uwzględniając wszystkie warunki i ich
interakcje. Zwróć uwagę na miejsca, gdzie różne reguły mogą się nakładać
lub być ze sobą sprzeczne.

Jakie luki w specyfikacji mogą prowadzić do problemów w granicznych
przypadkach? Rozważ sytuacje, gdy kredytobiorca ma dokładnie 65 lub 60
lat.

## Ćwiczenie 9: Walidator harmonogramu pracowniczego

System weryfikuje poprawność harmonogramu według przepisów:

Harmonogram jest poprawny gdy: liczba godzin w dniu G (0-24), liczba dni
pracy w tygodniu D (0-7) oraz liczba tygodni w miesiącu T (1-5)
spełniają warunki: G ≤ 12 dla pojedynczego dnia, G × D ≤ 48 dla
tygodnia, oraz G × D × T ≤ 168 dla miesiąca. Dodatkowo, jeśli D \> 5, to
maksymalne G = 8, a jeśli G \> 10, to wymagana jest przerwa co najmniej
11 godzin, co redukuje efektywne G w kolejnym dniu do maksymalnie 13.

Zaprojektuj testy analizując kaskadowe zależności między parametrami.
Określ, które kombinacje wartości brzegowych są fizycznie niemożliwe,
ale dozwolone przez system.

Czy specyfikacja uwzględnia wszystkie wymagania prawne? Jakie przypadki
graniczne mogą prowadzić do naruszeń przepisów prawa pracy?

## Ćwiczenie 10: System wykrywania anomalii w przelewach firmowych z wykorzystaniem prawa Benforda

System antyfraudowy w firmie monitoruje przelewy wychodzące i oznacza
transakcje jako podejrzane według następujących kryteriów:

1.  System analizuje przelewy w przedziale 100-999999 zł
2.  Dla każdego miesiąca oblicza rozkład pierwszych cyfr znaczących kwot
    przelewów
3.  Transakcja jest oznaczana jako PODEJRZANA gdy spełniony jest jeden z
    warunków:
    - Kwota zaczyna się od cyfry C, gdzie odchylenie częstości
      występowania C od oczekiwanej wartości Benforda przekracza 15
      punktów procentowych
    - Kwota znajduje się w przedziale, gdzie więcej niż 40% transakcji
      ma identyczną pierwszą cyfrę
    - Kwota jest “okrągła” (kończy się na co najmniej 2 zera) ORAZ jej
      pierwsza cyfra występuje rzadziej niż przewiduje rozkład Benforda
4.  Dodatkowo system stosuje próg minimalny: analiza Benforda jest
    wykonywana tylko gdy w danym miesiącu jest co najmniej 50 transakcji

Oczekiwane częstości według prawa Benforda:

- Cyfra 1: 30,1%
- Cyfra 2: 17,6%
- Cyfra 3: 12,5%
- Cyfra 4: 9,7%
- Cyfra 5: 7,9%
- Cyfra 6: 6,7%
- Cyfra 7: 5,8%
- Cyfra 8: 5,1%
- Cyfra 9: 4,6%

### Zadanie:

Zaprojektuj przypadki testowe wykorzystując analizę wartości brzegowych
dla tego systemu. Musisz uwzględnić:

1.  Wartości brzegowe dla kwot przelewów (100-999999 zł)
2.  Wartości brzegowe dla odchyleń od rozkładu Benforda (próg 15%)
3.  Wartości brzegowe dla procentu transakcji z identyczną pierwszą
    cyfrą (próg 40%)
4.  Interakcje między różnymi warunkami oznaczania jako podejrzane
5.  Graniczne przypadki dla liczby transakcji w miesiącu (próg 50)

Dla każdego przypadku testowego określ:

- Zestaw transakcji testowych
- Oczekiwany wynik (PODEJRZANA/NORMALNA)
- Którą regułę system powinien zastosować

### Pytania do rozważenia:

1.  Jak system powinien zachować się, gdy mamy dokładnie 50 transakcji w
    miesiącu i jedna z nich jest analizowana?

2.  Co się stanie, gdy kwota wynosi dokładnie 100 zł lub 999999 zł? Czy
    te wartości brzegowe mogą zakłócić analizę Benforda?

3.  Jak testować przypadek, gdy odchylenie wynosi dokładnie 15%? Czy
    system powinien oznaczyć taką transakcję jako podejrzaną?

4.  Czy definicja “okrągłej” kwoty jest wystarczająco precyzyjna? Jak
    system powinien traktować kwoty jak 1000 zł (3 zera) vs 100 zł (2
    zera)?

5.  Jakie problemy mogą wystąpić, gdy analizujemy małą firmę, która
    regularnie wykonuje przelewy o podobnych kwotach (np. wypłaty dla
    pracowników)?

Pamiętaj, że testując system oparty na analizie statystycznej, musisz
myśleć nie tylko o pojedynczych transakcjach, ale o całym kontekście.
Wartość brzegowa w tym przypadku może dotyczyć nie tylko kwoty
pojedynczego przelewu, ale także:

- Rozkładu całego zbioru transakcji
- Momentu, w którym rozkład przestaje być “naturalny”
- Granicy między normalnym skupieniem wartości a podejrzaną manipulacją

Rozważ także przypadki, gdzie naturalne procesy biznesowe mogą generować
rozkłady odbiegające od prawa Benforda (np. firma płacąca wszystkim
pracownikom podobne pensje zaczynające się od tej samej cyfry).

Czy potrafisz zidentyfikować scenariusz, w którym oszust znający prawo
Benforda mógłby manipulować kwotami tak, aby uniknąć wykrycia przez
system? Jak można by zmodyfikować reguły, aby wykryć takie wyrafinowane
próby oszustwa?