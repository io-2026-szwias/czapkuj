# Lista ryzyk

| ID    | Ryzyko                                     | Prawdopodobieństwo | Wpływ   | Działania zapobiegawcze                                          |
| ----- | ------------------------------------------ | ------------------ | ------- | ---------------------------------------------------------------- |
| R1-1  | Opóźnienia w konfiguracji repo             | Niskie             | Średnie | Utworzenie repo i testowe push/pull wcześniej                    |
| R1-2  | Niepełne przygotowanie analizy ryzyk       | Średnie            | Wysokie | Zaplanowanie dedykowanego czasu na analizę ryzyk                 |
| R1-3  | Samodzielna realizacja zwiększa obciążenie | Wysokie            | Wysokie | Dokładne planowanie każdego dnia, dzielenie zadań na małe kroki  |
| R1-4  | Awaria repo GitHub (utrata zmian)          | Niskie             | Wysokie | Regularne backupy lokalne                                        |
| R2-1  | Niejasne wymagania aplikacji               | Niskie             | Wysokie | Stworzenie listy funkcji i podstawowego backlogu                 |
| R2-2  | Zbyt duża liczba funkcji do jednej osoby   | Średnie            | Wysokie | Priorytetyzacja funkcji i ograniczenie MVP                       |
| R2-3  | Brak testów w trakcie analizy              | Wysokie            | Średnie | Przygotowanie prostych testów koncepcji przed implementacją      |
| R2-4  | Drobne błędy w dokumentacji                | Średnie            | Niskie  | Kontrola dokumentacji przy każdym commicie                       |
| R3-1  | Błędne diagramy UML                        | Niskie             | Średnie | Regularne sprawdzanie spójności diagramów z wymaganiami          |
| R3-2  | Nieprzewidziane zależności między modułami | Średnie            | Wysokie | Rozpisanie interfejsów i schematów modułów wcześniej             |
| R3-3  | Zbyt duża szczegółowość scenariuszy        | Wysokie            | Średnie | Ograniczenie scenariuszy do kluczowych przypadków                |
| R3-4  | Błędy w prostych diagramach UML            | Wysokie            | Niskie  | Sprawdzenie diagramów podczas implementacji                      |
| R4-1  | Niepoprawne użycie wzorców i SOLID         | Niskie             | Średnie | Testowe implementacje kluczowych modułów przed resztą kodu       |
| R4-2  | Złożoność projektu dla jednej osoby        | Średnie            | Wysokie | Dzielenie diagramów i funkcji na mniejsze kroki                  |
| R4-3  | Błędy w diagramach klas i sekwencji        | Wysokie            | Średnie | Weryfikacja diagramów podczas implementacji, dopasowanie do kodu |
| R4-4  | Nieistotne błędy w diagramach              | Niskie             | Niskie  | Szybka kontrola i poprawa, bez wpływu na projekt                 |
| R5-1  | Brak pokrycia testami jednostkowymi        | Niskie             | Wysokie | Systematyczne pisanie testów TDD                                 |
| R5-2  | Niepoprawne testy                          | Średnie            | Średnie | Weryfikacja testów w zespole                                     |
| R5-3  | Opóźnienia w konfiguracji GitHub Projects  | Wysokie            | Średnie | Wcześniejsze przygotowanie boardów i planowanie sprintów         |
| R5-4  | Literówki w dokumentacji testów            | Średnie            | Niskie  | Sprawdzanie dokumentacji przy każdym commicie                    |
| R6-1  | Niedoszacowanie czasu implementacji        | Niskie             | Wysokie | Podział zadań na mniejsze elementy i wyznaczenie priorytetów     |
| R6-2  | Problemy techniczne z technologią          | Średnie            | Średnie | Testy prototypów i dokumentacja wybranych technologii            |
| R6-3  | Problemy z integracją modułów              | Wysokie            | Wysokie | Częsta integracja i testy po kawałkach                           |
| R6-4  | Małe problemy techniczne                   | Wysokie            | Niskie  | Szybka naprawa i testowanie jednostkowe                          |
| R7-1  | Brak pokrycia testami funkcjonalnymi       | Niskie             | Wysokie | Regularne testowanie podczas sprintu                             |
| R7-2  | Nieprzewidziane błędy                      | Średnie            | Średnie | Rewizja kodu i testy regresji po każdej iteracji                 |
| R7-3  | Opóźnienia w integracji modułów            | Wysokie            | Wysokie | Planowanie sprintów i integracja na bieżąco                      |
| R7-4  | Drobnne błędy w testach                    | Średnie            | Niskie  | Szybkie poprawki i weryfikacja testów                            |
| R8-1  | Brak pełnej funkcjonalności w demo         | Niskie             | Wysokie | Sprawdzenie wszystkich modułów przed prezentacją                 |
| R8-2  | Nieczytelna prezentacja                    | Średnie            | Średnie | Przygotowanie slajdów i próba generalna                          |
| R8-3  | Opóźnienia w przygotowaniu raportu         | Wysokie            | Średnie | Rozpoczęcie pracy nad raportem wcześniej                         |
| R8-4  | Niezauważony drobny problem w demo         | Niskie             | Niskie  | Szybkie sprawdzenie przed prezentacją                            |
| R9-1  | Braki w dokumentacji kodu                  | Niskie             | Średnie | Systematyczne uzupełnianie dokumentacji                          |
| R9-2  | Niejasne komentarze w kodzie               | Średnie            | Średnie | Stosowanie standardów dokumentacji i sprawdzanie kodu            |
| R9-3  | Zbyt skomplikowane rozwiązania             | Wysokie            | Średnie | Upraszczanie implementacji i przeglądy kodu                      |
| R9-4  | Drobne błędy w dokumentacji                | Średnie            | Niskie  | Szybka korekta przy commicie                                     |
| R10-1 | Konflikty w repozytorium                   | Niskie             | Średnie | Regularne pull/merge i komunikacja w zespole                     |
| R10-2 | Niekompletne funkcje                       | Średnie            | Wysokie | Planowanie sprintów i priorytetyzacja zadań                      |
| R10-3 | Błędy w integracji                         | Wysokie            | Wysokie | Testowanie integracyjne co sprint i planowanie buforu czasowego  |
| R10-4 | Drobne konflikty w repo                    | Średnie            | Niskie  | Natychmiastowe rozwiązywanie konfliktów                          |
| R11-1 | Brak pokrycia testami funkcjonalnymi       | Niskie             | Wysokie | Tworzenie testów przypadków użycia równolegle z implementacją    |
| R11-2 | Niewystarczające testy regresji            | Średnie            | Średnie | Testy regresyjne po każdej iteracji i poprawki błędów            |
| R11-3 | Odkrycie poważnych błędów                  | Wysokie            | Wysokie | Ciągłe testowanie i naprawianie błędów na bieżąco                |
| R11-4 | Drobne błędy w testach regresji            | Średnie            | Niskie  | Szybkie poprawki i weryfikacja testów                            |
| R12-1 | Opóźnienia w przygotowaniu demo            | Niskie             | Wysokie | Wcześniejsze przygotowanie materiałów i testy funkcjonalności    |
| R12-2 | Nieczytelna prezentacja                    | Średnie            | Średnie | Próby generalne i przygotowanie slajdów                          |
| R12-3 | Niekompletna funkcjonalność w prezentacji  | Wysokie            | Wysokie | Testowanie wszystkich funkcji przed demo                         |
| R12-4 | Niezauważony drobny problem w prezentacji  | Niskie             | Niskie  | Szybka korekta przed prezentacją                                 |
