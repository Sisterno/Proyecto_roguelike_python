#Este proyecto se inicio el 28/09/2019 
# Autor: Gonzalo Rojas Alvarez
# \


import random

_camino='░'
_window_height_max=50
_window_width_max=100
_avanzes=[1,0,-1]
def _get_ramdom():
    return random.randint(1,5)
class mapa_o():
    map_forma=[]
    # map_array [_window_height_max][_window_width_max]
    

    def __init__(self,sa):
        # self.salsa=sa
        # for i in range(_window_height_max):
        #     self.map_forma.append([])
        #     for j in range(_window_width_max):
                # self.map_forma[i].append('█')
        print('holas')
    
    def print_map(self):
        # for i in range(_window_height_max):

        #     for j in range(_window_width_max):
        #        print(map_forma[i][j])
            print('\n')

    def crear_caminos(self):
        centro_x=_window_height_max//2
        centro_y=_window_width_max//2

    def bot_ciego(self,x,pos_x,pos_y):
        espacios_disp=x
        bot_pos_x=pos_x
        bot_pos_y=pos_y
        while x>0:
            bot_pos_x+=random.choice(_avanzes)
            bot_pos_y+=random.choice(_avanzes)
            if random.randint(10)==1 and x>=2:
                bot_ciego(x-1,bot_pos_x,bot_pos_y)
            x-=1
            

        
