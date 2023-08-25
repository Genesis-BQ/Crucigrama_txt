#-----Las biblotecas de uso------------
import tkinter as tk
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image #importar imagen 
#_______________________________________________________________________________________________________
class Ventanas():
    def __init__(self, menuPrincipal):
        self.menuPrincipal = menuPrincipal
        self.ventanaAdmin = None
    def ventanaPrincipal(self): #Ventana de incio y menu principal.
        self.menuPrincipal.title("Principal")
        self.menuPrincipal.geometry('900x600+400+150')
        # Cargar la imagen de fondo
        image_path = "mente.png"
        imagen_fondo = Image.open(image_path)
        imagen_fondo = imagen_fondo.resize((900, 600), Image.LANCZOS)  # Ajusta el tamaño de la imagen al tamaño de la ventana
        imagen_fondo = ImageTk.PhotoImage(imagen_fondo)
        # Mostrar la imagen de fondo en un Label
        fondo_label = tk.Label(self.menuPrincipal, image=imagen_fondo)
        fondo_label.place(x=0, y=0, relwidth=1, relheight=1)  # Para que la imagen se ajuste al tamaño de la ventana
        # Asegúrate de mantener una referencia a la imagen para evitar que se elimine automáticamente.
        fondo_label.image = imagen_fondo
        e1 = tk.Label(self.menuPrincipal, text="Bienvenidos al juedo cucigrama", font=("Castellar", 14), fg="white", bg="#c20000")
        e1.pack()
        e2 = tk.Label(self.menuPrincipal, text="Seleccion", font=("Castellar", 14), fg="white", bg="#c20000")
        e2.pack(padx=5, pady=(10, 450))
        botonAdmin = tk.Button(self.menuPrincipal, text="Iniciar", font=("Castellar", 14), fg="white", bg="#c20000",command=self.abrirVentanaSecundaria)
        botonAdmin.place(x=750, y=550)
        self.menuPrincipal.mainloop()
#________________________________________________________________________________________________________________________
    def abrirVentanaSecundaria(self):
        self.ventana_secundaria = tk.Toplevel()
        self.ventana_secundaria.title("Selección")
        self.ventana_secundaria.geometry('900x600+400+150')
        self.menuPrincipal.withdraw() 
        # Cargar la imagen de fondo
        image_path = "mente.png"
        imagen_fondo = Image.open(image_path)
        imagen_fondo = imagen_fondo.resize((900, 600), Image.LANCZOS)  # Ajusta el tamaño de la imagen al tamaño de la ventana
        imagen_fondo = ImageTk.PhotoImage(imagen_fondo)
        # Mostrar la imagen de fondo en un Label
        fondo_label = tk.Label(self.ventana_secundaria, image=imagen_fondo)
        fondo_label.place(x=0, y=0, relwidth=1, relheight=1)  # Para que la imagen se ajuste al tamaño de la ventana
        # Asegúrate de mantener una referencia a la imagen para evitar que se elimine automáticamente.
        fondo_label.image = imagen_fondo
        botonUsuario = tk.Button(self.ventana_secundaria, text="Usuario", font=("Castellar", 14), fg="white", bg="#c20000",command=self.ventanaUsuario)
        botonUsuario.place(x=570,y=250)
        botonAdm = tk.Button(self.ventana_secundaria, text="Administrador", font=("Castellar", 14), fg="white", bg="#c20000",command=self.ventanaAdministrador)
        botonAdm.place(x=230,y=250)
        boton_regresar = tk.Button(self.ventana_secundaria, text="➢",font=("Castellar", 14), fg="white", bg="#33CCFF",command=self.regresarPrincipal)
        boton_regresar.place(x=90, y= 550)
#__________________________________________________________________________________________________________
    def ventanaAdministrador(self):
        self.ventana_secundaria.withdraw()
        self.ventanaAdmin = tk.Toplevel()
        self.ventanaAdmin.title("Administrador")
        self.ventanaAdmin.geometry('900x600+400+150')
        # Cargar la imagen de fondo
        image_path = "preguntados.png"
        imagen_fondo = Image.open(image_path)
        imagen_fondo = imagen_fondo.resize((900, 600), Image.LANCZOS)
        imagen_fondo = ImageTk.PhotoImage(imagen_fondo)
        fondo_label = tk.Label(self.ventanaAdmin, image=imagen_fondo)
        fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
        fondo_label.image = imagen_fondo
        lblFilas = tk.Label(self.ventanaAdmin, text="Filas:", font=("Castellar", 14), fg="#8d4925", bg="#33CCFF", height=1, width=12)
        lblFilas.place(x=130, y=50)
        self.fila = tk.Entry(self.ventanaAdmin, font=("Castellar", 14), fg="#8d4925", bg="#107acc", width=10)
        self.fila.place(x=320,y=50)
        lblColumnas = tk.Label(self.ventanaAdmin, text="Columnas:", font=("Castellar", 14), fg="#8d4925", bg="#33CCFF", height=1, width=12)
        lblColumnas.place(x=130, y=100)
        self.columna = tk.Entry(self.ventanaAdmin, font=("Castellar", 14), fg="#8d4925", bg="#107acc", width=10)
        self.columna.place(x=320,y=100)
        self.btnCasillasNulas = tk.Button(self.ventanaAdmin, text="Elegir casillas Nulas", font=("Castellar", 14), fg="#8d4925", bg="#33CCFF", command=self.verificarDimensiones)
        self.btnCasillasNulas.place(x=128, y=150)
        self.btnTextoCasillas = tk.Button(self.ventanaAdmin, text="Ingresar palabras", font=("Castellar", 14), fg="#8d4925", bg="#33CCFF", command=self.textoCasillas )
        self.btnTextoCasillas.place(x=128, y=210)
        self.btnPistasHorizontales = tk.Button(self.ventanaAdmin, text="Pistas palabras horizontales", font=("Castellar", 14), fg="#8d4925", bg="#33CCFF", command=self.pistasHorizontales)
        self.btnPistasHorizontales.place(x=128, y=270)
        self.btnPistasVerticales = tk.Button(self.ventanaAdmin, text="Pistas palabras verticales", font=("Castellar", 14), fg="#8d4925", bg="#33CCFF", command=self.pistasVerticales)
        self.btnPistasVerticales.place(x=128, y=330)
        lblNombre = tk.Label(self.ventanaAdmin, text="Ingrese el nombre del Crucigrama", font=("Castellar", 14), fg="#8d4925", bg="#33CCFF")
        lblNombre.place(x=115, y=390)
        self.txtNombre = tk.Entry(self.ventanaAdmin, width=22, font=("Castellar", 14), justify="center")
        self.txtNombre.place(x=128,y=430)
        self.btnGuardar = tk.Button(self.ventanaAdmin, text="Guardar", bg="#107acc", width=15, height=1, font=("Castellar", 14), command=self.guardar)
        self.btnGuardar.place(x= 80, y = 500)
        self.btnCancelar = tk.Button(self.ventanaAdmin, text="Limpiar", bg="#107acc", width=15, height=1, font=("Castellar", 14),command=self.LimpiarCampos)
        self.btnCancelar.place(x= 330, y = 500)
        boton_regresar = tk.Button(self.ventanaAdmin, text="➢",font=("Castellar", 14), fg="#8d4925", bg="#33CCFF",command=self.regresarSecundaria)
        boton_regresar.place(x=720, y= 550)
#__________________________________________________________________________________________________________
    def verificarDimensiones(self):
        try:
            filas = int(self.fila.get())
            columnas = int(self.columna.get())
            if filas == "":                    
                messagebox.showwarning("FILAS", "Ingrese la cantidad de filas")#verifica que la casilla de filas no este vacia
            elif columnas == "":
                messagebox.showwarning("COLUMNAS", "Ingrese la cantidad de columnas")#verifica que la casilla columnas no este vacia 
            else:
                self.casillasNulas()
        #Verificar cualquier otro error y arroja un mensaje
        except Exception:
            messagebox.showerror("ALERTA", "Debes ingresar los valores de las dimensiones del crucigrama, solo puedes ingresar numeros")
            self.fila.delete("0","end") #Borra lo que se haya escrito en las casillas.
            self.columna.delete("0","end") 
#__________________________________________________________________________________________________________
    def casillasNulas(self):#Crea una ventana para que el administrador pueda seleccionar las casillas de manera grafica
        self.ventanaNulas = tk.Toplevel()
        self.ventanaNulas.geometry("+700+300")
        filas = int(self.fila.get())
        columnas = int(self.columna.get())
        self.listaNulas = [] 
        #Cambia de color las casillas al darle click
        def seleccionNulas(fila, columna):
            if (nulas[fila][columna]["bg"] == "SystemButtonFace"):
                nulas[fila][columna]["bg"] = "#107acc"
            else:
                nulas[fila][columna]["bg"] = "SystemButtonFace"
        # Confirmamos las casillas nulas y se guardan las casillas en una lista para crear el crucigrama real 
        def confirmarNulas():
            for fila in range(filas):
                for columna in range(columnas):
                    if nulas[fila][columna]["bg"] == "#107acc":
                        self.listaNulas.append([fila,columna])    
            messagebox.showinfo("CONFIRMACION", "Las casillas nulas han sido guardadas")
            self.ventanaNulas.destroy()
            self.btnTextoCasillas.config(state="active")
            self.btnCasillasNulas.config(state="disabled")
            self.fila.config(state="readonly")
            self.columna.config(state="readonly")
        
        #Se crea la matriz de botones para la seleccion de las casillas nulas
        nulas = []
        for fila in range(filas):
            filaBotones = []
            for columna in range(columnas):
                boton = tk.Button (self.ventanaNulas, width = 3, height=2, command= lambda fila=fila, columna=columna: seleccionNulas(fila,columna))
                boton.grid(row=fila, column=columna, padx = 0, pady= 0, ipadx =4 ) 
                filaBotones.append(boton)
            nulas.append(filaBotones)
        
        botonConfirmar = tk.Button(self.ventanaNulas, text="CONFIRMAR", bg="#33CCFF", command=confirmarNulas)
        botonConfirmar.grid(row=filas, columnspan=columnas)
#__________________________________________________________________________________________________________
    def textoCasillas(self):
        self.ventanaTexto = tk.Toplevel()
        self.ventanaTexto.geometry("+700+300")
        filas = int(self.fila.get())
        columnas = int(self.columna.get())
        fuenteTxt= tkFont.Font(size=30)
        self.letrasIngresadas = []
        #Valida que se ingrese solo una letra por casilla desde teclado  mediante validate y validate command en cada entry
        def validarIngreso(nuevo_valor):
            if len(nuevo_valor) > 1:
                return False
            return True
        
        validacion = self.ventanaTexto.register(validarIngreso)
        #Matriz de entrys para ingresar las palabras
        textoCasillas = []
        for fila in range(filas):
            filaTxt = []
            for columna in range(columnas):
                txt = tk.Entry (self.ventanaTexto,validate="key", validatecommand=(validacion,"%P"), width = 1, font= fuenteTxt, justify="center")
                txt.grid(row=fila, column=columna, padx = 0, pady= 0, ipadx =4) 
                filaTxt.append(txt)
            textoCasillas.append(filaTxt)
        for fila, columna in self.listaNulas:
            textoCasillas[fila][columna].config(state="disable")
        #Recorre la matriz y guarda en una lista las letras con su respectivo entry
        def confirmarLetras():
            for fila in range(filas):
                filaLetras = []
                for columna in range(columnas):
                    letra = textoCasillas[fila][columna].get().upper()
                    filaLetras.append((letra, fila,columna))
                self.letrasIngresadas.append(filaLetras)
            messagebox.showinfo("CONFIRMACION", "Palabras Guardadas correctamente")
            self.ventanaTexto.destroy()
            self.btnPistasHorizontales.config(state="active")
            self.btnTextoCasillas.config(state="disabled")
        botonConfirmar = tk.Button(self.ventanaTexto, text="CONFIRMAR", bg="#33CCFF", command=confirmarLetras)
        botonConfirmar.grid(row=filas, columnspan=columnas)
#__________________________________________________________________________________________________________
    def pistasHorizontales(self):
        self.ventanaPistasH = tk.Toplevel()
        self.ventanaPistasH.geometry("+425+220")
        self.pistasH = ""
        txtPistasH = tk.Text(self.ventanaPistasH, bd=10,  highlightbackground="#107acc", width=100, height=30)
        txtPistasH.tag_configure("left",justify="left")
        txtPistasH.grid(row=0, column=0)
        def confirmarPistasH():
            self.pistasH = txtPistasH.get("1.0", "end-1c")
            messagebox.showinfo("CONFIRMACION", "Pistas guardadas con exito")
            self.ventanaPistasH.destroy()
            self.btnPistasHorizontales.config(state="active")
            self.btnPistasHorizontales.config(state="disabled")
        botonConfirmar = tk.Button(self.ventanaPistasH, text="CONFIRMAR", bg="#33CCFF", command=confirmarPistasH)
        botonConfirmar.grid(row=1, column=0)
#__________________________________________________________________________________________________________
    def pistasVerticales(self):
        self.ventanaPistasV = tk.Toplevel()
        self.ventanaPistasV.geometry("+425+220")
        self.pistasV = ""
        txtPistasV = tk.Text(self.ventanaPistasV, bd=10,  highlightbackground="#107acc", width=100, height=30)
        txtPistasV.tag_configure("left",justify="left")
        txtPistasV.grid(row=0, column=0)
        def confirmarPistasV():
            self.pistasV = txtPistasV.get("1.0", "end-1c")
            messagebox.showinfo("CONFIRMACION", "Pistas guardadas con exito")
            self.ventanaPistasV.destroy()
            self.btnPistasVerticales.config(state="disable")
            self.btnGuardar.config(state="active")
            self.btnCancelar.config(state="active")
        botonConfirmar = tk.Button(self.ventanaPistasV, text="CONFIRMAR", bg="#33CCFF", command=confirmarPistasV)
        botonConfirmar.grid(row=1, column=0)
#__________________________________________________________________________________________________________
    def guardar(self):
        try:
            filas = str(self.fila.get())
            columnas = str(self.columna.get()) 
            nombreCrucigrama = self.txtNombre.get() 
            if (nombreCrucigrama == ""):
                messagebox.showerror("ERROR","Debe ingresar un nombre para el crucigrama")
            else:
                nombreCrucigrama = self.txtNombre.get() + ".txt"
                archivo = open(nombreCrucigrama,"w")
                archivo.write("Filas:" + filas + "\n")
                archivo.write("Columnas:" + columnas + "\n")
                archivo.write("Casillas Nulas:" + str(self.listaNulas) + "\n")
                archivo.write("Solucion:" + str(self.letrasIngresadas) + "\n")
                archivo.write("Pistas horizontales:"+ str(self.pistasH) + "\n")
                archivo.write("Pistas Verticales:" + str(self.pistasV)  + "\n")
                archivo.close()
                messagebox.showinfo("CONFIRMACIÓN", "La información del crucigrama se ha guardado con éxito")
                self.ventanaAdmin.destroy()
                self.menuPrincipal.deiconify()
        except Exception:
            messagebox.showerror("ERROR", "Se generó un error al guardar la información del crucigrama. Contacte al departamento de TI")
#__________________________________________________________________________________________________________
    def ventanaUsuario(self):
        self.ventana_secundaria.withdraw()
        self.ventaUsuario = tk.Toplevel()
        self.ventaUsuario.title("Usuario")
        self.ventaUsuario.geometry('900x600+400+150')
        # Cargar la imagen de fondo
        image_path = "preguntados.png"
        imagen_fondo = Image.open(image_path)
        imagen_fondo = imagen_fondo.resize((900, 600), Image.LANCZOS)
        imagen_fondo = ImageTk.PhotoImage(imagen_fondo)
        fondo_label = tk.Label(self.ventaUsuario, image=imagen_fondo)
        fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
        fondo_label.image = imagen_fondo
        e1 = tk.Label(self.ventaUsuario, text="Usuario", font=("Castellar", 14), fg="#8d4925", bg="#33CCFF")
        e1.pack()
        lbl1 = tk.Label(self.ventaUsuario, text="Elija el modo de juego:  ", font=("Castellar", 14), fg="#8d4925", bg="#33CCFF")
        lbl1.place(x=150, y=100)
        opciones = ["Dificil", "Facil"]
        self.combo = ttk.Combobox(self.ventaUsuario, values=opciones, font=("Castellar", 10), foreground="#8d4925", background="#33CCFF")
        self.combo.place(x=620, y=190)
        self.combo.bind("<<ComboboxSelected>>", self.actualizarBoton)
        lbl2 = tk.Label(self.ventaUsuario, text="Elija el crucigrama que desea jugar: ", font=("Castellar", 14), fg="#8d4925", bg="#33CCFF")
        lbl2.place(x=150, y=190)
        self.abrir_txt = tk.Button(self.ventaUsuario, text="Abrir crucigrama", font=("Castellar", 14), fg="#8d4925", bg="#33CCFF", state="disabled", command=self.Obtener_Info)
        self.abrir_txt.place(x=150, y=280)
        self.jugar = tk.Button(self.ventaUsuario, text="Jugar", font=("Castellar", 14), fg="#8d4925", bg="#33CCFF", state="disabled", command=self.ventanaJuego)
        self.jugar.place(x=150, y=370)
        boton_regresar = tk.Button(self.ventaUsuario, text="➢",font=("Castellar", 14), fg="#8d4925", bg="#33CCFF",command=self.regresaSecundaria2)
        boton_regresar.place(x=720, y= 550)
    def mostrarSeleccion(self):
        opcionSeleccionada = self.combo.get()
        return opcionSeleccionada 
    def actualizarBoton(self, event):
        opcionSeleccionada = self.combo.get()
        if opcionSeleccionada:
            self.abrir_txt.config(state="active")
        else:
            self.abrir_txt.config(state="disabled")
#______________________________________________________________________________________________#Metodos de regresar ventanas
    def regresarPrincipal(self):
        self.ventana_secundaria.destroy()#Cierra la ventana secundaria
        self.menuPrincipal.deiconify() #Muestra la ventana Principal
    def regresarSecundaria(self):
        self.ventanaAdmin.destroy()#Cierra la ventana Admi
        self.ventana_secundaria.deiconify() #Muestra la ventana Secundaria
    def regresaSecundaria2(self):
        self.ventaUsuario.destroy()#Cierra la ventana Usuario
        self.ventana_secundaria.deiconify()#Muestra la ventana Secundaria
    def regresaUsario(self):
        self.ventJuego.destroy()#Cierra la ventana juego
        self.ventaUsuario.deiconify()#Muestra la ventana Usuario
#______________________________________________________________________________________________#Metodo de limpiar campos
    def LimpiarCampos(self):
        self.fila.delete(0, 'end')
        self.columna.delete(0, 'end')
        self.txtNombre.delete(0, 'end')
#__________________________________________________________________________________________________________
    def ventanaJuego(self):
        self.ventaUsuario.withdraw()
        self.ventJuego = tk.Toplevel()
        self.ventJuego.title("Juego")
        self.ventJuego.geometry("+400+100")
        # Cargar la imagen de fondo
        image_path = "preguntados.png"
        imagen_fondo = Image.open(image_path)
        imagen_fondo = imagen_fondo.resize((1200, 600), Image.LANCZOS)
        imagen_fondo = ImageTk.PhotoImage(imagen_fondo)
        fondo_label = tk.Label(self.ventJuego, image=imagen_fondo)
        fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
        fondo_label.image = imagen_fondo
        # Frames
        frame1 = tk.Frame(self.ventJuego, borderwidth=2, relief="solid", bg="#107acc", width=400, height=300)  
        frame1.grid(row=0, column=0, padx=10, pady=10, rowspan=2)
        frame2 = tk.Frame(self.ventJuego, borderwidth=2, relief="solid", bg="#107acc", width=200, height=50)  
        frame2.grid(row=0, column=1, padx=20, pady=10)
        frame3 = tk.Frame(self.ventJuego, borderwidth=2, relief="solid", bg="#107acc", width=400, height=300)  
        frame3.grid(row=0, column=2, padx=20, pady=10, rowspan=2)
        frame4 = tk.Frame(self.ventJuego, borderwidth=2, relief="solid", bg="#107acc", width=200, height=200)  
        frame4.grid(row=2, column=1, padx=20, pady=10)
        boton_regresar = tk.Button(self.ventJuego, text="➢",font=("Castellar", 14), fg="#8d4925", bg="#33CCFF",command=self.regresaUsario)
        boton_regresar.grid(row=2, column=3, padx=20, pady=10)
#__________________________________________________________________________________________________________
        def verificarGanador():
            self.letrasSolucion = []
            for filaS, columnas_letras in enumerate(self.solucion):
                for columnaS, tupla in enumerate(columnas_letras):
                    if tupla[0]: 
                        letra, _, _ = tupla
                        self.letrasSolucion.append(letra)
                    else:
                        self.letrasSolucion.append('')
            
            self.letrasUsuario = []
            for fila in range(len(self.entradas_matriz)):
                for columna in range(len(self.entradas_matriz[fila])):
                    letra = self.entradas_matriz[fila][columna].get().upper()
                    self.letrasUsuario.append((letra))
            
            if self.letrasUsuario == self.letrasSolucion:
                messagebox.showinfo("Excelente!", "Has completado el crucigrama correctamente.")
                self.ventJuego.withdraw()
                self.ventaUsuario.deiconify()
            else:
                messagebox.showinfo("Incorrecto", "El crucigrama no es correcto.")
#_____________________________________________________________________________________________________________________
        def mostrarSolucion():
            self.cronometroActivo == False
            self.cronometro = tk.Label(frame3, font=fuenteReloj, text="00:00", bg="#107acc")
            for filaS, columnas_letras in enumerate(self.solucion):
                for columnaS, tupla in enumerate(columnas_letras):
                    if tupla[0]: 
                        letra, _, _ = tupla
                        entrada = tk.Entry(frame1, validate="key", validatecommand=(validacion, "%P"), width=1, font=("Castellar", 14), justify="center")
                        entrada.insert(0, letra)
                        entrada.grid(row=filaS, column=columnaS, padx=0, pady=0, ipadx=4)
                        entrada.config(state="readonly")
                        self.btnFin.config(state="disabled")
                        self.btnSolucion.config(state="disabled")
                    else:
                        pass
#_____________________________________________________________________________________________________________________
        def mostrarSolucion2():
            for filaS, columnas_letras in enumerate(self.solucion):
                for columnaS, tupla in enumerate(columnas_letras):
                    if tupla[0]: 
                        letra, _, _ = tupla
                        entrada = tk.Entry(frame1, validate="key", validatecommand=(validacion, "%P"), width=1, font=("Castellar", 14), justify="center")
                        entrada.insert(0, letra)
                        entrada.grid(row=filaS, column=columnaS, padx=0, pady=0, ipadx=4)
                        entrada.config(state="readonly")
                        self.btnFin.config(state="disabled")
                        self.btnSolucion.config(state="disabled")
                    else:
                        pass
#_____________________________________________________________________________________________________________________

        #Valida que se ingrese solo una letra a la vez en las casillas del crucigrama
        def validarIngreso(nuevo_valor):
            if len(nuevo_valor) > 1:
                return False
            return True
        validacion = self.ventJuego.register(validarIngreso)
#_____________________________________________________________________________________________________________________
        #Crucigrama en el frame 1
        self.entradas_matriz = []
        for i in range(self.filasC):
            fila = []
            for j in range(self.columnasC):
                entrada = tk.Entry(frame1, validate="key", validatecommand=(validacion,"%P"), width=1, font=("Castellar", 14), justify="center")
                entrada.grid(row=i, column=j, padx=0, pady=0, ipadx=4)
                fila.append(entrada)
            self.entradas_matriz.append(fila)
        
        for fila, columna in self.casillas_nulas:
            entrada = self.entradas_matriz[fila][columna]
            entrada.config(state="disabled")
#_____________________________________________________________________________________________________________________
        if self.mostrarSeleccion() == "Dificil":
            fuenteReloj = tkFont.Font(family=("Castellar", 14))
            self.cronometro = tk.Label(self.ventJuego, font=fuenteReloj, text="05:00", bg="#33CCFF")
            self.cronometro.grid(row=2, column=0)

            self.cronometroActivo = True
            def cuentaRegresiva(minutos, segundos):
                if segundos == 0:
                    if minutos == 0:
                        # Tiempo finalizado
                        self.cronometro.config(text="Tiempo finalizado.")
                        if self.cronometro["text"] == "Tiempo finalizado.":
                            messagebox.showwarning("SE ACABÓ EL TIEMPO", "Se terminó el tiempo. Esta es la solución")
                            mostrarSolucion()
                            return
                    else:
                        minutos -= 1
                        segundos = 59
                else:
                    segundos -= 1

                # Actualizar etiqueta con el nuevo tiempo
                self.cronometro.config(text=f"{minutos:02d}:{segundos:02d}")

                # Llamar a la función countdown() después de 1 segundo (1000 milisegundos)
                self.ventJuego.after(1000, cuentaRegresiva, minutos, segundos)

            # Iniciar la cuenta regresiva
            cuentaRegresiva(5, 0)
            # Cargar la imagen mostrar solucion
            imagen_solucion = Image.open("h.png")
            imagen_solucion = imagen_solucion.resize((50, 50), Image.LANCZOS)  # Ajustar tamaño de la imagen
            self.imagen_solucion = ImageTk.PhotoImage(imagen_solucion)
            
            # Cargar la imagen verificar
            imagen_solucion2 = Image.open("png-click.png")
            imagen_solucion2 = imagen_solucion2.resize((50, 50), Image.LANCZOS)  # Ajustar tamaño de la imagen
            self.imagen_solucion2 = ImageTk.PhotoImage(imagen_solucion2)
            

            self.btnFin = Button(frame3, image=self.imagen_solucion2, command=verificarGanador)
            self.btnFin.grid(row=0, column=0, pady=10)
            self.btnSolucion = Button(frame3, image=self.imagen_solucion, command=mostrarSolucion)
            self.btnSolucion.grid(row=1, column=0, pady=10)
        else:
            # Cargar la imagen mostrar solución
            imagen_solucion = Image.open("h.png")
            imagen_solucion = imagen_solucion.resize((50, 50), Image.LANCZOS)  # Ajustar tamaño de la imagen
            self.imagen_solucion = ImageTk.PhotoImage(imagen_solucion)
            
            # Cargar la imagen verificar
            imagen_solucion2 = Image.open("png-click.png")
            imagen_solucion2 = imagen_solucion2.resize((50, 50), Image.LANCZOS)  # Ajustar tamaño de la imagen
            self.imagen_solucion2 = ImageTk.PhotoImage(imagen_solucion2)
            
            self.btnFin = Button(frame3, image=self.imagen_solucion2, command=verificarGanador)
            self.btnFin.grid(row=0, column=0, pady=10)
            self.btnSolucion = Button(frame3, image=self.imagen_solucion, command=mostrarSolucion2)
            self.btnSolucion.grid(row=1, column=0, pady=10)
#_____________________________________________________________________________________________________________________
        #Pistas de palabras horizontales en el frame 2
        lblHorizontales = tk.Label(frame2, text="HORIZONTALES", bg="#33CCFF")
        lblHorizontales.grid(row=0, column=0)
        textoPistasH = tk.Text(frame2, width=60, height=10, wrap="word", bg="#107acc")
        textoPistasH.tag_configure("left", justify="left")
        for pista in self.pistas_horizontales:
            textoPistasH.insert(tk.END, pista + "\n")
        textoPistasH.grid(row=1, column=0)
#_____________________________________________________________________________________________________________________        
        #Pistas de palabras verticales en el frame 4        
        lblVerticales = tk.Label(frame4,text="VERTICALES", bg="#33CCFF")
        lblVerticales.grid(row=0, column=0)
        textoPistasV = tk.Text(frame4, width=60, height=10, wrap="word", bg="#107acc")
        textoPistasV.tag_configure("left", justify="left")
        for pista in self.pistas_verticales:
            textoPistasV.insert(tk.END, pista + "\n")   
        textoPistasV.grid(row=1, column=0)
#__________________________________________________________________________________________________________
    def Obtener_Info(self):
        self.archivoA = filedialog.askopenfilename(filetypes=(("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")))
        self.jugar.config(state="active")
        with open(self.archivoA, 'r') as file:
            contenido = file.read()
            filas_inicio = contenido.index("Filas:") + len("Filas:")
            filas_fin = contenido.index("Columnas:")
            columnas_inicio = contenido.index("Columnas:") + len("Columnas:")
            columnas_fin = contenido.index("Casillas Nulas:")
            casillas_nulas_inicio = contenido.index("Casillas Nulas:") + len("Casillas Nulas:")
            casillas_nulas_fin = contenido.index("Solucion:")
            solucion_inicio = contenido.index("Solucion:") + len("Solucion:")
            solucion_fin = contenido.index("Pistas horizontales:")
            pistas_horizontales_inicio = contenido.index("Pistas horizontales:") + len("Pistas horizontales:")
            pistas_horizontales_fin = contenido.index("Pistas Verticales:")
            pistas_verticales_inicio = contenido.index("Pistas Verticales:") + len("Pistas Verticales:")
            # Obtener las filas y columnas
            self.filasC = int(contenido[filas_inicio:filas_fin].strip())
            self.columnasC = int(contenido[columnas_inicio:columnas_fin].strip())
            # Obtener las casillas nulas
            self.casillas_nulas_str = contenido[casillas_nulas_inicio:casillas_nulas_fin].strip()
            self.casillas_nulas = eval(self.casillas_nulas_str)
            # Obtener la solución
            solucion_str = contenido[solucion_inicio:solucion_fin].strip()
            self.solucion = eval(solucion_str)
            # Obtener las pistas horizontales y verticales
            pistas_horizontales_str = contenido[pistas_horizontales_inicio:pistas_horizontales_fin].strip()
            self.pistas_horizontales = pistas_horizontales_str.split('\n')
            pistas_verticales_str = contenido[pistas_verticales_inicio:].strip()
            self.pistas_verticales = pistas_verticales_str.split('\n')
        return self.filasC, self.columnasC, self.casillas_nulas, self.solucion, self.pistas_horizontales, self.pistas_verticales
#_________________________________________Convocar la pantalla__________________________________________
def main():
    ventanaPrincipal = tk.Tk()
    juego = Ventanas(ventanaPrincipal)
    juego.ventanaPrincipal()
main()