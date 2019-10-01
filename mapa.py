#Este proyecto se inicio el 28/09/2019 
# Autor: Gonzalo Rojas Alvarez
# \


import random
import sys
import threading


_camino='░'

_avanzes=[1,-1]
def _get_ramdom():
    return random.randint(1,5)
class mapa_o():
    # map_array [_window_height_max][_window_width_max]
    
    def __init__(self,canti_max,x_max,y_max):
        self._window_height_max=x_max
        self._window_width_max=y_max
        self.max=canti_max
        self.map_forma=[]
        for i in range(self._window_height_max):
            self.map_forma.append(list())
            # linea=list()
            for j in range(self._window_width_max):
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

    def bot_ciego(self,x,pos_x,pos_y):
        # espacios_disp=x
        bot_pos_x=pos_x
        bot_pos_y=pos_y
        bit_casilla_vacia=False
        while x>0:
            pos_ini_x=bot_pos_x
            pos_ini_y=bot_pos_y
            while bit_casilla_vacia==False :
                if random.randint(0,2):
                    bot_pos_x+=random.choice(_avanzes)
                else:
                    bot_pos_y+=random.choice(_avanzes)
                if bot_pos_x>self._window_height_max or bot_pos_y>self._window_width_max or bot_pos_x<0 or bot_pos_y<0 :
                    bot_pos_x=pos_ini_x
                    bot_pos_y=pos_ini_y

                print('x={} - Y={}'.format(bot_pos_x,bot_pos_y))
                if self.map_forma[bot_pos_x][bot_pos_y]!=' ' :
                    self.map_forma[bot_pos_x][bot_pos_y]=' '
                    if random.randint(1,10)==1 and x>=2:
                        self.bot_ciego(x-1,bot_pos_x,bot_pos_y)
                    x-=1
                    bit_casilla_vacia=True
                    pass
                pass
            bit_casilla_vacia=False
        pass
    
    
    def crear_caminos(self):
        centro_x=self._window_height_max//2
        centro_y=self._window_width_max//2
        self.map_forma[centro_x][centro_y]=' '
        print('x={} - Y={}'.format(centro_x,centro_y))
        self.bot_ciego(self.max,centro_x,centro_y)
        pass

    

        
