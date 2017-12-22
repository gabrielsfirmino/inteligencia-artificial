import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def calculateF(x, y):
    fx = ((4 - 2.1*(x**2) + (x**4/3))*(x**2) +(x*y) - (4 * (1-(y**2))*(y**2)))
    return fx

def calculateDFx(x, y):
    dfx = 2*(x**5 - 4.2*x**3 + 4*x + 0.5*y)
    return dfx

def calculateDFy(x, y):
    dfy = x + 16*y**3 - 8*y
    return dfy

def calculateDDFxx(x, y):
    ddfxx = 10*x**4 - 25.2*x**2 + 8
    return ddfxx

def calculateDDFxy(x, y):
    return 1

def calculateDDFyx(x, y):
    return 1

def calculateDDFyy(x, y):
    ddfyy = 48*y**2 - 8
    return ddfyy

def calculateGradient(x, y):
    gradient = [calculateDFx(x, y), calculateDFy(x, y)]
    print("Gradient = %s" %gradient)
    return gradient

def calculateHessian(x, y):
    hessian = [calculateDDFxx(x,y), calculateDDFxy(x, y), calculateDDFyx(x, y), calculateDDFyy(x, y)]
    print("Hessian = %s"%hessian)

def calculateD(x, y):
    g = calculateGradient(x, y)
    calculateHessian(x, y)
    d = [g[0]*(-1), g[1]*(-1)]
    print("d = %s" %d)
    return d

def gradientMethod(x, y, alpha):
    d = calculateD(x, y)
    xnew = x + alpha*d[0]
    ynew = y + alpha*d[1]
    return [xnew, ynew]

def stepsGradient(xi, yi, tolerance, interations, alpha):    
    count = 0
    stepDiference = 1 + tolerance
    vetorx = []
    vetory = []
    vetorz = []

    while((count < interations) & (stepDiference > tolerance)):
        print("[x, y] = %s" %[xi, yi])
        new = gradientMethod(xi, yi, alpha)
        vetorx.append(xi)
        vetory.append(yi)
        vetorz.append(calculateF(xi, yi))
        stepDiference = abs(calculateF(xi, yi) - calculateF(new[0], new[1]))
        count = count + 1
        print("Numero da iteracao = %s" %count)
        xi = new[0]
        yi = new[1]
        print("#########################")

    return vetorx, vetory, vetorz

def main():
    vx, vy, vz = stepsGradient(-3,0.75,0.0001,500,0.001)

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.plot(vx, vy, vz, color='r', label='progression')
    ax.legend()

    X = np.arange(-3, 3.01,0.01)
    Y = np.arange(-2, 2.01,0.01)
    X, Y = np.meshgrid(X, Y)
    Z = calculateF(X,Y)

    ax.plot_wireframe(X, Y, Z, color='g', rstride=10, cstride=10)

    plt.show()

main()
