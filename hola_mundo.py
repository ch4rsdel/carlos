#instalar bpython
'''
print "hola Mundo"

print "te quiero"
'''
#for i in xrange(0,5):
#	print "barbara barbarosa",i

#listas
#frutas = ['manzana','pera']
#numeros = range(1,20)

#print frutas

#conjuntos se pueden hacer todas las operaciones 

 #con1 = set ([2,3,7,9])
#con2 = set ([1,2,7,10])

#print con1

#condicional
'''
x = 0

if type(x) is int:
	
	if x < 0:
		print "negativo"
	elif x > 0:
		print "positivo"
	else:
		print "cero"
'''
'''	
num = raw_input("introduce un numero")

print num
'''

'''
import math

def exacta(x):
	y = math.sqrt(x)
	
	if int(y)==y:
		return True
	else:
		return False

def f(x):
	if x%2 is 0:
		y = True
	else:
		y = False
	return y
	
	
print [x for x in xrange(1, 100) if not f(x) and exacta(x)]	
	'''
# reduce recibe dos parametros	
#print reduce(lambda x,y:x+y,[1,2,3,4,5])	
#map solo recibe un parametro
#print map(lambda x:x*2,[1,2,3,4,5])

'''
def f(x):
	if x%2 ==0:
		return True
	return False #asi es como un else
	
print filter(lambda x:f(x),[1,2,3,4,5])	'''

import pdb 
for i in xrange(1, 10):
	pdb.set_trace()
	print i%2==0 and "es par" or (i==3 and "es tres" or "no se que es")
	
	
#para pdb	
'''
l: linEA ACTUAL 
n: next line
q:quit
c: continue
w: revision de llamadas
'''	



 
