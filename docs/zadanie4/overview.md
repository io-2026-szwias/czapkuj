# 🧩 DESIGN PATTERNS
## 🏗️ 1. Service Layer Pattern 🧠

### Where:

- `TreeService` *(DRZEWO)*
- `KodeksView` *(KODEKS)*
- `TodoService` *(PANEL WM)*

### Why:

Centralizes business logic outside models and views:

- tree construction logic
- legal/code orchestration
- task management operations

➡️ One place for application logic instead of spreading it across layers.

------

## 🧱 2. Builder Pattern 🏗️

### Where:

- `generate_full_tree()` *(DRZEWO)*
- `build_layers_and_edges_from_db()` *(DRZEWO)*
- `ImportService` *(SKARBIEC)*

### Why:

Multi-step construction process:

- fetch data
- transform structure
- assemble final object/graph

➡️ Separates *how something is built* from *what it is*.

------

## 📦 3. DTO Pattern 📦

### Where:

- `TreeNode` *(DRZEWO)*
- `ZarzadzenieSSUJ` *(WNIOSKI)*
- `mapa_dane()` *(MAPA)*

### Why:

Lightweight transport structures between layers:

- ORM → API
- backend → frontend
- external → internal normalization

➡️ Clean data contracts without business logic.

------

## 🔌 4. Adapter Pattern 🔌

### Where:

- `GraphRenderer` *(DRZEWO)*
- `SSUJService` *(WNIOSKI)*
- `mapa_dane()` *(MAPA)*

### Why:

Transforms incompatible interfaces:

- domain → visualization formats
- external system → internal model
- DB → frontend JSON

➡️ Bridges system boundaries.

------

## 🎯 5. Strategy Pattern 🎯

### Where:

- `PricingEngine` *(PINY)*
- `MatchingService` *(SKARBIEC)*
- `SongFormatter` *(ŚPIEWNIK)*

### Why:

Interchangeable algorithms:

- pricing rules
- transaction matching rules
- formatting rules for songs

➡️ Behavior can change without modifying core logic.

------

## 🧷 6. State Pattern 🧷

### Where:

- `Order.status` *(PINY)*
- `CelStatus / PlatnikStatus` *(SKARBIEC)*
- `EditProposal.status` *(ŚPIEWNIK)*

### Why:

Behavior depends on lifecycle state:

- order progression
- payment status
- moderation workflow

➡️ Explicit modeling of system states.

------

## 🧠 7. Domain Model Pattern 🧠

### Where:

- `Zadanie` *(PANEL WM)*
- `Order / OrderItem / Pin` *(PINY)*
- `PrawoObowiazek` *(KODEKS)*

### Why:

Rich business entities:

- tasks with dependencies
- orders with items
- legal relationships

➡️ Models real-world concepts directly.

------

## 🌲 8. Composite Pattern 🌲

### Where:

- `Zadanie → dependencies` *(PANEL WM)*
- `Order → OrderItem` *(PINY)*
- `CelSkladkowy → CelSkladkowyPlatnik` *(SKARBIEC)*

### Why:

Hierarchical structures:

- graph dependencies
- order aggregates
- group payments

➡️ Tree/graph-like domain structures.

------

## 🔄 9. Workflow / Orchestration Pattern 🔄

### Where:

- `ImportService` *(SKARBIEC)*
- `CelService` *(SKARBIEC)*
- `SchedulerService` *(SKARBIEC)*

### Why:

Multi-step business processes:

- import → match → assign
- goal lifecycle management
- scheduled automation

➡️ Process-driven architecture instead of CRUD.

------

## 🗃️ 10. Repository / Query Pattern 🗃️

### Where:

- `SearchableManager` *(WYSZUKIWARKA)*
- `PinCatalogService` *(PINY)*
- `AdvancedSearchService` *(WYSZUKIWARKA)*

### Why:

Encapsulates data access logic:

- search abstraction
- catalog access layer
- complex querying

➡️ Hides persistence/query complexity.

------

## ⚡ 11. Event-Driven / Observer Pattern ⚡

### Where:

- `signals (indexing)` *(WYSZUKIWARKA)*
- `CompassService loop` *(MAPA/KOMPAS)*
- `SchedulerService` *(SKARBIEC)*

### Why:

System reacts to events:

- DB changes → indexing
- sensor updates → UI update
- time triggers → automation

➡️ Reactive system behavior.

------

## 🧩 12. Registry Pattern 🧩

### Where:

- `SEARCH_REGISTRY` *(WYSZUKIWARKA)*
- `register_search` *(WYSZUKIWARKA)*
- `WyszukiwarkaConfig` *(WYSZUKIWARKA)*

### Why:

Dynamic module discovery:

- plug-in search models
- no hardcoded dependencies

➡️ Extensible architecture.

------

## 🧾 13. Snapshot Pattern 🧾

### Where:

- `OrderItem.unit_price` *(PINY)*
- `Transakcja.kwota` *(SKARBIEC)*
- `PrzypisaniePlatnosci.kwota_przypisana` *(SKARBIEC)*

### Why:

Preserves historical correctness:

- price at purchase time
- transaction value at execution time
- frozen financial assignments

➡️ Immutable historical records.

------

## 🛡️ 14. Anti-Corruption Layer 🛡️

### Where:

- `SSUJService` *(WNIOSKI)*
- `ImportService (bank CSV)` *(SKARBIEC)*
- `PinCatalogService.sync()` *(PINY)*

### Why:

Protects domain from external systems:

- normalizes external APIs
- isolates schema changes
- prevents leakage of foreign models

➡️ Stable core despite external volatility.

------

## 🔍 15. Full-Text Search Pattern 🔍

### Where:

- `SearchableModel` *(WYSZUKIWARKA)*
- `SearchableQuerySet` *(WYSZUKIWARKA)*
- `tsvector indexing` *(WYSZUKIWARKA)*

### Why:

Advanced search capabilities:

- ranking results
- snippet highlighting
- multi-field search

➡️ Semantic search layer.

------

## 📌 CLEAN SUMMARY

- 🧠 Service Layer (DRZEWO, KODEKS, PANEL WM)
- 🏗️ Builder (DRZEWO, SKARBIEC)
- 📦 DTO (DRZEWO, MAPA, WNIOSKI)
- 🔌 Adapter (DRZEWO, MAPA, WNIOSKI)
- 🎯 Strategy (PINY, SKARBIEC, ŚPIEWNIK)
- 🧷 State (PINY, SKARBIEC, ŚPIEWNIK)
- 🧠 Domain Model (PANEL WM, PINY, KODEKS)
- 🌲 Composite (PANEL WM, PINY, SKARBIEC)
- 🔄 Workflow (SKARBIEC-heavy systems)
- 🗃️ Repository/Query (WYSZUKIWARKA, PINY)
- ⚡ Event-driven (WYSZUKIWARKA, MAPA, SKARBIEC)
- 🧩 Registry (WYSZUKIWARKA)
- 🧾 Snapshot (PINY, SKARBIEC)
- 🛡️ Anti-corruption layer (WNIOSKI, SKARBIEC, PINY)
- 🔍 Full-text search (WYSZUKIWARKA)



# 🧠 SOLID – analiza architektury systemu

## 🧩 Wprowadzenie

Architektura systemu została zaprojektowana w oparciu o warstwowy model (View → Service → Domain/ORM), z silnym naciskiem na separację odpowiedzialności oraz rozszerzalność. W praktyce wiele zasad SOLID jest realizowanych nie przez pojedyncze klasy, ale przez całe moduły i powtarzalne wzorce projektowe (np. strategy, service layer, polymorphism).

Dodatkowo istotną rolę odgrywa framework Django, który wymusza część dobrych praktyk architektonicznych (szczególnie SRP i DIP na poziomie aplikacji).

------

## 🧩 SRP – Single Responsibility Principle

W całym systemie widoczny jest wyraźny podział odpowiedzialności na poziomie warstw:

- widoki odpowiadają wyłącznie za komunikację HTTP i prezentację danych,
- logika biznesowa jest przeniesiona do dedykowanych serwisów,
- modele ORM pełnią rolę wyłącznie reprezentacji danych,
- operacje techniczne (np. import CSV, indeksowanie wyszukiwarki, dopasowanie transakcji) są izolowane w osobnych komponentach.

Dzięki temu każda zmiana w jednym obszarze (np. sposób dopasowania płatności w skarbcu) nie wpływa na resztę systemu.

W praktyce Django wspiera SRP poprzez rozdzielenie:

- `views.py` (warstwa HTTP),
- `models.py` (domena danych),
- `services.py` (logika aplikacyjna tworzona przez nas).

------

## 🧩 OCP – Open/Closed Principle

System jest silnie otwarty na rozszerzenia dzięki zastosowaniu:

- strategii (np. formatowanie tekstu w śpiewniku),
- modeli polimorficznych (np. wydarzenia w kalendarzu),
- systemu rejestracji (np. wyszukiwarka),
- warstwy filtrów (np. wyszukiwanie zaawansowane),
- integracji zewnętrznych (np. SSUJService, import bankowy).

Nowe funkcjonalności są dodawane przez:

- nowe strategie,
- nowe modele,
- nowe serwisy,

bez konieczności modyfikacji istniejącego rdzenia systemu.

Przykładowo: dodanie nowego sposobu formatowania pieśni nie wymaga zmian w logice renderowania — wystarczy nowa implementacja strategii.

------

## 🧩 LSP – Liskov Substitution Principle

Polimorfizm jest szeroko wykorzystywany w modelach domenowych:

- różne typy wydarzeń w kalendarzu mogą być traktowane jednolicie jako „wydarzenia kalendarzowe”,
- różne modele w wyszukiwarce są traktowane przez wspólny interfejs indeksowania,
- strategie formatowania w śpiewniku są wymienne bez wpływu na system nadrzędny.

Oznacza to, że każdy podtyp może zastąpić typ bazowy bez zmiany poprawności działania systemu.

------

## 🧩 ISP – Interface Segregation Principle

System unika „grubych interfejsów” poprzez rozdzielenie odpowiedzialności:

- wyszukiwanie, filtrowanie i indeksowanie są osobnymi mechanizmami,
- import danych, dopasowanie i powiadomienia w skarbcu są rozdzielone,
- integracje zewnętrzne (SSUJ, banki) są odseparowane od logiki domenowej.

Każdy komponent udostępnia tylko minimalny, potrzebny kontrakt — brak przypadków „jednej klasy do wszystkiego”.

------

## 🧩 DIP – Dependency Inversion Principle

System jest zbudowany w sposób, w którym:

- warstwa prezentacji zależy od serwisów, a nie od baz danych,
- logika biznesowa nie zależy od szczegółów implementacji (np. CSV, API banku),
- integracje zewnętrzne są odizolowane przez adaptery (SSUJService),
- wyszukiwarka i BI operują na abstrakcjach modeli, nie na konkretnych tabelach.

Django również wspiera DIP poprzez ORM i system aplikacji, który pozwala odwrócić zależności: modele nie znają widoków, a widoki nie znają szczegółów przechowywania danych.

------

## 🧠 Rola Django w realizacji SOLID

Framework Django wzmacnia zgodność z SOLID w kilku obszarach:

- **SRP:** rozdział models / views / templates
- **DIP:** ORM izoluje warstwę bazy danych
- **OCP:** system aplikacji umożliwia rozszerzanie funkcjonalności bez modyfikacji core frameworka
- **ISP:** modularność aplikacji Django (każda appka jako osobny kontekst domenowy)

Dzięki temu część zasad SOLID jest „wymuszona strukturalnie”, a nie tylko implementacyjnie.

------

## 📌 Podsumowanie

Architektura projektu realizuje SOLID nie na poziomie pojedynczych klas, ale jako:

- warstwowy podział systemu (View / Service / Domain),
- intensywne użycie strategii i polimorfizmu,
- modularność aplikacji Django,
- izolację integracji zewnętrznych,
- centralizację logiki biznesowej w serwisach.

Efektem jest system, który:

- łatwo rozszerzać,
- trudno „zepsuć przez przypadek”,
- i który naturalnie wspiera ewolucję funkcjonalności.





