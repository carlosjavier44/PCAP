try: 
    y = 1/0
    
except (ZeroDivisionError,ArithmeticError):
    print("Hubo un problema al hacer la operación")
    
except:
    print("Algo no va bien...")
    
print("FIN.")