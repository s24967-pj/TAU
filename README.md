# 1. TESTOWANIE OPGG
### Scenariusz 1 - opgg - dla każdej przeglądarki
Test ma na celu sprawdzenie poprawności działania strony OP.GG na europejskim serwerze oraz odczytanie pierwszego gracza w ranking wraz z punktami.
<li>Wchodzimy na stronę op.gg (EUNE)</li> 
<li>Klikamy w zakładkę "Leaderboards"</li>
<li>Próbujemy otrzymać nazwę gracza, który jest na pierwszym miejscu i go wypisać w logu</li>
<li>Próbujemy otrzymać punkty gracza, który jest na pierwszym miejscu i wypisać je w logu</li>

# 2. TESTOWANIE IKEA
### Scenariusz 2 - IKEA - dla każdej przeglądarki
Test sprawdza, czy użytkownik może przejść na stronę IKEA, wybrać produkt, dodać go do koszyka oraz czy w koszyku wyświetla się poprawna cena produktu.
<li>Wchodzimy na stronę ikea.com/pl/pl/ </li> 
<li>Rozwijamy, maksymalizujemy okno przeglądarki</li>
<li>Wybieramy kategorię "Meble"</li>
<li>Wybieramy podkategorię "Sofy i narożniki"</li>
<li>Klikamy na pierwszy dostępny produkt (lewy górny róg)</li>
<li>Dodajemy go do koszyka poprzez naciśnięcie przycisku "Dodaj do koszyka"</li>
<li>W okienku które nam wyskoczy wybieramy i klikamy opcję "Przejdź do koszyka"</li>
<li>Otrzymujemy cenę produktu i wypisujemy ją w logu</li>

# 3. TESTOWANIE MORELE
### Scenariusz 3 - Morele - dla każdej przeglądarki
Ten test ma na celu zweryfikowanie, czy próba zalogowania się na stronie Morele przy użyciu niezarejestrowanych danych wywołuje odpowiedni komunikat o błędzie.
<li>Wchodzimy na stronę Morele.net</li> 
<li>Akceptujemy ciasteczka klikając przycisk "Akceptuję wszystko"</li>
<li>Przechodzimy do zakładki logowania klikając opcję "Zaloguj się Załóż konto"</li>
<li>Wpisujemy nie zarejestrowany adres email</li>
<li>Wpisujemy przykładowe hasło</li>
<li>Klikamy przycisk "Zaloguj się"</li>
<li>Otrzymujemy powiadomienie o błędzie logowania i wypisujemy udany test w logu</li>

# 4. TESTOWANIE BURGERKING  
### Scenariusz 4 - Burger King - dla każdej przeglądarki
Ten test ma na celu sprawdzenie, czy użytkownik może zmienić język na stronie Burger King z polskiego na angielski, oraz czy po dokonaniu zmiany adres URL jest zgodny z oczekiwanym.
<li>Wchodzimy na stronę burgerking.pl/pl/</li> 
<li>Akceptujemy ciasteczka</li>
<li>Klikamy na ikonkę globusu w prawym górnym rogu strony</li>
<li>Wybieramy opcję "English"</li>
<li>Akceptujemy wybór przyciskiem</li>
<li>Weryfikujemy, czy URL strony zmienił się na wersję angielską</li>


