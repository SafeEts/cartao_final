import RPi.GPIO as GPIO
import serial
import time

class Leds():
        
    def status(self, item):
        arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=2)

        if (item == "Cadastrado"):
            msg = 'c'
            arduino.write(msg.encode())
            time.sleep(0.2)

        if (item == "NaoCadastrado"):
            msg = 'e'
            arduino.write(msg.encode())
            time.sleep(0.2)

        if (item == "Padrao"):
            msg = 'p'
            arduino.write(msg.encode())
            time.sleep(0.2)

        if (item == "PortaAberta"):
            msg = 'a'
            arduino.write(msg.encode())
            time.sleep(0.2)

        if (item == "ColetaIncorreta"):
            msg = 'i'
            arduino.write(msg.encode())
            time.sleep(0.2)

        if (item == "FimDeCiclo"):
            msg = 'f'
            arduino.write(msg.encode())
            time.sleep(0.2)
            
        if (item == "Inicio"):
            msg = 't'
            arduino.write(msg.encode())
            time.sleep(0.2)

        
class Porta():
    def __init__(self):
        self.trava = 7
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.trava, GPIO.OUT)
        
    def destravar(self):
        self.trava = 7
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.trava, GPIO.OUT)
        GPIO.output(self.trava, 1)
        print("---- Porta destrancada ----")
        
    def travar(self):
        GPIO.cleanup(7)
        #GPIO.output(self.trava, 1)
        print("---- Porta trancada  ----")