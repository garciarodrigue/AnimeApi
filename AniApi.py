#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys,time
from colorama import Style,  Back, Fore, init
init()

import requests
import json

if __name__ == '__main__':
  
    os.system('clear')

    name = Style.BRIGHT + Fore.MAGENTA + """         ⌘⌘ AniMencion.Api ⌘⌘ \n """

    for l in name:
        sys.stdout.flush()
        print(l,end="")
        time.sleep(0.1)
    #fin banner
    print("")
    
    IDE = int(input(Style.BRIGHT + Fore.RED + 'Busca Animes Random\nColoca cualquier Numero ➫ ' + Fore.GREEN) + "\n")
    api = "https://api.jikan.moe/v3/anime/{}".format(IDE)

    # -*-def BuscarPokemon(num): -*-
    pedir = requests.get(api)
    respuesta = json.loads(pedir.content)
    
    print("\n" + Style.BRIGHT + Fore.BLUE + 'Nombre ⌦ '+ Fore.YELLOW + respuesta['title_japanese'])
    print(respuesta['title'] + "\n")
    #print("")
    #time.sleep(2)
    #print("Estudio"+ str(respuesta["studios"]))
    #print("")
    fans = Style.BRIGHT + Fore.BLUE + "Fans ↬  "+ Fore.YELLOW + str(respuesta['members']) + "\n"
    puntuacion = Style.BRIGHT + Fore.BLUE + "Puntuacion ↬  "+ Fore.YELLOW + str(respuesta['score']) + "\n"
    #print("")
    #time.sleep(2)
    fecha = Style.BRIGHT + Fore.BLUE + "Fecha ↬  "+ Fore.YELLOW + str(respuesta["aired"]) + "\n"
    #print("")
    estado = Style.BRIGHT + Fore.BLUE + 'Estado ↬  '+ Fore.YELLOW + respuesta['status'] + "\n"
    #time.sleep(2.1)
    clasificacion = Style.BRIGHT + Fore.BLUE + 'Clasificacion ↬  '+ Fore.YELLOW + respuesta['rating'] + "\n"
    #print("")
    #time.sleep(2.1)
    popular = Style.BRIGHT + Fore.BLUE + "Popular ↬   "+ Fore.YELLOW + str(respuesta['popularity']) + "\n"
    #print("")
    episodios = Style.BRIGHT + Fore.BLUE + 'Episodios ↬  '+ Fore.YELLOW + str(respuesta['episodes']) + "\n"
    #print("")
    #time.sleep(2.1)
    duracion = Style.BRIGHT + Fore.BLUE + 'Duracion ↬  '+ Fore.YELLOW + respuesta['duration']
    #print("")
    #time.sleep(2.1)
    web = Style.BRIGHT + Fore.BLUE + 'Sitio ↬  '+ Fore.GREEN + respuesta['url']
    #print("")
    #time.sleep(2.1)
    #print(Style.BRIGHT + Fore.BLUE + "Synopsis: "+ Back.WHITE + Fore.BLACK + respuesta['synopsis'])
    #print("")
    inicio = Style.BRIGHT + Back.BLACK + Fore.BLUE + "Inicio como ↬  "+ Fore.YELLOW + respuesta['source']
    #print("")
    #time.sleep(2.1)
    tipo = Style.BRIGHT + Fore.BLUE + 'Tipo ↬  '+ Fore.YELLOW + respuesta['type']
    print(Style.BRIGHT + Fore.RED + "Esta es la info que te puedo mostrar" +  Fore.MAGENTA + """ 
    ➣ fans
    ➣ clasificacion
    ➣ tipo
    ➣ estado
    ➣ puntuacion
    ➣ fecha
    ➣ episodios
    ➣ web
    ➣ duracion
    ➣ inicio
    ➣ popular
    ➣ synopsis
          """) 
    #print(Style.BRIGHT + Fore.BLUE + 'Episodios '+ Fore.YELLOW + str(respuesta['episodes']))
    time.sleep(2.1)
#if __name__ == '__main__':
    #def pedirDatos():  
def datos():
    while True:
        try:
            elige = input(Style.BRIGHT + Fore.RED + "Escribe el tipo de Inf:➽  " + Fore.GREEN)

            if elige == "tipo":
                print("\n" + tipo)
    
            elif elige == "clasificacion":
                print("\n" + clasificacion)
    
            elif elige == "episodios":
                print("\n" + episodios)

            elif elige == "fecha":
                print("\n" + fecha)

            elif elige == "web":
                print("\n" + web)

            elif elige == "inicio":
                print("\n" + inicio)

            elif elige == "popular":
                print("\n" + popular)

            elif elige == "fans":
                print("\n" + fans)
        
            elif elige == "duracion":
                print("\n" + duracion)

            elif elige == "puntuacion":
                print("\n" + puntuacion)

            elif elige == "estado":
                print("\n" + estado)
            

            elif elige == "synopsis":
                print(Style.BRIGHT + Fore.MAGENTA + """\n              ◉ SYNOPSIS ◎                   """)
                time.sleep(2.4)
                name = Style.BRIGHT + Back.WHITE + Fore.BLACK + respuesta['synopsis\n'] + Back.BLACK
    
                for l in name:
                    sys.stdout.flush()
                    print(l,end="")
                    time.sleep(0.1)
            else:
                print(Style.BRIGHT + Fore.CYAN + "\nError\nAsegurate de aver Escrito bien\n")
    #pedirDatos();
    #print("adaptacion: "+ respuesta['Adaptation'])
            break
        except ValueError:
            print(Fore.RED ,"\ninfo no coinside\n")
datos()
while True:
    try:
        datos()
    except ValueError:
        datos()
