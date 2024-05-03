# CCTVscan.py

Ten skrypt Pythona jest narzędziem do skanowania adresów IP w poszukiwaniu dostępnych infrastruktur kamer IP. 

## Wymagania

Skrypt korzysta z następujących bibliotek:
- `requests`
- `concurrent.futures` (wbudowana)

## Użycie

Po uruchomieniu skryptu, użytkownik jest proszony o podanie trzech parametrów:

1. **Ilość wątków**: Ilość wątków używanych do skanowania. Więcej wątków oznacza szybsze skanowanie, ale większe obciążenie sieci i komputera.
2. **Czas na odpowiedź serwera**: Czas, jaki skrypt czeka na odpowiedź od serwera. Więcej czasu zwiększa szansę na znalezienie kamer, ale wydłuża czas skanowania.
3. **Rozmiar bufora**: Rozmiar bufora używanego podczas skanowania. Większy bufor zwiększa szansę na znalezienie kamer, ale wydłuża czas skanowania.

## Ostrzeżenia

Skrypt może:

- zostać wykryty przez systemy zabezpieczeń jako atak typu 'ddos'
- przeciążyć sieć i spowodować jej spowolnienie
- spowolnić działanie komputera

## Lista Infrastruktur kamer


- Axis
- DLink
- DLink-DCS-932
- Linksys
- Streamer
- Vije
- Foscam
- Canon
- Sony-CS3

## Lista portów

Skrypt skanuje następujące porty:

- Od 80 do 90
- Od 8080 do 8090
- Od 9000 Do 9010
- 1024
- 2000
- 5000
- 8888

Wybrane porty są jednymi z najczęściej wybieranych.
