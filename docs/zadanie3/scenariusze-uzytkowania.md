# Scenariusze przypadków użycia

---

## Hierarchia aktorów

```
Użytkownik
├── Odwiedzający
├── Posiadacz dashboardu
│   ├── Czapkowicz
│   ├── Członek Zarządu
│   │   ├── Wielki Mistrz
│   │   ├── Kasztelan
│   │   ├── Skarbnik
│   │   ├── Sekretarz
│   │   └── Cantandi
│   └── Moderator
└── Administrator
```

---

## OGÓLNODOSTĘPNE FUNKCJE STRONY

---

### UC-STR-01: Przeglądanie podstron serwisu

**Aktor:**

* Użytkownik

**Warunki początkowe:**

* Użytkownik nie musi być zalogowany.
* Użytkownik otwiera stronę czapkuj.pl.

**Warunki końcowe:**

* Użytkownik zapoznał się z treścią strony głównej lub przeszedł do wybranej podstrony.

**Scenariusz główny:**

1. Użytkownik otwiera stronę czapkuj.pl.
2. System wyświetla stronę główną zawierającą powitanie oraz opis celu serwisu.
3. Użytkownik wybiera ikonę menu (hamburger).
4. System wyświetla listę dostępnych podstron.
5. Użytkownik wybiera interesującą go podstronę.

**Scenariusze alternatywne:**

* A1. Użytkownik nie otwiera menu i pozostaje na stronie głównej.
* A2. Użytkownik zamyka stronę bez wykonywania dalszych działań.

---

### UC-STR-02: Zmiana trybu wyświetlania strony

**Aktor:**

* Użytkownik

**Warunki początkowe:**

* Użytkownik ma otwartą stronę czapkuj.pl lub którąś z jej podstron.

**Warunki końcowe:**

* Dostępne dla użytkownika funkcje zostały zmienione zgodnie z wybranym trybem wyświetlania strony.

**Scenariusz główny:**

1. Użytkownik wybiera ikonę trybu wyświetlania strony.
2. Użytkownik wybiera jedną z opcji.
3. Wygląd ikony się zmienia.

---

### UC-STR-03: Korzystanie z czatu

**Aktor:**

* Użytkownik

**Warunki początkowe:**

* Użytkownik znajduje się na dowolnej stronie serwisu.

**Warunki końcowe:**

* Rozmowa została zapisana w historii czatu.

**Scenariusz główny:**

1. Użytkownik wybiera ikonę czatu.
2. System sprawdza, czy użytkownik jest zalogowany.
3. W razie potrzeby system wyświetla ekran logowania.
4. Po zalogowaniu system otwiera okno czatu.
5. Użytkownik prowadzi rozmowę z moderatorem lub administratorem.
6. System zapisuje historię wiadomości.

**Scenariusze alternatywne:**

* A1. Użytkownik rezygnuje z logowania – czat nie zostaje uruchomiony.
* A2. Moderator jest niedostępny – system informuje o oczekiwaniu na odpowiedź.

---

### UC-STR-04: Zgłoszenie problemu ze stroną

**Aktor:**

* Użytkownik

**Warunki początkowe:**

* Użytkownik znajduje się na stronie serwisu.

**Warunki końcowe:**

* Zgłoszenie zostało zapisane.

**Scenariusz główny:**

1. Użytkownik wybiera ikonę „Zgłoś problem ze stroną”.
2. System wyświetla formularz zgłoszenia.
3. Użytkownik opisuje problem.
4. Użytkownik wysyła formularz.
5. System zapisuje zgłoszenie.

**Scenariusze alternatywne:**

* A1. Pole opisu pozostaje puste – system uniemożliwia wysłanie formularza.
* A2. Użytkownik rezygnuje z wysłania zgłoszenia.

---

### UC-STR-05: Wyświetlenie odnośników do mediów społecznościowych

**Aktor:**

* Użytkownik

**Warunki początkowe:**

* Użytkownik znajduje się na stronie serwisu.

**Warunki końcowe:**

* Wyświetlono odnośniki do oficjalnych profili Bractwa.

**Scenariusz główny:**

1. Użytkownik wybiera ikonę „Social media”.
2. System wyświetla odnośniki do oficjalnych profili Bractwa.

**Scenariusze alternatywne:**

* Brak.

---

### UC-STR-06: Dobrowolne wsparcie Bractwa

**Aktor:**

* Użytkownik

**Warunki początkowe:**

* Użytkownik znajduje się na stronie serwisu.

**Warunki końcowe:**

* Użytkownik otrzymał dane do wykonania przelewu.

**Scenariusz główny:**

1. Użytkownik wybiera ikonę „Postaw nam piwo”.
2. System wyświetla dane do przelewu umożliwiającego wsparcie Bractwa.

**Scenariusze alternatywne:**

* A1. Użytkownik zamyka okno bez wykonania dalszych działań.

---

### UC-STR-07: Przeglądanie kalendarza wydarzeń

**Aktor:**

* Użytkownik

**Warunki początkowe:**

* Użytkownik otworzył listę podstron.

**Warunki końcowe:**

* Użytkownik zapoznał się z kalendarzem wydarzeń.

**Scenariusz główny:**

1. Użytkownik otwiera podstronę „Kalendarz wydarzeń”.
2. System wyświetla kalendarz wydarzeń z widokiem bieżącego miesiąca.
3. System prezentuje przeszłe i nadchodzące wydarzenia Bractwa.
4. Użytkownik wybiera wydarzenie.
5. System prezentuje informacje dotyczące wydarzenia.

**Scenariusze alternatywne:**

* A1. W wybranym miesiącu nie ma żadnych wydarzeń – system wyświetla pusty kalendarz.
* A2. Użytkownik rezygnuje z wyboru wydarzenia.

---

### UC-STR-08: Dodanie kalendarza wydarzeń do Google Calendar

**Aktor:**

* Użytkownik

**Warunki początkowe:**

* Użytkownik ma otwarty kalendarz wydarzeń.

**Warunki końcowe:**

* Użytkownik dodał kalendarz wydarzeń do Kalendarza Google.

**Scenariusz główny:**

1. Użytkownik wybiera opcję dodania kalendarza do Kalendarza Google.
2. System przekierowuje użytkownika do procesu dodawania kalendarza.

**Scenariusze alternatywne:**

* A1. W wybranym miesiącu nie ma żadnych wydarzeń – system wyświetla pusty kalendarz.
* A2. Użytkownik rezygnuje z dodania kalendarza i wraca do przeglądania strony.

---

### UC-STR-09: Zgłoszenie chęci zamówienia własnej czapki

**Aktor:**

* Użytkownik

**Warunki początkowe:**

* Użytkownik znajduje się w sekcji „Sklep”.
* Użytkownik nie musi być zalogowany.

**Warunki końcowe:**

* Formularz został przesłany do Centrum Zarządzania.

**Scenariusz główny:**

1. Użytkownik wybiera opcję „Zamów własną czapkę!”.
2. System wyświetla ofertę oraz formularz uprawniający do uzyskania 50% zniżki.
3. Użytkownik uzupełnia wymagane dane.
4. Użytkownik zatwierdza formularz.
5. System zapisuje zgłoszenie.
6. System przesyła powiadomienie do Centrum Zarządzania.

**Scenariusze alternatywne:**

* A1. Użytkownik nie wypełni wszystkich wymaganych pól – system wyświetla komunikat o błędzie.
* A2. Użytkownik poda niepoprawny dane – system informuje o błędnym formacie.

---

### UC-STR-10: Przejście do sklepu z pinami belgijskimi

**Aktor:**

* Użytkownik

**Warunki początkowe:**

* Użytkownik znajduje się w sekcji „Sklep”.
* Użytkownik nie jest zalogowany.

**Warunki końcowe:**

* Użytkownik zostaje przekierowany do modułu sklepu.

**Scenariusz główny:**

1. Użytkownik wybiera opcję „Zamów piny belgijskie”.
2. System wyświetla ekran logowania Google.
3. Użytkownik loguje się.
4. System weryfikuje dane logowania.
5. System przekierowuje użytkownika do sklepu z pinami belgijskimi.

**Scenariusze alternatywne:**

* A1. Użytkownik anuluje logowanie – system wraca do strony sklepu.
* A2. Logowanie zakończy się niepowodzeniem – system wyświetla odpowiedni komunikat.

---

### UC-STR-11: Zamówienie pinów własnego projektu

**Aktor:**

* Użytkownik

**Warunki początkowe:**

* Użytkownik znajduje się w sekcji „Sklep”.
* Użytkownik posiada przygotowany plik PNG.

**Warunki końcowe:**

* Zamówienie zostało opłacone i przekazane do realizacji.

**Scenariusz główny:**

1. Użytkownik wybiera opcję „Zamów piny własnego projektu”.
2. System wyświetla instrukcję przygotowania projektu oraz formularz zamówienia.
3. Użytkownik przesyła plik PNG.
4. Użytkownik podaje liczbę zamawianych pinów.
5. System oblicza koszt realizacji zamówienia.
6. Użytkownik wybiera opcję „Złóż zamówienie”.
7. System przekierowuje użytkownika do płatności.
8. Użytkownik dokonuje płatności.
9. System potwierdza przyjęcie płatności.
10. System przesyła powiadomienie do Centrum Zarządzania.

**Scenariusze alternatywne:**

* A1. Przesłany plik ma niepoprawny format – system odrzuca plik.
* A2. Płatność nie powiedzie się lub zostanie anulowana – zamówienie nie zostaje przyjęte.
* A3. Użytkownik nie poda liczby pinów – system uniemożliwia złożenie zamówienia.

---

### UC-STR-12: Przeglądanie blogów i komentowanie wpisów

**Aktor:**

* Użytkownik

**Warunki początkowe:**

* Użytkownik otworzył podstronę „Blog”.

**Warunki końcowe:**

* Użytkownik przeczytał wpis lub dodał komentarz.

**Scenariusz główny:**

1. Użytkownik otwiera podstronę „Blog”.
2. System wyświetla listę dostępnych blogów.
3. Użytkownik wybiera blog.
4. System wyświetla wpisy.
5. Użytkownik czyta wpis.
6. Użytkownik dodaje komentarz.
7. System informuje, że komentarz oczekuje na akceptację moderatora.

**Scenariusze alternatywne:**

* A1. Użytkownik nie jest zalogowany – system uniemożliwia dodanie komentarza.
* A2. Użytkownik jedynie przegląda wpisy bez dodawania komentarza.

---

### UC-STR-13: Przeglądanie Czapkowego słowniczka

**Aktor:**

* Użytkownik

**Warunki początkowe:**

* Użytkownik znajduje się na stronie serwisu.
* Użytkownik nie musi być zalogowany.

**Warunki końcowe:**

* Użytkownik wyświetlił listę artykułów wybranej sekcji słowniczka.

**Scenariusz główny:**

1. Użytkownik otwiera podstronę „Czapkowy słowniczek”.
2. System wyświetla dostępne sekcje:

    * Czapkowe zwyczaje,
    * Czapkowy żargon,
    * Łacińskie zwroty,
    * Czapkowe cytaty,
    * Znane Czapki.
3. Użytkownik wybiera jedną z dostępnych sekcji.
4. System pobiera dane z odpowiedniego modułu.
5. System wyświetla listę artykułów powiązanych z wybraną sekcją.
6. Użytkownik wybiera artykuł do dalszego przeglądania.

**Scenariusze alternatywne:**

* A1. Wybrana sekcja nie zawiera żadnych artykułów – system wyświetla komunikat o braku dostępnych treści.
* A2. Wystąpi błąd podczas pobierania danych z odpowiedniego modułu – system wyświetla komunikat o niedostępności treści i umożliwia ponowienie próby.

---

## AKCJE KONT

---

### UC-12: Złożenie prośby o awans na Beana

**Aktor:**

* Odwiedzający

**Warunki początkowe:**

* Użytkownik posiada konto lub może się zalogować.
* Użytkownik znajduje się w trybie „Odwiedzający”.
* Użytkownik nie posiada statusu "Czapkowicz".

**Warunki końcowe:**

* Prośba o awans została przekazana moderatorom lub administratorom.

**Scenariusz główny:**

1. Użytkownik wybiera ikonę konta.
2. System wyświetla dostępne akcje.
3. Użytkownik wybiera opcję „Poproś o awans na beana”.
4. Jeżeli użytkownik nie jest zalogowany, system wyświetla ekran logowania.
5. Użytkownik loguje się.
6. System wyświetla formularz zawierający opis procedury awansu oraz pole do wprowadzenia 6-cyfrowego kodu.
7. Użytkownik wprowadza kod.
8. Użytkownik wybiera przycisk „Poproś o awans”.
9. System przesyła zgłoszenie do moderatorów i administratorów.
10. System informuje użytkownika o oczekiwaniu na decyzję moderatora.

**Scenariusze alternatywne:**

* A1. Użytkownik rezygnuje z logowania – proces zostaje przerwany.
* A2. Wprowadzony kod jest niepoprawny lub wygasł – system wyświetla komunikat o błędzie.
* A3. Użytkownik zamyka formularz bez jego wysłania.

---

### UC-13: Uzupełnienie danych do awansu

**Aktor:**

* Odwiedzający

**Warunki początkowe:**

* Prośba o awans została zaakceptowana.
* Użytkownik otrzymał powiadomienie z prośbą o uzupełnienie danych.

**Warunki końcowe:**

* Dane zostały przesłane moderatorom do weryfikacji.

**Scenariusz główny:**

1. Użytkownik otwiera powiadomienie.
2. System wyświetla formularz danych osobowych.
3. Użytkownik uzupełnia wymagane pola.
4. Użytkownik wskazuje pierwsze wydarzenie czapkowe.
5. Jeżeli wydarzenie znajduje się na liście, użytkownik wybiera je.
6. Użytkownik zatwierdza formularz.
7. System przesyła dane moderatorom.
8. System informuje użytkownika, że proces awansu oczekuje na zakończenie przez moderatorów.

**Scenariusze alternatywne:**

* A1. Wybranego wydarzenia nie ma na liście – system wyświetla formularz dodania nowego wydarzenia.
* A2. Użytkownik nie wypełni wszystkich wymaganych pól – system uniemożliwia wysłanie formularza.
* A3. Użytkownik rezygnuje z wypełniania formularza.

---

### UC-14: Uzupełnienie danych do bezpośredniego awansu na Członka

**Aktor:**

* Odwiedzający

**Warunki początkowe:**

* Prośba o awans została zaakceptowana.
* Użyty kod umożliwia bezpośredni awans na status „Członek”.

**Warunki końcowe:**

* Dane zostały przekazane moderatorom do zatwierdzenia.

**Scenariusz główny:**

1. System rozpoznaje rodzaj kodu awansu.
2. System wyświetla rozszerzony formularz.
3. Użytkownik uzupełnia wymagane informacje dotyczące swojej historii czapkowej.
4. Użytkownik zatwierdza formularz.
5. System przesyła dane moderatorom.
6. System informuje użytkownika o oczekiwaniu na zakończenie procesu awansu.

**Scenariusze alternatywne:**

* A1. Wymagana wartość nie znajduje się na liście – użytkownik wybiera opcję dodania nowej pozycji.
* A2. System wyświetla odpowiedni formularz zgłoszeniowy.
* A3. Zgłoszenie zostaje przekazane moderatorom do rozpatrzenia.
* A4. Użytkownik nie uzupełni wszystkich wymaganych pól – system blokuje wysłanie formularza.

---

### UC-15: Przeglądanie powiadomień

**Aktor:**

* Użytkownik

**Warunki początkowe:**

* Użytkownik jest zalogowany.

**Warunki końcowe:**

* Wybrane powiadomienie zostało oznaczone jako przeczytane.

**Scenariusz główny:**

1. Użytkownik wybiera ikonę konta.
2. System wyświetla listę dostępnych akcji.
3. Użytkownik wybiera opcję „Powiadomienia”.
4. System wyświetla listę powiadomień.
5. Nieprzeczytane powiadomienia są oznaczone ikoną wykrzyknika.
6. Użytkownik otwiera wybrane powiadomienie.
7. System wyświetla pełną treść.
8. Użytkownik wybiera opcję „Oznacz jako przeczytane”.
9. System oznacza powiadomienie jako przeczytane.
10. Użytkownik wraca do listy powiadomień.

**Scenariusze alternatywne:**

* A1. Użytkownik nie posiada żadnych powiadomień – system wyświetla odpowiedni komunikat.
* A2. Użytkownik zamyka powiadomienie bez oznaczania go jako przeczytanego.

---

### UC-16: Logowanie i rejestracja

**Aktor:**

* Użytkownik

**Warunki początkowe:**

* Użytkownik nie jest zalogowany.

**Warunki końcowe:**

* Użytkownik został zalogowany do systemu.

**Scenariusz główny:**

1. Użytkownik wybiera ikonę konta.
2. System wyświetla opcję „Zaloguj/zarejestruj”.
3. Użytkownik wybiera tę opcję.
4. System uruchamia proces logowania za pomocą konta Google.
5. Użytkownik uwierzytelnia się.
6. System loguje użytkownika.

**Scenariusze alternatywne:**

* A1. Użytkownik anuluje logowanie.
* A2. Logowanie zakończy się niepowodzeniem – system wyświetla komunikat o błędzie.

---

### UC-17: Wylogowanie

**Aktor:**

* Użytkownik

**Warunki początkowe:**

* Użytkownik jest zalogowany.

**Warunki końcowe:**

* Użytkownik został wylogowany.

**Scenariusz główny:**

1. Użytkownik wybiera ikonę konta.
2. System wyświetla dostępne akcje.
3. Użytkownik wybiera opcję „Wyloguj”.
4. System kończy sesję użytkownika.
5. System przełącza stronę do trybu „Odwiedzający”.

**Scenariusze alternatywne:**

* Brak.

---

### UC-18: Zmiana trybu wyświetlania strony

**Aktor:**

* Użytkownik

**Warunki początkowe:**

* Użytkownik ma uprawnienia do korzystania z więcej niż jednego trybu wyświetlania.

**Warunki końcowe:**

* Strona została przełączona do wybranego trybu.

**Scenariusz główny:**

1. Użytkownik wybiera ikonę trybu wyświetlania.
2. System wyświetla dostępne tryby.
3. Użytkownik wybiera nowy tryb.
4. System zmienia tryb wyświetlania strony.

**Scenariusze alternatywne:**

* A1. Użytkownik posiada tylko jeden dostępny tryb – system pozostawia aktualny widok.

---

### UC-19: Przeglądanie i zarządzanie biografią

**Aktor:**

* Czapkowicz

**Warunki początkowe:**

* Użytkownik jest zalogowany.
* Użytkownik ma status „Czapkowicz”.

**Warunki końcowe:**

* Biografia została wyświetlona lub użytkownik złożył wniosek o zmianę wybranych danych.

**Scenariusz główny:**

1. Użytkownik wybiera ikonę konta.
2. System wyświetla listę dostępnych akcji.
3. Użytkownik wybiera opcję „Bio”.
4. System wyświetla biografię użytkownika wraz z danymi osobowymi.
5. Użytkownik przegląda informacje zapisane w biografii.
6. Użytkownik edytuje pola, które może zmienić samodzielnie.
7. System zapisuje wprowadzone zmiany.

**Scenariusze alternatywne:**

* A1. Użytkownik wybiera pole wymagające zgody moderatora – system umożliwia wysłanie prośby o zmianę.
* A2. Użytkownik ma status „Członek” lub „Weteran” – system wyświetla dodatkowe pola biografii.
* A3. Użytkownik opuszcza widok bez zapisywania zmian.

---

### UC-20: Złożenie prośby o zmianę danych wymagających zgody moderatora

**Aktor:**

* Czapkowicz

**Warunki początkowe:**

* Użytkownik znajduje się w widoku „Bio”.

**Warunki końcowe:**

* Prośba o zmianę danych została przekazana moderatorom.

**Scenariusz główny:**

1. Użytkownik wybiera pole wymagające zgody moderatora.
2. System wyświetla formularz zmiany.
3. Użytkownik wprowadza nową wartość.
4. Użytkownik zatwierdza formularz.
5. System przesyła zgłoszenie moderatorom.
6. System informuje użytkownika o oczekiwaniu na decyzję.

**Scenariusze alternatywne:**

* A1. Użytkownik rezygnuje z wysłania formularza.
* A2. Użytkownik nie uzupełni wymaganych danych – system uniemożliwia wysłanie zgłoszenia.

---

### UC-21: Zarządzanie flagami użytkownika

**Aktor:**

* Czapkowicz

**Warunki początkowe:**

* Użytkownik znajduje się w widoku „Bio”.

**Warunki końcowe:**

* Prośba o nadanie lub usunięcie flagi została przekazana moderatorom.

**Scenariusz główny:**

1. Użytkownik wybiera opcję „Poproś o nadanie flagi” lub „Poproś o usunięcie flagi”.
2. System wyświetla odpowiedni formularz.
3. Użytkownik uzupełnia wymagane informacje.
4. Użytkownik zatwierdza formularz.
5. System przesyła zgłoszenie moderatorom.
6. System informuje użytkownika o oczekiwaniu na decyzję.

**Scenariusze alternatywne:**

* A1. Użytkownik rezygnuje z wysłania zgłoszenia.

---

### UC-22: Złożenie prośby o zmianę statusu

**Aktor:**

* Czapkowicz

**Warunki początkowe:**

* Użytkownik znajduje się w widoku „Bio”.

**Warunki końcowe:**

* Prośba o zmianę statusu została przekazana moderatorom.

**Scenariusz główny:**

1. Użytkownik wybiera opcję zmiany statusu.
2. System przesyła zgłoszenie moderatorom.
3. Moderator akceptuje zgłoszenie.
4. System wysyła użytkownikowi formularz do uzupełnienia.
5. Użytkownik uzupełnia formularz.
6. System przekazuje formularz moderatorowi.
7. Moderator zatwierdza formularz.
8. System zmienia status użytkownika.

**Scenariusze alternatywne:**

* A1. Moderator odrzuca zgłoszenie.
* A2. Użytkownik nie uzupełni formularza – proces zostaje wstrzymany.

---

### UC-23: Wyświetlenie drzewa genealogicznego z poziomu biografii

**Aktor:**

* Czapkowicz
* Członek Zarządu
* Moderator
* Administrator

**Warunki początkowe:**

* Użytkownik znajduje się w widoku „Bio”.

**Warunki końcowe:**

* Wyświetlono drzewo genealogiczne użytkownika.

**Scenariusz główny:**

1. Użytkownik wybiera opcję podglądu drzewa genealogicznego.
2. System generuje drzewo genealogiczne.
3. System wyświetla drzewo użytkownika.

**Scenariusze alternatywne:**

* A1. Dane genealogiczne są niekompletne – system wyświetla dostępne informacje.
* A2. Drzewo genealogiczne zostało już kiedyś wygenerowane i zapisane – system wyświetla je bez ponownej generacji

---

### UC-24: Korzystanie z panelu Dashboard

**Aktor:**

* Czapkowicz
* Członek Zarządu
* Moderator

**Warunki początkowe:**

* Użytkownik jest zalogowany.

**Warunki końcowe:**

* Użytkownik przechodzi do wybranego modułu systemu.

**Scenariusz główny:**

1. Użytkownik wybiera ikonę konta.
2. System wyświetla listę dostępnych akcji.
3. Użytkownik wybiera opcję „Dashboard”.
4. System wyświetla komunikat powitalny.
5. System prezentuje kafelki prowadzące do dostępnych modułów.
6. Użytkownik wybiera jeden z modułów.
7. System otwiera wybrany moduł.

**Scenariusze alternatywne:**

* A1. Wybrany moduł jest chwilowo niedostępny – system wyświetla odpowiedni komunikat.

---

### UC-25: Korzystanie z Centrum Zarządzania

**Aktor:**

* Członek Zarządu

**Warunki początkowe:**

* Użytkownik jest zalogowany.
* Użytkownik posiada jedną z funkcji Zarządu: Wielki Mistrz, Kasztelan, Skarbnik, Sekretarz lub Cantandi.

**Warunki końcowe:**

* Użytkownik przejrzał wybrane moduły lub wykonał operacje w modułach, do których ma uprawnienia.

**Scenariusz główny:**

1. Użytkownik wybiera ikonę konta.
2. System wyświetla listę dostępnych akcji.
3. Użytkownik wybiera opcję „Centrum Zarządzania”.
4. System wyświetla komunikat powitalny „Witaj, <funkcja w Zarządzie>!”.
5. System wyświetla panele Centrum Zarządzania wraz z dostępnymi modułami.
6. Użytkownik wybiera moduł.
7. System otwiera wybrany moduł.
8. Jeżeli użytkownik ma uprawnienia do edycji wybranego modułu, system udostępnia funkcje modyfikacji danych.
9. Jeżeli użytkownik nie posiada uprawnień do edycji, system udostępnia wyłącznie możliwość przeglądania danych.

**Scenariusze alternatywne:**

* A1. Wybrany moduł jest chwilowo niedostępny – system wyświetla komunikat o błędzie.
* A2. Użytkownik próbuje zmodyfikować dane w module, do którego nie posiada uprawnień – system blokuje operację i wyświetla komunikat o braku uprawnień.
* A3. Użytkownik zamyka Centrum Zarządzania bez wybierania modułu.

---

### UC-26: Przeglądanie i obsługa panelu moderatora

**Aktor:**

* Moderator

**Warunki początkowe:**

* Użytkownik jest zalogowany jako Moderator.

**Warunki końcowe:**

* Użytkownik otworzył panel administracyjny i może przejść do wybranych modułów.

**Scenariusz główny:**

1. Użytkownik wybiera ikonę konta.
2. System wyświetla listę dostępnych akcji.
3. Użytkownik wybiera „Panel moderatora”.
4. System wyświetla panel administracyjny.
5. Użytkownik przegląda dostępne sekcje systemu.
6. Użytkownik wybiera interesujący moduł do zarządzania.

**Scenariusze alternatywne:**

* A1. Brak uprawnień do panelu – system odmawia dostępu.
* A2. Wybrany moduł jest niedostępny – system wyświetla komunikat o błędzie.

---

### UC-27: Moderacja komentarzy

**Aktor:**

* Moderator

**Warunki początkowe:**

* Moderator znajduje się w sekcji „Komentarze”.

**Warunki końcowe:**

* Komentarze zostały zatwierdzone lub odrzucone.

**Scenariusz główny:**

1. Moderator otwiera listę komentarzy.
2. System wyświetla komentarze z możliwością filtrowania.
3. Moderator wybiera komentarze.
4. Moderator wybiera akcję „Zatwierdź” lub „Odrzuć”.
5. System zapisuje decyzję.
6. System wysyła powiadomienie do autora komentarza.
7. W przypadku zatwierdzenia komentarz staje się publiczny.

**Scenariusze alternatywne:**

* A1. Brak komentarzy do moderacji – system wyświetla pustą listę.
* A2. Moderator anuluje operację przed zatwierdzeniem.

---

### UC-28: Przegląd i banowanie użytkowników

**Aktor:**

* Moderator

**Warunki początkowe:**

* Moderator przegląda profil użytkownika.

**Warunki końcowe:**

* Użytkownik został zablokowany lub decyzja została anulowana.

**Scenariusz główny:**

1. Moderator otwiera profil użytkownika z poziomu komentarza.
2. System wyświetla dane konta oraz Bio (jeśli dostępne).
3. Moderator wybiera opcję „Banuj”.
4. System wyświetla opcje czasu blokady.
5. Moderator wybiera czas lub opcję „Do odwołania”.
6. Moderator zatwierdza decyzję.
7. System blokuje użytkownika.
8. System wysyła powiadomienie o banie.

**Scenariusze alternatywne:**

* A1. Moderator rezygnuje z banowania – operacja zostaje przerwana.
* A2. Użytkownik nie istnieje lub konto jest już zablokowane.

---

### UC-29: Rozpatrywanie próśb użytkowników

**Aktor:**

* Moderator

**Warunki początkowe:**

* Moderator znajduje się w sekcji „Rozpatrz prośby”.

**Warunki końcowe:**

* Prośby zostały zaakceptowane lub odrzucone.

**Scenariusz główny:**

1. Moderator otwiera listę próśb użytkowników.
2. System wyświetla zgłoszenia z danymi użytkowników.
3. Moderator wybiera jedną lub wiele próśb.
4. Moderator zatwierdza lub odrzuca zgłoszenia.
5. System wykonuje odpowiednią akcję:

    * aktualizacja Bio,
    * zmiana statusu,
    * nadanie lub usunięcie flag,
    * obsługa awansu użytkownika.
6. System wysyła powiadomienia do użytkowników.

**Scenariusze alternatywne:**

* A1. Nieprawidłowe zgłoszenie – system odrzuca operację.
* A2. Konflikt danych (np. brak użytkownika) – system zgłasza błąd.

---

### UC-30: Generowanie i drukowanie kodów awansu

**Aktor:**

* Moderator

**Warunki początkowe:**

* Moderator znajduje się w sekcji „Wygeneruj kody awansu”.

**Warunki końcowe:**

* Kody zostały wygenerowane i opcjonalnie zapisane jako PDF.

**Scenariusz główny:**

1. Moderator podaje liczbę kodów do wygenerowania.
2. System generuje unikalne kody.
3. System wyświetla kody wraz z datami ważności.
4. Moderator wybiera opcję „Wydrukuj kody”.
5. System generuje plik PDF z kodami.
6. Moderator zapisuje lub drukuje plik.

**Scenariusze alternatywne:**

* A1. Podano nieprawidłową liczbę kodów – system blokuje operację.
* A2. Brak możliwości wygenerowania unikalnych kodów – system zgłasza błąd.

---

### UC-31: Przegląd logów zmian

**Aktor:**

* Moderator

**Warunki początkowe:**

* Moderator ma dostęp do sekcji „Logi zmian”.

**Warunki końcowe:**

* Logi zostały wyświetlone.

**Scenariusz główny:**

1. Moderator wybiera opcję „Logi zmian”.
2. System wyświetla historię operacji systemowych.
3. Moderator przegląda wpisy zawierające:

    * datę,
    * użytkownika,
    * opis zmiany.

**Scenariusze alternatywne:**

* A1. Brak logów – system wyświetla pustą listę.
* A2. Błąd pobierania danych – system informuje o niedostępności logów.

---

### UC-32: Zmiana trybu użytkownika

**Aktor:**

* Moderator

**Warunki początkowe:**

* Moderator jest zalogowany.

**Warunki końcowe:**

* Zmieniono tryb użytkownika w systemie.

**Scenariusz główny:**

1. Moderator wybiera ikonę zmiany trybu.
2. System wyświetla dostępne tryby (Czapkowicz / Zarząd / Moderator).
3. Moderator wybiera tryb.
4. System przełącza widok.

**Scenariusze alternatywne:**

* A1. Brak uprawnień do wybranego trybu – system blokuje zmianę.
* A2. Moderator pozostaje w aktualnym trybie.

---

### UC-33: Generowanie specjalnych kodów awansu

**Aktor:**

* Administrator

**Warunki początkowe:**

* Użytkownik jest zalogowany jako Administrator.
* Użytkownik ma dostęp do panelu administracyjnego.

**Warunki końcowe:**

* Kody awansu zostały wygenerowane i zapisane lub wyeksportowane.

**Scenariusz główny:**

1. Użytkownik wybiera ikonę konta.
2. System wyświetla listę dostępnych akcji.
3. Użytkownik wybiera opcję „Wygeneruj specjalne kody”.
4. Użytkownik wybiera „Dodaj nową pozycję”.
5. System wyświetla listę typów kodów awansu.
6. Użytkownik wybiera typ kodu (np. awans na Beana, Członka, Weterana itd.).
7. Użytkownik określa liczbę kodów do wygenerowania.
8. System generuje unikalne kody.
9. System wyświetla wygenerowane kody wraz z datą utworzenia i datą wygaśnięcia.
10. Użytkownik może powtarzać proces generowania dla kolejnych typów kodów.
11. Użytkownik wybiera opcję „Wydrukuj kody”.
12. System generuje plik PDF zawierający wszystkie wygenerowane kody w formacie umożliwiającym ich wydruk i wycięcie.

**Scenariusze alternatywne:**

* A1. Użytkownik poda nieprawidłową liczbę kodów – system blokuje operację.
* A2. Użytkownik nie wybierze typu kodu – system nie pozwala kontynuować.
* A3. System nie może wygenerować unikalnych kodów – operacja zostaje przerwana.
* A4. Użytkownik rezygnuje przed eksportem do PDF – kody pozostają w systemie jako niezatwierdzone.

---

### UC-34: Zarządzanie trybami systemu (rozszerzone uprawnienia)

**Aktor:**

* Administrator

**Warunki początkowe:**

* Użytkownik jest zalogowany jako Administrator.

**Warunki końcowe:**

* Użytkownik przełączył się do wybranego trybu systemu.

**Scenariusz główny:**

1. Administrator otwiera ikonę zmiany trybu wyświetlania.
2. System wyświetla wszystkie dostępne tryby:

    * Odwiedzający,
    * Czapkowicz,
    * Wielki Mistrz,
    * Kasztelan,
    * Skarbnik,
    * Sekretarz,
    * Cantandi,
    * Moderator,
    * Administrator.
3. Administrator wybiera dowolny tryb.
4. System przełącza widok wraz z odpowiednimi uprawnieniami.
5. System umożliwia wykonywanie operacji zgodnych z wybranym trybem.

**Scenariusze alternatywne:**

* A1. Wybrany tryb jest chwilowo niedostępny – system wyświetla komunikat o błędzie.
* A2. Administrator anuluje zmianę trybu – pozostaje w aktualnym widoku.

---

### UC-35: Dostęp do pełnego Centrum Zarządzania

**Aktor:**

* Administrator

**Warunki początkowe:**

* Administrator znajduje się w systemie.

**Warunki końcowe:**

* Administrator uzyskał dostęp do wszystkich modułów systemu.

**Scenariusz główny:**

1. Administrator przełącza się do trybu Zarządu lub wybranego panelu administracyjnego.
2. System udostępnia wszystkie panele Centrum Zarządzania.
3. Administrator przegląda i modyfikuje dane we wszystkich modułach.
4. System zapisuje wszystkie zmiany bez ograniczeń uprawnień.
5. Administrator przełącza się między modułami według potrzeb.

**Scenariusze alternatywne:**

* A1. Błąd dostępu do modułu – system wyświetla komunikat i blokuje operację.
* A2. Administrator podejmuje próbę wejścia w tryb bez uprawnień (np. usunięty dostęp) – system wymusza cofnięcie do bezpiecznego widoku.

---

### UC-36: Operacje dziedziczone z innych trybów

**Aktor:**

* Administrator

**Warunki początkowe:**

* Administrator jest zalogowany.

**Warunki końcowe:**

* Administrator korzysta z funkcji dostępnych w niższych trybach.

**Scenariusz główny:**

1. Administrator korzysta z funkcji:

    * Bio,
    * Dashboard,
    * Powiadomienia,
    * Komentarze,
    * Moderacja,
    * Logi zmian.
2. System udostępnia pełny zakres operacji bez ograniczeń uprawnień.
3. Administrator wykonuje operacje zgodnie z wybranym kontekstem trybu.

**Scenariusze alternatywne:**

* A1. Brak danych w wybranym module – system wyświetla pusty widok.
* A2. Konflikt uprawnień (rzadki przypadek błędu systemowego) – system blokuje operację i loguje zdarzenie.

---

**Uwaga:**
Tryby niższe (Moderator, Zarząd, Czapkowicz, Odwiedzający) są w pełni dostępne dla Administratora, który działa jako nadrzędny poziom uprawnień systemu.


---

## APLIKACJE OGÓLNODOSTĘPNE

---

### UC-KAL-01: Przeglądanie kalendarza wydarzeń

**Aktor:**

* Posiadacz dashboardu

**Warunki początkowe:**

* Użytkownik jest zalogowany i ma dostęp do Dashboardu.

**Warunki końcowe:**

* Użytkownik zapoznał się z wydarzeniami lub dodał kalendarz Bractwa do swojego Kalendarza Google.

**Scenariusz główny:**

1. Użytkownik otwiera moduł „Kalendarz” z poziomu Dashboardu.
2. System wyświetla kalendarz wydarzeń Bractwa.
3. Użytkownik wybiera wydarzenie.
4. System wyświetla szczegóły wydarzenia:

   * nazwę,
   * datę rozpoczęcia,
   * datę zakończenia,
   * miejsce,
   * typ wydarzenia.
5. Jeżeli wydarzenie zostało zakończone, system wyświetla również listę uczestników.
6. Użytkownik zamyka okno szczegółów wydarzenia.
7. Użytkownik wybiera opcję „Skopiuj kalendarz do Kalendarza Google”.
8. System dodaje kalendarz Bractwa do konta Google użytkownika.
9. Użytkownik wybiera opcję „Wróć do Dashboardu”.
10. System wyświetla Dashboard.

**Scenariusze alternatywne:**

* A1. Użytkownik nie wybiera żadnego wydarzenia i jedynie przegląda kalendarz.
* A2. Dodanie kalendarza do Google Calendar nie powiedzie się – system wyświetla komunikat o błędzie.
* A3. Wybrane wydarzenie nie posiada jeszcze listy uczestników – system wyświetla wyłącznie podstawowe informacje.

---

### UC-KAL-02: Zarządzanie kalendarzem wydarzeń

**Aktor:**

* Sekretarz

**Warunki początkowe:**

* Użytkownik jest zalogowany.
* Użytkownik ma uprawnienia Sekretarza.
* Użytkownik znajduje się w Centrum Zarządzania.

**Warunki końcowe:**

* Wydarzenie zostało dodane lub zmodyfikowane, a zmiany zostały zapisane i zarejestrowane na Osi Czasu.

**Scenariusz główny:**

1. Użytkownik otwiera moduł „Edytuj kalendarz”.
2. System wyświetla kalendarz wydarzeń.
3. Użytkownik wybiera opcję „Dodaj wydarzenie”.
4. System wyświetla formularz dodawania wydarzenia.
5. Użytkownik uzupełnia dane wydarzenia.
6. Użytkownik zatwierdza formularz.
7. System zapisuje wydarzenie i rejestruje operację na Osi Czasu.
8. Użytkownik wybiera istniejące wydarzenie.
9. Użytkownik wybiera opcję „Edytuj wydarzenie”.
10. System wyświetla formularz edycji.
11. Użytkownik wprowadza zmiany.
12. Użytkownik zatwierdza formularz.
13. System zapisuje zmiany i rejestruje je na Osi Czasu.
14. Użytkownik wybiera opcję „Wróć do Centrum Zarządzania”.
15. System wyświetla Centrum Zarządzania.

**Scenariusze alternatywne:**

* A1. Użytkownik anuluje dodawanie wydarzenia – system nie zapisuje zmian.
* A2. Użytkownik anuluje edycję wydarzenia – system pozostawia dotychczasowe dane.
* A3. Nie wypełniono wszystkich wymaganych pól formularza – system uniemożliwia zapisanie wydarzenia.
* A4. Wystąpi błąd podczas zapisywania danych – system wyświetla komunikat i umożliwia ponowienie operacji.

---

### UC-ENC-01: Przeglądanie encyklopedii

**Aktor:**

* Posiadacz dashboardu

**Warunki początkowe:**

* Użytkownik jest zalogowany.
* Użytkownik ma dostęp do Dashboardu.

**Warunki końcowe:**

* Użytkownik zapoznał się z wybranym artykułem encyklopedycznym lub wrócił do Dashboardu.

**Scenariusz główny:**

1. Użytkownik otwiera moduł „Encyklopedia” z poziomu Dashboardu.
2. System wyświetla spis pojęć pogrupowanych alfabetycznie.
3. Użytkownik wybiera pojęcie.
4. System wyświetla artykuł encyklopedyczny dotyczący wybranego pojęcia.
5. Użytkownik może filtrować artykuły według kategorii.
6. Użytkownik wybiera opcję „Wróć do Dashboardu”.
7. System wyświetla Dashboard.

**Scenariusze alternatywne:**

* A1. Użytkownik korzysta z filtrowania przed wyborem pojęcia – system wyświetla artykuły spełniające wybrane kryteria.
* A2. Wybrana kategoria nie zawiera żadnych artykułów – system wyświetla komunikat o braku wyników.
* A3. Użytkownik opuszcza moduł bez otwierania artykułu.

---

### UC-SLL-01: Przeglądanie słowniczka łacińskiego

**Aktor:**

* Posiadacz dashboardu

**Warunki początkowe:**

* Użytkownik jest zalogowany.
* Użytkownik ma dostęp do Dashboardu.

**Warunki końcowe:**

* Użytkownik zapoznał się z wybranymi zwrotami lub wrócił do Dashboardu.

**Scenariusz główny:**

1. Użytkownik otwiera moduł „Słowniczek łaciński” z poziomu Dashboardu.
2. System wyświetla listę zwrotów łacińskich wraz z ich tłumaczeniami na język polski.
3. Użytkownik przegląda dostępne zwroty.
4. Użytkownik może filtrować zwroty według kategorii.
5. Użytkownik wybiera opcję „Wróć do Dashboardu”.
6. System wyświetla Dashboard.

**Scenariusze alternatywne:**

* A1. Użytkownik korzysta z filtrowania – system wyświetla zwroty spełniające wybrane kryteria.
* A2. Wybrana kategoria nie zawiera żadnych zwrotów – system wyświetla komunikat o braku wyników.
* A3. Użytkownik opuszcza moduł bez korzystania z filtrowania.

---

### UC-PIN-01: Przeglądanie katalogu pinów belgijskich

**Aktor:**

* Czapkowicz
* Odwiedzający

**Warunki początkowe:**

* Użytkownik jest zalogowany kontem Google.
* Czapkowicz otworzył moduł „Piny belgijskie” z Dashboardu.
* Odwiedzający wybrał opcję "Zamów piny belgijskie" w sekcji "Sklep".

**Warunki końcowe:**

* Użytkownik zapoznał się z ofertą pinów lub przeszedł do koszyka.

**Scenariusz główny:**

1. Użytkownik otwiera moduł „Piny belgijskie”.
2. System wyświetla pierwszą kategorię pinów w postaci kafelków.
3. Każdy kafelek zawiera nazwę, grafikę, cenę oraz kontrolkę wyboru ilości.
4. Użytkownik może wyświetlić opis pina poprzez najechanie kursorem.
5. Użytkownik wybiera kategorię z menu.
6. System wyświetla piny należące do wybranej kategorii.
7. Użytkownik dodaje wybrane piny do koszyka.
8. Użytkownik otwiera koszyk.

**Scenariusze alternatywne:**

* A1. Użytkownik jest Odwiedzającym i nie jest zalogowany – system wymaga logowania kontem Google.
* A2. Wybrana kategoria nie zawiera żadnych pinów – system wyświetla odpowiedni komunikat.
* A3. Użytkownik opuszcza moduł bez dodawania pinów do koszyka.

---

### UC-PIN-02: Złożenie zamówienia na piny belgijskie

**Aktor:**

* Czapkowicz
* Odwiedzający

**Warunki początkowe:**

* W koszyku znajduje się co najmniej jeden pin.

**Warunki końcowe:**

* Zamówienie zostało zapisane i przesłane do Skarbnika.

**Scenariusz główny:**

1. Użytkownik otwiera koszyk.
2. System wyświetla zawartość koszyka wraz z łącznym kosztem zamówienia.
3. Użytkownik modyfikuje ilości wybranych pinów.
4. Użytkownik wybiera opcję „Zapisz zamówienie”.
5. System zapisuje zamówienie.
6. Użytkownik wybiera opcję „Wyślij zamówienie do Skarbnika”.
7. System przesyła zamówienie.
8. System wyświetla potwierdzenie wysłania.

**Scenariusze alternatywne:**

* A1. Koszyk jest pusty – system uniemożliwia zapisanie zamówienia.
* A2. Upłynął termin składania zamówień – system blokuje możliwość wysłania.
* A3. Wystąpił błąd podczas zapisywania zamówienia – system wyświetla komunikat.
* A4. W przypadku Czapkowicza koszyk wyświetla też licznik czasu, w którym możliwe jest ponowne przesłanie zamówienia.

---

### UC-PIN-03: Modyfikacja zapisanego zamówienia

**Aktor:**

* Odwiedzający
* Członek

**Warunki początkowe:**

* Użytkownik posiada zapisane zamówienie.
* Nie upłynął termin składania zamówień.

**Warunki końcowe:**

* Poprawiona wersja zamówienia została przesłana do Skarbnika.

**Scenariusz główny:**

1. Użytkownik otwiera listę swoich zamówień.
2. System wyświetla wszystkie zapisane zamówienia.
3. Użytkownik wybiera zamówienie na piny belgijskie.
4. System wyświetla zawartość koszyka.
5. Użytkownik zmienia ilości lub dodaje kolejne piny.
6. Użytkownik zapisuje zmiany.
7. Użytkownik ponownie wybiera opcję „Wyślij zamówienie do Skarbnika”.
8. System zastępuje poprzednią wersję zamówienia nową.
9. System wyświetla potwierdzenie aktualizacji.

**Scenariusze alternatywne:**

* A1. Termin składania zamówień upłynął – system blokuje możliwość edycji.
* A2. Użytkownik usuwa wszystkie piny z koszyka – system nie pozwala wysłać pustego zamówienia.
* A3. Użytkownik rezygnuje z zapisania zmian.

---

### UC-PIN-04: Zarządzanie zamówieniami pinów belgijskich

**Aktor:**

* Skarbnik

**Warunki początkowe:**

* Użytkownik ma uprawnienia Skarbnika.
* Użytkownik znajduje się w Centrum Zarządzania.

**Warunki końcowe:**

* Zamówienia zostały przejrzane lub zaktualizowano termin spłaty.

**Scenariusz główny:**

1. Użytkownik otwiera moduł „Piny belgijskie zamówienie”.
2. System wyświetla listę wszystkich zamówień.
3. Użytkownik wybiera zamówienie.
4. System wyświetla szczegóły zamówienia.
5. Użytkownik zamyka widok szczegółów.
6. Użytkownik wybiera opcję „Zmień termin spłaty”.
7. Użytkownik podaje nowy termin.
8. System zapisuje zmianę.
9. System wysyła powiadomienia do użytkowników posiadających zaległości.
10. System aktualizuje odpowiedni cel składkowy.
11. Użytkownik wraca do listy zamówień.

**Scenariusze alternatywne:**

* A1. Nabór zamówień nie został otwarty – lista pozostaje pusta.
* A2. Brak zalegających płatników – system nie wysyła powiadomień.
* A3. Wprowadzono niepoprawną datę – system odrzuca zmianę.

---

### UC-PIN-05: Zarządzanie katalogiem pinów belgijskich

**Aktor:**

* Skarbnik

**Warunki początkowe:**

* Użytkownik ma uprawnienia Skarbnika.

**Warunki końcowe:**

* Zmiany katalogu zostały zapisane.

**Scenariusz główny:**

1. Użytkownik wybiera opcję „Edytuj katalog pinów”.
2. System wyświetla katalog wszystkich pinów.
3. Użytkownik wybiera pin do edycji.
4. System wyświetla formularz edycji.
5. Użytkownik modyfikuje dane pina.
6. Użytkownik zatwierdza zmiany.
7. System zapisuje zmiany.
8. System rejestruje operację na Osi Czasu.
9. Użytkownik wraca do listy zamówień.

**Scenariusze alternatywne:**

* A1. Użytkownik anuluje edycję.
* A2. Nie wypełniono wymaganych pól formularza.
* A3. Wystąpił błąd podczas zapisywania zmian.

---

## APLIKACJE DASHBOARDOWE

---

### UC-SPI-01: Przeglądanie śpiewnika

**Aktor:**

* Posiadacz dashboardu

**Warunki początkowe:**

* Użytkownik jest zalogowany.
* Użytkownik ma dostęp do Dashboardu.

**Warunki końcowe:**

* Użytkownik zapoznał się z treścią piosenek lub wrócił do Dashboardu.

**Scenariusz główny:**

1. Użytkownik otwiera moduł „Śpiewnik”.
2. System wyświetla listę kategorii oraz pole wyszukiwania.
3. Użytkownik wybiera kategorię.
4. System wyświetla listę piosenek należących do wybranej kategorii.
5. Użytkownik wybiera piosenkę.
6. System wyświetla:

   * tytuł,
   * tytuł alternatywny,
   * autorów,
   * kategorie,
   * tekst z akordami,
   * tekst alternatywny (jeżeli istnieje).
7. Użytkownik wybiera opcję „Następna piosenka”.
8. System wyświetla kolejną piosenkę z bieżącej kategorii.
9. Użytkownik wybiera opcję „Poprzednia piosenka”.
10. System wyświetla poprzednią piosenkę z bieżącej kategorii.
11. Użytkownik wraca do listy kategorii.
12. Użytkownik wybiera opcję „Wróć do Dashboardu”.
13. System wyświetla Dashboard.

**Scenariusze alternatywne:**

* A1. Wybrana kategoria nie zawiera żadnych piosenek.
* A2. Wybrana piosenka nie posiada tekstu alternatywnego.
* A3. Użytkownik opuszcza moduł bez otwierania piosenki.

---

### UC-SPI-02: Wyszukiwanie zaawansowane i korzystanie z trybu Focus

**Aktor:**

* Posiadacz dashboardu

**Warunki początkowe:**

* Użytkownik ma dostęp do Dashboardu.

**Warunki końcowe:**

* Użytkownik zakończył korzystanie z trybu Focus lub wrócił do Dashboardu.

**Scenariusz główny:**

1. Użytkownik otwiera moduł „Śpiewnik”.
2. System wyświetla listę kategorii.
3. Użytkownik wybiera opcję „Więcej”.
4. System wyświetla panel wyszukiwania zaawansowanego.
5. Użytkownik wyszukuje piosenkę według wybranego kryterium.
6. System wyświetla listę wyników.
7. Użytkownik wybiera piosenkę.
8. Użytkownik uruchamia tryb „Focus”.
9. System wyświetla pierwszą zwrotkę oraz panel ustawień.
10. Użytkownik przechodzi pomiędzy zwrotkami.
11. Użytkownik zmienia ustawienia wyświetlania (opcjonalnie).
12. Użytkownik wyłącza tryb „Focus”.
13. Użytkownik wraca do Dashboardu.

**Scenariusze alternatywne:**

* A1. Wyszukiwanie nie zwraca wyników.
* A2. Użytkownik nie zmienia ustawień trybu Focus i korzysta z ustawień domyślnych.
* A3. Użytkownik kończy pracę bez uruchamiania trybu Focus.

---

### UC-SPI-03: Edycja piosenki

**Aktor:**

* Cantandi

**Warunki początkowe:**

* Użytkownik jest zalogowany jako Cantandi.
* Użytkownik znajduje się w Centrum Zarządzania.

**Warunki końcowe:**

* Zmiany zostały zapisane i zarejestrowane na Osi Czasu.

**Scenariusz główny:**

1. Użytkownik otwiera moduł „Edytuj śpiewnik”.
2. System wyświetla katalog piosenek.
3. Użytkownik wybiera piosenkę.
4. Użytkownik wybiera opcję „Edytuj piosenkę”.
5. System wyświetla formularz edycji.
6. Użytkownik modyfikuje dane piosenki.
7. Użytkownik zatwierdza zmiany.
8. System zapisuje zmiany.
9. System rejestruje operację na Osi Czasu.
10. Użytkownik wraca do Centrum Zarządzania.

**Scenariusze alternatywne:**

* A1. Użytkownik anuluje edycję.
* A2. Nie wypełniono wymaganych pól.
* A3. Wystąpił błąd podczas zapisu zmian.

---

### UC-SPI-04: Dodawanie nowej piosenki

**Aktor:**

* Cantandi

**Warunki początkowe:**

* Użytkownik jest zalogowany jako Cantandi.
* Użytkownik ma dostęp do modułu „Edytuj śpiewnik”.

**Warunki końcowe:**

* Nowa piosenka została dodana do śpiewnika i jest dostępna dla użytkowników.

**Scenariusz główny:**

1. Użytkownik wybiera opcję „Dodaj piosenkę”.
2. System wyświetla formularz dodawania piosenki.
3. System udostępnia instrukcję oraz szablon JSON.
4. Użytkownik wprowadza:

   * tytuł,
   * tytuł alternatywny,
   * autorów,
   * kategorie.
5. Użytkownik dodaje tekst piosenki oraz tekst alternatywny (opcjonalnie).
6. Użytkownik zatwierdza formularz.
7. System zapisuje nową piosenkę.
8. System rejestruje operację na Osi Czasu.
9. Nowa piosenka staje się dostępna w module „Śpiewnik”.
10. Użytkownik wraca do Centrum Zarządzania.

**Scenariusze alternatywne:**

* A1. Użytkownik anuluje dodawanie piosenki.
* A2. Dane formularza są niekompletne – system blokuje zapis.
* A3. Wystąpił błąd podczas zapisu nowej piosenki.

---

### UC-IDG-01: Przeglądanie drzewa genealogicznego

**Aktor:**

* Posiadacz dashboardu

**Warunki początkowe:**

* Użytkownik jest zalogowany.
* Użytkownik ma dostęp do Dashboardu.

**Warunki końcowe:**

* Użytkownik zakończył przeglądanie drzewa.

**Scenariusz główny:**

1. Użytkownik otwiera moduł „Drzewo genealogiczne”.
2. System wyświetla drzewo genealogiczne.
3. Użytkownik może przewijać drzewo w pionie i poziomie.
4. Użytkownik może przybliżać i oddalać widok.
5. Użytkownik klika węzeł.
6. System wyświetla biografię wybranej osoby.
7. Użytkownik zamyka biografię.

**Scenariusze alternatywne:**

* A1. Użytkownik nie wybiera żadnego węzła – tylko przegląda drzewo.
* A2. Biografia jest niedostępna – system wyświetla komunikat.
* A3. Drzewo nie zawiera powiązań – system wyświetla widok pusty.

---

### UC-IDG-02: Konfiguracja drzewa genealogicznego

**Aktor:**

* Posiadacz dashboardu

**Warunki początkowe:**

* Drzewo genealogiczne jest wyświetlone.

**Warunki końcowe:**

* Drzewo zostało przerysowane zgodnie z konfiguracją.

**Scenariusz główny:**

1. Użytkownik otwiera menu konfiguracji.
2. Użytkownik wybiera opcje „Filtry”, „Kolorowanie” lub „Widoki”.
3. System zapisuje wybrane ustawienia.
4. Użytkownik wybiera opcję „Odśwież”.
5. System generuje nowe drzewo zgodnie z konfiguracją.
6. System wyświetla zaktualizowane drzewo.

**Scenariusze alternatywne:**

* A1. Użytkownik wybiera wiele filtrów – system łączy warunki.
* A2. Użytkownik wybiera niedozwoloną kombinację filtrów – system wyświetla błąd.
* A3. Odświeżenie nie powiedzie się – system przywraca poprzedni widok.

---

### UC-IDG-03: Tryb zaznaczania i operacje na węzłach

**Aktor:**

* Posiadacz dashboardu

**Warunki początkowe:**

* Drzewo genealogiczne jest wyświetlone.

**Warunki końcowe:**

* Zaznaczone węzły zostały użyte w operacji lub wyczyszczone.

**Scenariusz główny:**

1. Użytkownik aktywuje tryb „Zaznaczenie”.
2. Użytkownik klika węzły – system dodaje je do zaznaczenia.
3. Użytkownik może używać Shift + naciśnięcie do zaznaczania ścieżek między węzłami.
4. System umożliwia cofanie i ponawianie akcji.
5. Użytkownik wybiera operację:

   * „Pokoloruj”
   * „Drukuj”
   * „Dodaj do nowego drzewa”
6. System wykonuje wybraną operację.

**Scenariusze alternatywne:**

* A1. Użytkownik nie zaznaczył żadnego węzła – operacje są niedostępne.
* A2. Cofnięcie operacji nie jest możliwe – system ignoruje żądanie.
* A3. Zaznaczenie zostaje utracone po odświeżeniu widoku.

---

### UC-IDG-04: Tworzenie i edycja nowego drzewa

**Aktor:**

* Posiadacz dashboardu

**Warunki początkowe:**

* Użytkownik posiada zaznaczone węzły.

**Warunki końcowe:**

* Nowe drzewo zostało utworzone lub zaktualizowane.

**Scenariusz główny:**

1. Użytkownik wybiera opcję „Dodaj do nowego drzewa”.
2. System tworzy nowe drzewo na podstawie zaznaczenia.
3. Użytkownik nadaje nazwę drzewu.
4. System zapisuje nowe drzewo.
5. Użytkownik może wracać do oryginalnego drzewa i dodawać kolejne węzły.
6. Użytkownik może przechodzić do nowego drzewa i usuwać węzły.
7. System aktualizuje strukturę drzewa.

**Scenariusze alternatywne:**

* A1. Nazwa drzewa jest pusta – system odrzuca zapis.
* A2. Użytkownik anuluje tworzenie drzewa.
* A3. Usunięcie węzłów powoduje pustą strukturę – system ostrzega użytkownika.

---

### UC-IDG-05: Eksport i druk drzewa genealogicznego

**Aktor:**

* Posiadacz dashboardu

**Warunki początkowe:**

* Użytkownik posiada drzewo lub zaznaczenie.

**Warunki końcowe:**

* Drzewo zostało zapisane jako plik PNG.

**Scenariusz główny:**

1. Użytkownik wybiera opcję „Drukuj drzewo”.
2. Użytkownik podaje nazwę pliku.
3. System generuje plik PNG i zapisuje go na urządzeniu.

**Scenariusze alternatywne:**

* A1. Brak miejsca na dysku – system wyświetla błąd.
* A2. Eksport zostaje anulowany.

---

### UC-IDG-06: Podgląd drzewa z biografii

**Aktor:**

* Posiadacz dashboardu
* Administrator

**Warunki początkowe:**

* Użytkownik znajduje się w profilu innego członka.

**Warunki końcowe:**

* Użytkownik obejrzał drzewo genealogiczne.

**Scenariusz główny:**

1. Użytkownik otwiera profil członka.
2. Użytkownik wybiera opcję „Pokaż drzewo”.
3. System generuje drzewo obejmujące:

   * rodziców,
   * daną osobę,
   * dzieci.
4. Użytkownik może zoomować i przewijać widok.
5. Użytkownik zamyka widok drzewa.

**Scenariusze alternatywne:**

* A1. Brak powiązań genealogicznych – system wyświetla pojedynczy węzeł.
* A2. Biografia nie zawiera drzewa – system blokuje opcję.

---

### UC-KOD-01: Przeglądanie Kodeksu

**Aktor:**

* Posiadacz dashboardu

**Warunki początkowe:**

* Użytkownik ma dostęp do Dashboardu.

**Warunki końcowe:**

* Użytkownik zapoznał się z wybraną częścią Kodeksu lub wrócił do Dashboardu.

**Scenariusz główny:**

1. Użytkownik otwiera moduł „Kodeks” z poziomu Dashboardu.
2. System wyświetla dostępne sekcje:

   * „Prawa i obowiązki”,
   * „Zasady wydarzeń”,
   * „Tradycje”,
   * „Księga znaku”.
3. Użytkownik wybiera sekcję „Prawa i obowiązki”.
4. System wyświetla listę rozwijalnych sekcji.
5. Użytkownik wybiera jedną z sekcji.
6. System wyświetla szczegółową listę praw i obowiązków.
7. Użytkownik wraca do listy głównych sekcji.
8. Użytkownik wybiera sekcję „Zasady wydarzeń”.
9. System wyświetla listę typów wydarzeń.
10. Użytkownik wybiera typ wydarzenia.
11. System wyświetla zasady obowiązujące dla wybranego typu wydarzenia.
12. Użytkownik wraca do listy głównych sekcji.
13. Użytkownik wybiera sekcję „Tradycje”.
14. System wyświetla listę tradycji.
15. Użytkownik wraca do listy głównych sekcji.
16. Użytkownik wybiera sekcję „Księga znaku”.
17. System wyświetla listę znaków.
18. Użytkownik wybiera opcję „Wróć do Dashboardu”.
19. System wyświetla Dashboard.

**Scenariusze alternatywne:**

* A1. Użytkownik przegląda tylko wybrane sekcje Kodeksu.
* A2. Wybrana sekcja nie zawiera jeszcze żadnych wpisów – system wyświetla komunikat o braku treści.
* A3. Użytkownik opuszcza moduł bez otwierania żadnej sekcji.

---

### UC-MAP-01: Przeglądanie mapy miejsc

**Aktor:**

* Posiadacz dashboardu

**Warunki początkowe:**

* Użytkownik ma dostęp do Dashboardu.

**Warunki końcowe:**

* Użytkownik zakończył przeglądanie mapy lub wrócił do Dashboardu.

**Scenariusz główny:**

1. Użytkownik otwiera moduł „Mapa” z poziomu Dashboardu.
2. System wyświetla mapę świata ze znacznikami miejsc, wyśrodkowaną na Polsce.
3. Użytkownik przybliża, oddala lub przesuwa mapę.
4. Użytkownik wskazuje znacznik.
5. System wyświetla nazwę miejsca, jego typ, adres oraz informację o ewentualnym trwałym zamknięciu.
6. Użytkownik wybiera znacznik.
7. System wyświetla wszystkie wzmianki o danym miejscu w Kronice Bractwa.
8. Użytkownik wybiera opcję „Wróć do Dashboardu”.
9. System wyświetla Dashboard.

**Scenariusze alternatywne:**

* A1. Miejsce nie posiada wpisów w Kronice – system wyświetla odpowiedni komunikat.
* A2. Użytkownik korzysta ze standardowych funkcji mapy (np. Street View).
* A3. Użytkownik zamyka moduł bez wybierania żadnego znacznika.

---

### UC-MAP-02: Filtrowanie miejsc na mapie

**Aktor:**

* Posiadacz dashboardu

**Warunki początkowe:**

* Wyświetlona jest mapa miejsc.

**Warunki końcowe:**

* Mapa została zaktualizowana zgodnie z wybranymi filtrami.

**Scenariusz główny:**

1. Użytkownik wybiera ikonę filtrowania.
2. System wyświetla panel filtrów.
3. Użytkownik wybiera typy miejsc oraz opcjonalnie filtr „Zamknięte na stałe”.
4. Użytkownik zatwierdza wybór.
5. System aktualizuje widok mapy.
6. System wyświetla znaczniki spełniające wybrane kryteria.

**Scenariusze alternatywne:**

* A1. Żadne miejsce nie spełnia kryteriów – system wyświetla pustą mapę i odpowiedni komunikat.
* A2. Użytkownik usuwa wszystkie filtry – system przywraca pełny widok mapy.

---

### UC-MAP-03: Korzystanie z Kompasu Nawojkowego (urządzenie mobilne)

**Aktor:**

* Posiadacz dashboardu

**Warunki początkowe:**

* Użytkownik korzysta z urządzenia mobilnego.
* Moduł Mapa jest otwarty.

**Warunki końcowe:**

* Kompas Nawojkowy został włączony lub wyłączony.

**Scenariusz główny:**

1. System wyświetla wskaźnik kierunku oparty na orientacji urządzenia.
2. Użytkownik wybiera ikonę „Kompas Nawojkowy”.
3. System wyświetla czerwony wskaźnik pokazujący kierunek przeciwny do położenia Domu Studenckiego Nawojka.
4. Użytkownik ponownie wybiera ikonę.
5. System ukrywa czerwony wskaźnik.

**Scenariusze alternatywne:**

* A1. Urządzenie nie udostępnia danych orientacji – system wyświetla komunikat o braku dostępności funkcji.
* A2. Użytkownik nie aktywuje Kompasu Nawojkowego.

---

### UC-MAP-04: Wyszukiwanie rekomendowanych miejsc wydarzenia

**Aktor:**

* Członek Zarządu

**Warunki początkowe:**

* Użytkownik znajduje się w Centrum Zarządzania.

**Warunki końcowe:**

* System wyświetlił rekomendowane miejsca wydarzenia.

**Scenariusz główny:**

1. Użytkownik otwiera moduł „Wywiad miejscówek”.
2. System wyświetla mapę wydarzeń.
3. Użytkownik podaje datę, godzinę rozpoczęcia, czas trwania wydarzenia oraz określa, czy jest to Karczma.
4. Użytkownik wybiera opcję „Znajdź najlepsze miejsca”.
5. System analizuje dostępne dane.
6. System wyświetla listę rekomendowanych miejsc.
7. Użytkownik filtruje wyniki według wybranych kryteriów.

**Scenariusze alternatywne:**

* A1. Nie znaleziono miejsc spełniających kryteria.
* A2. Użytkownik zmienia parametry wydarzenia i ponawia wyszukiwanie.

---

### UC-MAP-05: Wyszukiwanie miejsc na after

**Aktor:**

* Członek Zarządu

**Warunki początkowe:**

* Wyświetlona jest lista rekomendowanych miejsc wydarzenia.

**Warunki końcowe:**

* System wyświetlił propozycje miejsc na after.

**Scenariusz główny:**

1. Użytkownik wybiera jedno z rekomendowanych miejsc wydarzenia.
2. Użytkownik wybiera opcję „Znajdź miejscówki na after”.
3. System analizuje odległość, natężenie ruchu oraz oceny.
4. System wyświetla rekomendowane miejsca na after.

**Scenariusze alternatywne:**

* A1. Brak odpowiednich miejsc na after.
* A2. Użytkownik wybiera inne miejsce wydarzenia i ponawia wyszukiwanie.

---

### UC-MAP-06: Edycja informacji o miejscu

**Aktor:**

* Kasztelan

**Warunki początkowe:**

* Użytkownik znajduje się w module „Wywiad miejscówek”.

**Warunki końcowe:**

* Informacje o miejscu zostały zaktualizowane.

**Scenariusz główny:**

1. Użytkownik wybiera znacznik miejsca.
2. System wyświetla szczegółowe informacje.
3. Użytkownik wybiera opcję edycji.
4. Użytkownik wprowadza zmiany.
5. Użytkownik zapisuje zmiany.
6. System aktualizuje dane.
7. System zapisuje operację na Osi Czasu.
8. Użytkownik wraca do Centrum Zarządzania.

**Scenariusze alternatywne:**

* A1. Użytkownik rezygnuje z edycji.
* A2. Wprowadzone dane są niepoprawne – system wyświetla komunikat i nie zapisuje zmian.

---

### UC-KRO-01: Przeglądanie Kroniki

**Aktor:**

* Posiadacz dashboardu

**Warunki początkowe:**

* Użytkownik ma dostęp do Dashboardu.

**Warunki końcowe:**

* Użytkownik zapoznał się z wybraną zawartością Kroniki lub wrócił do Dashboardu.

**Scenariusz główny:**

1. Użytkownik otwiera moduł „Kronika”.
2. System wyświetla listę głównych sekcji.
3. Użytkownik rozwija wybraną sekcję.
4. System wyświetla listę podkategorii.
5. Użytkownik wybiera podkategorię.
6. System wyświetla przypisane do niej wpisy.
7. Użytkownik może zwijać i rozwijać kolejne sekcje.
8. Użytkownik wybiera opcję „Wróć do Dashboardu”.
9. System wyświetla Dashboard.

**Scenariusze alternatywne:**

* A1. Wybrana podkategoria nie zawiera wpisów.
* A2. Użytkownik przegląda wiele sekcji przed opuszczeniem modułu.

---

### UC-KRO-02: Wyszukiwanie informacji w Kronice

**Aktor:**

* Posiadacz dashboardu

**Warunki początkowe:**

* Moduł „Kronika” jest otwarty.

**Warunki końcowe:**

* Wyświetlono wyniki wyszukiwania zgodne z kryteriami użytkownika.

**Scenariusz główny:**

1. Użytkownik wpisuje frazę w polu wyszukiwania.
2. System filtruje wpisy.
3. System wyróżnia dopasowania:

   * dosłowne kolorem zielonym,
   * kontekstowe lub bliskoznaczne kolorem żółtym.
4. Użytkownik wybiera ikonę wyszukiwania zaawansowanego.
5. System prezentuje dane w formie tabeli.
6. Użytkownik filtruje dane według wartości poszczególnych kolumn.
7. System aktualizuje listę wyników.

**Scenariusze alternatywne:**

* A1. Nie znaleziono wyników.
* A2. Użytkownik usuwa wszystkie filtry i wraca do pełnej listy wpisów.
* A3. Użytkownik korzysta wyłącznie z wyszukiwania prostego.

---

### UC-CYT-01: Przeglądanie cytatów

**Aktor:**

* Posiadacz dashboardu

**Warunki początkowe:**

* Użytkownik ma dostęp do Dashboardu.

**Warunki końcowe:**

* Użytkownik zapoznał się z wybranym cytatem lub wrócił do Dashboardu.

**Scenariusz główny:**

1. Użytkownik otwiera moduł „Cytaty”.
2. System wyświetla cytaty pogrupowane według autorów.
3. Użytkownik wybiera cytat.
4. System wyświetla jego treść, autora oraz kontekst.
5. Użytkownik wybiera opcję „Następny cytat” lub „Poprzedni cytat”.
6. System wyświetla odpowiedni cytat.
7. Użytkownik zamyka widok szczegółowy.
8. Użytkownik wybiera opcję „Wróć do Dashboardu”.
9. System wyświetla Dashboard.

**Scenariusze alternatywne:**

* A1. Cytat jest skrócony na liście — pełna treść wyświetla się po otwarciu.
* A2. Użytkownik zamyka moduł bez otwierania żadnego cytatu.

---

### UC-CYT-02: Wyświetlenie Cytatu dnia

**Aktor:**

* Posiadacz dashboardu

**Warunki początkowe:**

* Moduł „Cytaty” jest otwarty.

**Warunki końcowe:**

* Wyświetlono Cytat dnia.

**Scenariusz główny:**

1. Użytkownik wybiera opcję „Cytat dnia”.
2. System wyświetla cytat przypisany do bieżącego dnia.
3. System prezentuje autora oraz kontekst cytatu.
4. Użytkownik zamyka widok Cytatu dnia.

**Scenariusze alternatywne:**

* A1. Dla danego dnia nie przypisano cytatu — system wyświetla losowy cytat lub odpowiedni komunikat.

---

### UC-SKL-01: Przeglądanie i deklaracja wpłaty składki

**Aktor:**

* Czapkowicz

**Warunki początkowe:**

* Użytkownik posiada przypisany co najmniej jeden cel składkowy.
* Użytkownik ma dostęp do Dashboardu.

**Warunki końcowe:**

* Deklaracja wpłaty została przesłana do Skarbnika.

**Scenariusz główny:**

1. Użytkownik otwiera moduł „Składki” z poziomu Dashboardu.
2. System wyświetla listę celów składkowych wraz z postępem wpłat oraz kodami do tytułu przelewu.
3. Użytkownik wybiera cel składkowy.
4. System wyświetla szczegóły celu:

   * nazwę,
   * kwotę docelową,
   * termin,
   * formularz deklaracji wpłaty.
5. Użytkownik wpisuje zadeklarowaną kwotę wpłaty.
6. Użytkownik zatwierdza formularz.
7. System przesyła deklarację do Skarbnika.
8. Po aktualizacji historii wpłat system odświeża postęp realizacji składki.
9. Użytkownik wybiera opcję „Wróć do Dashboardu”.
10. System wyświetla Dashboard.

**Scenariusze alternatywne:**

* A1. Cel składkowy nie wymaga deklaracji wpłaty — formularz nie jest wyświetlany.
* A2. Użytkownik anuluje wprowadzanie deklaracji.
* A3. Podana kwota jest niepoprawna — system wyświetla komunikat i nie zapisuje formularza.

---

### UC-SKL-02: Przeglądanie celu składkowego

**Aktor:**

* Członek Zarządu

**Warunki początkowe:**

* Użytkownik znajduje się w Centrum Zarządzania.

**Warunki końcowe:**

* Użytkownik zapoznał się ze stanem realizacji celu składkowego.

**Scenariusz główny:**

1. Użytkownik otwiera moduł „Cele składkowe”.
2. System wyświetla listę celów składkowych.
3. Użytkownik wybiera jeden z celów.
4. System wyświetla szczegóły celu:

   * nazwę,
   * termin,
   * kod do tytułu przelewu,
   * listę płatników,
   * status wpłat każdego płatnika.
5. System automatycznie aktualizuje statusy na podstawie danych ze Skarbca.

**Scenariusze alternatywne:**

* A1. Cel nie posiada przypisanych płatników.
* A2. Wymagana kwota jest ustalana indywidualnie na podstawie pliku CSV.

---

### UC-SKL-03: Wysyłanie przypomnień o składkach

**Aktor:**

* Skarbnik

**Warunki początkowe:**

* Wyświetlone są szczegóły celu składkowego.

**Warunki końcowe:**

* Wybrani płatnicy otrzymali przypomnienie.

**Scenariusz główny:**

1. Użytkownik zaznacza wybranych płatników lub wybiera opcję „Zaznacz zalegających płatników”.
2. Użytkownik wybiera opcję „Wygeneruj CSV do maila zbiorczego”.
3. System generuje plik CSV zawierający adresy e-mail oraz brakujące kwoty.
4. Użytkownik pobiera plik.
5. Użytkownik wybiera opcję „Wyślij przypomnienie systemowe”.
6. System wysyła powiadomienia do zaznaczonych płatników.

**Scenariusze alternatywne:**

* A1. Nie zaznaczono żadnego płatnika.
* A2. Wszyscy płatnicy opłacili składkę — przypomnienia nie są wysyłane.

---

### UC-SKL-04: Edycja i zamknięcie celu składkowego

**Aktor:**

* Skarbnik

**Warunki początkowe:**

* Wyświetlone są szczegóły celu składkowego.

**Warunki końcowe:**

* Cel składkowy został zaktualizowany lub zamknięty.

**Scenariusz główny:**

1. Użytkownik wybiera opcję „Edytuj cel składkowy”.
2. Użytkownik zmienia termin składki.
3. Użytkownik zapisuje zmiany.
4. System wysyła powiadomienie do wszystkich zalegających płatników.
5. Po uregulowaniu wszystkich wpłat użytkownik wybiera opcję „Zamknij cel składkowy”.
6. System zamyka cel składkowy.
7. System zapisuje operację na Osi Czasu.
8. Użytkownik wraca do Centrum Zarządzania.

**Scenariusze alternatywne:**

* A1. Nie wszystkie składki zostały opłacone — system nie pozwala zamknąć celu.
* A2. Użytkownik anuluje edycję celu składkowego.
* A3. Wprowadzony termin jest niepoprawny — system odrzuca zmiany.

---

### UC-PDZ-01: Przeglądanie planu działania

**Aktor:**

* Członek Zarządu

**Warunki początkowe:**

* Użytkownik znajduje się w Centrum Zarządzania.

**Warunki końcowe:**

* Użytkownik zapoznał się ze szczegółami zadania lub wrócił do Centrum Zarządzania.

**Scenariusz główny:**

1. Użytkownik otwiera moduł „Plan działania”.
2. System wyświetla listę zadań przypisanych do kadencji poszczególnych Zarządów.
3. Użytkownik wybiera zadanie.
4. System wyświetla:

   * opis zadania,
   * termin realizacji,
   * listę kroków wymaganych do ukończenia.
5. Po wykonaniu wszystkich wymaganych kroków użytkownik oznacza zadanie jako ukończone.
6. System zapisuje zmianę statusu zadania.
7. Użytkownik wybiera opcję „Wróć do Centrum Zarządzania”.
8. System wyświetla Centrum Zarządzania.

**Scenariusze alternatywne:**

* A1. Nie wszystkie wymagane kroki zostały wykonane — system nie pozwala oznaczyć zadania jako ukończone.
* A2. Użytkownik jedynie przegląda szczegóły zadania.

---

### UC-PDZ-02: Zarządzanie zadaniami planu działania

**Aktor:**

* Wielki Mistrz

**Warunki początkowe:**

* Użytkownik jest zalogowany jako Wielki Mistrz.
* Moduł „Plan działania” jest otwarty.

**Warunki końcowe:**

* Zadanie zostało dodane lub zaktualizowane.

**Scenariusz główny:**

1. Użytkownik wybiera opcję „Dodaj zadanie” lub „Edytuj zadanie”.
2. System wyświetla formularz zadania.
3. Użytkownik wprowadza lub modyfikuje:

   * nazwę,
   * opis,
   * termin realizacji,
   * listę kroków wymaganych do ukończenia.
4. Użytkownik zapisuje zmiany.
5. System aktualizuje plan działania.
6. System rejestruje operację na Osi Czasu.
7. Użytkownik wraca do Centrum Zarządzania.

**Scenariusze alternatywne:**

* A1. Użytkownik anuluje edycję lub dodawanie zadania.
* A2. Formularz zawiera niepoprawne lub niekompletne dane — system wyświetla komunikat i nie zapisuje zmian.

---

### UC-WOR-01: Przeglądanie i analiza organizacji studenckich

**Aktor:**

* Członek Zarządu

**Warunki początkowe:**

* Użytkownik znajduje się w Centrum Zarządzania.

**Warunki końcowe:**

* Użytkownik zapoznał się z danymi organizacji lub wrócił do Centrum Zarządzania.

**Scenariusz główny:**

1. Użytkownik otwiera moduł „Wywiad organizacji”.
2. System wyświetla listę organizacji studenckich, które miały kontakt z Bractwem.
3. Użytkownik wybiera organizację.
4. System wyświetla kartę wywiadu zawierającą:

   * nazwę organizacji,
   * e-maile kontaktowe,
   * obszar działania,
   * kierownictwo,
   * rok założenia,
   * listę członków,
   * historię wspólnych wydarzeń,
   * opinie poprzednich Zarządów.
5. Użytkownik przegląda dane.
6. Użytkownik zamyka widok szczegółów.

**Scenariusze alternatywne:**

* A1. Organizacja nie posiada pełnych danych — system wyświetla dostępne informacje.
* A2. Brak historii współpracy — sekcja jest ukryta.
* A3. Użytkownik nie wybiera organizacji i opuszcza moduł.

---

### UC-WOR-02: Edycja danych i dodawanie opinii o organizacji

**Aktor:**

* Wielki Mistrz

**Warunki początkowe:**

* Wyświetlona jest karta wywiadu organizacji.

**Warunki końcowe:**

* Dane organizacji lub opinia zostały zaktualizowane.

**Scenariusz główny:**

1. Użytkownik dodaje opinię o organizacji w imieniu aktualnego Zarządu.
2. Użytkownik edytuje wybrane informacje o organizacji.
3. Użytkownik zapisuje zmiany.
4. System rejestruje zmiany na Osi Czasu w Centrum Zarządzania.
5. System aktualizuje kartę organizacji.

**Scenariusze alternatywne:**

* A1. Użytkownik nie posiada uprawnień do edycji niektórych pól.
* A2. Wprowadzono niepoprawne dane — system odrzuca zmiany.
* A3. Użytkownik anuluje edycję.

---

### UC-WOR-03: Wyszukiwanie organizacji

**Aktor:**

* Członek Zarządu

**Warunki początkowe:**

* Moduł „Wywiad organizacji” jest otwarty.

**Warunki końcowe:**

* System wyświetlił listę dopasowanych organizacji.

**Scenariusz główny:**

1. Użytkownik wpisuje zapytanie w wyszukiwarce (np. e-mail lub nazwę).
2. System przeszukuje bazę organizacji.
3. System wyświetla powiązane organizacje.
4. Użytkownik wybiera jedną z wyników i przechodzi do karty organizacji.

**Scenariusze alternatywne:**

* A1. Brak wyników wyszukiwania — system wyświetla komunikat.

---

### UC-RSS-01: Przeglądanie i filtrowanie rozporządzeń SSUJ

**Aktor:**

* Członek Zarządu

**Warunki początkowe:**

* Użytkownik znajduje się w Centrum Zarządzania.
* Użytkownik jest zalogowany kontem Microsoft (lub zostaje do tego poproszony).

**Warunki końcowe:**

* Użytkownik zapoznał się z listą rozporządzeń lub wrócił do Centrum Zarządzania.

**Scenariusz główny:**

1. Użytkownik otwiera moduł „Rozporządzenia SSUJ”.
2. System weryfikuje logowanie Microsoft.
3. System wyświetla listę rozporządzeń podzieloną na:

   * „Nieprzeczytane”
   * „Przeczytane”
4. Użytkownik stosuje filtry:

   * rok,
   * aktualność,
   * tematyka.
5. System aktualizuje listę rozporządzeń.
6. Użytkownik wybiera rozporządzenie.
7. System wyświetla jego treść.

**Scenariusze alternatywne:**

* A1. Brak logowania Microsoft — system wymusza logowanie.
* A2. Brak rozporządzeń spełniających filtry — system wyświetla pustą listę.
* A3. Użytkownik nie wybiera żadnego dokumentu.

---

### UC-RSS-02: Analiza i aktualizacja rozporządzenia

**Aktor:**

* Członek Zarządu

**Warunki początkowe:**

* Wyświetlone jest wybrane rozporządzenie.

**Warunki końcowe:**

* Rozporządzenie zostało oznaczone i opisane przez użytkownika.

**Scenariusz główny:**

1. Użytkownik czyta treść rozporządzenia.
2. Użytkownik wpisuje streszczenie dokumentu.
3. Użytkownik oznacza aktualność rozporządzenia.
4. System zapisuje zmiany.
5. System rejestruje operację na Osi Czasu w Centrum Zarządzania.

**Scenariusze alternatywne:**

* A1. Streszczenie jest puste — system nie pozwala zapisać zmian.
* A2. Użytkownik anuluje edycję.
* A3. Oznaczenie aktualności nie zostało zmienione — system zapisuje tylko streszczenie.
* A4. Użytkownik nie ma uprawnień Kasztelana — oznaczenie aktualności nie zostanie zmienione.

---

### UC-RSS-03: Weryfikacja powiązanych rozporządzeń

**Aktor:**

* Kasztelan

**Warunki początkowe:**

* Użytkownik przegląda rozporządzenie.

**Warunki końcowe:**

* System zaktualizował status powiązanych rozporządzeń.

**Scenariusz główny:**

1. System wyszukuje powiązane rozporządzenia o podobnym tytule.
2. System prezentuje listę powiązanych dokumentów.
3. System prosi użytkownika o weryfikację ich aktualności.
4. Użytkownik oznacza rozporządzenia jako aktualne lub nieaktualne.
5. System zapisuje zmiany.
6. System rejestruje operację na Osi Czasu.

**Scenariusze alternatywne:**

* A1. Brak powiązanych rozporządzeń — system pomija etap weryfikacji.
* A2. Użytkownik pomija weryfikację — system zapisuje brak zmian.
* A3. System nie znajduje podobieństw — brak listy powiązań.

---

### UC-WNI-01: Przeglądanie i analiza wniosków

**Aktor:**

* Członek Zarządu

**Warunki początkowe:**

* Użytkownik znajduje się w Centrum Zarządzania.
* Użytkownik ma dostęp do modułu „Wnioski”.

**Warunki końcowe:**

* Użytkownik zapoznał się ze szczegółami wybranego wniosku lub wrócił do listy.

**Scenariusz główny:**

1. Użytkownik otwiera moduł „Wnioski”.
2. System wyświetla listę dotychczasowych wniosków.
3. System umożliwia:

   * sortowanie według daty złożenia,
   * sortowanie według daty ostatniej modyfikacji,
   * grupowanie według statusu akceptacji.
4. Użytkownik wybiera wniosek.
5. System wyświetla szczegóły wniosku:

   * nazwa,
   * data złożenia,
   * data ostatniej modyfikacji,
   * status akceptacji SSUJ,
   * podgląd dokumentu.
6. Użytkownik zamyka widok szczegółów.

**Scenariusze alternatywne:**

* A1. Brak wniosków — system wyświetla pustą listę.
* A2. Użytkownik nie wybiera żadnego wniosku.
* A3. Brak uprawnień do podglądu dokumentu — system blokuje dostęp.

---

### UC-WNI-02: Tworzenie nowego wniosku na bazie istniejącego

**Aktor:**

* Kasztelan

**Warunki początkowe:**

* Lista wniosków jest wyświetlona.
* Użytkownik ma dostęp do edycji.

**Warunki końcowe:**

* Nowy wniosek zostaje zapisany ze statusem „Czeka na akceptację”.

**Scenariusz główny:**

1. Użytkownik wybiera ikonę „+” przy istniejącym wniosku.
2. System tworzy kopię wniosku w trybie edycji.
3. Użytkownik wprowadza zmiany w treści.
4. Użytkownik zapisuje wniosek.
5. System dodaje nowy wniosek do listy.
6. System nadaje status „Czeka na akceptację”.

**Scenariusze alternatywne:**

* A1. Użytkownik anuluje tworzenie — wniosek nie zostaje zapisany.
* A2. Błąd zapisu — system nie tworzy nowego wpisu.

---

### UC-WNI-03: Edycja istniejącego wniosku

**Aktor:**

* Kasztelan

**Warunki początkowe:**

* Użytkownik przegląda listę wniosków.
* Wniosek istnieje i jest dostępny do edycji.

**Warunki końcowe:**

* Wniosek zostaje zaktualizowany, a data modyfikacji odświeżona.

**Scenariusz główny:**

1. Użytkownik wybiera ikonę edycji przy wniosku.
2. System umożliwia edycję:

   * nazwy,
   * daty,
   * statusu,
   * załączonego dokumentu.
3. Użytkownik wprowadza zmiany.
4. Użytkownik zapisuje zmiany.
5. System aktualizuje wniosek.
6. System aktualizuje datę ostatniej modyfikacji.
7. System zapisuje zdarzenie na Osi Czasu w Centrum Zarządzania.

**Scenariusze alternatywne:**

* A1. Użytkownik nie zapisuje zmian — system przywraca poprzednią wersję.
* A2. Niepoprawny format dokumentu — system odrzuca zapis.
* A3. Konflikt wersji — system wymaga ponownego odświeżenia danych.

---

### UC-SKA-01: Przegląd salda i historii transakcji

**Aktor:**

* Członek Zarządu

**Warunki początkowe:**

* Użytkownik znajduje się w Centrum Zarządzania.
* Użytkownik ma dostęp do modułu „Skarbiec”.

**Warunki końcowe:**

* Użytkownik zapoznał się z saldem, historią transakcji lub innymi sekcjami modułu.

**Scenariusz główny:**

1. Użytkownik otwiera moduł „Skarbiec”.
2. System wyświetla:

   * saldo konta,
   * numer konta,
   * skróty do:

      * historii transakcji,
      * spisu płatników,
      * spisu firm.
3. Użytkownik rozwija historię transakcji.
4. System wyświetla listę transakcji zawierającą:

   * tytuł operacji,
   * kwotę przelewu,
   * link do odbiorcy/adresata,
   * saldo po transakcji.

**Scenariusze alternatywne:**

* A1. Brak transakcji — system wyświetla pustą historię.
* A2. Brak dostępu do danych finansowych — system blokuje widok.

---

### UC-SKA-02: Import historii transakcji z pliku CSV

**Aktor:**

* Skarbnik

**Warunki początkowe:**

* Użytkownik znajduje się w module „Skarbiec”.
* Użytkownik posiada plik CSV z historią transakcji.

**Warunki końcowe:**

* Historia transakcji zostaje zaktualizowana o nowe dane.

**Scenariusz główny:**

1. Użytkownik wybiera opcję „Wczytaj historię”.
2. System wyświetla okno importu pliku CSV.
3. Użytkownik dodaje plik CSV.
4. System analizuje dane transakcji.
5. System dodaje transakcje do historii Skarbca.
6. System weryfikuje odbiorców i nadawców:

   * płatnicy,
   * firmy.
7. System przypisuje transakcje do istniejących obiektów lub wymaga ich utworzenia.
8. Użytkownik uzupełnia brakujące dane.
9. System zapisuje zaktualizowaną historię transakcji.

**Scenariusze alternatywne:**

* A1. Nieprawidłowy format CSV — system odrzuca plik.
* A2. Brak możliwości przypisania transakcji — system wstrzymuje import.
* A3. Użytkownik przerywa import — brak zmian w systemie.

---

### UC-SKA-03: Zarządzanie płatnikami

**Aktor:**

* Skarbnik

**Warunki początkowe:**

* Dane transakcji są dostępne w systemie.

**Warunki końcowe:**

* Dane płatników są zaktualizowane lub uzupełnione.

**Scenariusz główny:**

1. Użytkownik rozwija spis płatników.
2. System wyświetla listę płatników:

   * imię i nazwisko,
   * numer konta lub telefonu.
3. Użytkownik wybiera płatnika.
4. System wyświetla szczegóły:

   * adres zamieszkania,
   * e-mail,
   * powiązany profil użytkownika (jeśli istnieje).
5. Użytkownik wybiera opcję „Edytuj”.
6. Użytkownik modyfikuje dane.
7. System zapisuje zmiany.

**Scenariusze alternatywne:**

* A1. Brak powiązanego profilu — system wyświetla tylko dane podstawowe.
* A2. Użytkownik anuluje edycję — brak zmian.

---

### UC-SKA-04: Zarządzanie firmami

**Aktor:**

* Skarbnik

**Warunki początkowe:**

* Dane firm istnieją w systemie.

**Warunki końcowe:**

* Dane firm są zaktualizowane lub uzupełnione.

**Scenariusz główny:**

1. Użytkownik rozwija spis firm.
2. System wyświetla listę firm:

   * nazwa firmy,
   * numer konta.
3. Użytkownik wybiera firmę.
4. System wyświetla szczegóły:

   * adres siedziby,
   * e-mail,
   * numery telefonów,
   * opis działalności.
5. Użytkownik wybiera opcję „Edytuj”.
6. Użytkownik aktualizuje dane.
7. System zapisuje zmiany.
8. System rejestruje operację na Osi Czasu w Centrum Zarządzania.

**Scenariusze alternatywne:**

* A1. Brak pełnych danych firmy — system umożliwia częściową edycję.
* A2. Konflikt danych — system wymaga ponownego zatwierdzenia.

---

### UC-OCZ-01: Przegląd Osi Czasu działań Zarządu

**Aktor:**

* Członek Zarządu

**Warunki początkowe:**

* Użytkownik znajduje się w Centrum zarządzania.
* W systemie istnieją zapisane akcje Zarządu.

**Warunki końcowe:**

* Użytkownik zapoznał się z historią działań lub opuścił moduł.

**Scenariusz główny:**

1. Użytkownik otwiera moduł „Oś Czasu”.
2. System wyświetla pionową oś czasu skierowaną ku górze.
3. System prezentuje listę akcji zawierającą:

   * funkcję użytkownika wykonującego akcję,
   * moduł, w którym wykonano akcję,
   * datę i godzinę wykonania.
4. Użytkownik przewija listę osi czasu.

**Scenariusze alternatywne:**

* A1. Brak zapisanych akcji — system wyświetla pustą oś czasu.
* A2. Brak uprawnień — system blokuje dostęp do modułu.

---

### UC-OCZ-02: Zmiana orientacji osi czasu

**Aktor:**

* Członek Zarządu

**Warunki początkowe:**

* Oś czasu jest wyświetlona w widoku pionowym.

**Warunki końcowe:**

* Oś czasu zostaje wyświetlona w orientacji poziomej.

**Scenariusz główny:**

1. Użytkownik wybiera opcję „Odwróć oś o 90°”.
2. System zmienia orientację osi czasu na poziomą.
3. System zachowuje wszystkie aktualne dane i filtry.

**Scenariusze alternatywne:**

* A1. Błąd renderowania — system przywraca widok pionowy.
* A2. Użytkownik ponownie aktywuje opcję — system przełącza widok z powrotem.

---

### UC-OCZ-03: Filtrowanie i analiza działań

**Aktor:**

* Członek Zarządu

**Warunki początkowe:**

* Oś czasu jest wyświetlona (dowolna orientacja).

**Warunki końcowe:**

* Widok osi czasu jest zawężony do wybranych kryteriów.

**Scenariusz główny:**

1. Użytkownik wybiera filtrację.
2. System umożliwia filtrowanie według:

   * funkcji wykonującego,
   * miesiąca wykonania.
3. Użytkownik wybiera kryteria.
4. System aktualizuje widok osi czasu.
5. System wyświetla tylko pasujące akcje.

**Scenariusze alternatywne:**

* A1. Brak wyników — system wyświetla pustą oś czasu.
* A2. Użytkownik usuwa filtry — system przywraca pełny widok.

---

### UC-OCZ-04: Tryb prezentacji osi czasu

**Aktor:**

* Członek Zarządu

**Warunki początkowe:**

* Oś czasu jest otwarta.

**Warunki końcowe:**

* System przechodzi w tryb pełnoekranowy lub z niego wychodzi.

**Scenariusz główny:**

1. Użytkownik wybiera opcję „Tryb prezentacji”.
2. System przełącza widok na pełny ekran.
3. Oś czasu zostaje ustawiona poziomo i skierowana w prawo.
4. Użytkownik nawiguję po osi za pomocą klawiszy strzałek.
5. Użytkownik wybiera „Wróć”.
6. System opuszcza tryb prezentacji.
7. System umożliwia powrót do Centrum Zarządzania.

**Scenariusze alternatywne:**

* A1. Brak aktywności użytkownika — system pozostaje w trybie prezentacji.
* A2. Użytkownik zamyka przeglądarkę — stan nie jest zapisywany.
