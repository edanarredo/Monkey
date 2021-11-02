def generate_processes():
   # For 10,000 processes
   for i in range(0, 10000):
      old_clock = clock  
      event = event.getEvent()
      
      # Switch statement for event type(?)
      match event:
         case 1:
            return 1
         case 2:
            return 2
         case 3:
            return 3
         case 4:
            return 4
         case _: 
            return 5 
         
def caseResolve():
   print("This is a monkey haha")