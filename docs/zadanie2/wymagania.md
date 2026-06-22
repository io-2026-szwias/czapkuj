# WYMAGANIA

## Ograniczenia

**O-01 – Ograniczenia korespondencji z SSUJ**

System nie może umożliwiać oficjalnej korespondencji z SSUJ za pomocą maila organizacji, 
ponieważ SSUJ akceptuje wyłącznie wiadomości wysyłane z adresów w domenie uczelnianej.

**O-02 – Dostęp do danych historycznych**

System nie ma dostępu do wszystkich historycznych dokumentów organizacji znajdujących się na prywatnych dyskach członków 
i byłych zarządów. Dane te mogą zostać dodane do systemu wyłącznie ręcznie przez użytkowników.

**O-03 – Dane zewnętrzne SSUJ**

System może pobierać zarządzenia SSUJ tylko z publicznie dostępnych źródeł (np. strony internetowej SSUJ). 
Jeśli struktura strony się zmieni, funkcjonalność może przestać działać.

**O-04 – Dane bankowe**

System nie ma bezpośredniego dostępu do systemu bankowego i może przetwarzać historię transakcji wyłącznie na podstawie 
plików eksportowanych przez użytkownika (np. CSV).

## 4.4.2 Wymagania systemowe

**SYS-01 – Dostępność systemu**

System powinien być dostępny jako aplikacja webowa dostępna z poziomu przeglądarki internetowej.

**SYS-02 – Profile użytkowników**

System powinien obsługiwać co najmniej następujące role użytkowników:
- kandydat (bean)
- członek
- skarbnik
- kasztelan
- wielki mistrz
- muzyk

**SYS-03 – Liczba użytkowników**

System powinien obsługiwać co najmniej **200 użytkowników** jednocześnie zapisanych w bazie.

**SYS-04 – Przechowywanie danych**

System powinien przechowywać dane o:
- członkach organizacji
- wydarzeniach
- dokumentach
- transakcjach finansowych
- piosenkach w śpiewniku

**SYS-05 – Obsługiwane urządzenia**

System powinien działać na komputerach oraz urządzeniach mobilnych z przeglądarką internetową.

**SYS-06 – Integracje zewnętrzne**

System może integrować się z następującymi usługami:
- Facebook
- Google Calendar
- Google Drive

## 4.4.3 Wymagania funkcjonalne

### SPI - Śpiewnik

| Kod        | Wymaganie                                                                            | Priorytet |
|------------|--------------------------------------------------------------------------------------|-----------|
| SPI-FR-001 | System musi umożliwiać otwarcie modułu Śpiewnik z dashboardu.                        | M         |
| SPI-FR-002 | System musi wyświetlać listę kategorii piosenek.                                     | M         |
| SPI-FR-003 | System musi umożliwiać wyszukiwanie piosenek.                                        | S         |
| SPI-FR-004 | System musi wyświetlać listę piosenek przypisanych do wybranej kategorii.            | M         |
| SPI-FR-005 | System musi wyświetlać tekst piosenki wraz z akordami.                               | M         |
| SPI-FR-006 | System musi umożliwiać przechodzenie do następnej piosenki w obrębie kategorii.      | S         |
| SPI-FR-007 | System musi umożliwiać zwijanie i rozwijanie kategorii.                              | S         |
| SPI-FR-008 | System musi umożliwiać powrót do dashboardu.                                         | M         |
| SPI-FR-009 | System musi udostępniać zaawansowane wyszukiwanie po tytule.                         | C         |
| SPI-FR-010 | System musi udostępniać zaawansowane wyszukiwanie po fragmencie tekstu.              | C         |
| SPI-FR-011 | System musi udostępniać wyszukiwanie po pierwszym akordzie.                          | C         |
| SPI-FR-012 | System musi udostępniać wyszukiwanie po sekwencji akordów.                           | C         |
| SPI-FR-013 | System musi grupować wyniki wyszukiwania według kategorii.                           | S         |
| SPI-FR-014 | System musi udostępniać tryb Focus dla muzyków.                                      | S         |
| SPI-FR-015 | System musi umożliwiać wyświetlanie jednej lub dwóch zwrotek w trybie Focus.         | S         |
| SPI-FR-016 | System musi umożliwiać zmianę koloru prezentacji akordów.                            | C         |
| SPI-FR-017 | System musi umożliwiać nawigację pomiędzy zwrotkami gestami lub kliknięciami ekranu. | S         |

### IDG - Interaktywne drzewo genealogiczne

| Kod        | Wymaganie                                                                                     | Priorytet |
|------------|-----------------------------------------------------------------------------------------------|-----------|
| IDG-FR-001 | System musi umożliwiać otwarcie drzewa genealogicznego z dashboardu.                          | M         |
| IDG-FR-002 | System musi wyświetlać interaktywne drzewo genealogiczne.                                     | M         |
| IDG-FR-003 | System musi umożliwiać stosowanie filtrów drzewa.                                             | M         |
| IDG-FR-004 | System musi umożliwiać kolorowanie węzłów według wybranego kryterium.                         | S         |
| IDG-FR-005 | System musi umożliwiać aktywację dodatkowych widoków drzewa.                                  | S         |
| IDG-FR-006 | System musi obsługiwać zoomowanie drzewa.                                                     | M         |
| IDG-FR-007 | System musi obsługiwać przewijanie drzewa w pionie i poziomie.                                | M         |
| IDG-FR-008 | System musi wyświetlać biografię osoby po kliknięciu węzła.                                   | M         |
| IDG-FR-009 | System musi podświetlać węzeł po wskazaniu kursorem.                                          | S         |
| IDG-FR-010 | System musi umożliwiać zaznaczanie pojedynczych węzłów.                                       | S         |
| IDG-FR-011 | System musi umożliwiać zaznaczanie ścieżki pomiędzy dwoma węzłami przy użyciu klawisza Shift. | C         |
| IDG-FR-012 | System musi obsługiwać operacje Cofnij i Ponów dla zaznaczeń.                                 | S         |
| IDG-FR-013 | System musi umożliwiać kolorowanie zaznaczonych węzłów.                                       | C         |
| IDG-FR-014 | System musi umożliwiać drukowanie zaznaczeń.                                                  | C         |
| IDG-FR-015 | System musi umożliwiać tworzenie nowych drzew z zaznaczeń.                                    | C         |
| IDG-FR-016 | System musi umożliwiać dodawanie węzłów do istniejącego drzewa użytkownika.                   | C         |
| IDG-FR-017 | System musi umożliwiać usuwanie węzłów z drzewa użytkownika.                                  | C         |
| IDG-FR-018 | System musi umożliwiać eksport drzewa do pliku PNG.                                           | S         |
| IDG-FR-019 | System musi umożliwiać otwarcie drzewa z poziomu biografii członka.                           | S         |

### KOD - Kodeks

| Kod        | Wymaganie                                            | Priorytet |
|------------|------------------------------------------------------|-----------|
| KOD-FR-001 | System musi udostępniać moduł Kodeks.                | M         |
| KOD-FR-002 | System musi prezentować sekcję Prawa i obowiązki.    | M         |
| KOD-FR-003 | System musi prezentować sekcję Zasady wydarzeń.      | M         |
| KOD-FR-004 | System musi prezentować sekcję Tradycje.             | M         |
| KOD-FR-005 | System musi prezentować sekcję Księga znaku.         | M         |
| KOD-FR-006 | System musi obsługiwać rozwijanie i zwijanie sekcji. | S         |

### MAP - Mapa

| Kod        | Wymaganie                                                          | Priorytet |
|------------|--------------------------------------------------------------------|-----------|
| MAP-FR-001 | System musi wyświetlać mapę świata ze znacznikami miejsc.          | M         |
| MAP-FR-002 | System musi domyślnie wyśrodkowywać mapę na Polsce.                | S         |
| MAP-FR-003 | System musi obsługiwać przybliżanie, oddalanie i przewijanie mapy. | M         |
| MAP-FR-004 | System musi prezentować szczegóły miejsca po najechaniu kursorem.  | M         |
| MAP-FR-005 | System musi wyświetlać wzmianki z Kroniki po kliknięciu znacznika. | S         |
| MAP-FR-006 | System musi umożliwiać filtrowanie miejsc według typu.             | M         |
| MAP-FR-007 | System musi umożliwiać filtrowanie miejsc zamkniętych na stałe.    | S         |
| MAP-FR-008 | System musi aktualizować liczbę znaczników zgodnie z filtrami.     | M         |
| MAP-FR-009 | System mobilny musi wyświetlać wskaźnik kierunku urządzenia.       | S         |
| MAP-FR-010 | System mobilny musi udostępniać funkcję Kompas Nawojkowy.          | C         |

### KAL - Kalendarz

| Kod        | Wymaganie                                                                      | Priorytet |
|------------|--------------------------------------------------------------------------------|-----------|
| KAL-FR-001 | System musi wyświetlać kalendarz wydarzeń Bractwa.                             | M         |
| KAL-FR-002 | System musi prezentować szczegóły wydarzenia.                                  | M         |
| KAL-FR-003 | System musi prezentować listę uczestników dla wydarzeń zakończonych.           | S         |
| KAL-FR-004 | System musi umożliwiać integrację z Google Calendar.                           | S         |
| KAL-FR-005 | System musi umożliwiać dodanie kalendarza Bractwa do konta Google użytkownika. | S         |

### KRO - Kronika

| Kod        | Wymaganie                                                                 | Priorytet |
|------------|---------------------------------------------------------------------------|-----------|
| KRO-FR-001 | System musi prezentować sekcje tematyczne Kroniki.                        | M         |
| KRO-FR-002 | System musi obsługiwać wielopoziomową strukturę kategorii i podkategorii. | M         |
| KRO-FR-003 | System musi umożliwiać przeglądanie pozycji przypisanych do podkategorii. | M         |
| KRO-FR-004 | System musi umożliwiać wyszukiwanie pełnotekstowe.                        | M         |
| KRO-FR-005 | System musi wyróżniać dopasowania dokładne kolorem zielonym.              | S         |
| KRO-FR-006 | System musi wyróżniać dopasowania kontekstowe kolorem żółtym.             | S         |
| KRO-FR-007 | System musi udostępniać wyszukiwanie zaawansowane.                        | C         |
| KRO-FR-008 | System musi prezentować dane w formie tabelarycznej.                      | C         |
| KRO-FR-009 | System musi umożliwiać filtrowanie kolumn w trybie włączającym.           | C         |
| KRO-FR-010 | System musi umożliwiać filtrowanie kolumn w trybie wykluczającym.         | C         |

### ENC - Encyklopedia

| Kod        | Wymaganie                                                             | Priorytet |
|------------|-----------------------------------------------------------------------|-----------|
| ENC-FR-001 | System musi prezentować spis pojęć pogrupowanych alfabetycznie.       | M         |
| ENC-FR-002 | System musi umożliwiać wybór pojęcia.                                 | M         |
| ENC-FR-003 | System musi wyświetlać artykuł encyklopedyczny dla wybranego pojęcia. | M         |

### CYT - Cytaty

| Kod        | Wymaganie                                                    | Priorytet |
|------------|--------------------------------------------------------------|-----------|
| CYT-FR-001 | System musi wyświetlać cytaty pogrupowane według autorów.    | M         |
| CYT-FR-002 | System musi umożliwiać otwarcie szczegółów cytatu.           | M         |
| CYT-FR-003 | System musi prezentować autora i kontekst cytatu.            | M         |
| CYT-FR-004 | System musi umożliwiać przechodzenie do następnego cytatu.   | S         |
| CYT-FR-005 | System musi umożliwiać przechodzenie do poprzedniego cytatu. | S         |
| CYT-FR-006 | System musi prezentować Cytat Dnia.                          | C         |

### PIN - Piny belgijskie

| Kod        | Wymaganie                                                                        | Priorytet |
|------------|----------------------------------------------------------------------------------|-----------|
| PIN-FR-001 | System musi prezentować katalog pinów w formie kafelków.                         | M         |
| PIN-FR-002 | System musi prezentować nazwę, cenę i grafikę pina.                              | M         |
| PIN-FR-003 | System musi umożliwiać wybór ilości pinów.                                       | M         |
| PIN-FR-004 | System musi wyświetlać opis pina po najechaniu kursorem.                         | S         |
| PIN-FR-005 | System musi umożliwiać filtrowanie pinów według kategorii.                       | M         |
| PIN-FR-006 | System musi obsługiwać koszyk zakupowy.                                          | M         |
| PIN-FR-007 | System musi wyświetlać sumę zamówienia.                                          | M         |
| PIN-FR-008 | System musi umożliwiać wysłanie zamówienia do Skarbnika.                         | M         |
| PIN-FR-009 | System musi umożliwiać ponowne przesłanie zamówienia przed upływem limitu czasu. | S         |
| PIN-FR-010 | System musi prezentować licznik czasu na modyfikację zamówienia.                 | S         |

### SKL - Składki

| Kod        | Wymaganie                                                         | Priorytet |
|------------|-------------------------------------------------------------------|-----------|
| SKL-FR-001 | System musi prezentować cele składkowe przypisane do użytkownika. | M         |
| SKL-FR-002 | System musi prezentować postęp wpłat dla każdego celu.            | M         |
| SKL-FR-003 | System musi prezentować szczegóły celu składkowego.               | M         |
| SKL-FR-004 | System musi umożliwiać deklarowanie dokonanej wpłaty.             | M         |
| SKL-FR-005 | System musi przekazywać deklarację wpłaty do Skarbnika.           | M         |
| SKL-FR-006 | System musi aktualizować historię wpłat i postęp realizacji celu. | M         |


## 4.4.4 Wymagania niefunkcjonalne

**NFR-01 – Wydajność**

System powinien zwracać wyniki wyszukiwania w czasie krótszym niż **2 sekundy** dla bazy zawierającej do 10 000 rekordów.

**NFR-02 – Bezpieczeństwo danych**

Dane użytkowników muszą być przechowywane zgodnie z zasadami ochrony danych osobowych (RODO).

**NFR-03 – Dostępność**

System powinien być dostępny przez co najmniej **99% czasu w skali miesiąca**.

**NFR-04 – Kopie zapasowe**

System powinien wykonywać automatyczną kopię zapasową bazy danych co najmniej raz na dobę.

**NFR-05 – Responsywność**

Interfejs użytkownika powinien być dostosowany do ekranów komputerów i urządzeń mobilnych.

