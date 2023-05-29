import time
import serial
from saidas import Leds, Porta
from sensores import monitora

LED = Leds()
porta = Porta()

arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=2)


lst = ["509121", "123456", "111111"] # Lista de crachás cadastrados
z = 3
x1 = 3
inicio = True

while True:
    if (inicio == True):
        time.sleep(2)
        LED.status("Inicio")
        time.sleep(1)
        inicio = False

    LED.status("Padrao")

    try:
        text = input('Número do crachá: ')

        if text not in lst:
            print("\nVocê não tem permissão!\n")
            # Acende LED vermelho -> Usuário não cadastrado
            LED.status("NaoCadastrado")
            time.sleep(3)
            continue

        # Acende LED verde -> Usuário identificado
        LED.status("Cadastrado")
        porta.destravar()

        pul = monitora() # Faz a leitura dos sensores e retona uma lista
        
        x = pul.count(1)
        y = pul.count(0)
        
        print(pul)
        
       # print("True =", x)
       # print("False =>", y)
                 
        w = x - y  # W -> análise atual; Z-> análise passada
       # print("w -> ", w)
       # print("z -> ", z)
        
        if(w != z):
            print("\nOcorreu uma alteração")
            qnt = x1 - x
            
            if (qnt < 0):
                print("Foram acrescentadas", abs(qnt), "pulseiras.")
            elif (qnt > 0):
                print("Foram retiradas", abs(qnt), "pulseiras.")
            z = w
            x1 = x
                
        else:
            print("\nNão houve alteração")
        time.sleep(1)
        
        print("Itens salvos")
        LED.status("FimDeCiclo")
        porta.travar()
        
    except KeyboardInterrupt: # 'Ctrl + C'
        GPIO.cleanup()
        
    finally:
        print("\n========= NEXT =========\n")
        
GPIO.cleanup()