#---------------------------------------------------------------
# calculer l'exposantiation modulaire en utilisant l'algorithme
# de SQUARE AND MULTIPLY
#---------------------------------------------------------------

import tkinter as tk 
wind=tk.Tk()
canvas1 = tk.Canvas(wind, width=800, height=600, relief='raised', bg='#8db9ca')
canvas1.pack()

label1 = tk.Label(wind, text='Exponantiation Modulaire')
label1.config(font=('times', 18, 'bold'))
canvas1.create_window(400, 25, window=label1)

label_a = tk.Label(wind, text='Base :')
label_a.config(font=('Lucida Console', 18))
canvas1.create_window(400, 100, window=label_a)
input_a = tk.Entry(wind, bg='white', font=('Lucida Console',18, 'bold')) 
canvas1.create_window(400, 135, window=input_a)

label_b = tk.Label(wind, text='Exposant :')
label_b.config(font=('Lucida Console', 18))
canvas1.create_window(400, 190, window=label_b)
input_b = tk.Entry(wind, bg='white', font=('Lucida Console',18, 'bold')) 
canvas1.create_window(400, 225, window=input_b)

label_m = tk.Label(wind, text='Modulo :')
label_m.config(font=('Lucida Console', 18))
canvas1.create_window(400, 280, window=label_m)
input_m = tk.Entry(wind, bg='white', font=('Lucida Console',18, 'bold')) 
canvas1.create_window(400, 315, window=input_m)

def expo_mod():
    Base = int(input_a.get())
    Exposant=int(input_b.get())
    Modulo=int(input_m.get())
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
        label3 = tk.Label(wind, text=str(Bs)+' ^ '+str(Exposant)+' mod '+str(Modulo)+' = '+str(1),font=('Lucida Console', 25, 'bold'))
    elif Exposant == 1:
        label3 = tk.Label(wind,text=str(Bs)+' ^ '+str(Exposant)+' mod '+str(Modulo)+' = '+str(Base),font=('Lucida Console', 25, 'bold'))
    else : 
        for i in range(1, Ex_BitLen):
            if Ex_Bin[i] == '1':
                # SQUARE AND MULTIPLY
                result = pow(Base,2,Modulo) 
                result = (result * Bs) % Modulo
            else:
                # SQUARE
                result = pow(Base,2,Modulo) 
            Base = result
        label3 = tk.Label(wind,text=str(Bs)+' ^ '+str(Exposant)+' mod '+str(Modulo)+' = '+str(result),font=('Lucida Console', 25, 'bold'))
    canvas1.create_window(400, 450, window=label3)

if __name__ == '__main__':
    button1 = tk.Button(text='Calculer', command=expo_mod, bg='#fbb034', fg='white', font=('Lucida Console', 18, 'bold'))
    canvas1.create_window(400, 400, window=button1)

wind.mainloop()

    # #---------------------------------------------------------------
    # # Calculer Base^Exposant mod Modulo
    # #---------------------------------------------------------------
    # print(expo_mod(2, 3, 5))
    # print(expo_mod(3, 2, 5))
    # print(expo_mod(145423212312, 2121321212312, 222254554845))
    # print(expo_mod(56852654, 2175465, 23212156))