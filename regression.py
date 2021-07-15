from numpy import *
def standRegres(xArr, yArr):
    xMat = mat(xArr);
    yMat = mat(yArr).T
    xTx = xMat.T * xMat
    if linalg.det(xTx) == 0.0:
        print("This matrix is singular, cannot do inverse")
        return
    ws = xTx.I * (xMat.T * yMat)
    return ws
def answer(yuce,ws):
    xMatnew=mat(yuce)
    yHat=xMatnew*ws
    b={}
    k = '1'
    for i in yHat:
        shunxu=int(k)-1
        b[k]=float(str(yHat[shunxu])[2:-2])
        k=str(int(k)+1)
    return b
