#Este proyecto se inicio el 28/09/2019 
# Autor: Gonzalo Rojas Alvarez
#  Vamo crear un semilla para q los mapas se creen de manera prosedural
# PS: esto estoy poniendo para recordar lo  que me ense;aron mis profesores de la universidad :v


import random 

class seed:
    @staticmethod
    def gen_seed():
        x=''
        for i in range(6):
            if(random.randint(1,2)==2):
                if(random.randint(1,2)==2):
                    x+= chr(random.randint(65,90))
                    pass
                else:
                    x+= chr(random.randint(97,122))
                    pass
            else:
                x+=chr(random.randint(48,57))
                pass
            pass
        return x 