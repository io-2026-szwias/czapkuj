# 1. OGRANICZENIA SYSTEMOWE (CONSTRAINTS)

## 1.1. Integracje i technologie

* **CON-1** System musi wspierać logowanie OAuth2 (Google) dla użytkowników.

* **CON-2** Wybrane moduły (np. Rozporządzenia SSUJ) muszą wspierać OAuth2 Microsoft.

* **CON-3** System integruje się z:

  * Google Calendar (sync wydarzeń)
  * Google Drive (pliki)
  * Gmail (powiadomienia)
  * systemem bankowym (import CSV)

* **CON-4** System wspiera formaty danych:

  * CSV (finanse)
  * JSON (śpiewnik)
  * PDF (raporty, kody)
  * PNG (genealogia)

---

## 1.2. Bezpieczeństwo

* **CON-5** System używa RBAC (Role-Based Access Control):

  * Odwiedzający / Bean / Czapkowicz / Członek / Weteran
  * Zarząd / Moderator / Administrator

* **CON-6** Dane finansowe dostępne tylko dla Skarbnika i Administratora.

* **CON-7** Operacje krytyczne wymagają:

  * autoryzacji roli
  * zapisania w Osi Czasu

* **CON-8** Kody awansu:

  * jednorazowe
  * TTL max 30 dni
  * nie mogą być ponownie użyte

---

## 1.3. Dane i spójność

* **CON-9** System utrzymuje SSOT (Single Source of Truth) dla:

  * użytkowników
  * wydarzeń
  * finansów
  * treści
  * ról

* **CON-10** Każda zmiana danych jest:

  * wersjonowana
  * logowana w Osi Czasu

* **CON-11** Drzewo genealogiczne nie może zawierać cykli.

---

## 1.4. Operacyjne

* **CON-12** System działa na desktop / mobile / tablet (responsywność).
* **CON-13** Tryb Focus w śpiewniku musi mieć wysoki kontrast (nocny UX).
* **CON-14** Mapa działa w trybie cache offline (ograniczona funkcjonalność).

---

# 2. WYMAGANIA SYSTEMOWE (ARCHITEKTURA)

## 2.1. Architektura

* **ARC-1** System oparty o modular monolith lub microservices:

  * Auth Service
  * User Service
  * Events Service
  * Finance Service
  * Content Service
  * Music Service
  * Map Service
  * Notification Service
  * Audit Log Service (Oś Czasu)

---

## 2.2. Role i uprawnienia

* **ARC-2** System wspiera RBAC + ABAC.
* **ARC-3** Uprawnienia są kontekstowe (np. edycja Bio wymaga moderacji).
* **ARC-4** Administrator może:

  * nadawać role
  * generować kody awansu
  * zmieniać konfigurację systemu

---

## 2.3. Powiadomienia

* **ARC-5** System wspiera powiadomienia real-time (push + in-app).
* **ARC-6** Każde zdarzenie krytyczne generuje alert:

  * zmiana roli
  * ban
  * składki
  * komentarze

---

## 2.4. Audyt (Oś Czasu)

* **ARC-7** Każda operacja CRUD w modułach administracyjnych jest logowana.
* **ARC-8** Log zawiera:

  * user ID
  * rolę
  * timestamp
  * moduł
  * typ operacji
  * diff danych

---

## 2.5. Pliki

* **ARC-9** System obsługuje upload:

  * PNG
  * CSV

* **ARC-10** System generuje:

  * PDF (raporty, kody)
  * PNG (genealogia)

* **ARC-11** Pliki są walidowane (format, rozmiar, struktura).

---

# 3. NIEFUNKCJONALNE WYMAGANIA (NFR)

---

## 3.1. Wydajność

* **NFR-PERF-1** 95% requestów API ≤ 400 ms
* **NFR-PERF-2** dashboard ≤ 800 ms
* **NFR-PERF-3** ciężkie widoki (mapa, genealogia, śpiewnik search) ≤ 2.5 s
* **NFR-PERF-4** generowanie PDF (do 10 kodów) ≤ 5 s
* **NFR-PERF-5** import CSV (do 2 000 transakcji) ≤ 10 s
* **NFR-PERF-6** logowanie OAuth ≤ 5 s

---

## 3.2. Skalowalność

* **NFR-SCAL-1** System obsługuje:

  * 100 aktywnych użytkowników jednocześnie
  * 10 równoległych edycji śpiewnika (max realny scenariusz)
  * 50 operacji finansowych/min

* **NFR-SCAL-2** Backend musi wspierać poziome skalowanie bez downtime.

---

## 3.3. Dostępność

* **NFR-AVL-1** SLA systemu: 99.5%
* **NFR-AVL-2** maksymalny downtime: 3.6h/miesiąc
* **NFR-AVL-3** moduły finansowe i wydarzenia: 99.9% uptime

---

## 3.4. Spójność i niezawodność

* **NFR-DATA-1** transakcje finansowe ACID
* **NFR-DATA-2** operacje awansu atomowe
* **NFR-DATA-3** synchronizacja statusów ≤ 5 s
* **NFR-DATA-4** brak utraty danych przy awarii

---

## 3.5. Bezpieczeństwo

* **NFR-SEC-1** TLS 1.2+
* **NFR-SEC-2** hasła (jeśli lokalne): Argon2/Bcrypt
* **NFR-SEC-3** OAuth token TTL ≤ 1h
* **NFR-SEC-4** blokada konta po 5 błędnych próbach
* **NFR-SEC-5** kody awansu:

  * jednorazowe
  * max 30 dni ważności

---

## 3.6. Audytowalność

* **NFR-AUD-1** 100% operacji admin logowane
* **NFR-AUD-2** logi nieusuwalne przez moderatorów
* **NFR-AUD-3** retencja min. 2 lata
* **NFR-AUD-4** eksport CSV/PDF

---

## 3.7. UX

* **NFR-UX-1** max 3 kliknięcia do wydarzenia
* **NFR-UX-2** max 2 kliknięcia do śpiewnika
* **NFR-UX-3** max 3 kliknięcia do składek
* **NFR-UX-4** wszystkie kluczowe funkcje ≤ 2 poziomy menu
* **NFR-UX-5** tryb Focus: brak rozproszeń + wysoki kontrast

---

## 3.8. Accessibility

* **NFR-A11Y-1** WCAG 2.1 AA
* **NFR-A11Y-2** pełna obsługa klawiatury
* **NFR-A11Y-3** kontrast ≥ 4.5:1
* **NFR-A11Y-4** alt text dla wszystkich grafik
* **NFR-A11Y-5** tryb nocny obowiązkowy dla mapy i śpiewnika

---

## 3.9. Kompatybilność

* **NFR-COMP-1** Chrome / Firefox / Edge (2 ostatnie wersje)
* **NFR-COMP-2** Safari desktop + mobile
* **NFR-COMP-3** responsywność 320px – 4K

---

## 3.10. Współbieżność

* **NFR-CONC-1** optimistic locking dla śpiewnika
* **NFR-CONC-2** brak utraty danych przy równoległej edycji
* **NFR-CONC-3** konflikty rozwiązywane wersjonowaniem

---

## 3.11. Integracje

* **NFR-INT-1** Google sync ≤ 5 s
* **NFR-INT-2** Microsoft OAuth ≤ 2 s
* **NFR-INT-3** CSV bankowy walidacja ≤ 10 s

---

## 3.12. Monitoring

* **NFR-MON-1** logi + metryki + tracing
* **NFR-MON-2** alert krytyczny < 1 min
* **NFR-MON-3** alert przy spadku SLA < 99%

---

# 4. PODSUMOWANIE

System musi zapewniać:

* kontrolę dostępu (RBAC + audyt)
* małą, realną skalę (~100 użytkowników)
* spójność danych (finanse + role)
* szybkie UX (≤ 2–3 kliknięcia)
* pełny audyt (Oś Czasu)
* integracje Google/Microsoft
* wysoką niezawodność i prostą skalowalność
