#Uncomment line above & run cell to save solution
#TODO Define class that implements positionInterface & allows for the management of a position

import os
import sys
from implementations.securitySolution import security, securityInterface
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
    
class positionInterface():
    def __init__(self, security, initialPosition: int) -> None:
        pass

    def getSecurity(self) -> securityInterface:
        pass

    def getPosition(self) -> int:
        pass
    
    def setPosition(self, inputValue: int) -> None:
        pass
    
    def addPosition(self, inputValue: int) -> None:
        pass
    
class position(positionInterface):
    thesecurity:security = security('')
    position:int = 0

    def __init__(self, asecurity, initialPosition: int) -> None:
        super().__init__(asecurity, initialPosition)
        
        ## security is either a string of the security or the security itself
        if isinstance(asecurity, str) : 
            self.thesecurity = security(asecurity)
        else:
            self.thesecurity = asecurity
            
        ##setting Position
        self.position = initialPosition
        
    def getSecurity(self) -> securityInterface:
        return self.thesecurity

    def getPosition(self) -> int:
        return self.position
    
    def setPosition(self, inputValue: int) -> None:
        self.position = inputValue
        if self.position < 0 :
            raise Exception("Position is below 0")  # Raise Erro
        
        
    def addPosition(self, inputValue: int) -> None:  
        self.position += inputValue
        if self.position < 0 :
            raise Exception("Position is below 0")  # Raise Erro
        