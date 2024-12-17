try: 
    y = 1/0
    
except ZeroDivisionError:
    print("¡División entre cero!")

except ArithmeticError:
    print("¡Problema aritmético!")
    
except:
    print("Algo no va bien...")
    
print("FIN.")