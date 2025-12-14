#Importações
import socket
import pyfiglet
import argparse
from colorama import Fore
from concurrent.futures import ThreadPoolExecutor, as_completed
#=======================================================================================================================

#Lista das portas comuns
ports = [20, 21, 22, 23, 25, 53, 67, 68, 80, 81, 82, 83, 88, 110, 111, 123, 135, 137, 138, 139, 143, 161, 162, 179,
         389, 443, 445, 465, 587, 636, 993, 995, 989, 990, 10250, 10255, 10257, 10259, 1433, 1434, 1521, 1522,
         1529, 161, 162, 179, 587, 6379, 6443, 7000, 7001, 7002, 7003, 7004, 7005, 8000, 8080, 8081,
         8082, 8088, 8089,8090,8443, 8444, 8834, 8888, 8883, 9000, 9001, 9080, 9090, 9091, 9092, 9093, 9094, 9100,
         9200, 9201, 9300, 9440, 9443, 10000, 10255, 10257, 10259, 11211, 15672, 1701, 1723, 179, 1883, 2181, 2375,
         2376, 2525, 27015, 27017, 27018, 27019, 28017, 3000, 3001, 30080, 30443, 3306, 3389, 3478, 4190, 4194, 5060,
         5061, 5173, 5174, 5349, 5601, 5672, 5985, 5986, 6000, 5900, 5987, 5988, 9418, 10443, 1194, 4500,
         500, 5080, 5081, 2049, 464, 3268, 3128, 8085, 8086, 8880, 4433, 50000, 50013, 199,502, 1911, 47808, 50070,
         8020]
#=======================================================================================================================

#Tentar se conectar a uma porta
def scann_port(host, port, timeout=1.5):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        code = sock.connect_ex((host, port))
        sock.close()
        return port, code == 0
    except:
        return port, False
#=======================================================================================================================

#Escanear todas as 65.535 portas
def scan_range(host):
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scann_port, host, port) for port in range(1, 65536)]

        for future in as_completed(futures):
            port, is_open = future.result()
            if is_open:
                print(Fore.GREEN + f'Port {port} is open')
#=======================================================================================================================

#Escanear as portas comuns
def scann_common_ports(host):
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(scann_port, host, port) for port in ports]

        for future in as_completed(futures):
            port, is_open = future.result()
            if is_open:
                print(Fore.GREEN + f'Port {port} is open')
#=======================================================================================================================

#Função main
def main():
    try:
        # Banner
        texto = pyfiglet.figlet_format('Port Scanner', font='slant')
        print(Fore.MAGENTA + "*" * 100)
        print(Fore.MAGENTA + texto)
        print(Fore.CYAN + "GitHub: github.com/Wevertonf45" + "\n")
        print(Fore.MAGENTA + "*" * 100)
        print("\n")

        # Argumentos
        parser = argparse.ArgumentParser(description='Port Scanner')

        parser.add_argument(
            "-H", "--host",
            required=True,
            help="Host to scan"
        )

        parser.add_argument(
            "-m", "--mode",
            choices=['full', 'common'],
            default='common',
            help="Tipo de scan: 'Full (65.535 portas)' ou common (As portas mais comuns)"
        )

        args = parser.parse_args()

        # Validar o host
        try:
            socket.gethostbyname(args.host)
        except:
            print("Endereço inválido!")
            exit(1)

        # Executar o modo escolhido
        if args.mode == 'common':
            scann_common_ports(args.host)
        elif args.mode == 'full':
            scan_range(args.host)
        else:
            print("Opção Inválida!")
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Scan interrompido pelo usuário.")
        exit(1)

if __name__ == '__main__':
    main()