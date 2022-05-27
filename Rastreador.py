from pyfirmata import Arduino, SERVO, util
import datetime
import serial
import pytz
import pandas as pd
import time
from csv import writer


"Conectar placa"
uno = Arduino("/dev/ttyACM0")
"""
while True:
    try:
        uno = serial.Serial("/dev/ttyACM0", timeout=1.8)
#bauderate default = 9600, timeout ajustado para 1.8s (tempo de espera de processamento)
        print("Conexão estabelecida com sucesso")
        break
    except:
        print("conexão falhou, confira se a porta está com acesso liberado \n"
              "ou se o caminho fornecido está correto \n"
              " "
              "DICA: Use o terminal")
        break
"""


#Data
def tempo():
  "função retorna a hora atual do fuso horário do RN sempre que é chamada"
#https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568
  hAtual = pytz.timezone('Brazil/East')
  data_agora = str(datetime.datetime.now(hAtual))
  return data_agora[0:16]


#Sensores LDR
def leitura01():
    "variável uno deve sempre ficar no mesmo bloco da leitura"
    uno = Arduino("/dev/ttyACM0")
    it = util.Iterator(uno)
    it.start()
    ldr_leitura = uno.get_pin("a:0:i")
    "por default, ldr_leitura ficará com o A0"
    time.sleep(1)
    ldr_leitura = ldr_leitura.read()
    return ldr_leitura


def leitura02():
    uno = Arduino("/dev/ttyACM0")
    it = util.Iterator(uno)
    it.start()
    ldr_leitura = uno.get_pin("a:1:i")
    "por default, ldr_leitura ficará com o A1"
    time.sleep(1)
    ldr_leitura = ldr_leitura.read()
    return ldr_leitura

def leitura03():
    uno = Arduino("/dev/ttyACM0")
    it = util.Iterator(uno)
    it.start()
    ldr_leitura = uno.get_pin("a:2:i")
    "por default, ldr_leitura ficará com o A2"
    time.sleep(1)
    ldr_leitura = ldr_leitura.read()
    return ldr_leitura

def leitura04():
    uno = Arduino("/dev/ttyACM0")
    it = util.Iterator(uno)
    it.start()
    ldr_leitura = uno.get_pin("a:3:i")
    "por default, ldr_leitura ficará com o A3"
    time.sleep(1)
    ldr_leitura = ldr_leitura.read()
    return ldr_leitura


#Registro
def registrar():
    with open('dataset_ldr.csv', 'a') as arquivo:
        contador_head = 0
        registro = writer(arquivo)
        if contador_head < 1:
            registro.writerow(['Leitura_1', 'Leitura_2','Leitura_3','Leitura_4', 'Data'])
            contador_head += 1
        registro.writerow([str(leitura01()), str(leitura02()),str(leitura02()),
                               str(leitura04()),str(tempo())])



#SERVOS
uno.digital[3].mode = SERVO
uno.digital[6].mode = SERVO



def ajuste(angle):
    uno.digital[3].write(angle)
    time.sleep(0.1)


def ajuste2(angles):
    uno.digital[6].write(angles)
    time.sleep(0.08)

x = 90
y = 5

while True:
    ldr1 = int(leitura01() * 100)
    ldr2 = int(leitura02() * 100)
    ldr3 = int(leitura03() * 100)
    ldr4 = int(leitura04() * 100)
    if ldr1+ldr2>ldr3+ldr4:
        if x != 170:
            x+=10
        ajuste2(x)
        print(ldr1,ldr2,ldr3, ldr4, x)



    if ldr1 + ldr2 < ldr3 +ldr4:
        if x != 0:
            x+=-10
        ajuste2(x)
        print(ldr1, ldr2, ldr3, ldr4, x)


    if ldr1 + ldr3 > ldr2 +ldr4:
        if y != 70:
            y += 5
        ajuste(y)
        print(ldr1, ldr2, ldr3, ldr4, y)

    if ldr1 + ldr3 < ldr2 + ldr4:
        if y != 0:
            y += -5
        ajuste(y)
        print(ldr1, ldr2, ldr3, ldr4, y)






