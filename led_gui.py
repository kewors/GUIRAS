from tkinter import*
import RPi.GPIO as GPIO
from gpiozero import LED
import tkinter.font

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

##hadware##
led = LED(4)

##funciones##
def prender_led():
    if led.is_lit:
        led.off()
        print ('led off')
        ledButton["text"] = "LED off"
    else:
        led.on()
        print('led on')
        ledButton["text"] = "LED on"
    
def close ():
    GPIO.cleanup()
    v1.destroy()
    
##GUI VENTANA##
v1=Tk()
v1.title("LED")
v1.geometry("500x210")
v1.config(bg="black")
myFont = tkinter.font.Font(family = 'helvatica',size = 12, weight = 'bold')

##widgets##
label = Label(v1, text="on-of/led",font=myFont, fg="blue")
label.grid(row=0, column=2)

ledButton=Button(v1, text="Led", fg="red", font=myFont, command=prender_led, bg ='blue', height=1, width = 24)
ledButton.grid(row=2, column=2)

exitButton=Button(v1, text = 'exit',font = myFont, command = close, bg = 'red', height = 1, width = 6)
exitButton.grid(row=0, column=3)

v1.mainloop()

print('Limpiando...')
GPIO.cleanup()