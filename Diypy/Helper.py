class Helper:

    import numpy as np

    def addpy(name):
        print(name + "py")

    def addanextrapy(name):
        print(name + ("py" * 10))

    def addanextrapy2(name,repeat):
        print(name + ("py" * repeat))
    
    def mytitle(name):
        return ("*" * 10) + (" " * 2) + name.upper() + (" " * 2)  +  ("*" * 10)