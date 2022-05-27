import time
from pyfirmata import Arduino, util
import datetime
import pytz
import pandas as pd
uno = Arduino('/dev/ttyACM0')

def tempo():
  "função retorna a hora atual do fuso horário do RN sempre que é chamada"
#https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568
  hAtual = pytz.timezone('Brazil/East')
  data_agora = str(datetime.datetime.now(hAtual))
  return data_agora[0:16]




def leitura02():
    uno = Arduino("/dev/ttyACM0")
    it = util.Iterator(uno)
    it.start()
    ldr_leitura = uno.get_pin("a:1:i")
    time.sleep(0.03)
    ldr_leitura = ldr_leitura.read()
    return ldr_leitura


def leitura01():
    "variável uno deve sempre ficar no mesmo bloco da leitura"
    uno = Arduino("/dev/ttyACM0")
    it = util.Iterator(uno)
    it.start()
    ldr_leitura = uno.get_pin("a:0:i")
    "por default, ldr_leitura ficará com o A0"
    time.sleep(0.03)
    ldr_leitura = ldr_leitura.read()
    return ldr_leitura


def leitura03():
    uno = Arduino("/dev/ttyACM0")
    it = util.Iterator(uno)
    it.start()
    ldr_leitura = uno.get_pin("a:2:i")
    time.sleep(1)
    ldr_leitura = ldr_leitura.read()
    return ldr_leitura

def leitura04():
    uno = Arduino("/dev/ttyACM0")
    it = util.Iterator(uno)
    it.start()
    ldr_leitura = uno.get_pin("a:3:i")
    time.sleep(1)
    ldr_leitura = ldr_leitura.read()
    return ldr_leitura

from csv import writer


def registrar():
    with open('dataset_ldr.csv', 'a') as arquivo:
        contador_head = 0
        registro = writer(arquivo)
        "adicionar +3 leituras(2-3-4)"
        contador_head += 1
        registro.writerow([str(leitura01()), str(tempo())])




"""for x in range(10):
    superior = int(leitura01() * 100)
    inferior = int(leitura02() * 100)
    esquerda = int(leitura03() * 100)
    direita = int(leitura04() * 100)

    print(f'a leitura 1 é: {superior}')
    time.sleep(1)
    print(f'a leitura 2 é: {inferior}')
    time.sleep(1)
    print(f'a leitura 3 é: {esquerda}')
    time.sleep(1)
    print(f'a leitura 4 é: {direita}')
    time.sleep(1)
    print('')"""



uno.exit()