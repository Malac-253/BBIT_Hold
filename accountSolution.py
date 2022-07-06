#Uncomment line above & run cell to save solution
#TODO Define class that implements accountInterface & allows for the management of an account

import os
import sys
from implementations.securitySolution import security, securityInterface
from implementations.positionSolution import position, positionInterface
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

#from positionInterface import positionInterface
from typing import Any, Dict, Set, Iterable



class accountInterface():
    def __init__(self, positions: Set[positionInterface], accountName: str) -> None:
        pass

    def getName(self) -> str:
        pass

    def getAllPositions(self) -> Iterable[positionInterface]:
        pass

    def getPositions(self, securities: Set) -> Dict[Any, positionInterface]:
        pass

    def addPositions(self, positions: Set[positionInterface]) -> None:
        pass
    
    def removePositions(self, securities: Set) -> None:
        pass
    
    
class account(accountInterface):
    the_positions:set = {}  
    the_accountName:str = 'unnamed'

    def __init__(self, positions: Set[positionInterface], accountName: str) -> None:
        super().__init__(positions, accountName)
        self.the_accountName = accountName
        self.the_positions = positions
        
    def getName(self) -> str:
        return self.the_accountName

    def getAllPositions(self) -> Iterable[positionInterface]:
        print(self.the_positions)
        return self.the_positions
    
    ## KEY_LIST = [security("TEST_SEC_A"), "TEST_SEC_B", "TEST_NOT_FOUND_STR", security("TEST_NOT_FOUND_POS")]
    ## return name and postion
    def getPositions(self, securities: Set) -> Dict[Any, positionInterface]:
        
        ans_dict = {}
        
        # Iterating all positions
        for a_position in the_positions:
            # Iterating all query values
            for securityset in securities:
                ## security is either a string of the security or the security itself
                if isinstance(securityset, str) : 
                    if securityset == a_position.getSecurity.getName():
                        ans_dict[a_position.getSecurity.getName()] = a_position    
                else:
                    if securityset == a_position.getSecurity():
                        ans_dict[a_position.getSecurity.getName()] = a_position

        return ans_dict

    def addPositions(self, positions: Set[positionInterface]) -> None:
        pass
    
    def removePositions(self, securities: Set) -> None:
        pass