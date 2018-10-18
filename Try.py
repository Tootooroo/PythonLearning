class Section:
    secA = ''
    secB = ''
    secC = ''

    def __init__(self, secA_, secB_, secC_):
        self.secA = secA_
        self.secB_ = secB_
        self.secC_ = secC_

    def secAVal(self):
        return self.secA

    def secBVal(self):
        return self.secB

    def secCVal(self):
        return self.secC

class Path:
    path = ''

    def __init__(self):
        self.path = list()

    def pathPrint(self):
        print(self.path)
    
    def pathAppend(self, path_):
        self.path.append(path_)

def optimalPath(pathPair, section): 
    pathA = pathPair[0]
    pathB = pathPair[1]
    
    totalA = ''
    for v in pathA:
        totalA += v[1] 

    totalB = ''
    for v in pathB:
        totalB += v[1]

    toAFromA = ''
    toAFromA = totalA + section.secAVal()
    toAFromB = ''
    toAFromB = totalB + section.secBVal() + section.secCVal()
    toBFromA = ''
    toBFromA = totalA + section.secAVal() + section.secCVal()
    toBFromB = ''
    toBFromB = totalB + section.secBVal()

    if toAFromA < toAFromB:
        pathA.pathAppend(('A', section.secAVal()))
    else:
        pathA.pathAppend(('B', section.secBVal()))
        pathA.pathAppend(('C', section.secCVal()))

    if toBFromA < toBFromB:
        pathB.pathAppend(('A', section.secAVal()))
        pathB.pathAppend(('C', section.secCVal()))
    else:
        pathB.pathAppend(('B', section.secBVal()))
        
    return (pathA, pathB)

def main():
    pathA = Path()
    pathB = Path()
    secArray = [ 
        Section(50, 10, 30), Section(5, 90, 20),     
        Section(40, 2, 25), Section(10, 8, 0)
    ]
    for sec in secArray:
        optimalPath((pathA, pathB), sec)

