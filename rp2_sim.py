def asm_pio(*args, **kwargs):
'''asm_pio es un decorador que acoge argumentos y los guarda en listas
donde *args => son argumentos que no se le asigna variables y **kawargs => son argumentos que
se le asignan variables
'''
    def decorador(programa):
    '''
    esta funcion es un decorador que recibe funciones a partir de "programa"
    '''
        def compilador():
        '''
        Funcion que se ejecuta a base de la funcion recibida del decorador
        '''
            print("Parámetros", kwargs) 
            programa()
            return None
        return compilador
    return decorador

def decorador_instr(fun_inst):
'''
Esta funcion es un decorador que recibe cierta funcion para modificar en el parametro del programa
'''
    def decoracion_instr(self,*args, **kwargs):
    '''
    Esta funcion llama a la funcion (fun_inst)
    '''
        fun_inst(self,*args, **kwargs)
        return None 
    return decoracion_instr

pins='pins'

class PIO():
    OUT_LOW='PIO.OUT_LOW'
    

class StateMachine:
  def __init__(self, id_, program, freq=125000000, **kwargs):
  '''       
    Es el constructor de la clase StateMachine, donde se utiliza parametro id_ a usar
    program => que se define como el programa que se ejecutara en la clase StateMachine
    frec => que define la frecuencia usada de en la maquina de estado
    **kwargs => Que son los argumentos de lista. El constructor imprime las instrucciones que llegan
    por medio de (**kwargs)
  '''
        global sm_iniciandose,fsms
        sm_iniciandose=self
        #print('StateMachine.__init__',id_, program, freq, kwargs)
        self.lista_instr=[]
        program()
        print('Fueron leidas',len(self.lista_instr), 'instrucciones')
        sm_iniciandose=None
        fsms[id_]=self
        pass
      
        
  def active(self, x=None):
    '''
    Esta rutina simula exclisivamnte esa FSM. Sería interesante
    crear simulación en parlelo con otras FSM
    '''
    if x==1:
        print('Está pendiente de realizar la simulacón')

fsms=[None]*8

sm_iniciandose=None    


class nop:
    @decorador_instr
    def __init__(self,*args, **kwargs):
    '''
    El constructor de la clase nop @decorador_instr que imprime el nombre
    de la clase enviado por (self)
    '''
        global sm_iniciandose
        print(self.__class__.__name__)#,'nop.__init__',args,kwargs)
        sm_iniciandose.lista_instr.append(self)

        pass
     
    def __getitem__(self,name):
    '''
    Funcion que tiene un (_getitem_) y contiene el parametro
    (self) y (name)
    '''
        #print('nop.__getattr__',name)
        pass
        
class set(nop):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        pass
   
class wrap_target(nop):
    def __init__(self,*args, **kwargs):
    '''
    Constructor de (set) que usa (unit) en la funcion de la clase
    '''
         super().__init__(*args, **kwargs)
         pass 
  
class wrap(nop):
    def __init__(self,*args, **kwargs):
    '''
    Constructor de (set) que usa (unit) en la funcion de la clase
    '''

         super().__init__(*args, **kwargs)
         pass 
         
         
