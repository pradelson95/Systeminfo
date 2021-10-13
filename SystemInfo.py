import platform
import socket
from tabulate import *
from colorama import *
from time import sleep

Systeminfo = [["Sistema operativo ", platform.system()], ["El procesador",platform.processor()],
              ["La arquitectura ",platform.architecture()], ["Version de sistema",platform.version()],
              ["Tipo de maquina",platform.machine()],["Nombre del equipo",platform.node()]]

ListSystemInfo = ["obteniendo informacion del sistema operativo",
                  "Obteniendo informacion del procesador",
                  "Obteniendo informacion de la arquitectura"
                 ,"Obteniendo la version del sistema operativo",
                  "Obtetiendo el tipo de maquina",
                  "Obteniendo la ip"]

for elemento in ListSystemInfo:
    print(Fore.LIGHTGREEN_EX + elemento)
    sleep(2)

print(Fore.LIGHTRED_EX + tabulate(Systeminfo))
sleep(1)

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print("La direccion ip de la maquina es", ip)

Resultados = open("SystemInfo.txt","w")

for informacion in Systeminfo:
    Resultados.write(str(informacion) + "\n")
Resultados.close()

