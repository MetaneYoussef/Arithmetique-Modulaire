import tkinter as tk 
wind=tk.Tk()
canvas1 = tk.Canvas(wind, width=500, height=600, relief='raised', bg='#8db9ca')
canvas1.pack()

label1 = tk.Label(wind, text='Montgomery Modular Reduction')
label1.config(font=('times', 18, 'bold'))
canvas1.create_window(250, 25, window=label1)

label_a = tk.Label(wind, text='a :')
label_a.config(font=('helvetica', 18))
canvas1.create_window(250, 100, window=label_a)
input_a = tk.Entry(wind, bg='white', font=('helvetica',18, 'bold')) 
canvas1.create_window(250, 135, window=input_a)

label_b = tk.Label(wind, text='b :')
label_b.config(font=('helvetica', 18))
canvas1.create_window(250, 190, window=label_b)
input_b = tk.Entry(wind, bg='white', font=('helvetica',18, 'bold')) 
canvas1.create_window(250, 225, window=input_b)

label_m = tk.Label(wind, text='m :')
label_m.config(font=('helvetica', 18))
canvas1.create_window(250, 280, window=label_m)
input_m = tk.Entry(wind, bg='white', font=('helvetica',18, 'bold')) 
canvas1.create_window(250, 315, window=input_m)

#------------------------------------------------------------
# 1 - calculer de l'inverse modulaire
#------------------------------------------------------------

#---------------------------------------------
# 1- 1- Calcule de pgcd par la methode d'euclide 
#---------------------------------------------
def pgcd(a,b):
    while (b > 0):
        r = a % b
        a = b
        b = r  
    return a


#----------------------------------------------------------------------------
# 1- 2- calcule des conficient de bizout en utilisant l'algorithme d'euclide etendu
#----------------------------------------------------------------------------
def bezout(a,b):
    u0,v0,u1,v1=1,0,0,1
    while b!=0:
        q=a//b
        a,u0,v0,b,u1,v1 = b,u1 , v1, a-q*b, u0-q*u1, v0-q*v1
        if a<0:
            return -a,-u0,-v0
    return a,u0,v0

#------------------------------------------------------------
# 1- 3- calcule de l'inverse modulaire
#------------------------------------------------------------
def reciprocal_mod(x, mod):
    gcd,u,v = bezout(mod,x)
    if gcd == 1 :
        if v < 0 :
            return v+mod
        else:
            return v
    else :
        raise ValueError("pas d'inverse")



#------------------------------------------------------------
# 2 - Initialisation
#------------------------------------------------------------
def initialisation ():
    global mod,reducerbits,reducer,mask,reciprocal,factor
    # tester si mod est superieur a 3 et impair
    if mod < 3 or mod % 2 == 0:
        print("Modulo doit etre superieur a 3 et impair")
        exit()
    else: 
        # Calcule de R
        reducerbits = (mod.bit_length()//8 + 1) * 8 # Nombre de bits de R = 8 * (nombre de bytes de mod)
        reducer =  1 << reducerbits  # R = 2^reducerbits
        mask = reducer - 1 # Masque pour extraire les reducerbits bits de poids faible de x*y (x*y & mask)
        if ((reducer > mod) and (pgcd(reducer, mod) == 1)) :  # si R > mod et R et mod sont premiers entre eux
            reciprocal = reciprocal_mod(reducer % mod, mod) # inverse de R mod mod
            factor = (reducer * reciprocal - 1) // mod # (R*R^-1 - 1)/mod
            convertedone = reducer % mod
        else:
            print("R doit etre superieur a mod et R et mod doivent etre premiers entre eux")
            exit()

# ------------------------------------------------------------
# 3- multiplication de montgomery
#------------------------------------------------------------
# ------------------------------------------------------------
# 3- 1-  ecrire x sous forme montgomery
#------------------------------------------------------------
def convert_in(x):
	return (x << reducerbits) % mod # x*R mod mod = montgomery form

# ------------------------------------------------------------
# 3- 2-  convertir x a la forme normale
#------------------------------------------------------------
def convert_out(x):
	return (x * reciprocal) % mod # x*R^-1 mod mod = normal form

# ------------------------------------------------------------
# 3- calculer x*y mod mod
#------------------------------------------------------------
# Inputs and output are in Montgomery form and in the range [0, modulus[
def multiply(x, y):
	modulo = mod
	assert 0 <= x < modulo and 0 <= y < modulo # x et y sont dans la forme montgomery
	product = x * y 
	temp = ((product & mask) * factor) & mask # (x*y & mask) * factor & mask
	reduced = (product + temp * modulo) >> reducerbits # (x*y + (x*y & mask) * factor & mask * mod) / R
	result = reduced if (reduced < modulo) else (reduced - modulo) 
	assert 0 <= result < modulo
	return result
    

def montgomery():
    #------------------------------------------------------------
    #X*Y mod mod
    #------------------------------------------------------------
    global mod,X,Y

    X=int(input_a.get())
    Y=int(input_b.get())
    mod=int(input_m.get())
    initialisation ()
    xnorm=convert_in(X)
    ynorm=convert_in(Y)
    res=convert_out(multiply(ynorm,xnorm))
    print (f"x={X}, y={Y}, p={mod}")
    print (f"\n({X}x{Y}) (mod {mod})={res}")
    label3 = tk.Label(wind,text=str(res)+' = '+str(X)+' * '+str(Y)+' mod '+str(mod) ,font=('helvetica', 14, 'bold'))
    canvas1.create_window(250, 500, window=label3)


button1 = tk.Button(text='Calculate', command=montgomery, bg='brown', fg='white', font=('helvetica', 18, 'bold'))
canvas1.create_window(250, 400, window=button1)

wind.mainloop()