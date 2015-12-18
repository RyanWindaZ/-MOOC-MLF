import numpy as np
import random

#data1[feature1,feature2,feature3,feature4,feature5]
data = np.array([[1,2,3,4,7],[5,6,7,8,9],[9,10,11,12,13],[5,5,5,5,5],[5,7,5,5,-6]])
#result = [data1,data2,data3,data4]
result = [6,-8,-1,-5,8]
#weighting of each feature(1~5)
w = np.array([0,0,0,0,0])#is vector, not list
#max iteration
max_iter = 20

#calculate false number
def _calc_false(vec):
    false_num = 0
    f = 0
    for feature in data:
        h = np.dot(vec.T, feature)
        if np.sign(result[f]) != np.sign(h):
            false_num += 1
        f = f + 1
    return false_num

#initial value
least_false = _calc_false(w)
pocket_w = w
print 'Initial pocket_w: %r' % w
print 'Initial least false num: %d' % least_false

#pocket algorithm
f = 0
for i in xrange(max_iter):
    print 'Iteration %d:' % i
    feature = random.choice(data)
    t = np.dot(w.T,feature)
    if np.sign(result[f]) != np.sign(t):
        h = w + result[f] * feature
        h_false = _calc_false(h)
        w = h
        if h_false <= least_false:
            least_false = h_false
            pocket_w = h
            print 'Find better pocket_w!'
            print 'pocket_w: %r' % h
            print 'least false num: %d' % h_false
            
print 'Final pocket_w: %r' % pocket_w
print 'Final least false num: %d' % least_false