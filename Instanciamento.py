"""
import serial
import pyfirmata
from tkinter import*

Class
-Arduino
uno = (porta arduino)
>Ligar
>Informar comunicação definida ou não

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

-Servo
servo1
uno.digital[6].mode = SERVO
pin6 = uno.get_pin('d:6:o')
def move_servo(a):
    uno.digital[6].write(a)

root = Tk()

scale = Scale(root,

              command = move_servo,
              to = 90,
              orient = HORIZONTAL,
              length = 400,
              label = 'Angle')
scale.pack(anchor = CENTER)
root.mainloop()

servo2

-Sensor
ldr1
ldr2
ldr3
ldr4
def registrar():
    with open('dataset_ldr.csv', 'a') as arquivo:
        contador_head = 0
        registro = writer(arquivo)
        while True:
            if contador_head < 1:
                registro.writerow(['Leitura', 'Data'])
            "adicionar +3 leituras(2-3-4)"
            contador_head += 1
            registro.writerow([str(leitura01()), str(tempo())])
#esta função registra termos em loop quando é invocada
-PlacaSolar
placa_solar

-GUI

"""
from pyfirmata import Arduino, util
import time

x = 0

esquerda = leitura01()
direita = leitura04()
inferior = 20
while esquerda > direita:
    x+=1
    print(x)
    ajuste1(x)
    if esquerda == direita:
        break

uno = Arduino("/dev/ttyACM0")
uno.exit()
