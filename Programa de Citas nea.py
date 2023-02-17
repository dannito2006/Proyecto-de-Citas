#!/usr/bin/env python
# coding: utf-8

# In[ ]:


try:
    resultado = a / b
except:
    print("Valores incorrectos")
    


# In[20]:


import pyttsx3

engine = pyttsx3.init()

def heteroman():
    print(" ¿Listo para encontrar la mujer de tus sueños? :D")
    engine.say("¿Listo para encontrar la mujer de tus sueños? ")
    engine.runAndWait()
    engine.say("¿Acceso a la ubicacion?")
    engine.runAndWait()
    input(" ¿Acceso a la ubicación? ")
    engine.say("Introduce la distancia en kilometros en donde quieras encontrar a tu pareja: ")
    engine.runAndWait()
    input(" Introduce la distancia en kilometros en donde quieras encontrar a tu pareja: ")
    engine.say("Introduce tu Correo Electronico: ")
    engine.runAndWait()
    input(" Introduce tu Correo Electronico: ")
    engine.say("Introduce tu clave: ")
    engine.runAndWait()
    clavehm=int(input("Introduce tu clave: "))
    while clavehm!=456:
        print("Clave Incorrecta")
        engine.say("Clave Incorrecta ")
        engine.runAndWait()
        engine.say("Introduce tu clave: ")
        engine.runAndWait()
        clavehm=int(input("Introduce tu clave: "))
    print(" ¡Bienvenido ve por tu match!")
    engine.say("¡Bienvenido ve por tu match! ")
    engine.runAndWait()
        
def hombregay():
    print(" Somos Una App LGBTQ+ Friendly :D")
    engine.say(" Somos Una App LGBTQ+ Friendly :D")
    engine.runAndWait()
    engine.say("¿Acceso a la ubicacion? ")
    engine.runAndWait()
    input(" Acceso a la ubicacion? ")
    engine.say("Introduce la distancia en kilometros en donde quieras encontrar a tu pareja: ")
    engine.runAndWait()
    input(" Introduce la distancia en kilometros en donde quieras encontrar a tu pareja: ")
    engine.say("Introduce tu Correo Electronico: ")
    engine.runAndWait()
    input(" Introduce tu Correo Electronico: ")
    engine.say("Introduce tu clave: ")
    engine.runAndWait()
    clavehh=int(input("Introduce tu clave: "))

    while clavehh!=123:
        print("Clave Incorrecta")
        engine.say("Clave Incorrecta")
        engine.runAndWait()
        engine.say("Introduce tu Clave")
        engine.runAndWait()
        clavehh=int(input("Introduce tu Clave"))
        
    print(" ¡Bienvenido ve por tu match!")
    engine.say("¡Bienvenido ve por tu match!")
    engine.runAndWait()
    
def heteromujer():
    print(" Lista para encontrar el hombre de tus sueños? ")
    engine.say("¿Lista para encontrar el hombre de tus sueño? ")
    engine.runAndWait()
    engine.say("¿Acceso a la ubicacion? ")
    engine.runAndWait()
    input(" Acceso a la ubicacion? ")
    engine.say("Introduce la distancia en kilometros en donde quieras encontrar a tu pareja: ")
    engine.runAndWait()
    input(" Introduce la distancia en kilometros en donde quieras encontrar a tu pareja: ")
    engine.say("Introduce tu Correo Electronico: ")
    engine.runAndWait()
    input(" Introduce tu Correo Electronico: ")
    engine.say("Introduce tu clave: ")
    engine.runAndWait()
    clavemh=int(input("Introduce tu clave: "))

    while clavemh!=789:
        print("Clave Incorrecta")
        engine.say("Clave Incorrecta: ")
        engine.runAndWait()
        engine.say("Introduce tu clave: ")
        engine.runAndWait()
        clavemh=int(input("Introduce tu clave: "))
        
    print(" ¡Bienvenida ve por tu match!")
    engine.say("¡Bienvenido ve por tu match! ")
    engine.runAndWait()
        
def mujergay():
    print(" Somos Una App LGBTQ+ Friendly :D")
    engine.say(" Somos Una App LGBTQ+ Friendly :D")
    engine.runAndWait()
    engine.say("¿Acceso a la ubicacion? ")
    engine.runAndWait()
    input(" ¿Acceso a la ubicación? ")
    engine.say("Introduce la distancia en kilometros en donde quieras encontrar a tu pareja: ")
    engine.runAndWait()
    input(" Introduce la distancia en kilometros en donde quieras encontrar a tu pareja: ")
    engine.say("Introduce tu Correo Electronico: ")
    engine.runAndWait()
    input(" Introduce tu Correo Electronico: ")
    engine.say("Introduce tu Clave: ")
    engine.runAndWait()
    clavemm=int(input("Introduce tu clave: "))
  
    while clavemm!=0:
        print("Clave Incorrecta")
        engine.say("Clave Incorrecta")
        engine.runAndWait()
        engine.say("Introduce tu Clave: ")
        engine.runAndWait()
        clavemm=int(input("Introduce tu clave: "))
        
    print(" ¡Bienvenida ve por tu match!")
    engine.say(" ¡Bienvenida ve por tu match!")
    engine.runAndWait()
        
print("Bienvenido a la aplicación")
engine.say("Bienvenido a la aplicación")
engine.runAndWait()
engine.say("¿Eres hombre o mujer?")
engine.runAndWait()
opcion1 = input("¿Eres hombre o mujer? ").lower()
opcion2 = "hombre"
opcion3 = "mujer"


if opcion1 == "hombre":
    engine.say("Qué género estás buscando para tu cita? ")
    engine.runAndWait()
    opcion2 = input("¿Qué género estás buscando para tu cita? ").lower()
    if opcion2 == "hombre":
        print("Elegiste hombre, tienes un 15% de descuento en la aplicación")
        engine.say("Elegiste hombre, tienes un 15% de descuento en la aplicación")
        engine.runAndWait()
        hombregay()
    else: 
        print("Elegiste mujer, tienes un 30% de descuento en la aplicación")
        engine.say("Elegiste mujer, tienes un 30% de descuento en la aplicación")
        engine.runAndWait()
        heteroman()
else:
    engine.say("Qué género estás buscando para tu cita? ")
    engine.runAndWait()
    opcion3 = input("¿Qué género estás buscando para tu cita? ").lower()
    if opcion3 == opcion2:
        print("Elegiste hombre, tienes un 25% de descuento en la aplicación")
        engine.say("Elegiste hombre, tienes un 25% de descuento en la aplicación")
        engine.runAndWait()
        heteromujer()
    else:
        print("Elegiste mujer, tienes un 18% de descuento en la aplicación")
        engine.say("Elegiste mujer, tienes un 18% de descuento en la aplicación")
        engine.runAndWait()
        mujergay()

        
engine.runAndWait()


# In[12]:





# In[ ]:





# In[ ]:




