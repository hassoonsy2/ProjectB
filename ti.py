import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(0)


clock_pin = 19
data_pin = 26
data_pin1 = 13
latch_clock_pin = 6
shift_clock_pin = 5
servo = 25

GPIO.setup(shift_clock_pin, GPIO.OUT)
GPIO.setup(latch_clock_pin, GPIO.OUT)
GPIO.setup(data_pin1, GPIO.OUT)

GPIO.setup(servo, GPIO.OUT)
GPIO.setup(clock_pin, GPIO.OUT)
GPIO.setup(data_pin, GPIO.OUT)


def servo_rechts():
    p = GPIO.PWM(25, 50)
    p.start(2)
    p.ChangeDutyCycle(2)
    time.sleep(0.48)
    for i in range(0, 100, 1):
        servo_rechts()
    for i in range(100, 0, -1):
        servo_rechts()


def servo_links():
    p = GPIO.PWM(25, 50)
    p.start(12)
    p.ChangeDutyCycle(12)
    time.sleep(0.48)
    for i in range(0, 100, 1):
        servo_links()
    for i in range(100, 0, -1):
        servo_links()


def servo_midden():
    p = GPIO.PWM(25, 50)
    p.start(7)
    p.ChangeDutyCycle(7)
    time.sleep(0.48)
    for i in range(0, 100, 1):
        servo_midden()
    for i in range(100, 0, -1):
        servo_midden()



def hc595(shift_clock_pin, latch_clock_pin, data_pin1, value, delay):
    for i in range(8):

        byte = [int(z) for z in bin(value)[2:].zfill(8)]
        for bitje in byte:
            GPIO.output(data_pin1, bitje)
            GPIO.output(shift_clock_pin, True)
            time.sleep(delay)
            GPIO.output(shift_clock_pin, False)
            time.sleep(delay)

    GPIO.output(latch_clock_pin, True)
    GPIO.output(latch_clock_pin, False)




sr04_trig = 20
sr04_echo = 21
GPIO.setup(sr04_trig, GPIO.OUT)
GPIO.setup(sr04_echo, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def sr04(trig_pin, echo_pin):
    GPIO.output(sr04_trig, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(sr04_trig, GPIO.LOW)
    while GPIO.input(sr04_echo) == 0:
        start = time.time()
    while GPIO.input(sr04_echo) == 1:
        end = time.time()
    distance_m = end - start
    distance = (distance_m * 34300) / 2
    return distance

def afstand():
    print(sr04(sr04_trig,sr04_echo))
    delay = 0.0009

    time.sleep(1)

    while True:

        if sr04(sr04_trig, sr04_echo) <= 5:

            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 1, delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1,128,delay)

        elif sr04(sr04_trig, sr04_echo) <= 10:
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 1, delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1,128,delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 64, delay)
        elif sr04(sr04_trig, sr04_echo) <= 15:
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 1, delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1,128,delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 64, delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 32, delay)

        elif sr04(sr04_trig, sr04_echo) <= 20:
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 1, delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1,128,delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 64, delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 32, delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 16, delay)

        elif sr04(sr04_trig, sr04_echo) <= 25:
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 1, delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1,128,delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 64, delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 32, delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 16, delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 8, delay)

        elif sr04(sr04_trig, sr04_echo) <= 30:
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 1, delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1,128,delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 64, delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 32, delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 16, delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 8, delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 4, delay)

        elif sr04(sr04_trig, sr04_echo) <= 35:
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 1, delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1,128,delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 64, delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 32, delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 16, delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 8, delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 4, delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 2, delay)

        elif sr04(sr04_trig, sr04_echo) <= 40:
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 1, delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1,128,delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 64, delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 32, delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 16, delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 8, delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 4, delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 2, delay)
            hc595(shift_clock_pin, latch_clock_pin, data_pin1, 1, delay)

def apa102_send_bytes(clock_pin, data_pin, bytes):
    
        for byte in bytes:
            for j in byte:
                Binary_number = [int(i) for i in bin(j)[2:].zfill(8)]


                for bit in Binary_number:
                    if bit == 1:
                        GPIO.output(data_pin, GPIO.HIGH)
                    elif bit == 0:
                        GPIO.output(data_pin, GPIO.LOW)

                    GPIO.output(clock_pin, GPIO.HIGH)

                    GPIO.output(clock_pin, GPIO.LOW)
        



def apa102(clock_pin, data_pin, colors):
    
    Signal = [[0b000000000, 0b000000000, 0b000000000, 0b000000000]]
    
    wit = [0b11111111]
  
    for color in colors:
        for bit in color:
            wit.append(bit)
        Signal.append(wit)
        
        wit = [0b11111111]

    apa102_send_bytes(clock_pin, data_pin, Signal)


wit = [255, 255, 255]
blue = [255, 0, 0]
red = [0, 0, 255]
pink = [255,0,255]
cyan = [147,112,219]
blue2 = [255,140,0]

def colors(x, n, off):
    result = []
    for i in range(0, n):

        result.append(off)


    return result

def Vlag_cyan(clock_pin, data_pin, delay, n=9):
    
    
    for i in range(8):
        for x in range( n ):
            apa102( clock_pin, data_pin, colors( x, n,cyan ) )
  

def Vlag_blue(clock_pin, data_pin, delay, n=9):
    
    
    for i in range(8):
        for x in range( n ):
            apa102( clock_pin, data_pin, colors( x, n,blue ) )


def Vlag_pink(clock_pin, data_pin, delay, n=9):
    
    
    for i in range(8):
        for x in range( n ):
            apa102( clock_pin, data_pin, colors( x, n,pink ) )          

  
def Vlag_red(clock_pin, data_pin, delay, n=9):
    
    
    for i in range(8):
        for x in range( n ):
            apa102( clock_pin, data_pin, colors( x, n,red ) )


def Vlag_wit(clock_pin, data_pin, delay, n=9):
    
    
    for i in range(8):
        for x in range( n ):
            apa102( clock_pin, data_pin, colors( x, n,wit ) )




def Vlag_blue2(clock_pin, data_pin, delay, n=9):
    
    
    for i in range(8):
        for x in range( n ):
            apa102( clock_pin, data_pin, colors( x, n,blue2 ) )





