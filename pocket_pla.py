import numpy as np

def pocket_pla(datas, limit):
    ###############
    def _calc_false(vec):
        res = 0
        for data in datas:
            t = np.dot(vec, data[0])
            if np.sign(data[1]) != np.sign(t):
                res += 1
        return res
    ###############
    w = np.random.rand(5)
    least_false = _calc_false(w)
    res = w

    for i in xrange(limit):
        data = random.choice(datas)
        t = np.dot(w, data[0])
        if np.sign(data[1]) != np.sign(t):
            t = w + data[1] * data[0]
            t_false = _calc_false(t)

            w = t

            if t_false <= least_false:
                least_false = t_false
                res = t
    return res, least_false