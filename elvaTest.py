import array as arr
"Iniciamos con la matriz que genera un array con los números enteros con un while para dejar el código mas limpio y escalable"
"We start with the matrix that generates an array with the integers with a while to leave the code cleaner and more scalable"
def matriz():  
    arr.testingnumber = []
    i = 0   
    while i <= 9:
        arr.testingnumber.append(i) 
        i+= 1  
        "-----TARGET------"
    target = 13
    return target, arr.testingnumber   
"A Continuación obtenemos los datos del target y del array con los enteros"
"Next we get the data from the target and the array with the integers"
target, arr.testingnumber = matriz()
count = -1
"Generamos el array donde inyectaremos los numeros los cuales su suma da como resultado el target"
"We generate the array where we will inject the numbers whose sum results in the target"
arr.sumnumber = []
"Depuramos los datos del target para poder hacer una validación sencilla con un for"
"We purge the target data to be able to do a simple validation with a for"
if target % 2 == 0:
    result = target / 2
    result1 = result + 1
    result2 = result - 1
else:
    result = target / 2
    result1 = result + .5
    result2 = result - .5
targetRes1 = round(result1)
targetRes2 = round(result2)
"Realizamos un rastreo de los datos del array para ver cuales son los números dentro de ella que sumándolos dan como resultado el target"
"We perform a scan of the array data to see which are the numbers within it that, adding them, result in the target"
for x in arr.testingnumber:
   if arr.testingnumber[x] == targetRes1:
    arr.sumnumber.append(arr.testingnumber[x])
   if arr.testingnumber[x] == targetRes2:
    arr.sumnumber.append(arr.testingnumber[x])
   count += 1
print('Index1 numeros a comparar ',arr.testingnumber)
print('Index2 numeros que al sumar dan como resultado el target',arr.sumnumber)










   








