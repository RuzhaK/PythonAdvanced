try:
    open('text.txt')
    print('File exists')
except FileNotFoundError:
    print('File not found')

# alternativno:
import os.path
print('File exists'if os.path.exists('text.txt') else 'File not found')
# отваряме в байнъри режим:

f=open('text.txt', 'rb')
while(c:=f.read(1) !=b''):
    print(c)
# := towa e walrus operator - creates expression which assigns value as well
#  domashno 1:12
# f.readline() - chete celia red ili opredelen broi simvoli podadeni v skobite
# .find('some string)- vadi indexa v kadeto zapochwa stringa w texta, posle s daljinata mojem da widim i kade swarshwa
# result=_ - towa prisvoiava stoinostta na poslednia izraz
# primerno:
# list(range(3)) e [0,1,2]
# result=_    resultata  ste stane [0,1,2]
# f.seek(0) - vrashta kursora na nuleva pozicia
# towa pyk ste prochete 5 reda:
f.readlines(5)

