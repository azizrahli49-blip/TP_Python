from timeit import timeit

def fibonacci_recursif(n):
    """
    Fonction récursive qui permet à partir d'un rang n de retourner sa valeur de la suite de Fibonacci à ce rang
    Entreé: entier positif
    Sortie: entier positif
    >> fibonacci_recursif(0) retourne 0
    >> fibonacci_recursif(5) retourne 5
    >> fibonacci_recursif(10) retourne 55
    >> fibonacci_recursif(-4) retourne ValueError
    """
    if n<0 :
        raise ValueError("La valeur entrée soit être positive")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci_recursif(n-1)+fibonacci_recursif(n-2)

def fibonacci_iteratif(n):
    '''
    Fonction récursive qui permet à partir d'un rang n de retourner sa valeur de la suite de Fibonacci à ce rang
    Entreé: entier positif
    Sortie: entier positif
    >> fibonacci_recursif(0) retourne 0
    >> fibonacci_recursif(5) retourne 5
    >> fibonacci_recursif(10) retourne 55
    '''
    resultat=0
    nombre1=0
    nombre2=1
    for i in range(n):
        resultat=nombre2+nombre1
        nombre2,nombre1=nombre1,resultat
    return resultat

def cache(fonction):
    '''
    Fonction cache de l'exercice 2
    '''
    dict={}
    def wrapper(parametre):
        if parametre in dict.keys():
            return dict[parametre]
        else:
            dict[parametre]=fonction(parametre)
            return dict[parametre]
    return wrapper
@cache
def fibonacci_cache(n):
    if n < 0:
        raise ValueError("La valeur entrée soit être positive")
    elif n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci_cache(n-1)+fibonacci_cache(n-2)

def main() :
    '''
    Mesure du temps d'exécution de la fonction fibonnacci_recurcive pour n=35 et n=36
    >> pour n=35 on obtient 5,11 secondes
    >> pour n=36 on obtient 8,11 secondes
    Nous remarquons que le temps de calcul augmente considérablement entre les n+1
    '''
    print(f"Pour n =35 avec la fonction récurcive : {timeit('fibonacci_recursif(35)', globals=globals(), number=1)} ")
    print(f"Pour n =36 avec la fonction récurcive : {timeit('fibonacci_recursif(36)', globals=globals(), number=1)} ")

    '''
    Mesure du temps d'exécution de la fonction fibonnacci_itératif pour n=35 et n=36
    >> pour n=35 on obtient 7,9.10^(-6) secondes
    >> pour n=36 on obtient 6,0.10^(-6) secondes
    Nous remarquons que le temps de calcul est nettement plus rapide puisque la fonction n'a plus besoin d'être appeler plusieurs fois
    '''
    print(f"Pour n =35 avec la fonction itérative : {timeit('fibonacci_iteratif(1)', globals=globals(), number=1)} ")
    print(f"Pour n =36 avec la fonction itérative : {timeit('fibonacci_iteratif(36)', globals=globals(), number=1)} ")

    '''
    Mesure du temps d'exécution de la fonction fibonnacci_cache pour n=35 et n=36
    >> pour n=35 on obtient 1,4.10^(-4) secondes
    >> pour n=36 on obtient 8,9.10^(-6) secondes
    Nous remarquons que me cache permet de réduire considérablement le temps de calcul, puisqu'il ne fait plus 
    appel à la fonction récursive à chaque étape mais récupére le résultat dans le cache s'il a déjà été 
    calculé. Il semblerait que la vitesse d'exécution tende à être aussi rapide qu-avec la fonction itérative.
    '''
    print(f"Pour n =35 avec la fonction itérative utilisant le cache : {timeit('fibonacci_cache(35)', globals=globals(), number=1)} ")
    print(f"Pour n =36 avec la fonction itérative utilisant le cache : {timeit('fibonacci_cache(36)', globals=globals(), number=1)} ")


main()