# PODRÓŻE UŻYTKOWNIKA

---

## STRONA czapkuj.pl

---
### OGÓLNODOSTĘPNE FUNKCJE STRONY

1. Użytkownik otwiera stronę `czapkuj.pl`.
2. System wyświetla stronę główną zawierającą powitanie oraz opis celu serwisu. 
Ikona trybu wyświetlania w prawym górnym rogu jest ustawiona na tryb `"Odwiedzający"`.
3. Użytkownik wybiera ikonę menu (hamburger).
4. System wyświetla listę odnośników do podstron.
5. Użytkownik otwiera podstronę `Kalendarz wydarzeń`.
6. System wyświetla kalendarz przeszłych i nadchodzących wydarzeń Bractwa z widokiem ustawionym na bieżący miesiąc. 
Użytkownik może dodać kalendarz do Kalendarza Google.
7. Użytkownik otwiera podstronę `Sklep`.
8. System wyświetla trzy dostępne opcje:
   - `Zamów własną czapkę!`,
   - `Zamów piny belgijskie`,
   - `Zamów piny własnego projektu`.
9. Użytkownik wybiera opcję `Zamów własną czapkę!`.
10. System wyświetla ofertę czapki studenckiej oraz formularz uprawniający do uzyskania 50% zniżki. 
Formularz zawiera pola:
    - adres e-mail,
    - imię i nazwisko,
    - uczelnia,
    - wydział,
    - numer albumu.
11. Użytkownik uzupełnia formularz i zatwierdza go. 
Powiadomienie zawierające dane z formularza zostaje przesłane do `Powiadomień` w `Centrum Zarządzania`.
12. Użytkownik wybiera opcję `Wróć`, a następnie `Zamów piny belgijskie`.
13. System prosi użytkownika o zalogowanie przy użyciu konta Google.
14. Użytkownik loguje się.
15. System przekierowuje użytkownika do strony sklepu. 
Szczegóły działania opisano w scenariuszu [PIN – Piny belgijskie, Użytkownik: ODWIEDZAJĄCY](#użytkownik-odwiedzający).
16. Użytkownik wybiera opcję `Wróć`, a następnie `Zamów piny własnego projektu`.
17. System wyświetla stronę zawierającą:
    - instrukcję przygotowania pliku PNG ze wzorem pinów,
    - szablon GIMP do przygotowania pliku PNG,
    - formularz umożliwiający podanie adresu e-mail, przesłanie pliku PNG oraz określenie liczby pinów.
18. Użytkownik przesyła plik PNG ze wzorem pinów oraz podaje liczbę zamawianych egzemplarzy.
19. System oblicza koszt realizacji zamówienia w czasie rzeczywistym i wyświetla go obok pola z liczbą pinów.
20. Użytkownik wybiera opcję `"Złóż zamówienie"`.
21. System przekierowuje użytkownika do strony płatności.
22. Po pomyślnym zakończeniu płatności system wyświetla potwierdzenie przyjęcia płatności.
23. Powiadomienie zawierające dane zamówienia zostaje przesłane do `Powiadomień` w `Centrum Zarządzania`.
24. Użytkownik otwiera podstronę `Blog`.
25. System wyświetla listę dostępnych blogów. Każda pozycja zawiera:
    - tytuł będący odnośnikiem do bloga,
    - krótki opis tematyki bloga,
    - początek najnowszego wpisu zakończony wielokropkiem oraz odnośnik `"Czytaj dalej"` 
    prowadzący do pełnej treści wpisu.
26. Użytkownik wybiera jeden z blogów.
27. Blog umożliwia:
    - czytanie wpisów,
    - wybór wpisu z listy,
    - dodawanie komentarzy. W tym celu użytkownik musi być zalogowany, 
    a każdy komentarz wymaga zatwierdzenia przez moderatora przed publikacją. 
    System informuje użytkownika o procesie moderacji.
28. Użytkownik otwiera podstronę `Czapkowy słowniczek`.
29. System wyświetla następujące sekcje:
    - Czapkowe zwyczaje (wykorzystuje dane z modułu [Encyklopedia](#enc--encyklopedia)),
    - Czapkowy żargon (wykorzystuje dane z modułu [Encyklopedia](#enc--encyklopedia)),
    - Łacińskie zwroty (wykorzystuje dane z modułu [Słowniczek łaciński](#sll--słowniczek-łaciński)),
    - Czapkowe cytaty (wykorzystuje dane z modułu [Cytaty](#cyt--cytaty)),
    - Znane Czapki.

    Po wybraniu jednej z sekcji system wyświetla listę odnośników do powiązanych artykułów.
30. Użytkownik wybiera ikonę czatu.
31. System prosi o zalogowanie, jeśli użytkownik nie jest jeszcze zalogowany.
32. Po zalogowaniu system wyświetla okno czatu z moderatorem lub administratorem. Historia wiadomości jest zapisywana, 
dzięki czemu użytkownik może kontynuować rozmowę podczas kolejnych wizyt.
33. Użytkownik zamyka okno czatu i wybiera ikonę `"Zgłoś problem ze stroną"`.
34. System wyświetla formularz zgłoszenia problemu z polem tekstowym oraz informacją, że w przypadku potrzeby uzyskania 
pomocy użytkownik może skorzystać z czatu.
35. Użytkownik wysyła formularz, a następnie wybiera ikonę `"Social media"`.
36. System wyświetla odnośniki do oficjalnych profili Bractwa w mediach społecznościowych.
37. Użytkownik wybiera ikonę `"Postaw nam piwo"`.
38. System wyświetla dane do przelewu umożliwiającego dobrowolne wsparcie Bractwa.

---

### AKCJE KONTA NA czapkuj.pl

---

#### TRYB: ODWIEDZAJĄCY

1. Użytkownik wybiera ikonę konta.
2. System wyświetla listę dostępnych akcji:
    - `"Poproś o awans na beana"`
    - `"Powiadomienia"`
    - `"Zaloguj/zarejestruj"` – widoczne dla niezalogowanych.
    - `"Wyloguj"` – widoczne dla zalogowanych.
3. Użytkownik wybiera opcję `"Poproś o awans na beana"`.
4. Jeśli użytkownik nie jest zalogowany, system prosi go o zalogowanie się.
5. Po zalogowaniu system wyświetla formularz zawierający:
    - opis korzyści wynikających z awansu,
    - opis procedury awansu,
    - pole do wprowadzenia 6-cyfrowego kodu,
    - przycisk `"Poproś o awans"`.
6. Użytkownik uzupełnia formularz i zatwierdza go.
7. Dane z formularza zostają przesłane do `Powiadomień` na kontach moderatorskich i administratorskich.
8. Po zaakceptowaniu prośby przez moderatora/administratora użytkownik otrzymuje powiadomienie z prośbą o uzupełnienie 
danych.
9. Użytkownik otwiera formularz zawierający pola:
    - imię,
    - nazwisko,
    - zaimki,
    - przezwiska (oddzielone przecinkami),
    - pierwsze wydarzenie czapkowe (wybór z listy lub zgłoszenie nowego wydarzenia).

   W przypadku wybrania opcji dodania nowego wydarzenia, po zatwierdzeniu formularza system wyświetla kolejny formularz 
zawierający pola:
    - data wydarzenia,
    - miejsce,
    - nazwa wydarzenia,
    - uwagi (opcjonalnie).
10. Możliwy jest również awans bezpośrednio do statusu `"Członek"` z pominięciem statusu `"Bean"`. 
Zakres formularza zależy od rodzaju użytego 6-cyfrowego kodu. 
Jeżeli kod uprawnia do bezpośredniego awansu, system wyświetla dodatkowe pola:
    - wydarzenie chrzcielne (wybór z listy),
    - rodzice czapkowi (wybór z listy),
    - zadanie czapkowe,
    - dzieci czapkowe (wybór z listy),
    - posiadane czapki (wybór z listy),
    - członkostwo w organizacjach (wybór z listy).

    Jeżeli wymagana wartość nie znajduje się na liście, użytkownik może wybrać opcję jej dodania. 
System wyświetla wówczas odpowiedni formularz, którego treść zostaje przesłana do moderatorów w celu rozpatrzenia.
11. Dane z formularzów zostają wysłane do moderatorów/administratora
12. Po wypełnieniu formularzy system informuje użytkownika, że moderatorzy muszą wykonać ostatni etap procesu awansu.
13. Po zakończeniu procesu status użytkownika oraz tryb wyświetlania strony zostają zmienione na 
`"Czapkowicz"`.
14. Użytkownik może zmieniać tryb wyświetlania strony za pomocą ikony trybu wyświetlania znajdującej się w prawym górnym 
rogu strony.
15. Użytkownik wybiera opcję `"Powiadomienia"`.
16. System wyświetla listę powiadomień. Nieprzeczytane powiadomienia są oznaczone czerwoną ikoną wykrzyknika.
17. Użytkownik wybiera jedno z powiadomień.
18. System wyświetla pełną treść powiadomienia oraz przycisk `"Oznacz jako przeczytane"`.
19. Użytkownik oznacza powiadomienie jako przeczytane, a następnie wybiera opcję `"Wróć"`.
20. Użytkownik wybiera opcję `"Wyloguj"`.
21. System wylogowuje użytkownika.
22. Użytkownik wybiera opcję `"Zaloguj/zarejestruj"`.
23. System umożliwia zalogowanie lub rejestrację za pomocą konta Google.

---

#### TRYB: CZAPKOWICZ

1. Użytkownik wybiera ikonę konta.
2. System wyświetla listę dostępnych akcji:
    - `"Bio"`
    - `"Dashboard"`
    - `"Powiadomienia"`
    - `"Zaloguj/zarejestruj"` – widoczne dla niezalogowanych.
    - `"Wyloguj"` – widoczne dla zalogowanych.
3. Użytkownik wybiera opcję `"Bio"`.
4. System wyświetla widok biografii użytkownika. Dostępne są:
   - lista informacji osobowych:
       - **imię** – edytowalne za zgodą moderatora,
       - **imię czapkowe** – edytowalne za zgodą moderatora,
       - **nazwisko** – edytowalne za zgodą moderatora,
       - **zaimki** – edytowalne,
       - **przezwiska** – edytowalne,
       - **pierwsze wydarzenie** – edytowalne za zgodą moderatora,
       - **rodzice czapkowi** – edytowalne za zgodą moderatora,
       - **posiadane czapki** – edytowalne za zgodą moderatora,
       - **członkostwo w organizacjach** – edytowalne za zgodą moderatora,
       - **coś o sobie** – edytowalne.

     Użytkownicy posiadający flair `"Członek"` lub `"Weteran"` mają dodatkowo dostępne pola:
     - **wydarzenie chrzcielne** – edytowalne za zgodą moderatora,
     - **zadanie czapkowe** – edytowalne za zgodą moderatora,
     - **dzieci czapkowe** – edytowalne za zgodą moderatora.

     Dodatkowo dostępne są:
     - **lista odznak (flairs)** – nadawanych przez moderatorów,
     - **zdjęcie profilowe** – edytowalne za zgodą moderatora,
     - **przycisk podglądu drzewa genealogicznego** – generowanego automatycznie,
     - **przycisk `"Poproś o usunięcie flagi"`** – umożliwiający wysłanie prośby do moderatora o usunięcie wybranej flagi,
     - **przycisk `"Poproś o nadanie flagi"`** – umożliwiający wysłanie prośby o nadanie nowej flagi,
     - **przycisk `"Poproś o zmianę statusu na Członka"`** – wysyłający prośbę o zmianę statusu. W razie pozytywnego 
     rozpatrzenia użytkownik dostaje w powiadomieniu formularz do wypełnienia, który po zatwierdzeniu przez 
     moderatora zmienia status użytkownika na `"Członek"`,
     - **przycisk `"Poproś o zmianę statusu na Weterana"`** – wysyłający prośbę o zmianę statusu.
5. Użytkownik wybiera opcję `"Dashboard"`.
6. System wyświetla komunikat powitalny w postaci `"Witaj, <imię>!"` oraz siatkę kafelków prowadzących do modułów:
    - [Cytaty](#cyt--cytaty)
    - [Drzewo genealogiczne](#idg--interaktywne-drzewo-genealogiczne)
    - [Encyklopedia](#enc--encyklopedia)
    - [Kalendarz](#kal--kalendarz)
    - [Kodeks](#kod--kodeks)
    - [Kronika](#kro--kronika)
    - [Mapa](#map--mapa)
    - [Piny belgijskie](#pin--piny-belgijskie)
    - [Składki](#skl--składki)
    - [Słowniczek łaciński](#sll--słowniczek-łaciński)
    - [Śpiewnik](#spi--śpiewnik)
7. Pozostałe akcje konta działają analogicznie jak w trybie `"Odwiedzający"`.

---

#### TRYB: CZŁONEK ZARZĄDU

Obejmuje tryby: `Wielki Mistrz`, `Kasztelan`, `Skarbnik`, `Sekretarz` oraz `Cantandi`.

Każdy członek Zarządu może przeglądać moduły ze wszystkich paneli w `Centrum Zarządzania`, 
jednak wprowadzanie zmian jest możliwe wyłącznie w modułach przypisanych do pełnionej funkcji.

1. Użytkownik wybiera ikonę konta.
2. System wyświetla listę dostępnych akcji:
    - `"Bio"`
    - `"Dashboard"`
    - `"Centrum Zarządzania"`
    - `"Powiadomienia"`
    - `"Zaloguj/zarejestruj"` – widoczne dla niezalogowanych.
    - `"Wyloguj"` – widoczne dla zalogowanych.
3. Użytkownik wybiera opcję `"Centrum Zarządzania"`.
4. System wyświetla komunikat powitalny w postaci `"Witaj, <funkcja w Zarządzie>!"` oraz panele zawierające moduły:
    - `Panel Wspólny`
        - [Oś Czasu](#ocz--oś-czasu)
    - `Panel Wielkiego Mistrza`
        - [Plan działania](#pdz--plan-działania)
        - [Wywiad organizacji](#wor--wywiad-organizacji)
    - `Panel Kasztelana`
        - [Rozporządzenia SSUJ](#rss--rozporządzenia-ssuj)
        - [Wywiad miejscówek](#użytkownik-kasztelan)
        - [Wnioski](#wni--wnioski)
    - `Panel Skarbnika`
        - [Skarbiec](#ska--skarbiec)
        - [Cele składkowe](#użytkownik-skarbnik-1)
        - [Piny belgijskie zamówienie](#użytkownik-skarbnik)
    - `Panel Sekretarza`
        - [Edytuj kalendarz](#kal--kalendarz)
    - `Panel Cantandiego`
        - [Edytuj śpiewnik](#użytkownik-cantandi)
5. Pozostałe akcje konta działają analogicznie jak w trybie `"Czapkowicz"`.

---

#### TRYB: MODERATOR

1. Użytkownik wybiera ikonę konta.
2. System wyświetla listę dostępnych akcji:
    - `"Powiadomienia"`
    - `"Panel moderatora"`
    - `"Dashboard"`
    - `"Komentarze"`
    - `"Rozpatrz prośby"`
    - `"Wygeneruj kody awansu na beana"`
    - `"Logi zmian"`
    - `"Zaloguj/zarejestruj"` – widoczne dla niezalogowanych.
    - `"Wyloguj"` – widoczne dla zalogowanych.
3. Użytkownik wybiera opcję `"Panel moderatora"`.
4. System wyświetla panel administracyjny umożliwiający zarządzanie danymi w sposób analogiczny do panelu administratora Django.
5. Użytkownik wybiera opcję `"Komentarze"`.
6. System wyświetla listę komentarzy z możliwością filtrowania według statusu moderacji. Każda pozycja zawiera:
    - pole wyboru,
    - datę i godzinę dodania komentarza,
    - adres e-mail autora będący odnośnikiem do jego konta,
    - tytuł komentowanego wpisu,
    - treść komentarza.
7. Użytkownik zaznacza wybrane komentarze, a następnie wybiera opcję `"Zatwierdź"` lub `"Odrzuć"`.
8. Autor komentarza otrzymuje powiadomienie o decyzji moderatora. W przypadku zatwierdzenia komentarz staje się publicznie widoczny.
9. Użytkownik wybiera odnośnik do konta autora komentarza.
10. System wyświetla okno zawierające karty:
    - **Konto**,
    - **Bio** – dostępną wyłącznie dla użytkowników posiadających status `"Czapkowicz"`.

    Karta **Konto** zawiera:
    - adres e-mail,
    - datę rejestracji,
    - historię aktywności,
    - przycisk `"Banuj"`.

    Karta **Bio** wyświetla biografię użytkownika, jeśli ją posiada.
11. Użytkownik wybiera opcję `"Banuj"`.
12. System wyświetla możliwość wyboru czasu trwania blokady oraz opcję `"Do odwołania"`.
13. Użytkownik wybiera jedną z opcji i zatwierdza decyzję.
14. Zablokowany użytkownik otrzymuje powiadomienie o nałożeniu blokady. Od tego momentu nie może komentować, 
korzystać z czatu ani zgłaszać problemów ze stroną.
15. Użytkownik wybiera opcję `"Rozpatrz prośby"`.
16. System wyświetla listę próśb dotyczących zmian informacji, statusów, flag oraz innych danych. Każda pozycja zawiera:
    - pole wyboru,
    - datę i godzinę zgłoszenia,
    - adres e-mail zgłaszającego będący odnośnikiem do jego konta,
    - treść prośby.
17. Użytkownik zaznacza wybrane prośby, a następnie wybiera opcję `"Zatwierdź"` lub `"Odrzuć"`.
18. W zależności od rodzaju prośby system:
    - **zmienia informacje w `Bio`** – aktualizuje wskazane dane,
    - **zmienia status użytkownika** – nadaje nowy status,
    - **nadaje flagę** – umożliwia wybór istniejącej flagi lub utworzenie nowej poprzez podanie jej nazwy. 
    Po zatwierdzeniu flaga zostaje przypisana do użytkownika,
    - **usuwa flagę** – usuwa wskazaną flagę z `Bio` użytkownika,
    - **rozpatruje prośbę o awans na beana** – zmienia status użytkownika na `"Czapkowicz"` 
    lub przesyła formularz uzupełnienia danych, jeśli jest on wymagany.
19. Użytkownik wybiera opcję `"Wygeneruj kody awansu na beana"`.
20. Użytkownik podaje liczbę kodów do wygenerowania.
21. System wyświetla wygenerowane kody wraz z datą utworzenia oraz datą wygaśnięcia. Każdy kod jest jednorazowy i może 
zostać wykorzystany tylko raz.
22. Użytkownik wybiera opcję `"Wydrukuj kody"` i zatwierdza operację.
23. System generuje plik PDF zawierający listę kodów wraz z datami wygenerowania i wygaśnięcia, przygotowany w układzie 
ułatwiającym wycięcie pojedynczych kodów.
24. Użytkownik wybiera opcję `"Logi zmian"`.
25. System wyświetla listę zmian wprowadzonych przez moderatorów i administratorów. Każda pozycja zawiera:
    - datę i godzinę wprowadzenia zmiany,
    - adres e-mail użytkownika, który wprowadził zmianę,
    - opis zmiany.
26. Pozostałe akcje konta działają analogicznie jak w trybie `"Czapkowicz"`.
27. Użytkownik wybiera ikonę zmiany trybu wyświetlania w prawym górnym rogu strony i przełącza się do 
trybu `"Czapkowicz"` lub, jeśli ma odpowiednie uprawnienia, do jednego z trybów Zarządu. 
W tych trybach ponownie uzyskuje dostęp do funkcji komentowania oraz własnego `Bio`, 
które nie są dostępne w trybie `"Moderator"`.

---

### TRYB: ADMINISTRATOR

1. Użytkownik wybiera ikonę konta.
2. System wyświetla listę dostępnych akcji:

    - `"Powiadomienia"`
    - `"Dashboard"`
    - `"Wygeneruj specjalne kody"`
    - `"Zaloguj/zarejestruj"` – widoczne dla niezalogowanych.
    - `"Wyloguj"` – widoczne dla zalogowanych.
3. Użytkownik wybiera opcję `"Wygeneruj specjalne kody"`.
4. Użytkownik wybiera opcję `"Dodaj nową pozycję"`, a następnie określa typ generowanych kodów:
    - `"Kod awansu na Beana"`
    - `"Kod awansu na Członka"`
    - `"Kod awansu na Weterana"`
    - `"Kod awansu na Wielkiego Mistrza"`
    - `"Kod awansu na Kasztelana"`
    - `"Kod awansu na Skarbnika"`
    - `"Kod awansu na Sekretarza"`
    - `"Kod awansu na Cantandiego"`
    - `"Kod awansu na Moderatora"`
    - `"Kod awansu na Administratora"`

   oraz liczbę kodów do wygenerowania.
5. System wyświetla wygenerowane kody wraz z datą utworzenia oraz datą wygaśnięcia.
Każdy kod jest jednorazowy i może zostać wykorzystany tylko raz.
6. Użytkownik może wielokrotnie powtarzać krok 4, a następnie wybiera opcję `"Wydrukuj kody"` i zatwierdza operację.
7. System generuje plik PDF zawierający listę kodów wraz z datami wygenerowania i wygaśnięcia, 
przygotowany w układzie ułatwiającym wycięcie pojedynczych kodów.
8. Pozostałe akcje konta działają analogicznie jak w trybie `"Moderator"`.
9. Administrator ma dostęp do wszystkich trybów wyświetlania strony, w tym do wszystkich trybów Zarządu, 
co umożliwia mu wprowadzanie zmian we wszystkich panelach `Centrum Zarządzania`. 
Funkcje komentowania oraz korzystania z `Bio` są dostępne w trybach `"Odwiedzający"`, `"Czapkowicz"` i zarządowych. 

---

## APLIKACJE OGÓLNODOSTĘPNE

---

### KAL – Kalendarz

#### Użytkownik: CZŁONEK

1. Użytkownik otwiera moduł `„Kalendarz”` z poziomu `dashboardu`.
2. System wyświetla kalendarz zawierający wydarzenia Bractwa.
3. Po wybraniu wydarzenia system wyświetla jego szczegóły, obejmujące nazwę, datę rozpoczęcia, datę zakończenia,
   miejsce oraz typ wydarzenia. W przypadku wydarzeń zakończonych wyświetlana jest również lista uczestników.
4. Użytkownik zamyka okno szczegółów wydarzenia.
5. Użytkownik wybiera opcję `„Skopiuj kalendarz do Kalendarza Google”`.
6. System dodaje kalendarz Bractwa do kalendarza użytkownika w usłudze Google Calendar.
7. Użytkownik wybiera opcję `„Wróć do dashboardu”`.
8. System wyświetla `Dashboard`.

#### Użytkownik: SEKRETARZ

1. Użytkownik otwiera moduł `"Edytuj kalendarz"` z `Panelu Sekretarza`.
2. System wyświetla kalendarz zawierający wydarzenia Bractwa.
3. Użytkownik wybiera opcję `"Dodaj wydarzenie"`.
4. System wyświetla formularz dodawania wydarzenia obejmujący tytuł, datę rozpoczęcia, datę zakończenia,
   a także wybór miejsca, typu wydarzenia i uczestników.
5. Użytkownik zatwierdza zmiany. Zmiany zostają zarejestrowane na `Osi Czasu` w `Centrum zarządzania`.
6. Użytkownik wybiera wydarzenie, a następnie wybiera opcję `"Edytuj wydarzenie"`.
7. Użytkownik wprowadza, a następnie zatwierdza zmiany. Zmiany zostają zarejestrowane na `Osi Czasu`
   w `Centrum zarządzania`.
8. Użytkownik wybiera opcję `"Wróć do Centrum zarządzania`.
9. System wyświetla `Centrum zarządzania`.


---

### ENC – Encyklopedia

1. Użytkownik otwiera moduł `„Encyklopedia”` z poziomu `dashboardu`.
2. System wyświetla spis pojęć pogrupowanych alfabetycznie.
3. Użytkownik wybiera pojęcie.
4. System wyświetla artykuł encyklopedyczny dotyczący wybranego pojęcia.
5. Użytkownik może filtrować artykuły po kategorii.
6. Użytkownik wybiera opcję `„Wróć do dashboardu”`.
7. System wyświetla `Dashboard`.

---

### SLL – Słowniczek łaciński

1. Użytkownik otwiera moduł `"Słowniczek łaciński` z poziomu `dashboardu`.
2. System wyświetla listę zwrotów. Każda pozycja zawiera zwrot w łacinie i tłumaczenie na polski
3. Użytkownik może filtrować artykuły po kategorii
4. Użytkownik wybiera opcję `"Wróć do dashboardu"`
5. System wyświetla `Dashboard`

---

### PIN – Piny belgijskie

#### Użytkownik: CZŁONEK

1. Użytkownik wybiera moduł `„Piny belgijskie”` z `dashboardu`.
2. System wyświetla katalog pinów z pierwszej kategorii w formie kafelków; każdy kafelek zawiera nazwę, cenę, grafikę
   oraz kontrolkę wyboru ilości.
3. Po najechaniu kursorem na kafelek pina wyświetlany jest jego opis.
4. Użytkownik wybiera inną kategorię pinów z menu po lewej stronie.
5. Wyświetlana lista pinów zostaje zaktualizowana zgodnie z wybraną kategorią.
6. Użytkownik otwiera koszyk.
7. System wyświetla piny dodane do koszyka w formie kafelków.
   Kontrolka dodawania ilości zostaje zastąpiona kontrolką ustawiania ilości,
   a przycisk dodawania do koszyka jest niedostępny. Na dole widoczna jest łączna suma kosztów zamówienia.
8. Użytkownik wybiera opcję `"Zapisz zamówienie`.
9. Użytkownik wybiera opcję `„Wyślij zamówienie do Skarbnika”`.
10. System wyświetla potwierdzenie pomyślnego przesłania zamówienia.
11. W prawym górnym rogu interfejsu widoczny jest licznik czasu pozostałego na modyfikację lub
    ponowne przesłanie zamówienia; po jego upływie funkcja wysyłania zostaje zablokowana.
12. Użytkownik modyfikuje ilości pinów i ponownie wybiera opcję `„Wyślij zamówienie do Skarbnika”`,
    zastępując wcześniejszą wersję zamówienia aktualną.
13. Użytkownik wybiera opcję `„Wróć do dashboardu”`.
14. System wyświetla `Dashboard`.

#### Użytkownik: ODWIEDZAJĄCY

1. Użytkownik wybiera otwiera podstronę `Sklep`, następnie `Zamów piny belgijskie`.
2. Użytkownik loguje się swoim kontem Google, jeśli jeszcze nie jest zalogowany.
3. System wyświetla katalog pinów z pierwszej kategorii w formie kafelków; każdy kafelek zawiera nazwę, cenę, grafikę
   oraz kontrolkę wyboru ilości.
4. Po najechaniu kursorem na kafelek pina wyświetlany jest jego opis.
5. Użytkownik wybiera inną kategorię pinów z menu po lewej stronie.
6. Wyświetlana lista pinów zostaje zaktualizowana zgodnie z wybraną kategorią.
7. Użytkownik otwiera koszyk.
8. System wyświetla piny dodane do koszyka w formie kafelków.
   Kontrolka dodawania ilości zostaje zastąpiona kontrolką ustawiania ilości,
   a przycisk dodawania do koszyka jest niedostępny. Na dole widoczna jest łączna suma kosztów zamówienia.
9. Użytkownik wybiera opcję `"Zapisz zamówienie`.
10. Użytkownik otwiera moduł `Konto` i wybiera akcję `Przeglądaj zamówienia`.
11. Wyświetlają się wszystkie zamówienia wykonane w sklepie przez użytkownika.
12. Użytkownik wybiera zamówienie na piny belgijskie.
13. Wyświetla się koszyk sklepu z pinami belgijskimi.
14. Użytkownik wybiera opcję `"Przejdź do sklepu`.
15. Użytkownik dodaje nowe piny do koszyka.
16. Użytkownik wybiera opcję `"Wyślij zamówienie do Skarbnika"`
17. Skarbnik otrzymuje zamówienie na moduł `Piny belgijskie zamówienie`
18. System wyświetla potwierdzenie pomyślnego przesłania zamówienia.

#### Użytkownik: SKARBNIK

1. Użytkownik wybiera opcję `"Piny belgijskie zamówienie"` z `Centrum Zarządzania`.
2. System wyświetla termin składania zamówień oraz listę zamówień. Każda pozycja zawiera odnośnik do płatnika, liczbę
   zamówionych pinów oraz status spłaty w formacie `<zapłacono> zł / <pełna kwota> zł`.
3. Przed uruchomieniem opcji `"Otwórz zamówienia na piny"` lista zamówień pozostaje pusta.
    - Każde wybranie opcji `"Wyślij zamówienie do Skarbnika"` powoduje dodanie nowej pozycji lub aktualizację istniejącej
      pozycji na liście.
    - Otwarcie zamówień jest rejestrowane na `Osi Czasu` w `Centrum Zarządzania`.
4. Użytkownik wybiera jedną z pozycji. System wyświetla szczegóły zamówienia, obejmujące wcześniej widoczne informacje
   oraz katalog zamówionych przez płatnika pinów. Każda pozycja katalogu zawiera nazwę pina, grafikę, cenę jednostkową w
   euro oraz zamówioną ilość.
5. Użytkownik zamyka widok szczegółów zamówienia.
6. Użytkownik wybiera opcję `"Zmień termin spłaty"`.
7. Użytkownik wprowadza nowy termin i zatwierdza zmianę. System wysyła powiadomienie do wszystkich płatników
   posiadających zaległości.
8. Zamówienie jest automatycznie rejestrowane jako cel składkowy w module `Cele składkowe` w `Panelu Skarbnika`.
    - możliwe jest wygenerowanie pliku CSV do wykorzystania przy wysyłce wiadomości zbiorczej,
    - zamknięcie celu składkowego dotyczącego pinów belgijskich powoduje zakończenie okresu spłaty oraz wysłanie
      powiadomienia do wszystkich zalegających płatników.
9. Użytkownik wybiera opcję `"Edytuj katalog pinów"`.
10. System wyświetla katalog wszystkich pinów belgijskich w formie analogicznej do modułu `"PIN - Piny belgijskie"`.
11. Użytkownik edytuje informacje dotyczące pinów. Po zatwierdzeniu zmian są one rejestrowane na `Osi Czasu`
    w `Centrum Zarządzania`.
12. Użytkownik wybiera opcję `"Wróć"`.
13. System wyświetla listę zamówień.
14. Użytkownik wybiera opcję `"Wróć do Centrum Zarządzania"`.
15. System wyświetla `Centrum Zarządzania`.

---

## APLIKACJE DASHBOARDOWE

---

### SPI – Śpiewnik

#### Użytkownik: CZŁONEK

1. Użytkownik otwiera moduł `"Śpiewnik"` z poziomu `dashboardu`.
2. Wyświetla się lista kategorii wraz z polem wyszukiwania.
3. Użytkownik wybiera kategorię.
4. System wyświetla listę piosenek przypisanych do wybranej kategorii.
5. Użytkownik wybiera piosenkę.
6. System wyświetla tytuł piosenki, tytuł alternatywny, autorów, kategorie piosenki oraz jej tekst wraz z akordami, 
ewentualnie tekst alternatywny.
7. Użytkownik wybiera opcję `„Następna piosenka”`.
8. System wyświetla kolejną piosenkę z bieżącej kategorii.
9. Użytkownik wybiera opcję `„Wróć”`.
10. System powraca do widoku listy kategorii.
11. Użytkownik ponownie wybiera wcześniej wybraną kategorię.
12. Lista piosenek w tej kategorii zostaje zwinięta.
13. Użytkownik wybiera opcję `„Wróć do dashboardu”`.
14. System wyświetla `dashboard`.

#### Użytkownik: MUZYK

1. Użytkownik otwiera moduł `"Śpiewnik"` z poziomu `dashboardu`.
2. Wyświetla się lista kategorii wraz z polem wyszukiwania.
3. Użytkownik wybiera opcję `„Więcej”` obok pola wyszukiwania.
4. System wyświetla panel wyszukiwania zaawansowanego umożliwiający wyszukiwanie:
   - po tytule,
   - po fragmencie tekstu,
   - po pierwszym akordzie,
   - po sekwencji akordów.
5. System wyświetla listę wyników pogrupowanych według kategorii.
6. Użytkownik wybiera piosenkę i uruchamia tryb `„Focus”` (ikona gitary).
7. System wyświetla pierwszą zwrotkę utworu oraz panel ustawień trybu `„Focus”` zawierający opcje:
   - wyświetlania jednej lub dwóch zwrotek jednocześnie,
   - prezentacji akordów w kolorze czerwonym lub czarnym.
     Domyślnie aktywne są ustawienia: `„1 zwrotka”` oraz `„czerwone akordy”` (akordy czerwone i pogrubione, tekst czarny).
8. Użytkownik przechodzi pomiędzy zwrotkami, naciskając prawą część ekranu (`„następna zwrotka”`) lub lewą część ekranu (`„poprzednia zwrotka”`).
9. Użytkownik wyłącza tryb `„Focus”`, wybierając ikonę gitary.
10. Użytkownik wybiera opcję `„Wróć do dashboardu”`.
11. System wyświetla `Dashboard`.

#### Użytkownik: CANTANDI

1. Użytkownik otwiera moduł `"Edytuj śpiewnik"` z `Panelu Cantandiego`.
2. System wyświetla zawartość modułu `SPI - Śpiewnik`, umożliwiając edycję każdej piosenki po wybraniu opcji 
`"Edytuj piosenkę"`. Możliwa jest modyfikacja:
   - tytułu i tytułu alternatywnego,
   - autorów,
   - kategorii,
   - tekstu i tekstu alternatywnego,
   - akordów.
3. Wszystkie wprowadzone zmiany są rejestrowane na `Osi Czasu` w `Centrum Zarządzania`.
4. Użytkownik wybiera opcję `"Dodaj piosenkę"`.
5. System wyświetla formularz umożliwiający wprowadzenie:
   - tytułu i tytułu alternatywnego,
   - autorów,
   - kategorii
   oraz udostępnia możliwość pobrania lub skopiowania:
   - pliku JSON zawierającego instrukcję korzystania z formatu,
   - szablonu JSON do dodawania tekstu z akordami.
6. Użytkownik dodaje tekst piosenki za pomocą opcji `"Dodaj tekst"` lub `"Dodaj tekst alternatywny"`.
7. Użytkownik zatwierdza zmiany. Dodanie nowej piosenki zostaje zarejestrowane na `Osi Czasu` w `Centrum Zarządzania`.
8. Nowa piosenka staje się dostępna dla wszystkich członków w module `Śpiewnik`.
9. Użytkownik wybiera opcję `"Wróć do Centrum Zarządzania"`.
10. System wyświetla `Centrum Zarządzania`.

---

### IDG – Interaktywne drzewo genealogiczne

#### Z dashboardu

1. Użytkownik wybiera moduł `„Drzewo genealogiczne”` z `dashboardu`.
2. Wyświetla się drzewo genealogiczne wraz z menu konfiguracji:
   - `„Filtry”` – wymagają ponownej generacji drzewa poprzez opcję `„Odśwież”`; 
   możliwe jest włączenie wielu filtrów jednocześnie,
   - `„Kolorowanie”` – zmienia kolor węzłów według wybranego kryterium; aktywna może być tylko jedna opcja,
   - `„Widoki”` – rozszerzają funkcjonalność drzewa; możliwe jest włączenie wielu opcji jednocześnie.
3. Użytkownik wybiera wybrane opcje konfiguracji.
4. System aktualizuje i przerysowuje drzewo zgodnie z ustawieniami.
   - Drzewo umożliwia zoomowanie oraz przewijanie w pionie i poziomie.
   - Kliknięcie węzła otwiera biografię osoby, a najechanie kursorem powoduje jego podświetlenie.
5. Użytkownik aktywuje tryb `„Zaznaczenie”`.
   - Kliknięcie węzła dodaje go do zaznaczenia.
   - Przytrzymanie klawisza Shift i kliknięcie dwóch węzłów zaznacza również wszystkie węzły znajdujące się na ścieżce między nimi.
   - Dostępne są opcje `„Cofnij”` i `„Ponów”`.
6. Użytkownik wybiera jedną z dostępnych akcji dla zaznaczenia: `„Pokoloruj”`, `„Drukuj”`, `„Dodaj do nowego drzewa”`.
7. Otwiera się nowe okno zawierające drzewo z utworzonych zaznaczeń.
8. Nowe drzewo otrzymuje nazwę nadawaną przez użytkownika.
9. Użytkownik wraca do oryginalnego widoku i zaznacza kolejne węzły; dostępna staje się opcja `„Dodaj węzły do drzewa <nazwa>”`.
10. Użytkownik przechodzi do nowego drzewa i zaznacza węzły; dostępna jest opcja `„Usuń węzły”`.
11. Użytkownik wybiera opcję `„Drukuj drzewo”`.
12. System wyświetla okno wyboru formatu eksportu.
13. Użytkownik wybiera format `„PNG”` i zatwierdza drukowanie.
14. Wprowadza nazwę pliku i zapisuje go na urządzeniu.
15. Użytkownik zamyka okno nowego drzewa.
16. Użytkownik wybiera opcję `„Wróć do dashboardu”`.
17. System wyświetla `Dashboard`.

#### Z biografii członka 

1. Użytkownik otwiera profil innego członka. 
2. Wybiera opcję `„Pokaż drzewo”`. 
3. System wyświetla drzewo obejmujące rodziców, danego członka oraz jego dzieci. 
4. Widok drzewa umożliwia podświetlanie węzłów, przewijanie oraz zoomowanie.

---

### KOD – Kodeks

1. Użytkownik wybiera moduł `„Kodeks”` z `dashboardu`.
2. Wyświetlane są cztery sekcje:
   - `„Prawa i obowiązki”`,
   - `„Zasady wydarzeń”`,
   - `„Tradycje”`,
   - `„Księga znaku”`.
3. Użytkownik wybiera `„Prawa i obowiązki”`.
   1. System wyświetla listę rozwijalnych sekcji.
   2. Użytkownik wybiera jedną z sekcji.
   3. System wyświetla szczegółową listę praw i obowiązków.
4. Użytkownik wraca i wybiera `„Zasady wydarzeń”`.
   1. System wyświetla listę typów wydarzeń.
   2. Użytkownik wybiera jeden typ wydarzeń.
   3. System wyświetla zasady wydarzeń.
5. Użytkownik wraca i wybiera `„Tradycje”`.
   1. System wyświetla listę tradycji.
6. Użytkownik wraca i wybiera `„Księga znaku”`.
   1. System wyświetla listę znaków.
7. Użytkownik wybiera opcję `„Wróć do dashboardu”`.
8. System wyświetla `Dashboard`.

---

### MAP – Mapa

#### Urządzenie: komputer 
1. Użytkownik otwiera moduł `„Mapa”` z poziomu `dashboardu`. 
2. System wyświetla mapę świata ze znacznikami w formie emotikon, domyślnie wyśrodkowaną na obszarze Polski. 
3. Mapa umożliwia przybliżanie, oddalanie oraz przewijanie. 
Dostępne są również standardowe funkcje mapowe, takie jak `"Street View"`.
4. Po najechaniu kursorem na znacznik wyświetla się podpowiedź zawierająca nazwę miejsca, jego typ, adres oraz 
informację o ewentualnym trwałym zamknięciu. 
5. Po kliknięciu znacznika system otwiera okno zawierające wszystkie wzmianki o danym miejscu w Kronice Bractwa. 
6. Po wybraniu ikony filtrowania system wyświetla panel filtrów zawierający listę typów miejsc oraz 
filtr `„Zamknięte na stałe”`. 
7. Użytkownik wybiera interesujące go typy miejsc oraz opcjonalne filtry. 
8. System aktualizuje widok mapy i odpowiednio zmienia liczbę wyświetlanych znaczników. 
9. Użytkownik wybiera opcję `„Wróć do dashboardu”`. 
10. System wyświetla `Dashboard`. 

#### Urządzenie mobilne 
1. Użytkownik otwiera moduł `„Mapa”` z poziomu `dashboardu`. 
2. Oprócz funkcjonalności dostępnych w wersji komputerowej system wyświetla niebieski wskaźnik kierunku oparty na 
orientacji urządzenia. 
3. Użytkownik wybiera ikonę `„Kompas Nawojkowy”`. 
4. System wyświetla dodatkowy czerwony wskaźnik, wskazujący kierunek przeciwny do położenia hotelu Dom Studencki Nawojka. 
5. Ponowne wybranie ikony `„Kompas Nawojkowy”` powoduje ukrycie czerwonego wskaźnika. 
6. Użytkownik wybiera opcję `„Wróć do dashboardu”`. 
7. System wyświetla `Dashboard`.

#### Użytkownik: KASZTELAN
1. Użytkownik wybiera moduł `"Wywiad miejscówek"` z `Panelu Kasztelana`.
2. System wyświetla mapę świata sfokusowaną na Krakowie ze znacznikami odpowiadającymi miejscom, w których odbywały się
   wydarzenia.
   - Najechanie na znacznik wyświetla tooltip zawierający nazwę, kategorię oraz adres.
   - Naciśnięcie na znacznik dodatkowo pokazuje godziny otwarcia, informację czy miejsce nadaje się na Karczmę,
     ocenę Google, ocenę Zarządu, dostępne zniżki w poszczególne dni tygodnia oraz trzy ostatnie wydarzenia w danym miejscu.
3. Użytkownik wybiera datę oraz czas rozpoczęcia i czas trwania planowanego wydarzenia w prawym panelu bocznym, określa
   czy jest to Karczma i wybiera opcję `"Znajdź najlepsze miejsca"`.
4. System analizuje zniżki, natężenie ruchu, przydatność miejsca do organizacji Karczmy, oceny oraz inne czynniki i na
   tej podstawie wskazuje najlepsze lokalizacje.
5. Wyniki można filtrować według kategorii, odległości od centrum, przydatności do organizacji Karczmy, ocen oraz
   dostępnych zniżek w danym dniu tygodnia.
6. Użytkownik zaznacza jedną z rekomendowanych miejscówek jako miejsce wydarzenia i wybiera opcję
   `"Znajdź miejscówki na after"`.
7. System analizuje natężenie ruchu, odległość od wybranego miejsca wydarzenia oraz oceny, a następnie wskazuje
   najlepsze lokalizacje na after.
8. Użytkownik naciska jeden ze znaczników i wybiera opcję edycji.
9. Użytkownik edytuje informacje i zapisuje zmiany. Akcje zostają zarejestrowane na `Osi Czasu` w `Centrum Zarządzania`.
10. Użytkownik odznacza miejsce wydarzenia i wybiera opcję `"Wróć do Centrum Zarządzania"`.
11. Użytkownik wybiera opcję `„Wróć do Centrum Zarządzania”`.
12. System wyświetla `Centrum Zarządzania`.

---

### KRO – Kronika

1. Użytkownik otwiera moduł `„Kronika”` z poziomu `dashboardu`. 
2. System wyświetla listę rozwijalnych sekcji, takich jak `„Osoby”`, `„Dokumenty”`, `„Miejsca”` oraz pozostałe 
kategorie tematyczne. 
3. Po rozwinięciu wybranej sekcji system wyświetla listę rozwijalnych podkategorii. 
4. Użytkownik wybiera podkategorię. System wyświetla pozycje zawierające informacje przypisane do wybranego zakresu 
tematycznego. 
5. Użytkownik zwija otwarte sekcje. 
6. Użytkownik wpisuje frazę `„koziołek”` w polu wyszukiwania. 
7. System filtruje wyniki, pozostawiając wyłącznie pozycje powiązane z podaną frazą. 
Dopasowania dosłowne mają wyszukiwaną frazę podświetloną na zielono, natomiast dopasowania bliskoznaczne lub kontekstowe 
(np. `„Kozioł”`) są oznaczane kolorem żółtym. 
8. Użytkownik wybiera ikonę wyszukiwania zaawansowanego. 
9. Po rozwinięciu podkategorii system prezentuje dane w formie tabeli. Każda kolumna umożliwia filtrowanie wartości 
zarówno w trybie włączającym (pokazanie wybranych wartości), jak i wykluczającym (ukrycie wybranych wartości). 
10. Użytkownik wybiera opcję `„Wróć do dashboardu”`. 
11. System wyświetla `Dashboard`.

---

### CYT – Cytaty

1. Użytkownik otwiera moduł `„Cytaty”` z poziomu `dashboardu`. 
2. System wyświetla cytaty pogrupowane według autorów; część cytatów może być skrócona za pomocą wielokropka. 
3. Użytkownik wybiera cytat. 
4. System wyświetla widok szczegółowy zawierający cytat, jego autora oraz kontekst. 
5. W widoku dostępne są opcje `„Następny cytat”` oraz `„Poprzedni cytat”`, umożliwiające nawigację pomiędzy cytatami 
bez opuszczania widoku szczegółów. 
6. Użytkownik zamyka widok cytatu. 
7. Użytkownik wybiera opcję `„Cytat dnia”`. 
8. System wyświetla cytat przypisany do danego dnia wraz z jego autorem i kontekstem. 
9. Użytkownik wybiera opcję `„Wróć do dashboardu”`. 
10. System wyświetla `Dashboard`.

---

### SKL – Składki

#### Użytkownik: CZŁONEK

1. Użytkownik wybiera moduł `„Składki”` z `dashboardu`. 
2. System wyświetla listę celów składkowych przypisanych do użytkownika wraz z postępem wpłat 
w formacie „zapłacono x z y zł” oraz kodem do tytułu przelewu. 
3. Użytkownik wybiera jeden z celów składkowych. 
4. System wyświetla szczegóły celu, obejmujące tytuł, kwotę docelową, termin oraz ewentualny formularz wpłaty. 
5. Użytkownik wpisuje zadeklarowaną kwotę w polu `„Zapłacił_m x zł”` i zatwierdza formularz. 
`Skarbnik` otrzymuje informację o deklaracji, aktualizuje historię wpłat, a system odświeża postęp realizacji składki. 
6. Użytkownik wybiera opcję `„Wróć do dashboardu”`. 
7. System wyświetla `Dashboard`.

#### Użytkownik: SKARBNIK

1. Użytkownik wybiera moduł `"Cele składkowe"` z `Panelu Skarbnika`.
2. System wyświetla listę celów składkowych. Każda pozycja zawiera nazwę, termin, kod do tytułu przelewu oraz liczbę osób, które wpłaciły
   dowolną kwotę i liczbę osób, które opłaciły składkę w całości, w formacie `x/y`.
3. Użytkownik wybiera jeden z celów składkowych.
4. System wyświetla okno zawierające nazwę celu, termin, kod do tytułu przelewu oraz listę płatników.
   - Każda pozycja listy zawiera odnośnik do płatnika oraz status spłaty w formacie `<zapłacono> zł / <pełna kwota> zł`.
   - Status spłaty jest automatycznie aktualizowany na podstawie historii transakcji `Skarbca` i kodu składki.
   - Wymagana kwota może być wspólna dla wszystkich płatników lub określana indywidualnie za pomocą pliku CSV,
     do którego odnośnik znajduje się w szczegółach celu składkowego.
5. Użytkownik zaznacza wybranych płatników lub wybiera opcję `"Zaznacz zalegających płatników"`.
6. Użytkownik wybiera opcję `"Wygeneruj CSV do maila zbiorczego"`.
7. System generuje plik CSV zawierający brakujące kwoty przypisane do adresów e-mail zaznaczonych płatników.
8. Użytkownik pobiera plik w celu wykorzystania go podczas wysyłania zbiorczego przypomnienia o składce.
9. Użytkownik zaznacza wybranych płatników i wybiera opcję `"Wyślij przypomnienie systemowe"`.
10. System wysyła przypomnienie do każdego zaznaczonego płatnika za pośrednictwem konta systemowego.
11. Użytkownik wybiera opcję `"Edytuj cel składkowy"` i zmienia termin składki. Po zapisaniu zmian każdy zalegający
    płatnik otrzymuje powiadomienie na swoje konto systemowe.
12. Po uregulowaniu wpłat przez wszystkich płatników użytkownik wybiera opcję `"Zamknij cel składkowy"`.
    Operacja zostaje odnotowana na `Osi Czasu` w `Centrum Zarządzania`.
13. Użytkownik wybiera opcję `"Wróć do Centrum Zarządzania"`.
14. System wyświetla `Centrum Zarządzania`.

---

## APLIKACJE ZARZĄDOWE

---

### PDZ – Plan działania

1. Użytkownik wybiera moduł `„Plan działania”` z `Panelu Wielkiego Mistrza`. 
2. System wyświetla listę zadań przypisanych do kadencji poszczególnych Zarządów. 
3. Użytkownik otwiera wybrane zadanie. 
4. System wyświetla szczegóły zadania, obejmujące opis, 
termin realizacji oraz listę kroków wymaganych do jego ukończenia. 
Odhaczenie zadania jest możliwe wyłącznie po spełnieniu wszystkich warunków. 
5. Użytkownik może dodawać oraz edytować zadania; każda zmiana jest rejestrowana na `Osi Czasu` w `Centrum Zarządzania`. 
6. Użytkownik wybiera opcję `„Wróć do Centrum Zarządzania”`. 
7. System wyświetla `Centrum Zarządzania`.

---

### WOR – Wywiad organizacji

1. Użytkownik wybiera moduł `„Wywiad organizacji”` z `Panelu Wielkiego Mistrza`. 
2. System wyświetla listę organizacji studenckich, które weszły w kontakt z Bractwem. 
3. Użytkownik wybiera jedną z organizacji. 
4. System wyświetla kartę wywiadu zawierającą: nazwę organizacji, adresy e-mail, obszar działania, 
aktualne kierownictwo, rok założenia, listę członków, historię wspólnych wydarzeń oraz opinie poprzednich Zarządów. 
5. Użytkownik dodaje opinię o organizacji w imieniu aktualnego Zarządu. Może też edytować resztę informacji. 
6. Użytkownik zamyka widok szczegółów organizacji. 
7. Użytkownik wpisuje w wyszukiwarkę dowolną informację dotyczącą organizacji (np. adres e-mail lub nazwę). 
8. System wyświetla powiązane organizacje na podstawie wprowadzonego zapytania. 
9. Wszystkie dokonane przez użytkownika zmiany zostaną zarejestrowane na `Osi Czasu` w `Centrum zarządzania`.
10. Użytkownik wybiera opcję `„Wróć do Centrum Zarządzania”`.
11. System wyświetla `Centrum Zarządzania`.

---

### RSS – Rozporządzenia SSUJ

1. Użytkownik wybiera moduł `„Rozporządzenia SSUJ”` z `Panelu Kasztelana`. 
2. System prosi o zalogowanie się kontem Microsoft, jeśli użytkownik nie jest jeszcze zalogowany. 
3. System wyświetla listę rozporządzeń SSUJ dotyczących m.in. wniosków o dofinansowanie oraz zmian budżetowych, 
podzieloną na sekcje `„Nieprzeczytane”` oraz `„Przeczytane”`. 
4. Użytkownik może filtrować rozporządzenia według roku, aktualności oraz tematyki. 
5. Użytkownik wybiera jedno z rozporządzeń. 
6. System wyświetla treść dokumentu wraz z formularzem do uzupełnienia. 
7. Użytkownik zapoznaje się z dokumentem, wpisuje streszczenie w formularzu oraz oznacza aktualność dokumentu. 
8. System wyszukuje powiązane rozporządzenia o podobnym tytule i prosi użytkownika o weryfikację ich aktualności, 
prezentując szacowany czas potrzebny na wykonanie zadania. 
9. Użytkownik oznacza nieaktualne rozporządzenia, korzystając ze streszczeń pozostawionych 
przez poprzednich `Kasztelanów`. 
10. Wszystkie dokonane przez użytkownika zmiany zostaną zarejestrowane na `Osi Czasu` w `Centrum zarządzania`.
11. Użytkownik wybiera opcję `„Wróć do Centrum Zarządzania”`. 
12. System wyświetla `Centrum Zarządzania`.

---

### WNI – Wnioski

1. Użytkownik wybiera moduł `„Wnioski”` z `Panelu Kasztelana`.
2. System wyświetla listę dotychczasowych wniosków. Dostępne są opcje sortowania według daty złożenia lub daty 
ostatniej modyfikacji, a także grupowania według statusu akceptacji.
3. Użytkownik wybiera jeden z wniosków.
4. System wyświetla szczegóły wniosku, obejmujące nazwę, datę złożenia, datę ostatniej modyfikacji, status akceptacji 
przez SSUJ oraz podgląd dokumentu.
5. Użytkownik zamyka widok wniosku.
6. Użytkownik wybiera ikonę dodawania (plus) dostępną przy jednym z istniejących wniosków.
7. System otwiera kopię wybranego wniosku w trybie edycji.
8. Użytkownik wprowadza zmiany i zapisuje dokument.
9. System dodaje nowy wniosek do listy oraz nadaje mu status `„Czeka na akceptację”`.
10. Użytkownik wybiera ikonę edycji przy wybranym wniosku.
11. System umożliwia modyfikację nazwy, daty, statusu oraz załączonego dokumentu.
12. Po zapisaniu zmian system automatycznie aktualizuje datę ostatniej modyfikacji.
13. Użytkownik zapisuje zmiany i zamyka widok wniosku.
14. Wszystkie dokonane przez użytkownika zmiany zostaną zarejestrowane na `Osi Czasu` w `Centrum zarządzania`.
15. Użytkownik wybiera opcję `„Wróć do Centrum Zarządzania”`.
16. System wyświetla `Centrum Zarządzania`.

---

### SKA – Skarbiec

1. Użytkownik wybiera moduł `"Skarbiec"` z `Panelu Skarbnika`.
2. System wyświetla saldo oraz numer konta, a także skróty do historii transakcji, spisu płatników i spisu firm.
3. Użytkownik rozwija historię transakcji. Każda pozycja zawiera tytuł operacji, kwotę przelewu, 
link do odbiorcy/adresata oraz saldo konta po transakcji.
4. Użytkownik wybiera opcję `"Wczytaj historię"`.
5. System otwiera okno umożliwiające przeciągnięcie lub wybranie pliku CSV zawierającego historię transakcji konta 
bankowego.
6. Użytkownik dodaje plik CSV.
7. System analizuje transakcje i dodaje je do historii transakcji `Skarbca`.
8. Jeśli system nie odnajdzie odbiorcy lub nadawcy w spisie płatników, lub firm, prosi użytkownika o wykonanie jednej z 
następujących akcji:
   - przyporządkowanie transakcji do istniejącego płatnika lub firmy wraz z uzupełnieniem nowych danych,
   - utworzenie nowego obiektu poprzez wskazanie, czy jest to płatnik, czy firma, oraz uzupełnienie dostępnych informacji 
   (np. opisu działalności, dodatkowych numerów telefonu).
9. Po udzieleniu odpowiedzi na wszystkie pytania historia transakcji `Skarbca` zostaje uzupełniona o nowe pozycje.
10. Użytkownik zwija historię transakcji i rozwija spis płatników:
    - Każda pozycja zawiera imię i nazwisko oraz numer konta lub numer telefonu.
    - Po wybraniu pozycji system wyświetla dodatkowo miejsce zamieszkania płatnika, adres e-mail oraz profil użytkownika, 
     jeśli istnieje on w systemie. Dane można modyfikować po wybraniu opcji `"Edytuj"`.
11. Użytkownik zwija spis płatników i rozwija spis firm.
    - Każda pozycja zawiera nazwę firmy oraz numer konta.
    - Po wybraniu pozycji system wyświetla dodatkowo adres siedziby, adresy e-mail, numery telefonów oraz opis
      działalności. Dane można modyfikować po wybraniu opcji `"Edytuj"`.
12. Wszystkie zmiany wprowadzone przez użytkownika są rejestrowane na `Osi Czasu` w `Centrum Zarządzania`.
13. Użytkownik zwija spis firm i wybiera opcję `"Wróć do Centrum Zarządzania"`.
14. System wyświetla `Centrum Zarządzania`.

---

### OCZ – Oś Czasu

1. Użytkownik wybiera moduł `"Oś Czasu"` z `Panelu Wspólnego`.
2. System wyświetla pionową oś czasu skierowaną ku górze, zawierającą wszystkie zatwierdzone akcje wykonane przez 
obecny Zarząd.
   - Każda pozycja zawiera informację o funkcji użytkownika wykonującego akcję (Wielki Mistrz, Kasztelan, Skarbnik, 
   Sekretarz lub Cantandi), module, za pomocą którego wykonano akcję, oraz dacie i godzinie jej wykonania.
3. Użytkownik wybiera opcję `"Odwróć oś o 90°"`.
4. System zmienia orientację osi czasu na poziomą.
5. Użytkownik filtruje akcje według funkcji wykonującego oraz miesiąca wykonania.
6. Użytkownik wybiera opcję `"Tryb prezentacji"`.
7. System przełącza widok w tryb pełnoekranowy z osią skierowaną w prawo. Przewijanie osi odbywa się za pomocą 
klawiszy strzałek w lewo i w prawo.
8. Użytkownik wybiera opcję `"Wróć"`, a następnie `"Wróć do Centrum Zarządzania"`.
9. System wyświetla `Centrum Zarządzania`.

---