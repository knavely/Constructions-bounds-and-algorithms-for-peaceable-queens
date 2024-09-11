from gekko import GEKKO
m = GEKKO()
m.clear()
y = m.Array(m.Var,4,lb=0,ub=1)
#yR,yC,yD,yA = y

z = m.Array(m.Var,16,lb=0,ub=1)

R = 0
C = 1
D = 2
A = 3

#z0,zR,zC,zD,zA,zRC,zRD,zRA,zCD,zCA,zDA,zRCD,zRCA,zCDA,zRDA,zRCDA = z

for i in range(4):
    zS = [z[j] for j in range(16) if (2**i & j)]    
    m.Equation(m.sum(zS) == y[i])

pairs = [(a,b) for a in range(4) for b in range(4) if a < b ]

for a,b in pairs:
    zS = [z[j] for j in range(16) if ((2**a & j) and ( 2**b & j))]
    m.Equation(m.sum(zS) == y[a]*y[b])


m.Equation(m.sum(z) == 1)
m.Equation(z[2**R | 2**C | 2**D | 2**A] >= z[0])

#m.Maximize(m.min2(z[2**R | 2**C | 2**D | 2**A], z[0]))
m.Maximize(z[0])


m.options.SOLVER=3
m.solve()

print("*****")
print("Theorem 1.4 t(n_odd) <= ", z[0][0],"n^2")
print("*****")
print("")
#RD,RA, BD, BA for even
