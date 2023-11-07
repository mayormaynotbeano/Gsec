from colorama import Fore
from modules import sub_output
from parsers import nuclei


def nuclei_cve_scan(domain: str) -> str:
    sub_output.subpro_scan(f"nuclei -u {domain} -t http/cves/ -severity medium,high,critical -silent -c 100 -j -o vulnerable.json")
    sub_output.subpro_scan(f"nuclei -u {domain} -t http/vulnerabilities/ -severity medium,high,critical -silent -c 100 -j -o vulnerable.json")
    sub_output.subpro_scan(f"nuclei -u {domain} -t http/misconfiguration/ -severity high,critical -silent -c 100 -j -o vulnerable.json")
    nuclei.parse()

    

def nuclei_ultimate_scan(domain: str) -> str:
    print(f"{Fore.MAGENTA}[+] {Fore.CYAN}- {Fore.WHITE}Task{Fore.CYAN}:{Fore.LIGHTBLUE_EX} CVE{Fore.WHITE} Status: {Fore.GREEN}Running...")
    sub_output.subpro_scan(f"nuclei -u {domain} -t http/cves/ -severity medium,critical,high -silent -c 100 -j -o vulnerable.json")
    nuclei.parse()
    print(f"{Fore.MAGENTA}[+] {Fore.CYAN}- {Fore.WHITE}Task{Fore.CYAN}:{Fore.LIGHTBLUE_EX} CVE{Fore.WHITE} Status: {Fore.GREEN}DONE!\n")
    print(f"{Fore.MAGENTA}[+] {Fore.CYAN}- {Fore.WHITE}Task{Fore.CYAN}:{Fore.LIGHTBLUE_EX} Vulnerabilities{Fore.WHITE} Status: {Fore.GREEN}Running...")
    sub_output.subpro_scan(f"nuclei -u {domain} -t http/vulnerabilities/ -severity medium,critical,high -silent -c 100 -j -o vulnerable.json")
    nuclei.parse()
    print(f"{Fore.MAGENTA}[+] {Fore.CYAN}- {Fore.WHITE}Task{Fore.CYAN}:{Fore.LIGHTBLUE_EX} Vulnerabilities{Fore.WHITE} Status: {Fore.GREEN}DONE!\n")
    print(f"{Fore.MAGENTA}[+] {Fore.CYAN}- {Fore.WHITE}Task{Fore.CYAN}:{Fore.LIGHTBLUE_EX} Misconfigurations{Fore.WHITE} Status: {Fore.GREEN}Running...")
    sub_output.subpro_scan(f"nuclei -u {domain} -t http/misconfiguration/ -severity medium,critical,high -silent -c 100 -j -o vulnerable.json")
    nuclei.parse()
    print(f"{Fore.MAGENTA}[+] {Fore.CYAN}- {Fore.WHITE}Task{Fore.CYAN}:{Fore.LIGHTBLUE_EX} Misconfiguration{Fore.WHITE} Status: {Fore.GREEN}DONE!\n")
    print(f"{Fore.MAGENTA}[+] {Fore.CYAN}- {Fore.WHITE}Status: {Fore.GREEN}All Tasks done!!")