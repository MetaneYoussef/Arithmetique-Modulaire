#---------------------------------------------------------------
# Test de primalite de Miller-Rabin
#---------------------------------------------------------------
import tkinter as tk 
import random
wind=tk.Tk()
canvas1 = tk.Canvas(wind, width=800, height=600, relief='raised', bg='#8db9ca')
canvas1.pack()

label1 = tk.Label(wind, text='Test de primalité')
label1.config(font=('times', 18, 'bold'))
canvas1.create_window(400, 25, window=label1)

label_a = tk.Label(wind, text='N :')
label_a.config(font=('Lucida Console', 18))
canvas1.create_window(400, 100, window=label_a)
input_a = tk.Entry(wind, bg='white', font=('Lucida Console',18, 'bold')) 
canvas1.create_window(400, 135, window=input_a)

def expo_mod(Base, Exposant, Modulo):
    #---------------------------------------------------------------
    # Etape 1 : calculer la representation binaire de l'exposant
    #---------------------------------------------------------------
    Ex_Bin = format(Exposant, 'b')
    Ex_BitLen = len(Ex_Bin)
    Bs = Base

    #-----------------------------------------------------------------
    # Etape 2 : calculer le resultat en utilisant SQUARE AND MULTIPLY
    #-----------------------------------------------------------------
    if Exposant == 0:
        return 1
    elif Exposant == 1:
        return Base
    else : 
        for i in range(1, Ex_BitLen):
            if Ex_Bin[i] == '1':
                # SQUARE AND MULTIPLY
                result = (Base**2) % Modulo
                result = (result * Bs) % Modulo
            else:
                # SQUARE
                result = (Base**2) % Modulo
            Base = result
        return result


def MillerRabin():
    n = int(input_a.get())
    #-------------------------------------------------
    # elimination des cas usuels 
    #-------------------------------------------------
    if n == 2 or n == 3: # 2 et 3 sont premiers
        label3 = tk.Label(wind,text=str(n)+' is a prime number',font=('Lucida Console', 25, 'bold'))
        return canvas1.create_window(400, 450, window=label3)
    if n <= 1 or n % 2 == 0: # 1 et les nombres pairs ne sont pas premiers
        label3 = tk.Label(wind,text=str(n)+' is not a prime number',font=('Lucida Console', 25, 'bold')) 
        return canvas1.create_window(400, 450, window=label3)
    #-------------------------------------------------------
    #Etape 1 : calcule de k et m tels que n-1 = 2^k * m
    #-------------------------------------------------------
    k = 0
    m = n - 1
    while m % 2 == 0:
        m = m // 2
        k += 1    

    #-------------------------------------------------------
    #Etape 2 : Trouver un a tel que 1 < a < n
    #-------------------------------------------------------
    a = random.randrange(2, n - 1)

    #-------------------------------------------------------
    #Etape 3 : calculer b0 = a^m mod n
    #-------------------------------------------------------
    b = expo_mod(a, m, n)

    #-------------------------------------------------------------------
    #Etape 4 : 
    # si b = 1  alors n est composé
    # si b = n-1 alors n est probablement premier
    # sinon, on calcule b1, b2, ..., bk-1
    #-----------------------------------------------------------------
    if b != 1 and b != n - 1:
        i = 1
        while i < k and b != n - 1:
            b = expo_mod(b, 2, n)
            if b == 1:
                label3 = tk.Label(wind,text=str(n)+' is a prime number',font=('Lucida Console', 25, 'bold'))
                return canvas1.create_window(400, 450, window=label3)
            i += 1
        if b != n - 1:
            label3 = tk.Label(wind,text=str(n)+' is not a prime number',font=('Lucida Console', 25, 'bold')) 
            return canvas1.create_window(400, 450, window=label3)
    label3 = tk.Label(wind,text=str(n)+' is a prime number',font=('Lucida Console', 25, 'bold')) 
    return canvas1.create_window(400, 450, window=label3)


if __name__ == '__main__':
    #---------------------------------------------------------------
    # Test de primalite de Miller-Rabin
    #---------------------------------------------------------------
    button1 = tk.Button(text='Tester', command=MillerRabin, bg='#fbb034', fg='white', font=('Lucida Console', 18, 'bold'))
    canvas1.create_window(400, 200, window=button1)

wind.mainloop()
