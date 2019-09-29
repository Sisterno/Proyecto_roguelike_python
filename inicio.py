
#Este proyecto se inicio el 28/09/2019 
# Autor: Gonzalo Rojas Alvarez
# 
# PS: esto estoy poniendo para recordar lo  que me ense;aron mis profesores de la universidad :v
# PS-2: El texto lo pondre en ingles, por que lo necesito practicar (si lo pongo mal y alguien ve este comentario, porfa aviseme)
import mapa.py


def _print_welcome():
    print('Welcome to project roguelike PICHY')
    print('what would you like to try?')
    print('*')
    print('[M]ap generation')

if __name__=='__main__':
    _print_welcome()

    opcion=input()
    opcion = opcion.upper()

    if opcion=='M':
        # Abrir funciones de mapa
        print('esto va a poco')
        m=mapa_o('my salsa')
        
        m.print_map()

            