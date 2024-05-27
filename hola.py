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
    n:list = ['a','e','i','o','u','A','E','I','O','U']
    for i in s:
        if pertenece (n,i) == True:
            cantidad += 1
            n = n.remove(i)
    return cantidad>=3
