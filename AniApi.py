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

    name = Style.BRIGHT + Fore.MAGENTA + """           AniMencion.Api \n """

    for l in name:
        sys.stdout.flush()
        print(l,end="")
        time.sleep(0.1)
    #fin banner
    print("")
    IDE = int(input(Style.BRIGHT + Fore.RED + 'N° de anime: ' + Fore.GREEN))
    api = "https://api.jikan.moe/v3/anime/{}".format(IDE)

    # -*-def BuscarPokemon(num): -*-
    pedir = requests.get(api)
    respuesta = json.loads(pedir.content)
    
    print(Style.BRIGHT + Fore.BLUE + 'Nombre: '+ Fore.YELLOW + respuesta['title_japanese'])
    print(respuesta['title'])
    print("")
    time.sleep(2)
    #print("Estudio"+ str(respuesta['studios']))
    print(Style.BRIGHT + Fore.BLUE + "Fans: "+ Fore.YELLOW + str(respuesta['members']))
    print(Style.BRIGHT + Fore.BLUE + "Puntuacion: "+ Fore.YELLOW + str(respuesta['score']))
    print("")
    time.sleep(2)
    print(Style.BRIGHT + Fore.BLUE +"Fecha: "+ Fore.YELLOW + str(respuesta["aired"]))
    print("")
    print(Style.BRIGHT + Fore.BLUE + 'Estado: '+ Fore.YELLOW + respuesta['status'])
    print("")
    time.sleep(2.1)
    print(Style.BRIGHT + Fore.BLUE + 'Clasificacion: '+ Fore.YELLOW + respuesta['rating'])
    print("")
    time.sleep(2.1)
    print(Style.BRIGHT + Fore.BLUE + "Popular: "+ Fore.YELLOW + str(respuesta['popularity']))
    print("")
    print(Style.BRIGHT + Fore.BLUE + 'Episodios '+ Fore.YELLOW + str(respuesta['episodes']))
    print("")
    time.sleep(2.1)
    print(Style.BRIGHT + Fore.BLUE + 'Duracion: '+ Fore.YELLOW + respuesta['duration'])
    print("")
    time.sleep(2.1)
    print(Style.BRIGHT + Fore.BLUE + 'Sitio: '+ Fore.GREEN + respuesta['url'])
    print("")
    time.sleep(2.1)
    #print(Style.BRIGHT + Fore.BLUE + "Synopsis: "+ Back.WHITE + Fore.BLACK + respuesta['synopsis'])
    #print("")
    print(Style.BRIGHT + Back.BLACK + Fore.BLUE + "Inicio como: "+ Fore.YELLOW + respuesta['source'])
    print("")
    time.sleep(2.1)
    print(Style.BRIGHT + Fore.BLUE + 'Tipo: '+ Fore.YELLOW + respuesta['type'])
    print("") 
    #print(Style.BRIGHT + Fore.BLUE + 'Episodios '+ Fore.YELLOW + str(respuesta['episodes']))
    time.sleep(2.1)
    print(Style.BRIGHT + Fore.MAGENTA + """                SYNOPSIS                   """)
    time.sleep(2.4)
    name = Style.BRIGHT + Back.WHITE + Fore.BLACK + respuesta['synopsis']
    
    for l in name:
        sys.stdout.flush()
        print(l,end="")
        time.sleep(0.1)

    #print("adaptacion: "+ respuesta['Adaptation'])


