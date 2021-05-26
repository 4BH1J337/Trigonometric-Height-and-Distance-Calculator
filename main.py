
import math
print(2* '\n')#Line Space
print('            TRIGONOMETRIC HEIGHT & DISTANCE CALCULATOR')
print(3* '\n')
Ask=int(input(" To Calculate Distance Enter [ 1 ], To Calculate Height Enter [ 2 ] --> "))# varible assinged to ask

if Ask == 1:
    print('\n')#Line Space
    print(' Distance calculation:')
    print('\n')
    
    AngleX=float(input(" >>> Enter the Angle = "))# varible assing for Angle
    
    Opposite=float(input(" >>> Enter the Height/Opposite side = "))# varible assing for Height
    
    Tan = math.tan(math.radians(AngleX)) #Getting tan theta of Give Angle
    
    Distance=Opposite/Tan #Calculating Adjacent side
    
    print(1* '\n')#Line Space
    print(' Results :')
    print('\n')
    
    print(" >>> tan of given angle  = ",round(Tan,3)) # Round for round figure
    print(" >>> Distance/Adjacent side = ",round(Distance,3)) # Round for round figure
    print(2* '\n')
    
    close=str(input("            -----------PRESS ENTER TO CLOSE ---------"))

elif Ask == 2:
    print('\n')
    print(' Height calculation:')
    print('\n')#Line Space
    
    AngleX=float(input(" >>> Enter the Angle = "))# varible asing for Angle
    
    Adjacent=float(input(" >>> Enter the Distance/Adjacent side = "))# varible asing for distance
    
    Tan = math.tan(math.radians(AngleX)) #Getting tan theta of Give Angle
    
    Height=Adjacent*Tan #Calculating Opposite side
    
    print(1* '\n')
    print(' Results :')
    print('\n')
    
    print(" >>> tan of given angle  = ",round(Tan,3)) # Round for round figure
    print(" >>> Height of Object/Opposite side = ",round(Height,3))# Round for round figure
    print(2* '\n')#Line Space
    
    close=str(input("           -----------PRESS ENTER TO CLOSE ---------"))
else:
    print(3* '\n')
    print("      Invalid Key !! ")
    print(2* '\n')
    close=str(input("           -----------PRESS ENTER TO CLOSE ---------"))
    





 







