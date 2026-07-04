# Diagramy przypadków użycia

---

## Ogólnodostępne funkcje strony

---

### UCD-STR-1

```mermaid
flowchart 
    U("👤Użytkownik")
    
    subgraph STR["Strona czapkuj.pl | UC-01"]
    
        SG([Strona główna\nUC-01])
        subgraph MENU["Menu"]
            KAL([Kalendarz wydarzeń\nUC-02])
            SKLEP(Sklep)
            BLOGI(Blogi)
        end
        KONTO([Konto])
        subgraph TRYB["Tryb wyświetlania"]
            ODW(Odwiedzający)
            CZA(Czapkowicz)
            WM(Wielki Mistrz)
            KAS(Kasztelan)
            SKA(Skarbnik)
            SEK(Sekretarz)
            CAN(Cantandi)
            MOD(Moderator)
            ADM(Administrator)
        end
        CZAT([Czat\nUC-07])
        ZP([Zgłoś problem\nUC-08])
        SM([Socjal media\nUC-09])
        
        DODGC([Dodaj do Google Calendar\nUC-02])
        DODGC -.->|&lt&ltextend&gt&gt| KAL
        
    end

%% Funkcje główne

    U --- SG
    U --- MENU
    U --- KONTO
    U --- TRYB
    U --- CZAT
    U --- ZP
    U --- SM
    
%% Menu

%%    KAL -.->|&lt&ltextend&gt&gt| E-KAL
%%    SKLEP -.->|&lt&ltextend&gt&gt| E-SKLEP
%%    BLOGI -.->|&lt&ltextend&gt&gt| E-BLOGI
```

**UC-01: Przeglądanie strony głównej i nawigacja**
* STR-FR-001 – System musi umożliwiać wyświetlenie strony głównej z opisem serwisu i trybem użytkownika.
* STR-FR-002 – System musi umożliwiać przełączanie trybu widoku (np. „Odwiedzający”, „Czapkowicz”).
* STR-FR-003 – System musi udostępniać menu hamburgerowe prowadzące do podstron serwisu.
* STR-FR-004 – System musi umożliwiać nawigację do modułu „Kalendarz wydarzeń” z poziomu menu.
* STR-FR-007 – System musi umożliwiać dostęp do sekcji „Sklep” z trzema opcjami zamówień z poziomu menu.
* STR-FR-035 – System musi przekierowywać użytkownika do odpowiednich modułów zgodnie z rolą i statusem konta.

