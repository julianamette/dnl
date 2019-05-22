'''
Programa DNL para analisis de campos en dos dimensiones.
author:@julianamette3@gmail.com

El objetivo de este programa es tener herramientas que permitan un analisis rapido
para sistemas de escuaciones de dos dimensiones.

'''
import numpy as np 
import matplotlib.pyplot as plt
from numpy import linalg as LA

#Aca se define la funcion de tu campo de dos cordenadas!
def f(x,y):
    return y**3-4*x, y**3-y-3*x 

### este es un ejemplo copado para mas adelante
def funcion_linda(x,y,a,b):        
    return y , a + b*x + x**2 -x*y
####


#Esta funcion, dada una matriz te devuelve los autovalores y autovectores de la misma
#Sirve para ver la parte lineal y la usamos mas delante para otras funcioens
def aval_avec(matrix):
    '''
    input: matriz de la parte lineal
    output: w vector de los autovalres y v vector que tiene los autovectores en columnas
    '''
    w,v = LA.eig(matrix)
    print('Los autovalores son ', w )
    print('Los autovectores son ', v[:,0], ' y ', v[:,1])
    return w,v


#La siguiente funcion es la que uno mas va a usar y es para graficar un campo y sus mulclinas
def nulclinas_y_campo(fn,xmin,xmax,ymin,ymax,nro_puntos, plot = 'si',m_lin = 'none',ax = 'none'):
    
    '''
    input:
    fn: funcion que quieras graficar
    xmin: minimo en el eje x que se quiere realizar el grafico
    xmax: maximo de x
    ymin: minimo de y
    ymax: maximo de y
    nro_puntos:  es la resolucion en la que queres que se grafiquen las cosas, recomendada: 1000
    plot: default: si, si pones plot = 'no' no va a graficar y podes usar lo que te devuelve para
          lo que quieras.
    m_lin: default : 'none',  si se introduce la matriz de la parte lineal te va a graficar
            los autovectores y decir sus autovalores, esta bueno a veces. Si no podes nada
            no los va a graficar.
    ax :  default: 'none' Es el par de ejes sobre el que queres que grafique, a menos que 
    quieras usar la funcion para meterla adentro de otra es mejor no poner ningun input.

    RECORDAR: si la funcion ya tiene un default no es necesario poner de input esos parametros
    NOTA: esta funcion tiene un parametro magico en la parte de ax.streamplot que es el de density
    ahora esta seteado en 1.5, si queres mas resolucion de las lineas de corriente, subilo, 
    1.7 o 1.9 es algo ya bien denso, el tema es que va a ser re caro hacer la animacion rapudo
    asi que no es tan trivial.
    '''
    x = np.linspace(xmin,xmax,nro_puntos)
    y = np.linspace(ymin,ymax,nro_puntos)
    X, Y = np.meshgrid(x,y)
    (u,v) = fn(X,Y)
    if ax == 'none':
        fig, ax = plt.subplots()
    ax.streamplot(X, Y, u, v,density=1.5,color = 'teal')
    cs_u = ax.contour(X,Y,u,[0],colors=['navy'])
    cs_v = ax.contour(X,Y,v,[0])
    ax.grid()
    try:
        ax.clabel(cs_u ,fmt = 'Nulclina x', colors=['navy'])
        ax.clabel(cs_v ,fmt = 'Nulclina y')
    except:
        pass
    if m_lin != 'none':
        w,v = aval_avec(m_lin)
        ax.plot((0,v[:,0][0]),(0,v[:,0][1]),'.-' , label = 'Avec con aval %f' %w[0])
        ax.plot((0,v[:,1][0]),(0,v[:,1][1]),'.-',  label = 'Avec con aval %f' %w[1])
        ax.legend()
    if plot == 'si':
        plt.show()

##La proxima seccion es para analizar como cambia el campo en funcion de los parametros
#y las diferentes bifurcaciones que tiene
#IMPORTANTE: Esta escrita para f(x,y,a,b) por lo que si es ese tu caso con muy pocos cambios
#lo vas a poder hacer pero la logica es la misma para mas variables asi que es muy analogo

#Supongo que tengo un campo que depende de dos parametros a y b, propongo una parametrizacion
#para ir moviendo estos. La siguiente es un circulo de radio 1.
def param(theta):
    return np.cos(theta) , np.sin(theta) #la primera coordenada es a y la segunda b

#Como la parametrizacion depende de theta pongo los valores entre los que me voy a mover
theta = np.linspace(0,2*np.pi,100)

#Ahora igualo los valores a la parametrizacion para ya tenerlos guardados
val = param(theta)

#La siguiente funcion es la animacion para ir variando los parametros
def animacion(fn,array,xmin,xmax,ymin,ymax):
    '''
    fn: funcion que quieras ver fn(x,y,a,b)
    array:  es el array de los valores que voy a ir variando.
    xmin, xmax, ymin, ymax son todos los bordes otra vez
    '''
    fig, ax = plt.subplots()    
    for i in range(len(theta)):
        def g(x,y):
            return fn(x,y, array[0][i], array[1][i])
        nulclinas_y_campo(g,xmin,xmax,xmin,xmax,1000,plot = 'no', ax = ax)
        ax.set_title('a = %.2f , b = %.2f' %(array[0][i],array[1][i]))
        plt.pause(0.1)
        ax.clear()

animacion(funcion_linda,val,-5,5,-5,5)
#nulclinas_y_campo(f,0,20,0,20,1000)