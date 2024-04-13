#include <avr/io.h>
#include <avr/eeprom.h>
#include <avr/interrupt.h>

#define F_CPU 16000000UL
#define BR 2400
#define UV ((F_CPU / (16UL * BR)) - 1)
#define ESA 0
#define ES 1024

void UI() {
    UBRR0H = (uint8_t)(UV >> 8);
    UBRR0L = (uint8_t)UV;
    UCSR0B = (1 << TXEN0) | (1 << RXEN0);
    UCSR0C = (1 << UCSZ01) | (1 << UCSZ00);
}

void UT(uint8_t d) {
    while (!(UCSR0A & (1 << UDRE0)));
    UDR0 = d;
}

uint8_t UR() {
    while (!(UCSR0A & (1 << RXC0)));
    return UDR0;
}

void EC() {
    for (uint16_t a = ESA; a < ESA + ES; a++) {
        eeprom_write_byte((uint8_t*)a, 0);
    }
}

int main(void) {
    UI();
    sei();
    EC();
    for (uint16_t a = ESA;; a++) {
        uint8_t r = UR();
        if (r == '$') {
            break;
        }
        eeprom_write_byte((uint8_t*)a, r);
    }
    for (uint16_t a = ESA;; a++) {
        uint8_t d = eeprom_read_byte((uint8_t*)a);
        if (d == '$') {
            break;
        }
        UT(d);
    }
    return 0;
}

