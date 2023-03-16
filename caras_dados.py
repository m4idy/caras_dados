n = int(input("ingrese el número de la cara: "))

if n==1 :

    rta = "La cara contraria es: 6"

else :
    if n==2 :

        rta = "La cara contraria es: 5"

    else :
        if n==3 :

            rta = "La cara contraria es: 4"

        else :
            if n==4 :

                rta = "La cara contraria es: 3"

            else :
                if n==5 :

                    rta = "La cara contraria es: 2"

                else:
                    if n==6 :

                        rta = "La cara contraria es: 1"

                    else :

                        rta = "no es una cara del dado "

print(rta)