"""porte.py : commande de la porte du sas (servo de verrouillage + moteur pas à pas).

Matériel : servomoteur sur GPIO 18, moteur 28BYJ-48 sur GPIO 17/20/24/23.
"""
import time
import lgpio

IN1, IN2, IN3, IN4 = 17, 20, 24, 23   # bobines du moteur pas à pas
SERVO_PIN = 18

chip = lgpio.gpiochip_open(0)
for pin in (IN1, IN2, IN3, IN4, SERVO_PIN):
    lgpio.gpio_claim_output(chip, pin)

# Séquence en pas complet (2 bobines alimentées à chaque phase)
SEQUENCE = [
    [1, 0, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
]
PHASES_90_DEG = 128   # 128 x 4 = 512 phases = 90° (2048 phases par tour en pas complet)

def step_motor(cycles, direction=1, delay=0.005):
    """Fait tourner le moteur. direction=1 : ouverture, -1 : fermeture."""
    seq = SEQUENCE if direction == 1 else SEQUENCE[::-1]
    for _ in range(cycles):
        for a, b, c, d in seq:
            lgpio.gpio_write(chip, IN1, a)
            lgpio.gpio_write(chip, IN2, b)
            lgpio.gpio_write(chip, IN3, c)
            lgpio.gpio_write(chip, IN4, d)
            time.sleep(delay)
    for pin in (IN1, IN2, IN3, IN4):      # coupe les bobines (évite la surchauffe)
        lgpio.gpio_write(chip, pin, 0)

def set_servo_angle(angle, hold=0.6):
    """Angle 0-180° -> impulsion de 500 à 2500 µs, à 50 Hz."""
    pulse_us = int(500 + (angle / 180.0) * 2000)
    lgpio.tx_servo(chip, SERVO_PIN, pulse_us, 50)
    time.sleep(hold)
    lgpio.tx_servo(chip, SERVO_PIN, 0)    # arrête le signal

def unlock_servo():
    set_servo_angle(90)
    print("Porte déverrouillée")

def lock_servo():
    set_servo_angle(0)
    print("Porte verrouillée")

def ouverture_porte():
    step_motor(PHASES_90_DEG, direction=1)
    print("Ouverture de la porte du sas")

def fermeture_porte():
    step_motor(PHASES_90_DEG, direction=-1)
    print("Fermeture de la porte du sas")

def cleanup():
    lgpio.gpiochip_close(chip)

if __name__ == "__main__":
    try:
        unlock_servo()
        ouverture_porte()
        time.sleep(5)
        fermeture_porte()
        lock_servo()
    except KeyboardInterrupt:
        print("Arrêt manuel")
    finally:
        cleanup()