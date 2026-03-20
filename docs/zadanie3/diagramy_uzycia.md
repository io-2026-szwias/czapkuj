graph LR

%% Aktorzy
Czlonek["Członek"]:::czlonek
Kandydat["Kandydat"]:::kandydat
Muzyk["Muzyk"]:::muzyk
Skarbnik["Skarbnik"]:::skarbnik
Kasztelan["Kasztelan"]:::kasztelan
WielkiMistrz["Wielki Mistrz"]:::wm

%% Funkcje Członka
Czlonek --> UC01["UC-01: Kalendarz wydarzeń"]
Czlonek --> UC02["UC-02: Sprawdzenie składek"]
Czlonek --> UC03["UC-03: Drzewo genealogiczne"]
Czlonek --> UC04["UC-04: Kompas nawojkowy"]
Czlonek --> UC24["UC-24: Piny belgijskie"]

%% Funkcje Skarbnika
Skarbnik --> UC05["UC-05: Import historii transakcji"]
Skarbnik --> UC06["UC-06: Cele składkowe"]
Skarbnik --> UC07["UC-07: Przypomnienia o płatnościach"]
Skarbnik --> UC08["UC-08: Analiza danych w BI"]
Skarbnik --> UC09["UC-09: Złożenie zamówienia pinów"]

%% Funkcje Kandydatów
Kandydat --> UC10["UC-10: Wyszukiwanie informacji"]
Kandydat --> UC11["UC-11: Wyszukiwanie zaawansowane"]
Kandydat --> UC12["UC-12: Przeglądanie kodeksu"]

%% Śpiewnik elektroniczny
Muzyk --> UC13["UC-13: Korzystanie ze śpiewnika"]
Muzyk --> UC14["UC-14: Tryb focus"]
Czlonek --> UC15["UC-15: Edycja piosenki"]
Muzyk --> UC16["UC-16: Akceptacja zmian"]
Muzyk --> UC17["UC-17: Tryb Cantandiego"]

%% Panel Wielkiego Mistrza
WielkiMistrz --> UC18["UC-18: Zarządzanie TODO"]
WielkiMistrz --> UC19["UC-19: Sprawdzanie znajomości organizacji"]

%% Łatwiejsze wnioski
Kasztelan --> UC20["UC-20: Tworzenie wniosku"]
Kasztelan --> UC21["UC-21: Przegląd zarządzeń SSUJ"]

%% Mapa miejscówek
Kasztelan --> UC22["UC-22: Przegląd mapy miejscówek"]
Kasztelan --> UC23["UC-23: Przegląd zniżek"]

%% Powiązania z wymaganiami

%% Członek
UC01 --> KW10["KW-10: Lista wydarzeń"]
UC01 --> KW11["KW-11: Subskrypcja kalendarza"]

UC02 --> SK10["SK-10: Historia wpłat i zaległości"]

UC03 --> DG10["DG-10: Generowanie drzewa genealogicznego"]
UC03 --> DG11["DG-11: Filtry drzewa"]

UC04 --> KN10["KN-10: Kompas przeciwny do D.S. Nawojka"]

UC15 --> SP10["SP-10: Edycja tekstu i akordów"]
UC15 --> SP12["SP-12: Zapis zmian w systemie"]

%% Muzyk
UC13 --> SP10
UC13 --> SP11["SP-11: Wyszukiwanie piosenki"]
UC13 --> SP12

UC14 --> SP13["SP-13: Tryb focus – wyświetlanie zwrotki"]
UC16 --> SP12
UC17 --> SP12

%% Skarbnik
UC05 --> SK11["SK-11: Przetwarzanie pliku CSV"]
UC05 --> SK12["SK-12: Zapis danych"]
UC06 --> SK13["SK-13: Zapis celu składkowego"]
UC07 --> SK14["SK-14: Wysyłanie przypomnienia"]
UC08 --> SB1["SB-1: Filtry raportów BI"]
UC09 --> PB0["PB-0: Złożenie zamówienia u dostawcy"]

%% Kandydat
UC10 --> WY10["WY-10: Przeszukiwanie bazy"]
UC10 --> WY11["WY-11: Wyświetlanie wyników"]
UC11 --> WY12["WY-12: Filtry zaawansowane"]
UC12 --> SB0["SB-0: Wyświetlenie kodeksu organizacji"]

%% Wielki Mistrz
UC18 --> WM11["WM-11: Oznaczenie zadania wykonanym"]
UC19 --> SB12["SB-12: Relacja z organizacją"]

%% Kasztelan
UC20 --> WN10["WN-10: Zapis wniosku"]
UC21 --> WN11["WN-11: Wyświetlenie zarządzeń"]
UC22 --> MG0["MG-0: Wyświetlenie mapy"]
UC23 --> MG1["MG-1: Wyświetlenie zniżek"]
UC24 --> PB10["PB-10: Wybór produktów"]
UC24 --> PB11["PB-11: Obliczenie kosztu"]

%% Styl aktorów
classDef czlonek fill:#FFCC00,stroke:#333,stroke-width:1px;
classDef kandydat fill:#66CCFF,stroke:#333,stroke-width:1px;
classDef muzyk fill:#FF99CC,stroke:#333,stroke-width:1px;
classDef skarbnik fill:#99FF99,stroke:#333,stroke-width:1px;
classDef kasztelan fill:#FF9966,stroke:#333,stroke-width:1px;
classDef wm fill:#CC99FF,stroke:#333,stroke-width:1px;