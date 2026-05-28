def outer(): 
    print("Starting the outer funciton from here")
    
    def inner(): 
        print("Inner Function") 
 
    inner() 

    print("Ending of the outer funciton")
    inner()

outer() 