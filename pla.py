#from numpy import *
import numpy as np

#known data & result
#np.array is vector rather than list
#data1[feature1,feature2,feature3,feature4,feature5]
data = np.array([[1,2,3,4,7],[5,6,7,8,9],[9,10,11,12,13],[5,5,5,5,5]])
#result = [data1,data2,data3,data4]
result = [1, 2, 3,-5]
#weighting of each feature(1~5)
w = np.array([0,0,0,0,0])#is vector, not list
iteration = 0

print 'Initial w: %r' % w
while True:
    iteration = iteration + 1
    false = 0
    f = 0
    
    for feature in data:
        h = np.dot(w.T, feature)
        if np.sign(result[f]) != np.sign(h):
            false = false + 1
            w = w + result[f] * feature
            print 'w--> %r' % w
        f = f + 1
    print 'End of Iteration %d: (false: %d / data: %d)' % (iteration, false, len(data))
    if false == 0: break
print '\nFinal Weighting: %r' % w
