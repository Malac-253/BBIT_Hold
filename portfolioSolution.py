#Uncomment line above & run cell to save solution
#TODO Define class that implements portFolioInterface & allows for the management of a portfolio


import os
import sys
from implementations.securitySolution import security, securityInterface
from implementations.positionSolution import position, positionInterface
from implementations.accountSolution import account, accountInterface
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from typing import Any, Dict, Set, Iterable

class portfolioInterface():
    def __init__(self, portfolioName: str, accounts: Set[accountInterface]) -> None:
        pass

    def getAllAccounts(self) -> Iterable[accountInterface]:
        pass

    def getAccounts(self, accountNamesFilter:Set[str], securitiesFilter:Set) -> Iterable[accountInterface]:
        pass 

    def addAccounts(self, accounts: Set[accountInterface]) -> None:
        pass

    def removeAccounts(self, accountNames: Set[str]) -> None:
        pass
    
    
class portfolio(portfolioInterface):
    the_accounts:set = set() 
    the_portfolioName:str = 'unnamed'

    def __init__(self, portfolioName: str, accounts: Set[accountInterface]) -> None:
        super().__init__(portfolioName, accounts)
        self.the_portfolioName = str(portfolioName)
        self.the_accounts = set(accounts)
     
    # def getName(self) -> str:
    #     return self.the_portfolioName
    
    def getAllAccounts(self) -> Iterable[accountInterface]:
        return self.the_accounts
    
    ##FILTERED_ACCOUNTS = p.getAccounts(inputAccount, inputSecurity)
    
    
    def getAccounts(self, accountNamesFilter:Set[str], securitiesFilter:Set) -> Iterable[accountInterface]:
        ans_list = dict()
        ## GOAL is one Pass
        
        ## Looking at all accounts
        for an_account in self.the_accounts:
            
            ## Checking if names match
            if !(an_account.getName() in accountNamesFilter:
                ans_list[an_account] = False
            else:
                ans_list[an_account] = True 
            
            ##Looking at all the securities/position in the account
            for a_position in an_account.getAllPositions():
                
                if a_position.getSecurity() in securitiesFilter:
                    #ans_list.append(an_account) 
                    ans_list[an_account] = True
                    #break
                    
        return ans_list
             
    def addAccounts(self, accounts: Set[accountInterface]) -> None:
        
        temp_update = set()
        
        ## Looking at all accounts
        for an_account in self.the_accounts:
            
            ## Looking at all new accounts
            for new_account in accounts:
                
                temp_update.add(an_account)
                
                if new_account.getName() == an_account.getName():
                    if new_account in temp_update:
                        temp_update.remove(an_account)
                    temp_update.add(new_account)
                else:
                    temp_update.add(new_account)    
            
        self.the_accounts = set(temp_update)
        
        
        
    def removeAccounts(self, accountNames: Set[str]) -> None:
        temp_update = set(self.the_accounts)
        
        # Iterating all accounts
        for an_account in self.the_accounts: 
            
            # Iterating all bad accounts
            for account_Names in accountNames: 
                
                if account_Names == an_account.getName():
                    temp_update.remove(an_account)
                    
        self.the_accounts = set(temp_update)