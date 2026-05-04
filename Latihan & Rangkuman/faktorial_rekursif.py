def faktporial_rekursif (n):
    if n == 0:
        return 1
    else:
        #bilangan n diklikan dengan faktorial dari n-1
        #contoh faktorial_rekursif(5) = 5 * faktorial_rekursif(4)

        return n * faktporial_rekursif(n-1)
    #contoh penggunaan
    print(faktporial_rekursif(5)) #output: 120
    