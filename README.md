I don't know if I translated correctly ,because my English is bad.

# python_view_variable
View variable name and methods in python.

# Copy the "view" function below ,and paste to your python.

    def view(variable, display=True):
        myIdNAME = 0
        myFIND = globals().copy().keys()
        myID = id(variable)
        
        for i in myFIND:
            if id(globals()[i]) == myID :
                myIdNAME = i
                break
        
        myFIND = dir(variable)
        
        if display :
            print("Variable Name : \" {}".format(myIdNAME)+" \"\n")
            print("Value : \" {}".format(variable)+" \"\n")
            print("Methods and Result : \n")      
            for i in myFIND :  
                print(i)
                print(eval(myIdNAME+"."+i))
                print("\n")   
            
        return [myIdNAME, list(myFIND)] 
    
# You can run likes this : 
    H = b"123"
    view(H)
    
# Get the Variable Name and Methods :
    A = "hello"
    name, methods = view(A,False)
    print(name)
    print(methods)
    
# You can follow the url below to test it in colab.  
https://github.com/wayne931121/python_view_variable/blob/main/View_Variable_Colab.ipynb
