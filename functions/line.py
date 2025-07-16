import sys

class Line:
    
        
    def __init__(self):
        pass

    def getCommand(self,name = "",callback = None):
        if name != "":
            prop = self.getProperty(name)
            if prop is not None:
                callback(prop)
            
            
            

    def getProperty(self,name = ""):
        indice =  sys.argv.index(name) if name in sys.argv else False
        if indice is not False:
            property = sys.argv[indice+1] if len(sys.argv) > indice + 1 else False
            return property if property is not False else False
     

    def getTwoProperty(self,name="",callback=None): 
        self.getCommand(name,lambda value: callback((name,value)))
    
    def getTwoCommand(self,name= "",callback = None):
        if name != "":
            self.getCommand(name,lambda value: self.getTwoProperty(value,callback))
            
    

            

        
        