import RPi.GPIO as GPIO
import time
from saidas import Leds

LED = Leds()
    
def monitora():

    PIN_PUL_1 = 11
    PIN_PUL_2 = 12
    PIN_PUL_3 = 13
    PIN_PUL_4 = 15
    PIN_PUL_5 = 18
    PIN_PUL_6 = 19
    PIN_PUL_7 = 21
    PIN_PUL_8 = 22
    PIN_PUL_9 = 23
    PIN_PUL_10 = 29
    PIN_PUL_11 = 31
    PIN_PUL_12 = 33
    PIN_PUL_13 = 36
    PIN_SENSOR_PORTA = 37
    
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN_PUL_1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_PUL_2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_PUL_3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_PUL_4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_PUL_5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_PUL_6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_PUL_7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_PUL_8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_PUL_9, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_PUL_10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_PUL_11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_PUL_12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_PUL_13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(PIN_SENSOR_PORTA, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    buf_sensor_porta = 0
    l = 3
     
    while True:
    
        pul_1 = GPIO.input(PIN_PUL_1)
        pul_2 = GPIO.input(PIN_PUL_2)
        pul_3 = GPIO.input(PIN_PUL_3)
        pul_4 = GPIO.input(PIN_PUL_4)
        pul_5 = GPIO.input(PIN_PUL_5)
        pul_6 = GPIO.input(PIN_PUL_6)
        pul_7 = GPIO.input(PIN_PUL_7)
        pul_8 = GPIO.input(PIN_PUL_8)
        pul_9 = GPIO.input(PIN_PUL_9)
        pul_10 = GPIO.input(PIN_PUL_10)
        pul_11 = GPIO.input(PIN_PUL_11)
        pul_12 = GPIO.input(PIN_PUL_12)
        pul_13 = GPIO.input(PIN_PUL_13)
        sensor_porta = GPIO.input(PIN_SENSOR_PORTA)
        time.sleep(0.2)

        
        if ((sensor_porta == 0) and (buf_sensor_porta == 0)): # abriu a porta
               buf_sensor_porta = 1
               
        if ((sensor_porta == 0) and (buf_sensor_porta == 1)):
                
                pul_vf = ["oi", pul_1, pul_2, pul_3] #  pul_4, pul_5,pul_6, pul_7, pul_8, pul_9,pul_10, pul_11, pul_12, pul_13
                x_vf = pul_vf.count(1)
                
                qnt_ = l - x_vf  
                
                if (qnt_ > 1):
                    print("---- Coleta Incorreta ----")
                    LED.status("ColetaIncorreta")
                    time.sleep(1.3)
                    alarme = 1
                    
                else:
                    print("---- Porta aberta ----")
                    LED.status("PortaAberta")
                    time.sleep(0.6)
                    alarme = 0
               
        if ((sensor_porta == 1) and (buf_sensor_porta == 1) and (alarme == 0)): # quando fechar a porta:
                
            # verificação de alteração
            # ...
            l = x_vf
            pul = ["oi", pul_1, pul_2, pul_3] #  pul_4, pul_5,pul_6, pul_7, pul_8, pul_9,pul_10, pul_11, pul_12, pul_13
            buf_sensor_porta = 0
            return pul
            break
        
        elif ((sensor_porta == 1) and (buf_sensor_porta == 1) and (alarme == 1)):
            print("---- Coleta Incorreta ----")
            LED.status("ColetaIncorreta")
            time.sleep(1.3)