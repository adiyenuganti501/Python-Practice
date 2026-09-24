from myPack import calc
from myPack import server
val = calc.sum(2,9)
print(calc.sub(3,1))
print(calc.mul(2,3))
print(val)

print("===========")
server.server_start()
print("Execution process")
server.server_stopped()