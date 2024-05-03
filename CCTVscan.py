#Biblioteki wymagające instalacji
import requests
#biblioteki wbudowane
import concurrent.futures

count = 0

print("╔═╗╔═╗╔╦╗╦  ╦┌─┐┌─┐┌─┐┌┐┌  ")
print("║  ║   ║ ╚╗╔╝└─┐│  ├─┤│││  ")
print("╚═╝╚═╝ ╩  ╚╝ └─┘└─┘┴ ┴┘└┘  ")
print("By Szibaszyn")
print("Wersja 1.5")
print("")
print("Program skanuje adresy ip w poszukiwaniu dostępnych 9 infrastruktór kamer IP")
print("Uwaga! Program może spowodować wykrycie przez systemy zabezpieczeń jako atak typu 'ddos'! Używaj z rozwagą!")
print("Uwaga! Program może przeciążyć sieć i spowodować jej spowolnienie. Używaj z rozwagą!")
print("Uwaga! Program może spowolnić działanie komputera! Używaj z rozwagą!")
print("")
# Wybór ilości wątków, czasu na odpowiedź serwera i rozmiaru bufora
print("Wybierz ilość wątków (zalecane: 128). Im więcej wątków, tym szybsze skanowanie, ale większe obciążenie sieci i komputera.")
workersmaxnumber = input("Wątki: ")
workersmaxnumber = int(workersmaxnumber)
print("Wybierz ilość czasu na odpowiedź serwera (zalecane: 5). Im więcej czasu, tym większa szansa na znalezienie kamer, ale dłuższe skanowanie.")
timeoftimeout = input("Czas na odpowiedź serwera: ")
timeoftimeout = int(timeoftimeout)
print("Wybierz rozmiar bufora (zalecane: 256). Im większy bufor, tym większa szansa na znalezienie kamer, ale dłuższe skanowanie.")
buffersize = input("Rozmiar bufora: ")
buffersize = int(buffersize)

print("")
print("Wczytuję listę portów...")

# Lista portów do skanowania
port = [
    80,81,82,83,84,85,86,87,88,89,90,
    8080,8081,8082,8083,8084,8085,8086,8087,8088,8089,8090,
    1024,
    2000,
    8888,
    5000,
    9000,9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,
    8000,8001,8002,8003,8004,8005,8006,8007,8008,8009,8010
]

print(f"Liczba portów do skanowania w adresach IP: {len(port)}")
print("Wczytuję listę adresów IP...")

# Otwórz plik z adresami IP
with open('addr_in.txt', 'r') as f:
    adresy_ip = f.read().splitlines()

print(f"Liczba adresów IP do skanowania: {len(adresy_ip)}")
print("Generuję listę adresów URL...")
print("")

# Generowanie listy URLi do skanowania
urls = []
for ip in adresy_ip:
    # Dodaj adres IP bez portu
    urls.append(f"http://{ip}/mjpg/video.mjpg")
    urls.append(f"http://{ip}/video/mjpg.cgi")
    urls.append(f"http://{ip}/mjpeg.cgi")
    urls.append(f"http://{ip}/img/video.mjpeg")
    urls.append(f"http://{ip}/?action=stream")
    urls.append(f"http://{ip}/asp/video.cgi")
    urls.append(f"http://{ip}/videostream.cgi?user=admin&pwd=")
    urls.append(f"http://{ip}/-wvhttp-01-/GetOneShot?frame_count=1000000000")
    urls.append(f"http://{ip}/image?speed=0")


    for port_number in port:
        urls.append(f"http://{ip}:{port_number}/mjpg/video.mjpg")
        urls.append(f"http://{ip}:{port_number}/video/mjpg.cgi")
        urls.append(f"http://{ip}:{port_number}/mjpeg.cgi")
        urls.append(f"http://{ip}:{port_number}/img/video.mjpeg")
        urls.append(f"http://{ip}:{port_number}/?action=stream")
        urls.append(f"http://{ip}:{port_number}/asp/video.cgi")
        urls.append(f"http://{ip}:{port_number}/videostream.cgi?user=admin&pwd=")
        urls.append(f"http://{ip}:{port_number}/-wvhttp-01-/GetOneShot?frame_count=1000000000")
        urls.append(f"http://{ip}:{port_number}/image?speed=0")

print("Rozpoczynam skanowanie...")
print("")

# Funkcja skanująca URL
def scan_url(url):
    try:
        # Wykonaj zapytanie HTTP
        with requests.get(url, timeout=timeoftimeout, stream=True) as response:
            # Sprawdź, czy status odpowiedzi to 200
            if response.status_code == 200:
                # Pobierz tylko pierwszy kawałek odpowiedzi
                first_chunk = next(response.iter_content(buffersize), None)

                # Jeżeli serwer zaczyna przesyłać plik
                if first_chunk:
                    with open('addr_out.txt', 'a') as f:
                        f.write(f"{url}\n")
                    print("!", end='', flush=True)
                    return url
                else:
                    return None
            else:
                print(".", end='', flush=True)
                return None
    except Exception as e:
        None

# Skanowanie URLi wielowątkowo
with concurrent.futures.ThreadPoolExecutor(max_workers=workersmaxnumber) as executor:
    results = executor.map(scan_url, urls)

print("\n")
print("Skanowanie zakończone!")
print("Wyniki zapisane!")
print("Listuje wyniki...")
print("")

for result in results:
    if result is not None:
        count += 1
        print(f"Znaleziono kamerę numer: {count} pod adresem: {result}")

# Zakończ program
print("")
print("Dziękuje za skorzystanie ze skanera!")
print(f"Łącznie znaleziono {count} kamer!")
input("Naciśnij Enter aby zakończyć...")
