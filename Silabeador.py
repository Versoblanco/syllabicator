#coding=UTF-8
# División silábica en español (Quilis, Tratado de fonética y fonología, p. 368 y ss.)
# V=vocal C = consonante. Estructura básica CV
# 1. VCV = V-CV
# 2. VCCV = a) VC-CV b) V-CCV (p, b, f, g, k + r, l / dr, tr)
# 3. VCCC(C)V = a)VCC (ns, bs) - CV b)VC-CCV (C + l, r) cons- truir an-sie-dad
# 4. VV = a) V-V (abiertas, abierta + cerrada tónica, cerrada tónica + abierta) b) VV (cerradas, abierta+cerrada átona, cerrada átona + abierta)
# La consonante no puede ser núcleo ni constituir sílaba por sí misma.
# prefijos = sub

consonantes =  map(lambda word: unicode(word, 'utf-8'), ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'])
vocales =map(lambda word: unicode(word, 'utf-8'), ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'ü'])
inseparables = map(lambda word: unicode(word, 'utf-8'), ['ch', 'll', 'rr', 'pr', 'pl', 'br', 'bl', 'fr', 'fl', 'gr', 'gl', 'kr', 'cr', 'kl', 'cl', 'dr', 'tr'])
vcerradas = map(lambda word: unicode(word, 'utf-8'),['i', 'u', 'ü'])

def es_vocal(letra):
  return letra in vocales

def es_consonante(letra):
  return letra in consonantes

def es_inseparable(letra1, letra2):
  if not letra1 or not letra2:
    return False
  return letra1+letra2 in inseparables

def es_diptongo(letra_anterior, letra):
  return letra in vcerradas or letra_anterior in vcerradas

def buscar_letra_anterior(palabra, index):
  return palabra[index-1]

def buscar_letra_siguiente(palabra, index):
  if index == len(palabra)-1:
    return '_'
  else:
    return palabra[index+1]
    
def pedir_palabra():
  while True:
    palabra = raw_input('Escriba la palabra (exit para salir): ').decode('utf-8')
    if palabra == 'exit':
      print 'Adiós'   
      exit()
    if len(palabra) > 0:
      return palabra
      break  
    
while True:
    
  palabra = pedir_palabra()  
  palabra = palabra.lower()
  silaba = palabra[0]
  
  for index, letra in enumerate(palabra):
    
    if index==0:
      continue
  
    letra_anterior = buscar_letra_anterior(palabra, index)
    letra_siguiente = buscar_letra_siguiente(palabra, index)
    
    if es_vocal(letra) and es_consonante(letra_anterior):
      silaba=silaba+letra
      
    elif es_vocal(letra) and es_vocal(letra_anterior):
      
      if es_diptongo(letra_anterior, letra):
        silaba=silaba+letra
      else:
        print silaba
        silaba = palabra [index]
        
    elif es_consonante(letra):
    
      if es_inseparable(letra_anterior, letra):
        silaba=silaba+letra
        
      elif es_inseparable(letra, letra_siguiente) or es_vocal(letra_siguiente):
        print silaba
        silaba = palabra [index]
          
      else:
        silaba=silaba+letra
        
    else:
      print 'Palabra no válida'
      break 
    
  print silaba

#silabeo= []
#for silaba in silabeo:
#  ' - '
#print 'cc: ' + letra_anterior + ' ' + letra + "\n"

		
