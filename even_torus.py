from gekko import GEKKO
m = GEKKO()
m.clear()
y = m.Array(m.Var,6,lb=0,ub=1)
#yR,yC,yD0,yA0,yD1,yA1, = y

z = m.Array(m.Var,64,lb=0,ub=1)

R = 0
C = 1
D0 = 2
A0 = 3
D1 = 4
A1 = 5

#z0,zR,zC,zD,zA,zRC,zRD,zRA,zCD,zCA,zDA,zRCD,zRCA,zCDA,zRDA,zRCDA = z

#2^4 2^5 BD,BA
#2^2 2^3 RD,RA

#helper to filter out non-zero z varibles
def isRedBlueZ(j):
    return (((j & 2**D1) and (j & 2**D0)) or ((j & 2**D1) and (j & 2**A0))
            or ((j & 2**A1) and (j & 2**D0)) or ((j & 2**A1) and (j & 2**A0)))

#is z a compatable Diagonal/AntiDiagonal 
def isRedRedZ(j):
    return ((j & 2**D1) and (j & 2**A1)) or ((j & 2**D0) and (j & 2**A0))

#is y a compatable Diagonal/AntiDiagonal 
def isRedRedY(a,b):
    return (a == D1 and b == A1) or (a == D0 and b == A0)

for i in range(6):
    zS = [z[j] for j in range(64) if (2**i & j) and not isRedBlueZ(j) ]    
    m.Equation(m.sum(zS) == y[i])

for i in range(64):
    if isRedBlueZ(i):
        m.Equation(z[i] == 0)


m.Equation(y[2] <= 1/2)
m.Equation(y[3] <= 1/2)
m.Equation(y[4] <= 1/2)
m.Equation(y[5] <= 1/2)

m.Equation(m.sum(z) == 1)

#set z vriables of impossible regions to 0
zRB = [z[j] for j in range(64) if isRedBlueZ(j)]
m.Equation(m.sum(zRB) == 0)

pairs = [(a,b) for a in range(6) for b in range(6) if a < b ]

for a,b in pairs:
    zS = [z[j] for j in range(64) if ((2**a & j) and ( 2**b & j))]
    if(isRedRedY(a,b)):
       m.Equation(m.sum(zS) == 2*y[a]*y[b])
    else: 
        m.Equation(m.sum(zS) == y[a]*y[b])

#m.Maximize(m.min2(z[3 | 2**4 | 2**5 ] + z[3 | 2**2 | 2**3 ], z[0]))
m.Equation(z[3 | 2**4 | 2**5 ] + z[3 | 2**2 | 2**3 ] >= z[0])

m.Maximize(z[0])
m.options.SOLVER=3 #IPOPT
m.solve()
print("*****")
print("Theorem 1.2 t(n_even) <= ", z[0][0],"n^2") 
print("*****")
print("")


print("***** Validating UPPER BOUND *****")
try:
    m.Equation(z[0] > 0.14014)
    m.solve()
except: print("better solution does not exist")
