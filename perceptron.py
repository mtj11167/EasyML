import numpy as np
class Perceptron(object):
    def __init__(self):
        W=0
        b=0
    def fit(self,X,Y,eta):
        '''

        :param X: numpy.ndarray [samples,features]
        :param Y:numpy.ndarray
        :param eta: float step
        :return:
        '''
        X = np.asarray(X)
        Y = np.reshape(Y,newshape=(Y.size,))
        self.W = np.zeros(shape=(X.shape[1],1))
        self.b = 0
        while True:
            repeat_flag = False
            for i in range(X.shape[0]):
                if Y[i]*(np.dot(self.W.T,X[i:i+1,:].T)+self.b) <= 0:
                    self.W += eta*Y[i]*X[i:i+1,:].T
                    self.b += eta*Y[i]
                    repeat_flag = True
                    break
            if repeat_flag ==False:
                break
    def pridict(self,X):
        if np.dot(self.W.T,X)+self.b > 0:
            return 1
        else:
            return -1
if __name__ == "__main__":
    X=np.array([[3,3],[4,4],[1,1]])
    Y =np.array([1,1,-1])
    p =Perceptron()
    p.fit(X,Y,1)
    print(p.W)
    print(p.b)