# Scenariusze przypadków użycia

## Funkcje członka

### UC-01 – Przeglądanie kalendarza wydarzeń

**Aktor:** Członek  
**Warunki początkowe:** Użytkownik jest zalogowany  
**Warunki końcowe:** Użytkownik widzi listę wydarzeń lub dodał kalendarz  
**Scenariusz główny:**
1. Użytkownik wybiera opcję „Kalendarz”
2. System wyświetla listę nadchodzących wydarzeń (KW-10)
3. Użytkownik wybiera opcję „Dodaj do Google Calendar”
4. System umożliwia subskrypcję kalendarza (KW-11)

### UC-02 – Sprawdzenie składek

**Aktor:** Członek  
**Warunki początkowe:** Użytkownik jest zalogowany  
**Warunki końcowe:** Użytkownik zna stan swoich płatności  
**Scenariusz główny:**
1. Użytkownik wybiera „Składki”
2. System wyświetla historię wpłat i zaległości (SK-10)

### UC-03 – Generowanie drzewa genealogicznego

**Aktor:** Członek  
**Warunki początkowe:** Dane członków istnieją w systemie  
**Warunki końcowe:** Wyświetlone drzewo genealogiczne  
**Scenariusz główny:**
1. Użytkownik wybiera „Drzewo genealogiczne”
2. System generuje drzewo na podstawie danych (**DG-10**)
3. Użytkownik może zastosować filtry (np. rocznik) (**DG-11**)  

**Scenariusz alternatywny:**
2a. Brak danych → system wyświetla komunikat

### UC-04 – Korzystanie z kompasu nawojkowego

**Aktor:** Członek  
**Warunki początkowe:** Użytkownik udostępnił lokalizację  
**Warunki końcowe:** Wyświetlony kierunek  
**Scenariusz główny:**
1. Użytkownik wybiera „Kompas nawojkowy”
2. System pobiera lokalizację użytkownika
3. System wyświetla kierunek przeciwny do D.S. Nawojka (**KN-10**)  

**Scenariusz alternatywny:**
2a. Brak zgody na lokalizację → system wyświetla komunikat

---

## Funkcje Skarbnika

### UC-05 – Import historii transakcji

**Aktor:** Skarbnik  
**Warunki początkowe:** Skarbnik posiada plik CSV  
**Warunki końcowe:** Dane zapisane w systemie  
**Scenariusz główny:**
1. Skarbnik wybiera „Import historii”
2. Przeciąga plik CSV
3. System przetwarza plik (SK-11)
4. System zapisuje dane (SK-12)  

**Scenariusz alternatywny:**
3a. Plik ma niepoprawny format → system wyświetla błąd

### UC-06 – Tworzenie celu składkowego

**Aktor:** Skarbnik  
**Warunki początkowe:** Skarbnik jest zalogowany  
**Warunki końcowe:** Cel zapisany w systemie  
**Scenariusz główny:**
1. Skarbnik wybiera „Cele składkowe”
2. Wprowadza dane celu (tytuł, kwota, termin, użytkownicy)
3. Zatwierdza
4. System zapisuje cel (SK-13)

### UC-07 – Wysyłanie przypomnienia o płatności

**Aktor:** Skarbnik  
**Warunki początkowe:** Istnieje cel składkowy  
**Warunki końcowe:** Wiadomości zostały wysłane  
**Scenariusz główny:**
1. Skarbnik wybiera cel
2. System wyświetla listę zalegających
3. Skarbnik klika „Wyślij przypomnienie”
4. System wysyła wiadomości (SK-14)

### UC-08 – Analiza danych w BI dla skarbnika

**Aktor:** Skarbnik  
**Warunki początkowe:** Skarbnik zalogowany w systemie  
**Warunki końcowe:** Skarbnik przegląda raporty dotyczące członków i organizacji  
**Scenariusz główny:**
1. Skarbnik wybiera opcję "BI" w "Panelu Skarbnika"
2. System prezentuje dostępne raporty i analizy
3. Skarbnik może filtrować dane według członków, organizacji i transakcji (**SB-1**)
4. Skarbnik przegląda wyniki i generuje potrzebne zestawienia

### UC-09 – Złożenie zamówienia pinów belgijskich przez skarbnika

**Aktor:** Skarbnik  
**Warunki początkowe:** Istnieją zamówienia od członków  
**Warunki końcowe:** Zamówienie zostało złożone u dostawcy  
**Scenariusz główny:**
1. Skarbnik wybiera „Skarbiec”
2. Wybiera sekcję „Piny belgijskie”
3. System wyświetla listę zamówień od członków
4. Skarbnik naciska „Złóż zamówienie”
5. System przekierowuje na stronę dostawcy
6. Skarbnik loguje się i opłaca zamówienie (**PB-0**)  

**Scenariusz alternatywny:**
5a. Błąd przekierowania → system wyświetla komunikat

---

## Funkcje Kandydatów

### UC-10 – Wyszukiwanie informacji

**Aktor:** Kandydat / Członek  
**Warunki początkowe:** Użytkownik jest zalogowany  
**Warunki końcowe:** Wyświetlone wyniki  
**Scenariusz główny:**
1. Użytkownik wpisuje frazę w wyszukiwarkę
2. System przeszukuje bazę danych (WY-10)
3. System wyświetla wyniki pogrupowane według kategorii (WY-11)

### UC-11 – Wyszukiwanie zaawansowane

**Aktor:** Kandydat / Członek  
**Warunki początkowe:** Wyniki wyszukiwania istnieją  
**Warunki końcowe:** Wyniki przefiltrowane  
**Scenariusz główny:**
1. Użytkownik wybiera „Wyszukiwanie zaawansowane”
2. System wyświetla strukturę danych
3. Użytkownik ustawia filtry
4. System filtruje wyniki (WY-12)

### UC-12 – Przeglądanie kodeksu przez kandydata

**Aktor:** Kandydat  
**Warunki początkowe:** Kandydat zalogowany w systemie  
**Warunki końcowe:** Kandydat zapoznał się z treścią kodeksu  
**Scenariusz główny:**
1. Kandydat wybiera opcję "Czapkopedia" z dashboardu
2. Wchodzi w sekcję "Kodeks"
3. System wyświetla aktualny kodeks zasad organizacji (**SB-0**)
4. Kandydat czyta i przegląda dokumenty

---

## Śpiewnik elektroniczny

### UC-13 – Korzystanie ze śpiewnika

**Aktor:** Muzyk  
**Warunki początkowe:** Użytkownik jest zalogowany  
**Warunki końcowe:** Wyświetlona piosenka  
**Scenariusz główny:**
1. Użytkownik wyszukuje piosenkę po tytule lub akordach (SP-10, SP-11)
2. System wyświetla piosenkę z wyróżnionymi akordami (SP-12)

### UC-14 – Tryb focus śpiewnika

**Aktor:** Muzyk  
**Warunki początkowe:** Otwarta piosenka  
**Warunki końcowe:** Wyświetlana jedna zwrotka  
**Scenariusz główny:**
1. Użytkownik włącza tryb focus
2. System wyświetla jedną zwrotkę
3. Użytkownik przechodzi do kolejnych fragmentów (SP-13)

### UC-15 – Edycja piosenki w śpiewniku

**Aktor:** Członek  
**Warunki początkowe:** Użytkownik jest zalogowany, piosenka istnieje  
**Warunki końcowe:** Zmiany zapisane lub przekazane do autoryzacji  
**Scenariusz główny:**
1. Użytkownik otwiera piosenkę
2. Wybiera opcję „Edytuj”
3. Wprowadza zmiany (tekst, akordy)
4. Wybiera „Przekaż do autoryzacji”
5. System zapisuje propozycję zmian (**SP-10**, **SP-12**)  

**Scenariusz alternatywny:**
4a. Użytkownik rezygnuje → zmiany nie są zapisywane

### UC-16 – Akceptacja zmian w śpiewniku

**Aktor:** Muzyk  
**Warunki początkowe:** Istnieją oczekujące zmiany  
**Warunki końcowe:** Zmiany zaakceptowane lub odrzucone  
**Scenariusz główny:**
1. Muzyk otwiera panel redakcji
2. System wyświetla listę zmian
3. Muzyk wybiera zmianę
4. Muzyk akceptuje lub odrzuca zmianę
5. System aktualizuje piosenkę (**SP-12**)  

**Scenariusz alternatywny:**
2a. Brak zmian → system wyświetla komunikat

### UC-17 – Tryb Cantandiego

**Aktor:** Muzyk  
**Warunki początkowe:** Piosenka jest otwarta  
**Warunki końcowe:** Akordy wyróżnione  
**Scenariusz główny:**
1. Użytkownik otwiera piosenkę
2. Włącza tryb „Cantandiego”
3. System wyróżnia akordy wizualnie (**SP-12**)

---

## Panel Wielkiego Mistrza

### UC-18 – Zarządzanie TODO

**Aktor:** Wielki Mistrz  
**Warunki początkowe:** Użytkownik jest zalogowany  
**Warunki końcowe:** Zadanie oznaczone jako wykonane  
**Scenariusz główny:**
1. Użytkownik otwiera listę zadań
2. System wyświetla zadania (WM-10)
3. Użytkownik sprawdza warunki
4. Użytkownik oznacza zadanie jako wykonane (WM-11)

### UC-19 – Sprawdzanie znajomości organizacji

**Aktor:** Wielki Mistrz  
**Warunki początkowe:** Dane istnieją w systemie  
**Warunki końcowe:** Wyświetlona relacja  
**Scenariusz główny:**
1. Użytkownik wybiera „Znajomości”
2. Wpisuje adres e-mail organizacji
3. System wyszukuje dane (**SB-12**)
4. System wyświetla relację z organizacją  

**Scenariusz alternatywny:**
3a. Brak wyników → system wyświetla komunikat

---

## Łatwiejsze wnioski

### UC-20 – Tworzenie wniosku

**Aktor:** Kasztelan  
**Warunki początkowe:** Użytkownik jest zalogowany  
**Warunki końcowe:** Wniosek zapisany  
**Scenariusz główny:**
1. Użytkownik wybiera „Nowy wniosek”
2. System wyświetla szablon wniosku
3. Użytkownik wypełnia dane
4. System zapisuje wniosek (WN-10)

### UC-21 – Przegląd najnowszych zarządzeń SSUJ

**Aktor:** Kasztelan  
**Warunki początkowe:** System ma dostęp do danych SSUJ  
**Warunki końcowe:** Wyświetlona lista zarządzeń  
**Scenariusz główny:**
1. Użytkownik wybiera „Zarządzenia”
2. System pobiera dane z dostępnych źródeł
3. System wyświetla listę zarządzeń (**WN-11**)  

**Scenariusz alternatywny:**
2a. Brak dostępu do danych → system wyświetla komunikat

---

## Mapa miejscówek

### UC-22 – Przegląd mapy miejscówek

**Aktor:** Kasztelan  
**Warunki początkowe:** Użytkownik jest zalogowany  
**Warunki końcowe:** Wyświetlona mapa z wynikami  
**Scenariusz główny:**
1. Użytkownik wybiera „Mapa miejscówek”
2. Ustawia filtry (typ miejsca, dystans)
3. System wyświetla miejsca na mapie (**MG-0**)  

**Scenariusz alternatywny:**
3a. Brak wyników → system wyświetla komunikat

### UC-23 – Przegląd zniżek

**Aktor:** Kasztelan  
**Warunki początkowe:** Dane o zniżkach istnieją  
**Warunki końcowe:** Wyświetlona lista miejsc  
**Scenariusz główny:**
1. Użytkownik wybiera „Mapa zniżek”
2. Wybiera dzień tygodnia
3. System wyświetla dostępne zniżki (**MG-1**)

## Aplikacja do zamówień pinów belgijskich

### UC-24 – Zamawianie pinów belgijskich
**Aktor:** Członek
**Warunki początkowe:** Lista pinów dostępna
**Warunki końcowe:** Zamówienie złożone
**Scenariusz główny:**
1. Użytkownik wybiera „Piny belgijskie”
2. Wybiera produkty (**PB-10**)
3. System oblicza koszt (**PB-11**)
4. Użytkownik zatwierdza zamówienie

**Scenariusz alternatywny:**
3a. Brak dostępnych pinów → system wyświetla komunikat
