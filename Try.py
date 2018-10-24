class Section:
    def __init__(self, secA_, secB_, secC_):
        self.secA = secA_
        self.secB = secB_
        self.secC = secC_

    def secAVal(self):
        return self.secA

    def secBVal(self):
        return self.secB

    def secCVal(self):
        return self.secC

class Path:
    def __init__(self):
        self.path = list()

    def pathPrint(self):
        print(self.path)
    
    def pathAppend(self, path_):
        self.path.append(path_)

    def getPath(self):
        return self.path

    def setPath(self, path_):
        self.path = path_

def optimalPath(pathPair, section): 
    pathA = pathPair[0]
    pathB = pathPair[1]
    
    totalA = 0
    totalB = 0
    for v in pathA.getPath():
        totalA += v[1] 
    for v in pathB.getPath():
        totalB += v[1]

    toAFromA = totalA + section.secAVal()
    toAFromB = totalB + section.secBVal() + section.secCVal()
    toBFromA = totalA + section.secAVal() + section.secCVal()
    toBFromB = totalB + section.secBVal()
    
    newPathToA = list()
    newPathToB = list()

    if toAFromA <= toAFromB:
        newPathToA += pathA.getPath()
        newPathToA.append(('A', section.secAVal()))
    else:
        newPathToA += pathB.getPath()
        newPathToA.append(('B', section.secBVal()))
        newPathToA.append(('C', section.secCVal()))

    if toBFromA <= toBFromB:
        newPathToB += pathA.getPath()
        newPathToB.append(('A', section.secAVal()))
        newPathToB.append(('C', section.secCVal()))
    else:
        newPathToB += pathB.getPath()
        newPathToB.append(('B', section.secBVal()))
    
    pathA.setPath(newPathToA)
    pathB.setPath(newPathToB)
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
    pathA.pathPrint();
    pathB.pathPrint();

main()
