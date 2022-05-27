from pyfirmata import Arduino, SERVO, PWM, util
import time

uno = Arduino("/dev/ttyACM0")

uno.digital[3].mode = SERVO
uno.digital[6].mode = SERVO


def ajuste(angle):
    uno.digital[3].write(angle)
    time.sleep(0.08)


def ajuste2(angles):
    uno.digital[6].write(angles)
    time.sleep(0.08)


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
def leitura04():
    uno = Arduino("/dev/ttyACM0")
    it = util.Iterator(uno)
    it.start()
    ldr_leitura = uno.get_pin("a:3:i")
    time.sleep(1)
    ldr_leitura = ldr_leitura.read()
    return ldr_leitura

x = 0
