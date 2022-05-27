import datetime
import time

import pandas as pd
import pytz
def tempo():
  "função retorna a hora atual do fuso horário do RN sempre que é chamada"
#https://gist.github.com/heyalexej/8bf688fd67d7199be4a1682b3eec7568
  hAtual = pytz.timezone('Brazil/East')
  data_agora = str(datetime.datetime.now(hAtual))
  return data_agora[0:16]


"""df = pd.DataFrame(lista, columns=['Data&Hora',
                                  'Leitura1',
                                  'Leitura2',
                                  'leitura3',
                                  'leitura4'])
#colocar dados de cada leitura
print(df)
"""



"""def leitura1(self):
    it = util.Iterator(uno)
    it.start()
    ldr_leitura = uno.get_pin("a:0:i")
    "por default, ldr_leitura ficará com o A0"
    time.sleep(0.3)
    ldr_leitura.read()
    if ldr_leitura == "None":
        ldr_leitura = 0
    elif ldr_leitura > 1:
            ldr_leitura = 0
    else:
        ldr_leitura = ldr_leitura
    file = open(arquivo, 'a')
    file.writelines(str(ldr_leitura))
    print(ldr_leitura)
    if count == 19:
        file.close()
"""



"""while count < 20:
    uno = Arduino("/dev/ttyACM0")
    it = util.Iterator(uno)
    it.start()
    ldr = uno.get_pin("a:0:i")
    time.sleep(0.3)
    leitura = ldr.read()
    if leitura == "None":
        leitura = 0
    elif leitura > 1:
        leitura = 0
    else:
        leitura = leitura
    file = open(arquivo, 'a')
    file.writelines(str(leitura))
    count = count + 1
    print(leitura)
    if count == 19:
        file.close()

print("coleta finalizada")
"""

"""
while True:
    if sensor1 - sensor2 > 5:
        motor1 += 1
        sensor2 += 1
        print("ajustando1")
        print(motor1, motor2, sensor1, sensor2)
        time.sleep(0.5)
    elif sensor2 - sensor1> 5:
        motor2 += 1
        sensor1 += 1
        print("ajustando2")
        time.sleep(0.5)
    elif sensor2 == sensor1:
        print("sistema balanceado")
        time.sleep(3)
        break"""

