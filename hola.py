def pertenece (s:list[int], e:int) -> bool:
    i:int = 0
    while i < len (s) and e != s[i]:
        i+=1
    
    return i < len (s)

def divide_a_todos (s:list[int], e:int) -> bool:
    i:int=0
    while i < len(s) and (s[i] % e) == 0:
        i+=1
    return i == len (s)


def suma_total (s:list[int]) -> int:
    i:int = 0
    n:int = 0
    while n < len(s):
        i += s[n]
        n += 1
    
    return i

def ordenados (s:list[int]) -> bool:
    i:int = 0
    while i < len(s)-1 and s[i]<s[i+1]:
        i+=1
    
    return i == len(s)-1

##ejercicio 5
def palabra_larga (s:list[str]) -> bool:
    i:int = 0
    while i < len (s) and len(s[i])<=7:
        i+=1
    
    return i < len(s)

##ejercicio 6
def palindromo (s:str) -> bool:
    i:int = 0
    if len (s)%2 == 0:
        while s[i] == s[len(s)-1-i] and len (s)/2 >= i:
            i+=1
        return i==(len(s)/2)+1
    else: 
        while s[i] == s[len(s)-1-i] and (len (s)+1)/2 > i:
            i+=1
        return i== (len(s)+1)/2
    
##def contraseña (s:str) -> str:
    ##if len (s) < 5:
    ##    return "ROJA"
    ##elif len (s) > 8:
   ## else: 
     ##   return "AMARILLA"

def saldo (s:list[(chr,int)]) -> int:
    i:int = 0
    for (x,y) in s:
        if x == 'I':
            i += y
        if x == 'R':
            i = i-y
    return i


def vocales (s:str) -> bool:
    cantidad:int = 0
    n:list[str] = ['a','e','i','o','u','A','E','I','O','U']
    for char in s:
        if pertenece (n,char):
            cantidad += 1
            n.remove(char)
    return cantidad>=3

def pertenece (s:list, e) -> bool:
    i:int = 0
    while i < len (s) and e != s[i]:
        i+=1
    
    return i < len (s)

def borrar_pares (s:list[float]) -> None:
    for i in range (0,len(s),2):
        s[i]=0

def borrar_pares_nuevo (s:list[float]) -> list[float]:
    n:list[float] = []
    for i in range (0,len(s)):
        if i%2 == 0:
            s[i]=0
            n.append(s[i])
        else:
            n.append(s[i])
    return n

print (borrar_pares_nuevo([1,2,3,4]))

def borrar_vocales (s:list[chr]) -> str:
    n:list = ['a','e','i','o','u','A','E','I','O','U']
    for char in s:
        if pertenece (n,char):
            s.remove(char)
    return s

print (borrar_vocales(['h','o','l','a']))

def reemplaza_vocales (s:list[chr]) -> list [chr]:
    n:list = ['a','e','i','o','u','A','E','I','O','U']
    for i in range(0,len(s)):
        if pertenece (n,s[i]):
            s[i]='-'
    return s

print (reemplaza_vocales(['a','b','c','a','i','r']))

def da_vuelta_str (s:list[chr]) -> list[chr]:
    n:list[chr] = []
    for i in range(len(s)-1,-1,-1):
        n.append(s[i])
    return n 

print (da_vuelta_str(['h','o','l','a']))

def eliminar_repetidos (s:list[chr]) -> list[chr]:
    for char in s:
        if s.count(char) > 1:
            s.remove(char)
    return s

## OTRA FORMA SIN REMOVE
def eliminar_repetidos_2 (s:list[chr]) -> list[chr]:
    n:list[chr]=[]
    for char in s:
        if not (pertenece (n,char)):
            n.append(char)
    return n

print (eliminar_repetidos_2 (['h','h','h','o','h','l','a','a']))

def aprobado (s:list[int]) -> int:
    res:int = None
    if promedio (s) >= 7 and not(menor_a_4(s)):
        res = 1
    elif not (menor_a_4 (s)):
        res = 2
    else:
        res = 3
    return res

def promedio (s:list[int]) -> int:
    prom:int = 0
    for nota in s:
        prom += nota
    return prom/len(s)

def menor_a_4 (s:list[int]) -> bool:
    res:bool = False
    for i in range(0,len(s)):
        if s[i]<4:
            res = True
    return res

def nombres () -> list[str]:
    n:list[str] = []
    s = input ("hola")
    while s != "listo":
        n.append(s)
        s = input("chau")
    return n

def pertenece_a_cada_uno (s:list[list[int]],e:int,res:list[bool]) -> None:
    for n in range(0,len(s)):
        if pertenece (s[n],e):
            res.append(True)
        else:
            res.append(False)

res = []
pertenece_a_cada_uno ([[1,2],[3,4],[2,3],[5,6],[3,8]],3, res)
print(res)

