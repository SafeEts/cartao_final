#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h>
#endif

#define PIN 6
#define NUMPIXELS 144
#define BRIGHTNESS 50

char msg = " ";

Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);


void setup() {

#if defined(__AVR_ATtiny85__) && (F_CPU == 16000000)
  clock_prescale_set(clock_div_1);
#endif

  pixels.begin();
  pixels.setBrightness(BRIGHTNESS);
//  pixels.show();
  Serial.begin(9600);

}

void loop() {

  while (Serial.available() > 0) {
    msg = Serial.read();

    switch (msg) {


//------------------------- Inicio (Azul rapidinho) -----------------------------
      case 't':
        theaterChase(pixels.Color(10,   255,   255), 1, 2, 500);
        break;
//------------------------- Padrão (Branco contínuo) -----------------------------
      case 'p':
        colorWipe(pixels.Color(  127, 127,   127) , 4);
        break;

//--------------- Usuário Cadastrado (Verde piscante/contínuo) -------------------
      case 'c':
        theaterChase(pixels.Color(0,   255,   0), 6, 2, 100);
        delay(500);
        colorWipe(pixels.Color(0,   255,   0) , 1);
        break;

//---------------- Usuário Não Cadastrado (Vermelho piscante) --------------------
      case 'e':
        theaterChase(pixels.Color(255,   0,   0), 5, 2, 100);
        break;
        
//----------------------- Porta Aberta (Amarelo piscante) ------------------------
      case 'a':
        theaterChase(pixels.Color(255,   250,   0), 1, 3, 300);
        break;

//----------------------- Fim de Ciclo (Branco piscante) -------------------------
      case 'f':
        theaterChase(pixels.Color(127, 127,   127), 4 , 3 , 90);
        colorWipe(pixels.Color(127, 127,   127) , 4);
        break;
        
//--------------- Coleta Incorreta (Vermelho piscante e apagado) ------------------
      case 'i':
        theaterChase(pixels.Color(255, 0,   0), 1 , 1 , 200);
        delay(600);
        theaterChase(pixels.Color(0, 0,   0), 1 , 1 , 200);
        delay(400);
        break;
    }
    delay(1);

  }

}

void colorWipe(uint32_t color, int wait) {
  for (int i = 0; i < pixels.numPixels(); i++) {
    pixels.setPixelColor(i, color);
    pixels.show();
    delay(wait);
  }
}

void theaterChase(uint32_t color, int rep, int vv, int wait) {
  for (int a = 0; a < rep; a++) {
    for (int b = 0; b < vv; b++) {
      pixels.clear();
      for (int c = b; c < pixels.numPixels(); c += 3) {
        pixels.setPixelColor(c, color);
      }
      pixels.show();
      delay(wait);
    }
  }
}
