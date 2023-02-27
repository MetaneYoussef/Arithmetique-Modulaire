import tkinter as tk 
wind=tk.Tk()
canvas1 = tk.Canvas(wind, width=800, height=600, relief='raised', bg='#8db9ca')
canvas1.pack()

label1 = tk.Label(wind, text='Calcul du PGCD et coefficents du Bezout')
label1.config(font=('times', 18, 'bold'))
canvas1.create_window(400, 25, window=label1)

label_a = tk.Label(wind, text='a :')
label_a.config(font=('Lucida Console', 18))
canvas1.create_window(400, 100, window=label_a)
input_a = tk.Entry(wind, bg='white', font=('Lucida Console',18, 'bold')) 
canvas1.create_window(400, 135, window=input_a)

label_b = tk.Label(wind, text='Modulo :')
label_b.config(font=('Lucida Console', 18))
canvas1.create_window(400, 190, window=label_b)
input_b = tk.Entry(wind, bg='white', font=('Lucida Console',18, 'bold')) 
canvas1.create_window(400, 225, window=input_b)

def euclide():
	a = int(input_a.get())
	b = int(input_b.get())
	#Initialisation des r0 , r1
	r0=a
	r1=b
	#Initialisation des coefficients pgcd = x*r0 + y*r1
	x=0
	old_x=1
	y=1 
	old_y=0
	#Debut de calcul
	reste=r0 % r1
	while(reste !=0 ):
		old_x,x=x,old_x - (r0 // r1) * x
		old_y,y=y,old_y - (r0 // r1) * y 
		r0=r1
		r1=reste
		reste=r0 % r1
	
	label3 = tk.Label(wind,text='PGCD = '+str(r1)+'\nCoeff du bezout: x='+str(x)+' y='+str(y),font=('Lucida Console', 25, 'bold'))
	canvas1.create_window(400, 500, window=label3)


button1 = tk.Button(text='Calculer', command=euclide, bg='#fbb034', fg='white', font=('Lucida Console', 18, 'bold'))
canvas1.create_window(400, 350, window=button1)

wind.mainloop()