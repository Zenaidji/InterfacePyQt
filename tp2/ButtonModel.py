class ButtonModel():
    idle=1
    hover=2
    pressIn=3
    pressOut=4
  
    
    def __init__(self):
        self.stat=self.idle
        
        
        
    def action(self):
        print("action")
    
    
    
 
    def  enter(self):
        if (self.stat==self.idle):
             self.stat=self.hover
             #print("hover")
        elif self.stat==self.pressOut:
           #print("pressin")
            self.stat=self.pressIn
    
    
    
    def leave(self):
        if (self.stat==self.pressIn):
             self.stat=self.pressOut
             #print("pressout")
        elif self.stat==self.hover:
            #print("idle")
            self.stat=self.idle
            
            
    
    
    def press(self):
        if (self.stat==self.hover):
            # print("pressin")            
             self.stat=self.pressIn
      
    
    
    
    
    def release (self):
        if (self.stat==self.pressOut):
             self.stat=self.idle
        elif self.stat==self.pressIn:
            self.action()
            self.stat=self.hover
        
                
        
    
    
        