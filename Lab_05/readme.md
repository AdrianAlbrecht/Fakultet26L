# Lab 05 - atrapy obiektów w testowaniu modułowym

# Mock jako atrapy obiektów

Obiekty Mock to specjalne typy obiektów używane w testowaniu oprogramowania. Służą jako atrapy rzeczywistych obiektów, pozwalając na izolację testowanego kodu od zewnętrznych zależności. Biblioteka `unittest.mock` w Pythonie dostarcza wszechstronne narzędzia do tworzenia takich atrap.

## **Tworzenie Mocków**

```python
from unittest.mock import Mock

# Podstawowe tworzenie obiektu Mock
my_mock = Mock(name='MyMock')

# Tworzenie z automatyczną specyfikacją
mock_obj =Mock(autospec=True)
```

Obiekt `Mock` pozwala na symulowanie dowolnego obiektu. Parametr `name` pozwala na nadanie nazwy, co ułatwia debugowanie. Parametr `autospec=True` tworzy mock, który zachowuje się jak obiekt, na którym został oparty, łącznie z wywoływaniem wyjątków dla nieprawidłowych wywołań metod.

# **Konfiguracja Return Value**

## Ustaw wartość zwracaną dla metody

```python
my_mock.get_data.return_value = 'dane_testowe'
```

Atrybut `return_value` określa wartość, którą zwróci metoda mocka przy wywołaniu.


# **Konfiguracja Side Effect**
```python
# Różne wartości dla kolejnych wywołań
mock_obj.some_method.side_effect = [ 10 , 20 , 30 ]

# Funkcja jako side_effect
def side_effect_func(*args, **kwargs):
    print("Side effect called with args:", args, kwargs)
    return "OK"


mock_obj.other_method.side_effect = side_effect_func


# Side effect rzucający wyjątek
mock_obj.error_method.side_effect = ValueError("Something went wrong")
```

Atrybut `side_effect` jest potężnym narzędziem mogącym:
- Zwracać różne wartości dla kolejnych wywołań 
- Wykonywać dowolną funkcję z argumentami wywołania 
- Rzucać wyjątki

Side effect ma zawsze priorytet nad `return_value`.

## Śledzenie Wywołań

```python
# Sprawdzenie czy metoda została wywołana
mock.called # True/False

# Liczba wywołań
mock.call_count # Liczba całkowita

# Argumenty ostatniego wywołania
mock.call_args # Tuple postaci ((args), {kwargs})

# Lista wszystkich wywołań
mock.call_args_list # Lista obiektów call_args
```

Metody te pozwalają na śledzenie historii wywołań mocka, co jest kluczowe w testowaniu interakcji.


## Weryfikacja Wywołań

```python
# Weryfikacja argumentów wywołania
my_mock.get_data.assert_called_with('user')

# Weryfikacja braku wywołań
mock.assert_not_called()

# Weryfikacja jednorazowego wywołania
mock.assert_called_once()

# Weryfikacja dokładnie jednego wywołania z konkretnymi argumentami
mock.assert_called_once_with( 1 , 2 , a= 3 )

# Weryfikacja sekwencji wywołań
mock.assert_has_calls([
    call.method1( 1 ),
    call.method2( 2 ),
    call.method1( 3 )
])

# Weryfikacja wywołań w dowolnej kolejności
mock.assert_has_calls([
    call.method2( 2 ),
    call.method1( 1 )
], any_order=True)
```

Metody asercji pozwalają na weryfikację czy mock został wywołany w oczekiwany sposób, co jest fundamentem testowania behawioralnego.

## ANY - Elastyczne Dopasowanie Argumentów

```python
from unittest.mock import ANY

# Ignorowanie wartości konkretnego argumentu
mock.assert_called_with(ANY, 123 , key="value")

# Dopasowanie w zagnieżdżonych strukturach
mock.assert_called_with({"a": [ANY, 2 , {"x": ANY}],"b": ANY})
```

Stała `ANY` to specjalny marker dopasowujący dowolną wartość. Jest przydatny, gdy nie interesuje nas dokładna wartość konkretnego argumentu.

## MagicMock

```python
from unittest.mock import MagicMock

# Konfiguracja metod specjalnych
magic_mock = MagicMock()
magic_mock.__len__.return_value = 5
magic_mock.__add__.return_value ="wynik dodawania"
magic_mock.__getitem__.side_effect = **lambda** key: f"wartość dla {key}"
magic_mock.__str__.return_value ="to jest magiczny mock"

# Użycie jako menedżera kontekstu
mock_context =MagicMock()
mock_context.__enter__.return_value ="wartość wewnątrz kontekstu"
mock_context.__exit__.return_value =False
```

`MagicMock` rozszerza `Mock` o domyślną implementację metod specjalnych Pythona (tzw. magicznych metod). Jest przydatny do mockowania klas z takimi metodami jak `__len__`, `__iter__`, czy metody kontekstowe.

## Zagnieżdżone Mocki i Konfiguracja

```python
# Automatyczne tworzenie zagnieżdżonych mocków
nested_mock = Mock()
nested_mock.outer.inner.method.return_value = "zagnieżdżona wartość"

# Konfiguracja wielu atrybutów jednocześnie
complex_mock =Mock()
complex_mock.configure_mock(
    **{
        'attr1': "wartość 1",
        'attr2.method1.return_value':"wynik metody 1",
        'attr2.method2.side_effect': [ 10 , 20 , 30 ]
    }
)
```

Mocki automatycznie tworzą zagnieżdżone mocki dla dowolnej ścieżki atrybutów. Metoda `configure_mock` pozwala na konfigurację wielu atrybutów i zagnieżdżonych mocków w jednym wywołaniu.

## Obiekty Call

```python
from unittest.mock import call

# Tworzenie obiektów call
c1 =call( 1 , 2 , 3 )
c2 =call('a', b= 10 )

# Tworzenie złożonych sekwencji wywołań
complex_call =call.method( 1 , 2 ).method2(a= 3 )
print("Lista wywołań:", complex_call.call_list())
```

Obiekty `call` reprezentują pojedyncze wywołania i są używane do porównywania z faktycznymi wywołaniami mocków lub do definiowania oczekiwanych sekwencji wywołań.

## Resetowanie Mocków

```python
# Resetowanie statystyk wywołań
mock.reset_mock()

# Resetowanie z zachowaniem wartości zwracanych
mock.reset_mock(return_value=False)
```

Metoda `reset_mock` pozwala na zresetowanie historii wywołań mocka, co jest przydatne w testach z wieloma asercjami.

## Elastyczne Odpowiedzi na Różne Argumenty

```python
# Różne odpowiedzi dla różnych argumentów
mock.side_effect = **lambda** x: {
    1 : "jeden",
    2 : "dwa",
    3 : "trzy"
}.get(x, "domyślna")
```

Ta technika pozwala na skonfigurowanie mocka, aby zwracał różne odpowiedzi w zależności od argumentów, co jest przydatne w symulacji złożonych zachowań.

## Własne Walidatory Argumentów

```python
class MyValidator:
    def __eq__(self, other):
        return isinstance(other,int) and other> 0

# Użycie własnego walidatora
mock.assert_called_with(MyValidator(), ANY, None)
```

Tworzenie własnych klas z przeciążoną metodą `__eq__` pozwala na elastyczną walidację argumentów, wykraczającą poza proste porównanie wartości.

## Dekorator `@patch`

W języku Python, dekorator `@patch` jest jednym z najważniejszych elementów biblioteki `unittest.mock`, służącym do zastępowania rzeczywistych obiektów ich atrapami (mockami) podczas testowania. Przyjrzyjmy się, do czego dokładnie służy i jak działa.

## Główne zastosowanie dekoratora `@patch`

Dekorator `@patch` pozwala na tymczasowe zastąpienie rzeczywistego obiektu, funkcji, klasy lub metody w określonym module atrapą (mockiem) na czas wykonania testu. Jest to szczególnie przydatne, gdy testujemy kod, który:

1. Komunikuje się z zewnętrznymi serwisami (np. API)
2. Wykonuje operacje I/O (np. odczyt/zapis do plików)
3. Posiada złożone zależności, które chcemy odizolować
4. Ma zachowania niedeterministyczne (np. losowe wartości)

## Jak działa `@patch`

Dekorator `@patch` tymczasowo podmienia oryginalny obiekt na atrapy tylko podczas wykonywania funkcji lub metody, którą dekoruje. Po zakończeniu testu, automatycznie przywraca oryginalny obiekt.

```python
import unittest
from unittest.mock import patch
from my_moduleimport function_that_calls_external_api

class TestMyFunction(unittest.TestCase):

    @patch('my_module.external_api_call')
    def test_my_function(self, mock_api_call):
        # Konfiguracja atrapy
        mock_api_call.return_value ={"data": "testowe dane"}

        # Wywołanie testowanej funkcji
        result = function_that_calls_external_api()

        # Sprawdzenie czy funkcja wywołała zewnętrzne API
        mock_api_call.assert_called_once()

        # Sprawdzenie wyniku
        self.assertEqual(result,"oczekiwany wynik")
```
## Różne sposoby używania @patch

1. **Jako dekorator funkcji testowej** :
```python
    @patch('moduł.klasa_lub_funkcja')
    def test_something(self, mock_obj):
       # Test z użyciem mock_obj
```
2. **Wiele patchów na raz** :
```python
    @patch('moduł.funkcja1')
    @patch('moduł.funkcja2')
    def test_something(self, mock_func2, mock_func1):
       # Zauważ odwróconą kolejność parametrów (od dołu do góry)
```
3. **Jako kontekst (context manager)** :
```python
    def test_something(self):
       with patch('moduł.funkcja')as mock_func:
          # Test z użyciem mock_func
```
4. **Bezpośrednie wywołanie** :

```python
patcher = patch('moduł.funkcja')
mock_func = patcher.start()
# Test z użyciem mock_func
patcher.stop() # Należy pamiętać o zatrzymaniu patchera
```

5. **Patching metod obiektów** :
```python
    @patch.object(KlasaX, 'nazwa_metody')
    def test_something(self, mock_method):
       # Test z podmienioną metodą obiektu
```

## Kluczowe aspekty używania `@patch`

1. **Ścieżka importu ma znaczenie** :

    Zawsze określamy ścieżkę, z której obiekt jest importowany w testowanym kodzie, a nie gdzie jest definiowany.

```python
# Jeśli w testowanym pliku mamy:
frompakiet.moduł import funkcja

# To w teście używamy:
@patch('testowany_plik.funkcja') # a NIE 'pakiet.moduł.funkcja'
```

2. **Konfiguracja zachowania atrap** :
```python
# Ustawienie wartości zwracanej
mock_func.return_value= "wynik"

# Ustawienie wyjątku
mock_func.side_effect =Exception("Błąd")

# Dynamiczne zachowanie
mock_func.side_effect =[ 1 , 2 , 3 ] # Kolejne wartości przy kolejnych wywołaniach
```

3. **Weryfikacja wywołań** :

```python
# Sprawdzenie czy funkcja została wywołana
mock_func.assert_called()

# Sprawdzenie czy funkcja została wywołana dokładnie raz
mock_func.assert_called_once()

# Sprawdzenie czy funkcja została wywołana z określonymi argumentami
mock_func.assert_called_with(arg1, arg2)
```

## Przykład:


```python
# weather.py
import requests

def get_weather(city):
    url = f"https://api.weather.com/current?city={city}"
    response =requests.get(url)
    if response.status_code== 200 :
        data =response.json()
        return f"Pogoda w {city}:{data['temperature']}°C, {data['conditions']}"
    return f"Nie udało się pobrać pogody dla {city}"

def display_weather(city):
    weather_info =get_weather(city)
    print(weather_info)
    return weather_info
```

Test z użyciem `@patch`:

```python
import unittest
from unittest.mock import patch, MagicMock
from weather import display_weather

class TestWeather(unittest.TestCase):

    @patch('weather.get_weather')
    def test_display_weather(self, mock_get_weather):
        # Konfiguracja atrapy
        mock_get_weather.return_value = "Pogoda w Warszawa: 22°C, słonecznie"

        # Wywołanie testowanej funkcji
        result = display_weather("Warszawa")

        # Weryfikacja, że nasza funkcja get_weather została wywołana z odpowiednim argumentem
        mock_get_weather.assert_called_once_with("Warszawa")


        # Weryfikacja wyniku
        self.assertEqual(result,"Pogoda w Warszawa: 22°C, słonecznie")


    @patch('weather.requests.get')
    def test_get_weather_directly(self, mock_requests_get):
        # Konfiguracja atrapy odpowiedzi HTTP
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value ={
            "temperature": 22 ,
            "conditions":"słonecznie"
        }
        mock_requests_get.return_value =mock_response

        # Teraz możemy testować get_weather bezpośrednio
        from weather import get_weather
        result = get_weather("Warszawa")

        # Weryfikacja
        self.assertEqual(result,"Pogoda w Warszawa: 22°C, słonecznie")
        mock_requests_get.assert_called_once()
```

# Zadania

## `Mock` jako atrapy obiektów

1.Wykonaj poniższe czynności:
- Utwórz obiekt Mock i nadaj mu nazwę
- Ustaw wartość zwracaną dla metody `get_data`
- Wywołaj metodęget_dataz argumentem `user`
- Sprawdź czy metoda została wywołana używając `assert_called_with`
- Sprawdź argumenty wywołania używając atrybutu `call_args`

2.Wykonaj poniższe czynności:
- Utwórz obiekt Mock z automatyczną specyfikacją (`autospec=True`)
- Ustaw różne wartości zwracane dla kolejnych wywołań tej samej metody
- Skonfiguruj efekt uboczny dla wywołania metody używając `side_effect`
- Ustaw `side_effect` jako funkcję, która modyfikuje argumenty
- Skonfiguruj `Mock`, aby rzucał wyjątek

3.Wykonaj poniższe czynności:
- Przeanalizuj atrybuty `called`, `call_count`, `call_args` i `call_args_list`
- Utwórz `Mock` i wykonaj kilka wywołań z różnymi argumentami
- Sprawdź liczbę wywołań za pomocą `call_count`
- Sprawdź listę wszystkich argumentów wywołań poprzez `call_args_list`
- Zbadaj strukturę obiektu `call_args`

4.Wykonaj poniższe czynności:
- Utwórz obiekt `MagicMock`
- Skonfiguruj zachowanie dla metod specjalnych jak `__len__`, `__add__`, `__getitem__`
- Sprawdź różnice w zachowaniu domyślnym między `Mock` a `MagicMock`
- Zaimplementuj zachowanie metody `__str__` dla `MagicMock`
- Użyj `MagicMock` jako kontekstu menedżera (`with` statement)


5.Wykonaj poniższe czynności:
- Skonfiguruj `Mock`, aby zwracał różne wartości dla różnych argumentów
- Użyj `return_value` oraz `side_effect` jednocześnie i zbadaj priorytet
- Skonfiguruj zagnieżdżone mocki (`mock.attribute.method`)
- Ustaw specyficzne wartości zwracane dla metod zagnieżdżonych
- Użyj `configure_mock()` do konfiguracji wielu atrybutów naraz

6.Wykonaj poniższe czynności:
- Użyj metod `assert_called()`, `assert_called_once()`, `assert_not_called()`
- Wypróbuj `assert_called_with()` i `assert_called_once_with()`
- Sprawdź kolejność wywołań za pomocą `assert_has_calls()`
- Użyj parametru `any_order = True` w `assert_has_calls()`
- Zbadaj jak działają `mock_calls` oraz `method_calls`

7.Wykonaj poniższe czynności:
- Zaimportuj `ANY` z `unittest.mock`
- Użyj `ANY` w asercjach do ignorowania wartości konkretnego argumentu
- Stwórz złożone wywołanie z kilkoma argumentami i sprawdź je używając `ANY`
- Zbadaj, jak `ANY` działa z różnymi typami danych
- Porównaj zachowanie `ANY` z własnym walidatorem argumentów

8.Wykonaj poniższe czynności:
- Wywołaj kilka metod na obiekcie `Mock`
- Użyj `reset_mock()` do zresetowania historii wywołań
- Porównaj stan przed i po resetowaniu
- Sprawdź działanie `reset_mock(return_value=False)`
- Zbadaj jak zachowują się zagnieżdżone mocki po resetowaniu

9.Wykonaj poniższe czynności:
- Utwórz obiekt `call` z argumentami
- Porównaj obiekty `call` z faktycznymi wywołaniami
- Użyj `call.call_list()` do utworzenia listy oczekiwanych wywołań
- Zbadaj strukturę obiektu `call`
- Sprawdź działanie `call` z argumentami pozycyjnymi i nazwanymi


## Mocki i testy

10. Zaimplementuj klasę `DataService`, która zawiera metodę `fetch_user_data` pobierającą dane użytkownika. Następnie napisz kompletny test jednostkowy przy użyciu `unittest`, który:
- Utworzy mock dla zewnętrznego API używanego przez `DataService(api_mock =
Mock())`
- Skonfiguruje różne wartości zwracane dla kolejnych wywołań metody `get_data` mocka `(api_mock.get_data.side_effect = [{'name': 'Jan'}, {'name': 'Anna'}])`
- Skonfiguruje efekt uboczny używając `side_effect`, który będzie rzucał wyjątek `ConnectionError` przy trzecim wywołaniu `(api_mock.get_data.side_effect = [{'data': 'value1'}, {'data': 'value2'}, ConnectionError(), {'data': 'value4'}])`
- Sprawdzi, czy metoda `fetch_user_data` przekazuje odpowiednie parametry do metody `get_data(api_mock.get_data.assert_called_with(user_id=123, details=True))`
- Zweryfikuje liczbę wywołań przy użyciucall_countoraz argumenty wszystkich wywołań używając `call_args_list(self.assertEqual(api_mock.get_data.call_count, 4)` oraz `calls = api_mock.get_data.call_args_list` z weryfikacją `calls[0][1]['user_id']`)

Klasa powinna implementować także mechanizm ponawiania prób w przypadku błędów połączenia. Napisz testy, które sprawdzą, czy mechanizm ponawiania działa poprawnie (poprzez weryfikację, że po wystąpieniu `ConnectionError` metoda zostaje wywołana ponownie określoną liczbę razy lub że zwracana jest odpowiednia wartość po udanym ponowieniu).

11. Zaimplementuj funkcję `generate_unique_filename()`, która generuje unikalną nazwę pliku bazując na aktualnym czasie (wykorzystuje wewnętrznie modułdatetime). Funkcja powinna zwracać nazwę w formacie `file_YYYYMMDD_HHMMSS.txt`.

Napisz testy jednostkowe dla tej funkcji, używając dekoratora `@patch` z modułu `unittest.mock`, aby zastąpić rzeczywisty czas systemowy ustalonym czasem testowym. Dzięki temu będziesz w stanie przewidzieć dokładny rezultat funkcji.

W testach: 
- Użyj dekoratora `@patch` do zastąpienia funkcji `datetime.now()`
- Sprawdź, czy generowana nazwa pliku ma prawidłowy format
- Sprawdź, czy przy dwóch różnych ustalonych czasach funkcja generuje różne nazwy plików
- Zweryfikuj, czy funkcja poprawnie obsługuje różne strefy czasowe

Zaimplementuj funkcję `generate_unique_filename()` oraz odpowiednie testy jednostkowe z wykorzystaniem dekoratora `@patch`.

12. Stwórz klasę `WeatherService`, która będzie zawierała metodę `get_current_temperature(city)` pobierającą aktualną temperaturę dla podanego miasta z zewnętrznego API. Następnie napisz testy jednostkowe za pomocą biblioteki `unittest`, gdzie użyjesz mocków do zasymulowania odpowiedzi z API.

W testach: 
- Zasymuluj poprawną odpowiedź z API (kod 200) zwracającą temperaturę 25°C
- Zasymuluj błędną odpowiedź z API (kod 404) i sprawdź, czy funkcja odpowiednio obsługuje taki przypadek 
- Zasymuluj timeout połączenia i sprawdź obsługę tego wyjątku

Zaimplementuj klasę `WeatherService` oraz odpowiednie testy jednostkowe, używając biblioteki unittest i mechanizmu mocków.

13. Zaimplementuj klasę `DataContainer`, która zachowuje się jak specjalny kontener danych z możliwością:
- dodawania elementów (przeciążenie operatora `+=`)
- pobierania elementu po indeksie lub kluczu (implementacja `__getitem__`)
- reprezentacji tekstowej zawartości (implementacja `__str__`)
- określenia długości (implementacja `__len__`)
- użycia jako menadżera kontekstu (implementacje `__enter__` i `__exit__`)

Następnie napisz testy jednostkowe przy użyciu unittest, które:
- Będą używać `MagicMock` do testowania wszystkich metod specjalnych
- Sprawdzą, czy kolekcja zdarzeń jest prawidłowo rejestrowana (w tym kolejność wywołań)
- Przetestują obsługę wyjątków w kontekściewith
- Porównają zachowanie `Mock` i `MagicMock` dla metod specjalnych
- Przetestują wewnętrzne metody pomocnicze używając asercji: `assert_called_with`, `assert_has_calls` z różnymi kombinacjami `any_order`

Napisz także przypadek testowy dla wyjątkowych sytuacji, np. próba dostępu do nieistniejącego klucza lub elementu poza zakresem.