#Uncomment line above & run cell to save solution
#TODO Define class that implements securityInterface & allows for the management of a security
class securityInterface():
    def __init__(self, name: str) -> None:
        pass
    
    def getName(self) -> str:
        return "Implement Me!"

class security(securityInterface):
    security:str = "" 
    
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.security = name   
    
    def getName(self) -> str:
        return self.security