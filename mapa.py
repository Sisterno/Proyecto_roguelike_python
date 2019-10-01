#Este proyecto se inicio el 28/09/2019 
# Autor: Gonzalo Rojas Alvarez
# \


import random
import sys


_camino='░'
_window_height_max=10
_window_width_max=20
_avanzes=[1,0,-1]
def _get_ramdom():
    return random.randint(1,5)
class mapa_o():
    # map_array [_window_height_max][_window_width_max]
    
    def __init__(self):
        self.map_forma=[]
        for i in range(_window_height_max):
            self.map_forma.append(list())
            # linea=list()
            for j in range(_window_width_max):
                self.map_forma[i].append('X')
            # self.map_forma[i].append(linea)
        print('holas')
        pass

    def print_map(self):
        # print self.map_forma[0][0]
        for i in self.map_forma:
            for j in i:
               print(j,end='')
                # print(j)
                # print('H')
            print('\n',end='')
        # print(self.map_forma[0][0])
        pass        

    def crear_caminos(self):
        centro_x=_window_height_max//2
        centro_y=_window_width_max//2
        pass

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
        pass    

        
