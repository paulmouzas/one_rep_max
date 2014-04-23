e = 2.71828
def epley(w, r):
    return int(w*(1+r/30))

def brzycki(w, r):
    return int(w * (36.0/(37.0-r)))

def lombardi(w, r):
    return int(w*r**0.1)
    
def mayhew(w, r):
    return int((100*w)/(52.2+(41.9*e**(-0.055*r))))

def lander(w, r):
    return int((100*w)/(101.3-2.67123*r))
    
def oconner(w,r):
    return int(w*(1+0.025*r))
    
def wathan(w,r):
    return int((100*w)/(48.8+53.8*e**(-0.075*r)))