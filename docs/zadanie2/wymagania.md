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

| Kod        | Wymaganie funkcjonalne                                                       | Priorytet |
|------------|------------------------------------------------------------------------------|-----------|
| SPI-FR-001 | System musi umożliwiać otwarcie modułu Śpiewnik z dashboardu.                | M         |
| SPI-FR-002 | System musi wyświetlać listę kategorii piosenek.                             | M         |
| SPI-FR-003 | System musi udostępniać wyszukiwarkę piosenek.                               | M         |
| SPI-FR-004 | System musi wyświetlać listę piosenek przypisanych do wybranej kategorii.    | M         |
| SPI-FR-005 | System musi prezentować tekst piosenki wraz z akordami.                      | M         |
| SPI-FR-006 | System musi umożliwiać przejście do następnej piosenki w obrębie kategorii.  | S         |
| SPI-FR-007 | System musi umożliwiać zwijanie i rozwijanie list piosenek w kategorii.      | S         |
| SPI-FR-008 | System musi umożliwiać powrót do dashboardu.                                 | M         |
| SPI-FR-009 | System musi udostępniać wyszukiwanie zaawansowane po tytule.                 | S         |
| SPI-FR-010 | System musi udostępniać wyszukiwanie po fragmencie tekstu.                   | S         |
| SPI-FR-011 | System musi udostępniać wyszukiwanie po pierwszym akordzie.                  | S         |
| SPI-FR-012 | System musi udostępniać wyszukiwanie po sekwencji akordów.                   | S         |
| SPI-FR-013 | System musi grupować wyniki wyszukiwania według kategorii.                   | M         |
| SPI-FR-014 | System musi udostępniać tryb Focus dla muzyków.                              | M         |
| SPI-FR-015 | System musi umożliwiać wyświetlanie jednej lub dwóch zwrotek w trybie Focus. | M         |
| SPI-FR-016 | System musi umożliwiać zmianę kolorystyki akordów w trybie Focus.            | M         |
| SPI-FR-017 | System musi umożliwiać nawigację między zwrotkami.                           | M         |

### IDG - Interaktywne drzewo genealogiczne

| Kod        | Wymaganie funkcjonalne                                                                        | Priorytet |
|------------|-----------------------------------------------------------------------------------------------|-----------|
| IDG-FR-001 | System musi wyświetlać interaktywne drzewo genealogiczne.                                     | M         |
| IDG-FR-002 | System musi umożliwiać filtrowanie danych drzewa.                                             | M         |
| IDG-FR-003 | System musi umożliwiać kolorowanie węzłów według wybranego kryterium.                         | S         |
| IDG-FR-004 | System musi umożliwiać aktywację dodatkowych widoków drzewa.                                  | S         |
| IDG-FR-005 | System musi obsługiwać zoom oraz przewijanie drzewa.                                          | M         |
| IDG-FR-006 | System musi otwierać biografię osoby po kliknięciu węzła.                                     | M         |
| IDG-FR-007 | System musi podświetlać węzeł po najechaniu kursorem.                                         | S         |
| IDG-FR-008 | System musi umożliwiać zaznaczanie pojedynczych węzłów.                                       | M         |
| IDG-FR-009 | System musi umożliwiać zaznaczanie ścieżki pomiędzy dwoma węzłami przy użyciu klawisza Shift. | S         |
| IDG-FR-010 | System musi udostępniać funkcje Cofnij i Ponów dla zaznaczeń.                                 | S         |
| IDG-FR-011 | System musi umożliwiać kolorowanie zaznaczonych węzłów.                                       | C         |
| IDG-FR-012 | System musi umożliwiać utworzenie nowego drzewa na podstawie zaznaczenia.                     | S         |
| IDG-FR-013 | System musi umożliwiać nadanie nazwy nowemu drzewu.                                           | S         |
| IDG-FR-014 | System musi umożliwiać dodawanie węzłów do istniejącego drzewa użytkownika.                   | C         |
| IDG-FR-015 | System musi umożliwiać usuwanie węzłów z drzewa użytkownika.                                  | C         |
| IDG-FR-016 | System musi umożliwiać eksport drzewa do pliku PNG.                                           | M         |
| IDG-FR-017 | System musi umożliwiać zapisanie pliku eksportu pod wskazaną nazwą.                           | M         |
| IDG-FR-018 | System musi umożliwiać wyświetlenie uproszczonego drzewa z poziomu biografii członka.         | M         |

### KOD - Kodeks

| Kod        | Wymaganie funkcjonalne                                                | Priorytet |
|------------|-----------------------------------------------------------------------|-----------|
| KOD-FR-001 | System musi udostępniać sekcję „Prawa i obowiązki”.                   | M         |
| KOD-FR-002 | System musi udostępniać sekcję „Zasady wydarzeń”.                     | M         |
| KOD-FR-003 | System musi udostępniać sekcję „Tradycje”.                            | M         |
| KOD-FR-004 | System musi udostępniać sekcję „Księga znaku”.                        | M         |
| KOD-FR-005 | System musi wyświetlać treść sekcji w postaci rozwijalnych kategorii. | M         |
| KOD-FR-006 | System musi umożliwiać powrót do dashboardu.                          | M         |

### MAP - Mapa

| Kod        | Wymaganie funkcjonalne                                                                         | Priorytet |
|------------|------------------------------------------------------------------------------------------------|-----------|
| MAP-FR-001 | System musi wyświetlać mapę świata z markerami miejsc.                                         | M         |
| MAP-FR-002 | System musi obsługiwać zoom i przewijanie mapy.                                                | M         |
| MAP-FR-003 | System musi wyświetlać tooltip zawierający nazwę, typ i adres miejsca.                         | M         |
| MAP-FR-004 | System musi informować o trwałym zamknięciu miejsca.                                           | S         |
| MAP-FR-005 | System musi wyświetlać wzmianki o miejscu z Kroniki po kliknięciu markera.                     | M         |
| MAP-FR-006 | System musi umożliwiać filtrowanie miejsc według typu.                                         | M         |
| MAP-FR-007 | System musi umożliwiać filtrowanie miejsc zamkniętych na stałe.                                | S         |
| MAP-FR-008 | System musi aktualizować mapę zgodnie z aktywnymi filtrami.                                    | M         |
| MAP-FR-009 | System musi wspierać funkcje mapowe dostawcy map (np. Street View).                            | S         |
| MAP-FR-010 | System mobilny musi wyświetlać wskaźnik kierunku zgodny z orientacją urządzenia.               | S         |
| MAP-FR-011 | System mobilny musi umożliwiać włączenie i wyłączenie Kompasu Nawojkowego.                     | C         |
| MAP-FR-012 | System musi umożliwiać analizę miejsc pod kątem organizacji wydarzeń.                          | M         |
| MAP-FR-013 | System musi rekomendować najlepsze lokalizacje wydarzeń na podstawie zdefiniowanych kryteriów. | M         |
| MAP-FR-014 | System musi umożliwiać filtrowanie rekomendowanych lokalizacji.                                | S         |
| MAP-FR-015 | System musi rekomendować lokalizacje na afterparty.                                            | S         |
| MAP-FR-016 | System musi umożliwiać edycję danych miejsc przez Kasztelana.                                  | M         |
| MAP-FR-017 | System musi rejestrować zmiany miejsc na Osi Czasu.                                            | M         |

### KAL - Kalendarz

| Kod        | Wymaganie funkcjonalne                                                                                                                                | Priorytet |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| KAL-FR-001 | System musi umożliwiać otwarcie modułu „Kalendarz” z dashboardu.                                                                                      | M         |
| KAL-FR-002 | System musi wyświetlać kalendarz wydarzeń Bractwa.                                                                                                    | M         |
| KAL-FR-003 | System musi prezentować szczegóły wydarzenia obejmujące nazwę, datę rozpoczęcia, datę zakończenia, miejsce oraz typ wydarzenia.                       | M         |
| KAL-FR-004 | System musi wyświetlać listę uczestników dla zakończonych wydarzeń.                                                                                   | S         |
| KAL-FR-005 | System musi umożliwiać subskrypcję kalendarza Bractwa w Google Calendar.                                                                              | S         |
| KAL-FR-006 | System musi umożliwiać powrót do dashboardu.                                                                                                          | M         |
| KAL-FR-007 | System musi umożliwiać Sekretarzowi otwarcie modułu „Edytuj kalendarz” z Panelu Sekretarza.                                                           | M         |
| KAL-FR-008 | System musi umożliwiać dodawanie nowych wydarzeń do kalendarza.                                                                                       | M         |
| KAL-FR-009 | System musi umożliwiać określenie tytułu, daty rozpoczęcia, daty zakończenia, miejsca, typu wydarzenia oraz uczestników podczas tworzenia wydarzenia. | M         |
| KAL-FR-010 | System musi umożliwiać edycję istniejących wydarzeń.                                                                                                  | M         |
| KAL-FR-011 | System musi rejestrować utworzenie wydarzenia na Osi Czasu w Centrum Zarządzania.                                                                     | M         |
| KAL-FR-012 | System musi rejestrować edycję wydarzenia na Osi Czasu w Centrum Zarządzania.                                                                         | M         |
| KAL-FR-013 | System musi umożliwiać powrót z modułu „Edytuj kalendarz” do Centrum Zarządzania.                                                                     | M         |

### KRO - Kronika

| Kod        | Wymaganie funkcjonalne                                                          | Priorytet |
|------------|---------------------------------------------------------------------------------|-----------|
| KRO-FR-001 | System musi prezentować dane w strukturze kategorii i podkategorii.             | M         |
| KRO-FR-002 | System musi umożliwiać rozwijanie i zwijanie sekcji.                            | M         |
| KRO-FR-003 | System musi udostępniać wyszukiwanie pełnotekstowe.                             | M         |
| KRO-FR-004 | System musi podświetlać dopasowania dokładne.                                   | M         |
| KRO-FR-005 | System musi oznaczać dopasowania kontekstowe odmiennym kolorem.                 | S         |
| KRO-FR-006 | System musi udostępniać wyszukiwanie zaawansowane.                              | S         |
| KRO-FR-007 | System musi prezentować wyniki wyszukiwania zaawansowanego w tabeli.            | S         |
| KRO-FR-008 | System musi umożliwiać filtrowanie kolumn w trybie włączającym i wykluczającym. | S         |

### ENC - Encyklopedia

| Kod        | Wymaganie funkcjonalne                                      | Priorytet |
|------------|-------------------------------------------------------------|-----------|
| ENC-FR-001 | System musi wyświetlać pojęcia pogrupowane alfabetycznie.   | M         |
| ENC-FR-002 | System musi umożliwiać otwarcie artykułu encyklopedycznego. | M         |
| ENC-FR-003 | System musi wyświetlać treść artykułu.                      | M         |

### CYT - Cytaty

| Kod        | Wymaganie funkcjonalne                                       | Priorytet |
|------------|--------------------------------------------------------------|-----------|
| CYT-FR-001 | System musi wyświetlać cytaty pogrupowane według autorów.    | M         |
| CYT-FR-002 | System musi umożliwiać otwarcie szczegółów cytatu.           | M         |
| CYT-FR-003 | System musi prezentować autora i kontekst cytatu.            | M         |
| CYT-FR-004 | System musi umożliwiać przechodzenie do następnego cytatu.   | S         |
| CYT-FR-005 | System musi umożliwiać przechodzenie do poprzedniego cytatu. | S         |
| CYT-FR-006 | System musi udostępniać funkcję Cytat dnia.                  | S         |

### PIN - Piny belgijskie

| Kod        | Wymaganie funkcjonalne                                                      | Priorytet |
|------------|-----------------------------------------------------------------------------|-----------|
| PIN-FR-001 | System musi wyświetlać katalog pinów podzielony na kategorie.               | M         |
| PIN-FR-002 | System musi umożliwiać dodawanie pinów do koszyka.                          | M         |
| PIN-FR-003 | System musi prezentować opis pina po najechaniu kursorem.                   | S         |
| PIN-FR-004 | System musi umożliwiać zapisywanie zamówienia.                              | M         |
| PIN-FR-005 | System musi umożliwiać wysłanie zamówienia do Skarbnika.                    | M         |
| PIN-FR-006 | System musi umożliwiać aktualizację wcześniej wysłanego zamówienia.         | S         |
| PIN-FR-007 | System musi ograniczać możliwość modyfikacji zamówienia po upływie terminu. | M         |
| PIN-FR-008 | System musi umożliwiać Skarbnikowi otwarcie okresu zamówień.                | M         |
| PIN-FR-009 | System musi prezentować listę zamówień i status spłaty.                     | M         |
| PIN-FR-010 | System musi automatycznie tworzyć cel składkowy dla zamówień pinów.         | M         |
| PIN-FR-011 | System musi umożliwiać zmianę terminu spłaty.                               | M         |
| PIN-FR-012 | System musi wysyłać powiadomienia o zaległościach.                          | S         |
| PIN-FR-013 | System musi umożliwiać edycję katalogu pinów.                               | M         |
| PIN-FR-014 | System musi rejestrować działania na Osi Czasu.                             | M         |

### SKL - Składki

| Kod        | Wymaganie funkcjonalne                                                             | Priorytet |
|------------|------------------------------------------------------------------------------------|-----------|
| SKL-FR-001 | System musi wyświetlać cele składkowe użytkownika.                                 | M         |
| SKL-FR-002 | System musi prezentować postęp wpłat.                                              | M         |
| SKL-FR-003 | System musi wyświetlać kod przelewu dla celu składkowego.                          | M         |
| SKL-FR-004 | System musi umożliwiać deklarację dokonanej wpłaty.                                | M         |
| SKL-FR-005 | System musi powiadamiać Skarbnika o deklaracji wpłaty.                             | M         |
| SKL-FR-006 | System musi umożliwiać zarządzanie celami składkowymi przez Skarbnika.             | M         |
| SKL-FR-007 | System musi automatycznie aktualizować status wpłat na podstawie historii Skarbca. | M         |
| SKL-FR-008 | System musi generować pliki CSV do przypomnień zbiorczych.                         | S         |
| SKL-FR-009 | System musi umożliwiać wysyłanie przypomnień systemowych.                          | S         |
| SKL-FR-010 | System musi umożliwiać zamknięcie celu składkowego.                                | M         |

### PDZ - Plan działania

| Kod        | Wymaganie funkcjonalne                                                                                | Priorytet |
|------------|-------------------------------------------------------------------------------------------------------|-----------|
| PDZ-FR-001 | System musi umożliwiać otwarcie modułu „Plan działania” z Panelu Wielkiego Mistrza.                   | M         |
| PDZ-FR-002 | System musi wyświetlać listę zadań pogrupowanych według kadencji Zarządów.                            | M         |
| PDZ-FR-003 | System musi umożliwiać otwarcie szczegółów zadania.                                                   | M         |
| PDZ-FR-004 | System musi prezentować opis zadania.                                                                 | M         |
| PDZ-FR-005 | System musi prezentować termin realizacji zadania.                                                    | M         |
| PDZ-FR-006 | System musi prezentować listę kroków wymaganych do ukończenia zadania.                                | M         |
| PDZ-FR-007 | System musi umożliwiać oznaczenie zadania jako ukończone wyłącznie po spełnieniu wszystkich warunków. | M         |
| PDZ-FR-008 | System musi umożliwiać tworzenie nowych zadań.                                                        | M         |
| PDZ-FR-009 | System musi umożliwiać edycję istniejących zadań.                                                     | M         |
| PDZ-FR-010 | System musi rejestrować utworzenie zadania na Osi Czasu.                                              | M         |
| PDZ-FR-011 | System musi rejestrować modyfikację zadania na Osi Czasu.                                             | M         |
| PDZ-FR-012 | System musi umożliwiać powrót do Centrum Zarządzania.                                                 | M         |

### WOR - Wywiad organizacji

| Kod        | Wymaganie funkcjonalne                                                                       | Priorytet |
|------------|----------------------------------------------------------------------------------------------|-----------|
| WOR-FR-001 | System musi umożliwiać otwarcie modułu „Wywiad organizacji” z Panelu Wielkiego Mistrza.      | M         |
| WOR-FR-002 | System musi wyświetlać listę organizacji współpracujących lub kontaktujących się z Bractwem. | M         |
| WOR-FR-003 | System musi umożliwiać otwarcie karty organizacji.                                           | M         |
| WOR-FR-004 | System musi przechowywać nazwę organizacji.                                                  | M         |
| WOR-FR-005 | System musi przechowywać adresy e-mail organizacji.                                          | M         |
| WOR-FR-006 | System musi przechowywać obszar działalności organizacji.                                    | M         |
| WOR-FR-007 | System musi przechowywać informacje o aktualnym kierownictwie organizacji.                   | M         |
| WOR-FR-008 | System musi przechowywać rok założenia organizacji.                                          | S         |
| WOR-FR-009 | System musi przechowywać listę członków organizacji.                                         | S         |
| WOR-FR-010 | System musi przechowywać historię wspólnych wydarzeń.                                        | M         |
| WOR-FR-011 | System musi przechowywać opinie poprzednich Zarządów.                                        | M         |
| WOR-FR-012 | System musi umożliwiać dodawanie opinii przez aktualny Zarząd.                               | M         |
| WOR-FR-013 | System musi umożliwiać edycję danych organizacji.                                            | M         |
| WOR-FR-014 | System musi umożliwiać wyszukiwanie organizacji po dowolnym przechowywanym atrybucie.        | M         |
| WOR-FR-015 | System musi prezentować organizacje powiązane z wyszukiwaną frazą.                           | M         |
| WOR-FR-016 | System musi rejestrować utworzenie opinii na Osi Czasu.                                      | M         |
| WOR-FR-017 | System musi rejestrować modyfikację danych organizacji na Osi Czasu.                         | M         |
| WOR-FR-018 | System musi umożliwiać powrót do Centrum Zarządzania.                                        | M         |

### RSS - Rozporządzenia SSUJ

| Kod        | Wymaganie funkcjonalne                                                                    | Priorytet |
|------------|-------------------------------------------------------------------------------------------|-----------|
| RSS-FR-001 | System musi umożliwiać otwarcie modułu „Rozporządzenia SSUJ” z Panelu Kasztelana.         | M         |
| RSS-FR-002 | System musi wymagać uwierzytelnienia kontem Microsoft przed dostępem do dokumentów SSUJ.  | M         |
| RSS-FR-003 | System musi pobierać listę rozporządzeń SSUJ.                                             | M         |
| RSS-FR-004 | System musi dzielić rozporządzenia na sekcje „Przeczytane” i „Nieprzeczytane”.            | M         |
| RSS-FR-005 | System musi umożliwiać filtrowanie rozporządzeń według roku.                              | M         |
| RSS-FR-006 | System musi umożliwiać filtrowanie rozporządzeń według tematyki.                          | M         |
| RSS-FR-007 | System musi umożliwiać filtrowanie rozporządzeń według aktualności.                       | M         |
| RSS-FR-008 | System musi wyświetlać treść rozporządzenia.                                              | M         |
| RSS-FR-009 | System musi udostępniać formularz streszczenia rozporządzenia.                            | M         |
| RSS-FR-010 | System musi umożliwiać oznaczenie aktualności rozporządzenia.                             | M         |
| RSS-FR-011 | System musi wyszukiwać potencjalnie powiązane rozporządzenia.                             | S         |
| RSS-FR-012 | System musi prezentować szacowany czas potrzebny do weryfikacji powiązanych rozporządzeń. | C         |
| RSS-FR-013 | System musi umożliwiać oznaczanie rozporządzeń jako nieaktualnych.                        | M         |
| RSS-FR-014 | System musi prezentować streszczenia pozostawione przez poprzednich Kasztelanów.          | S         |
| RSS-FR-015 | System musi rejestrować zmiany aktualności dokumentów na Osi Czasu.                       | M         |
| RSS-FR-016 | System musi rejestrować dodanie lub zmianę streszczenia na Osi Czasu.                     | M         |
| RSS-FR-017 | System musi umożliwiać powrót do Centrum Zarządzania.                                     | M         |

### WNI - Wnioski

| Kod        | Wymaganie funkcjonalne                                                                   | Priorytet |
|------------|------------------------------------------------------------------------------------------|-----------|
| WNI-FR-001 | System musi umożliwiać otwarcie modułu „Wnioski” z Panelu Kasztelana.                    | M         |
| WNI-FR-002 | System musi wyświetlać listę wniosków.                                                   | M         |
| WNI-FR-003 | System musi umożliwiać sortowanie wniosków według daty złożenia.                         | M         |
| WNI-FR-004 | System musi umożliwiać sortowanie wniosków według daty ostatniej modyfikacji.            | M         |
| WNI-FR-005 | System musi umożliwiać grupowanie wniosków według statusu akceptacji.                    | M         |
| WNI-FR-006 | System musi umożliwiać otwarcie szczegółów wniosku.                                      | M         |
| WNI-FR-007 | System musi prezentować nazwę wniosku.                                                   | M         |
| WNI-FR-008 | System musi prezentować datę złożenia wniosku.                                           | M         |
| WNI-FR-009 | System musi prezentować datę ostatniej modyfikacji.                                      | M         |
| WNI-FR-010 | System musi prezentować status akceptacji przez SSUJ.                                    | M         |
| WNI-FR-011 | System musi prezentować podgląd dokumentu wniosku.                                       | M         |
| WNI-FR-012 | System musi umożliwiać utworzenie nowego wniosku na podstawie kopii istniejącego.        | M         |
| WNI-FR-013 | System musi umożliwiać edycję nazwy wniosku.                                             | M         |
| WNI-FR-014 | System musi umożliwiać edycję dat powiązanych z wnioskiem.                               | M         |
| WNI-FR-015 | System musi umożliwiać zmianę statusu akceptacji.                                        | M         |
| WNI-FR-016 | System musi umożliwiać wymianę załączonego dokumentu.                                    | M         |
| WNI-FR-017 | System musi automatycznie aktualizować datę ostatniej modyfikacji po zapisaniu zmian.    | M         |
| WNI-FR-018 | System musi automatycznie nadawać status „Czeka na akceptację” nowo utworzonym wnioskom. | M         |
| WNI-FR-019 | System musi rejestrować utworzenie wniosku na Osi Czasu.                                 | M         |
| WNI-FR-020 | System musi rejestrować edycję wniosku na Osi Czasu.                                     | M         |
| WNI-FR-021 | System musi umożliwiać powrót do Centrum Zarządzania.                                    | M         |

### SKA - Skarbiec

| Kod        | Wymaganie funkcjonalne                                                                        | Priorytet |
|------------|-----------------------------------------------------------------------------------------------|-----------|
| SKA-FR-001 | System musi umożliwiać otwarcie modułu „Skarbiec” z Panelu Skarbnika.                         | M         |
| SKA-FR-002 | System musi wyświetlać aktualne saldo konta.                                                  | M         |
| SKA-FR-003 | System musi wyświetlać numer rachunku bankowego.                                              | M         |
| SKA-FR-004 | System musi udostępniać historię transakcji.                                                  | M         |
| SKA-FR-005 | System musi udostępniać rejestr płatników.                                                    | M         |
| SKA-FR-006 | System musi udostępniać rejestr firm.                                                         | M         |
| SKA-FR-007 | System musi umożliwiać import historii transakcji z pliku CSV.                                | S         |
| SKA-FR-008 | System musi analizować zaimportowane transakcje.                                              | M         |
| SKA-FR-009 | System musi automatycznie identyfikować płatników na podstawie danych transakcji.             | M         |
| SKA-FR-010 | System musi automatycznie identyfikować firmy na podstawie danych transakcji.                 | M         |
| SKA-FR-011 | System musi umożliwiać ręczne przypisanie nierozpoznanej transakcji do istniejącego płatnika. | M         |
| SKA-FR-012 | System musi umożliwiać ręczne przypisanie nierozpoznanej transakcji do istniejącej firmy.     | M         |
| SKA-FR-013 | System musi umożliwiać utworzenie nowego płatnika podczas obsługi nierozpoznanej transakcji.  | M         |
| SKA-FR-014 | System musi umożliwiać utworzenie nowej firmy podczas obsługi nierozpoznanej transakcji.      | M         |
| SKA-FR-015 | System musi przechowywać historię transakcji wraz z saldem po każdej operacji.                | M         |
| SKA-FR-016 | System musi prezentować dane kontaktowe płatnika.                                             | M         |
| SKA-FR-017 | System musi umożliwiać edycję danych płatnika.                                                | M         |
| SKA-FR-018 | System musi prezentować dane kontaktowe i biznesowe firmy.                                    | S         |
| SKA-FR-019 | System musi umożliwiać edycję danych firmy.                                                   | M         |
| SKA-FR-020 | System musi rejestrować import historii transakcji na Osi Czasu.                              | M         |
| SKA-FR-021 | System musi rejestrować utworzenie lub edycję płatnika na Osi Czasu.                          | M         |
| SKA-FR-022 | System musi rejestrować utworzenie lub edycję firmy na Osi Czasu.                             | M         |
| SKA-FR-023 | System musi umożliwiać powrót do Centrum Zarządzania.                                         | M         |

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

