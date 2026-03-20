graph LR

%% Aktorzy i UC
Czlonek --> UC01["UC-01: Kalendarz wydarzeń"]
Czlonek --> UC02["UC-02: Sprawdzenie składek"]
Czlonek --> UC03["UC-03: Drzewo genealogiczne"]
Czlonek --> UC04["UC-04: Kompas nawojkowy"]
Czlonek --> UC24["UC-24: Piny belgijskie"]

Skarbnik --> UC05["UC-05: Import historii transakcji"]
Skarbnik --> UC06["UC-06: Cele składkowe"]
Skarbnik --> UC07["UC-07: Przypomnienia o płatnościach"]
Skarbnik --> UC08["UC-08: Analiza danych w BI"]
Skarbnik --> UC09["UC-09: Złożenie zamówienia pinów"]

Kandydat --> UC10["UC-10: Wyszukiwanie informacji"]
Kandydat --> UC11["UC-11: Wyszukiwanie zaawansowane"]
Kandydat --> UC12["UC-12: Przeglądanie kodeksu"]

Muzyk --> UC13["UC-13: Korzystanie ze śpiewnika"]
Muzyk --> UC14["UC-14: Tryb focus"]
Czlonek --> UC15["UC-15: Edycja piosenki"]
Muzyk --> UC16["UC-16: Akceptacja zmian"]
Muzyk --> UC17["UC-17: Tryb Cantandiego"]

WielkiMistrz --> UC18["UC-18: Zarządzanie TODO"]
WielkiMistrz --> UC19["UC-19: Sprawdzanie znajomości organizacji"]

Kasztelan --> UC20["UC-20: Tworzenie wniosku"]
Kasztelan --> UC21["UC-21: Przegląd zarządzeń SSUJ"]
Kasztelan --> UC22["UC-22: Przegląd mapy miejscówek"]
Kasztelan --> UC23["UC-23: Przegląd zniżek"]

%% UC -> wymagania z opisami

UC01 --> KW10["KW-10: System wyświetla listę nadchodzących wydarzeń organizacji (Must)"]
UC01 --> KW11["KW-11: Użytkownik może dodać kalendarz wydarzeń organizacji do Google Calendar (Should)"]

UC02 --> SK10["SK-10: Członek może sprawdzić historię wpłat oraz zaległości (Must)"]

UC03 --> DG10["DG-10: System generuje drzewo genealogiczne organizacji (Should)"]
UC03 --> DG11["DG-11: Użytkownik może filtrować drzewo według kryteriów (Could)"]

UC04 --> KN10["KN-10: System pokazuje kierunek przeciwny do D.S. Nawojka (Could)"]

UC15 --> SP10["SP-10: System umożliwia wyszukiwanie piosenek po tytule (Must)"]
UC15 --> SP12["SP-12: System zapisuje zmiany w piosence / wyróżnia akordy (Must)"]

UC13 --> SP10
UC13 --> SP11["SP-11: System umożliwia wyszukiwanie piosenek po akordach (Should)"]
UC13 --> SP12

UC14 --> SP13["SP-13: Tryb focus - wyświetla jedną zwrotkę (Should)"]

UC16 --> SP12
UC17 --> SP12

UC05 --> SK11["SK-11: Skarbnik może wczytać historię transakcji z CSV (Must)"]
UC05 --> SK12["SK-12: System zapisuje transakcje w bazie (Must)"]
UC06 --> SK13["SK-13: Skarbnik tworzy cele składkowe z kwotą i listą użytkowników (Must)"]
UC07 --> SK14["SK-14: System umożliwia wysyłanie przypomnienia do zalegających (Should)"]
UC08 --> SB11["SB-11: Filtry i raporty BI dla skarbnika (Should)"]
UC09 --> PB0["PB-0: Skarbnik składa zamówienie u dostawcy"]

UC10 --> WY10["WY-10: System umożliwia wyszukiwanie w bazie danych (Must)"]
UC10 --> WY11["WY-11: System wyświetla wyniki pogrupowane według kategorii (Should)"]
UC11 --> WY12["WY-12: Filtrowanie wyników wyszukiwania (Could)"]
UC12 --> SB10["SB-10: Wyświetlenie centralnego kodeksu (Must)"]

UC18 --> WM11["WM-11: Użytkownik może oznaczać zadania jako wykonane (Must)"]
UC19 --> SB12["SB-12: System umożliwia wyszukiwanie informacji o organizacjach po e-mail (Could)"]

UC20 --> WN10["WN-10: System umożliwia utworzenie nowego wniosku (Should)"]
UC21 --> WN11["WN-11: System umożliwia przegląd zarządzeń SSUJ (Could)"]
UC22 --> MG0["MG-00: Wyświetlenie mapy miejscówek (Must)"]
UC23 --> MG1["MG-10: Wyświetlenie zniżek (Must)"]

UC24 --> PB10["PB-10: Członek wybiera produkty z listy (Should)"]
UC24 --> PB11["PB-11: System oblicza łączną kwotę zamówienia (Must)"]