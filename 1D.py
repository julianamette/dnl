from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np



#graficar una funcion x'(c,x)
def plot_function(xmin,xmax,fn):
    x = np.arange(xmin,xmax,0.001)
    plt.plot(x,fn(x))
    plt.xlabel('x')
    plt.ylabel('$\dot{x}$')
    plt.grid()
    plt.legend()
    plt.show()


#graficar el diagrama de bifurcaciones a partir de una funcion parametrica de las dos variables
def plot_param_2d(tmin,tmax,step,fn):
    '''
    Esta funcion plotea una curva parametrica. 
    Se puede ver el diagrama de bifurcaciones si,
    dada una ecuacion x'(c1,c2,x) se ven
    x' = 0 y dx'/dx = 0
    y se despeja c1(x) y c2(x)

    Parametros:

    tmin: valor minimo de la parametrizacion
    tmax: valor maximo de la parametrizacion
    step: paso de t
    fn: funcion fn(x) = (c1(x),c2(x))

    '''
    x = np.arange(tmin,tmax, step)
    plt.plot(fn(x)[0],fn(x)[1])
    plt.xlabel('c1')
    plt.ylabel('c2')
    plt.grid()
    plt.show()
###

#puntos fijos para una ecuacion x'(c1,c2,x) para ver en tres dimensiones pf
def plot_implicit_3d(fn, xmin, xmax, ymin, ymax, zmin, zmax):
    ''' 
    Esta funcion esta hecha para plottear una funcion F(x,y,z) = 0
    Funcion para realizar un grafico de los puntos fijos a partir de una
    funcion implicita. Esta se obtiene despues de ver cuadno la velocidad 
    del flujo x' = 0. Cuando el flujo es x'(c1,c2,x)
    Un buen ejemplo para ver es usar la siguiente funcion:
    def fn(x,y,z):
        return x - y*z + (z**2)/(1+z**2)
     y ver plot_implicit(fn,0,2,0,2,0,3)
    En este flujo se puede ver la 'manta doblada' quizas un poco diferente
    a como nos aconstumbramos a que nos hagan el dibujo.
    '''

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    Ax = np.linspace(xmin, xmax, 100) # resolution of the contour
    Ay = np.linspace(ymin, ymax, 100) # resolution of the contour



    ##Tengo que escribir las "slices" que voy a graficar de cada eje
    Sx = np.linspace(xmin, xmax, 50) # numero de slices en x
    Sy = np.linspace(ymin, xmax, 50) # numero de slices en y
    Sz = np.linspace(zmin, xmax, 50) # numero de slices en z


    A1,A2 = np.meshgrid(Ax,Ay) # grid en la que voy a plottear

    for z in Sz: # contornos en el plano XY
        X,Y = A1,A2
        Z = fn(X,Y,z)
        cset = ax.contour(X, Y, Z+z, [z], zdir='z')
        # [z] defines the only level to plot for this contour for this value of z

    for y in Sy: # contornos en el plano XZ
        X,Z = A1,A2
        Y = fn(X,y,Z)
        cset = ax.contour(X, Y+y, Z, [y], zdir='y')

    for x in Sx: # contornos en el plano YZ
        Y,Z = A1,A2
        X = fn(x,Y,Z)
        cset = ax.contour(X+x, Y, Z, [x], zdir='x')

    # must set plot limits because the contour will likely extend
    # way beyond the displayed level.  Otherwise matplotlib extends the plot limits
    # to encompass all values in the contour.
    ax.set_zlim3d(zmin,zmax)
    ax.set_xlim3d(xmin,xmax)
    ax.set_ylim3d(ymin,ymax)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    plt.show()
###

#EJEMPLO
def fn(x,y,z):
        return x - y*z + (z**2)/(1+z**2)

plot_implicit_3d(fn,0,2,0,2,0,3)

def param(x):
    return  (2*x**2)/(1+x**2)**2 - x**2/(1+x**2) , (2*x)/(1+x**2)**2 

plot_param_2d(-5,5,0.01,param)