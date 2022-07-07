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
        self.the_accountName = str(accountName)
        self.the_positions = set(positions)
        
    def getName(self) -> str:
        return self.the_accountName

    def getAllPositions(self) -> Iterable[positionInterface]:
        return self.the_positions
    
    ## KEY_LIST = [security("TEST_SEC_A"), "TEST_SEC_B", "TEST_NOT_FOUND_STR", security("TEST_NOT_FOUND_POS")]
    ## return name and postion
    def getPositions(self, securities: Set) -> Dict[Any, positionInterface]:
        ans_dict = {}
        # Iterating all positions
        for a_position in self.the_positions:
            # Iterating all query values
            for securityset in securities:
                ## security is either a string of the security or the security itself
                if isinstance(securityset, str) : 
                    if securityset == a_position.getSecurity().getName():
                        ans_dict[securityset] = a_position
                    ##else:
                        ##ans_dict[securityset] = "NOT_FOUND"
                else:
                    if securityset.getName() == a_position.getSecurity().getName():
                        ans_dict[securityset] = a_position
                    ##else:
                        ##ans_dict[securityset] = "NOT_FOUND"
        
        #print (ans_dict)
        
        # EXPECTED_MAP = {
        #     KEY_LIST[0] : position("TEST_SEC_A", 1000),
        #     KEY_LIST[1] : position("TEST_SEC_B", 2000),
        # }
        return ans_dict

    def addPositions(self, positions: Set[positionInterface]) -> None:
        temp_update = set()
        
        # Iterating all positions
        for a_position in self.the_positions: 
            
            # Iterating all new positions
            for new_position in positions: 
                temp_update.add(a_position)
                
                ## if same name, then update, if new add to adder
                if new_position.getSecurity().getName() == a_position.getSecurity().getName():
                    if a_position in temp_update:
                        temp_update.remove(a_position)
                    temp_update.add(new_position)
                else:
                    temp_update.add(new_position)
                               
        self.the_positions = set(temp_update)
                    
    def removePositions(self, securities: Set) -> None:
        temp_update = set(self.the_positions)
        
        # Iterating all positions
        for a_position in self.the_positions: 
            
            # Iterating all new positions
            for a_security in securities: 
                
                ## if same name, then update, if new add to adder
                if a_position.getSecurity().getName() == a_security.getName():
                    temp_update.remove(a_position)
                    
        self.the_positions = set(temp_update)