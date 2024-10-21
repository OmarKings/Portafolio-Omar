import os
import utilerias as ut

class juegobn:
    def __init__(self):
        self.matriz = []
        self.file = ""
        self.juego = ""
        self.aciertos = 0
        self.fallos = 0
        self.obj_ut = ut.utilerias()
        print("""
  _  _ _  ___  ___   ___         ___  ___  ___  ___  _    _    ___  
 | || | || __>/  _> | . |       | . >| . ||_ _|| . || |  | |  | . | 
_| || ' || _> | <_/\| | |       | . \|   | | | |   || |_ | |_ |   | 
\__/`___'|___>`____/`___'       |___/|_|_| |_| |_|_||___||___||_|_| 
                                                                    
                _ _  ___  _ _  ___  _                               
               | \ || . || | || . || |                              
               |   ||   || ' ||   || |_                             
               |_\_||_|_||__/ |_|_||___|   
        """)
        print("""                      
                                                          
        
                                                                              ▒▒                        
                                                                  ░░░░░░                        
                                                                  ▒▒▒▒                          
                                                                  ▒▒          ▒▒                
                                                            ░░                                  
                                                          ░░▒▒      ░░                          
                                                          ▒▒▒▒░░            ░░                  
                                                        ▒▒▒▒▒▒                                  
                                                        ▒▒▒▒            ░░░░                    
                                                          ▒▒            ▒▒▒▒                    
                                                      ▒▒▒▒            ▒▒  ▒▒                    
                                                    ▒▒▒▒▒▒░░                                    
                                                    ▒▒▒▒▒▒▒▒        ▒▒▒▒▒▒                      
                          ▒▒                        ▒▒▒▒▒▒          ▒▒▒▒▒▒                      
                        ░░▒▒░░                  ██████████████      ▒▒▒▒                        
                        ░░▒▒░░                  ██▒▒▒▒▒▒▒▒▒▒██      ▒▒                          
                      ░░  ▒▒  ░░                ██▒▒▒▒▒▒▒▒▒▒██  ██████████                      
                      ░░  ▒▒  ░░                ██▓▓▓▓▓▓▓▓▓▓██  ██▒▒▒▒▒▒██                      
                    ░░  ░░▒▒    ░░              ██▓▓▓▓▓▓▓▓▓▓██  ██▒▒▒▒▒▒██                      
                    ░░  ░░▒▒░░  ░░              ██▓▓▓▓▓▓▓▓▓▓██  ██▓▓▓▓▓▓██                      
                  ░░  ░░  ▒▒░░    ░░            ██▓▓▓▓▓▓▓▓▓▓██  ██▓▓▓▓▓▓██      ▒▒              
                ░░    ░░  ▒▒  ░░    ░░          ██▓▓▓▓▓▓▓▓▓▓██  ██▓▓▓▓▓▓██    ░░▒▒░░            
                ░░  ░░    ▒▒  ░░                ██▓▓▒▒▓▓▒▒▓▓██  ██▓▓▓▓▓▓██    ░░▒▒░░            
              ░░    ░░  ██▒▒████░░████░░▒▒████████▒▒▓▓▒▒██▒▒██  ██▓▓▓▓▓▓██  ░░  ▒▒  ░░          
            ░░    ░░  ██░░▒▒░░▒▒░░▒▒▒▒▒▒░░░░▒▒▒▒  ▒▒░░▒▒▒▒▓▓██  ██▓▓▓▓▓▓██░░    ▒▒  ░░          
          ░░      ░░  ██░░▒▒░░▒▒▒▒░░▒▒▒▒▒▒░░▒▒▒▒░░▒▒░░▒▒██▓▓██  ██▓▓▓▓▓▓██  ████████  ░░        
        ░░      ░░  ██▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒████████████████████▒▒▒▒▒▒▒▒██  ░░      
      ░░        ░░  ██████▒▒████████░░████████░░████████▒▒░░▒▒▒▒░░▒▒▒▒░░▒▒▒▒░░▒▒░░▒▒▒▒██  ░░    
████████      ░░    ██░░░░▒▒░░░░░░▒▒░░▒▒▒▒░░░░▒▒░░▒▒▒▒░░▒▒░░▒▒▒▒░░▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒████████████
██░░░░░░████████    ██▒▒░░▒▒░░▒▒░░▒▒▒▒░░▒▒░░░░▒▒▒▒░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████████████░░░░░░░░░░██
██░░░░░░░░░░░░░░██████████████▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒██████████████░░░░░░░░░░░░░░░░░░░░░░██
  ██░░░░░░░░░░░░▒▒░░░░░░░░░░▒▒████████████████████████████░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░▒▒▒▒██
  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓▓▓██
  ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓██  
    ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓██  
    ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██  
    ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████░░░░
      ██▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████  ██      ░░
      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████          ░░░░░░
      ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██    ██░░          ░░░░░░░░░░  
        ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████████████              ░░░░░░░░░░░░░░    
      ░░██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████    ██████░░            ░░░░░░  ░░░░░░░░░░░░░░░░      
  ░░░░░░  ▓▓▓▓▓▓▓▓▓▓▓▓████      ████                        ░░░░░░░░░░░░░░░░░░░░░░░░░░          
  ░░░░          ████                          ░░░░░░    ░░░░░░░░░░░░░░░░░░░░░░░░                
░░░░░░                    ░░░░  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                        
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                                
  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                                            

""")

        print("==============================================================")
        print("|Para iniciar indica el nombre del archivo que deseas cargar |")
        print("|Si deseas un juego nuevo simplemente oprime [ENTER]         |")
        print("|Escribe el nombre del archivo sin extension                 |")
        print("==============================================================")

        self.file = self.obj_ut.pide_cadena("indica el nombre del archivo: ", 0, 10)
        if len(self.file) == 0:
            self.file = "a1.csv"
        else:
            self.file += ".csv"
        self.carga_matriz_file()

    def carga_matriz_file(self):
        print("Juego de :", self.file, end="\n")
        if os.path.exists(self.file):
            with open(self.file, "r") as arch:
                self.matriz = []
                self.aciertos = 0 
                self.fallos = 0 
                for registro in arch:
                    registro = registro.strip()
                    lista = registro.split(",")
                    if len(lista) == 8:
                        self.matriz.append(lista)
                        self.aciertos += lista.count("A") 
                        self.fallos += lista.count("X")  
                    else:
                        self.obj_ut.error("Error, el archivo no tiene el formato correcto")
                        return
            if len(self.matriz) != 8:
                self.obj_ut.error("Error, el archivo no tiene el formato correcto")
                return
        else:
            self.obj_ut.error("Error, el archivo no existe")

    def muestra_matriz(self):
        if len(self.matriz) != 8 or any(len(fila) != 8 for fila in self.matriz):
            self.obj_ut.error("Error, la matriz no está correctamente cargada")
            return

        print("  0 1 2 3 4 5 6 7 ")
        print("  " + ("-" * 17))
        for ren in range(8):
            print(str(ren) + "|", end="")
            for col in range(8):
                if self.matriz[ren][col] == "V" or self.matriz[ren][col] == "B":
                    print(" ", end="|")
                else:
                    print(self.matriz[ren][col], end='|')
            if ren == 0:
                print("    |ACIERTOS =", self.aciertos, end="|")
            if ren == 1:
                print("    |FALLOS   =", self.fallos, end="|")
            
            print("")
            print("  " + "-" * 17)

    def descarga_matriz(self):
        nombre_file = self.obj_ut.pide_cadena("Indica el nombre del archivo: ", 1, 10)
        nombre_file += ".csv"
        with open(nombre_file, "w") as arch:
            for ren in range(8):
                registro = ",".join(self.matriz[ren]) + "\n"
                arch.write(registro)

    def tiro(self, ren, col):
        if ren >= 8 or col >= 8:
            texto = """
                               __/___            
                         _____/______|           
                 _______/_____\_______\_____     
                 \              < < <       |    
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ____   ____  __ __   ____  _____
 /    | /    ||  |  | /    |/ ___/
|  o  ||   __||  |  ||  o  (   \_ 
|     ||  |  ||  |  ||     |\__  |
|  _  ||  |_ ||  :  ||  _  |/  \ |
|  |  ||     ||     ||  |  |\    |
|__|__||___,_| \__,_||__|__| \___|
                                  

            """
            print(chr(27) + texto)
            self.guardaraprt(ren, col)
        else:
            if self.matriz[ren][col] == "A" or self.matriz[ren][col] == "X":
                self.obj_ut.error("Error, ya hay un tiro previo en esa celda")
            else:
                if self.matriz[ren][col] == "V":
                    self.obj_ut.error("Celda vacía, se incrementan los errores")
                    self.fallos += 1
                    self.matriz[ren][col] = "X"
                else:
                    self.obj_ut.error("Celda con barco, se incrementan los aciertos")
                    self.aciertos += 1
                    self.matriz[ren][col] = "A"

    def actualiza(self):
        with open(self.file, "w") as arch:
            for ren in range(8):
                registro = ",".join(self.matriz[ren]) + "\n"
                arch.write(registro)

    def restaurar_o_guardar(self, ren, col):
        respuesta = self.obj_ut.pide_cadena("¿Quieres restaurar el archivo original? (s/n): ", 1, 1)
        if respuesta.lower() == "s":
            for ren in range(8):
                for col in range(8):
                    if self.matriz[ren][col] == "X":
                        self.matriz[ren][col] = "V"
                    elif self.matriz[ren][col] == "A":
                        self.matriz[ren][col] = "B"
            self.actualiza()
        else:
            self.actualiza()

    def guardaraprt(self, ren, col):
        respuestaguard = self.obj_ut.pide_cadena("¿Quieres guardar en otro archivo? (s/n): ", 0, 1)
        if respuestaguard.lower() == "s":
            self.descarga_matriz()
            self.restaurar_o_guardar(ren, col)
        elif respuestaguard.lower() == "n":
            self.actualiza()
