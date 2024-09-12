from gekko import GEKKO
m = GEKKO(remote=False)
m.clear()
y = m.Array(m.Var,64,lb=0,ub=1)
z = m.Array(m.Var,64,lb=0,ub=1)

R = 0
C = 1
D0 = 2
D1 = 3
A0 = 4
A1 = 5

O = [R,C]
X = [D0,D1,A0,A1]

m.Equation(m.sum(z) == 1 ) #sum z_S = 1

OX = O + X
for i in OX:
    zS = [z[j] for j in range(64) if (2**i & j) ]    
    m.Equation(y[2**i] == m.sum(zS)) #first equality y_x = 

pairs = [(a,b) for a in range(6) for b in range(6) if a != b and a < b ]

for a,b in pairs:
    zS = [z[j] for j in range(64) if ((2**a & j) and (2**b & j))]
    m.Equation(y[2**a | 2**b] == m.sum(zS))  #second y_{X \cap X'} =

#zR zC zD0 zD1 zA0 zA1
t = 0


m.Equation(y[2**R | 2**C] == y[2**R]*y[2**C]) #y_R\cap C = y_Ry_C

#m.Equation(y[2**D0 | 2**A0] <= y[2**D0]*y[2**A0]) #y_D0\cap A0 = y_D0y_A0

#m.Equation(y[2**D1 | 2**A1] <= y[2**D1]*y[2**A1]) #y_D1\cap A1 = y_D1y_A1

for o in O:
   for x in X:
        m.Equation((y[2**o]**2)/4 + m.if3(1/4 - y[2**x],0,1)*m.if3(2*m.sqrt(y[2**x])-y[2**o],0,1) * y[2**x | 2**o] <= y[2**o] * m.sqrt(y[2**x]))
        #m.Equation(m.if3(1/4 - y[2**x],0,1)*m.if3(1 - m.sqrt(2 - 4*y[2**x])-y[2**o],0,1)*y[2**o|2**x] <= y[2**o]/2 )
        #m.Equation((m.sqrt(2-4*y[2**x]) + y[2**o] - 1)**2 + 4*m.if3(1/4 - y[2**x],0,1)*m.if3(m.sqrt(2 - 4*y[2**x]) + y[2**o]-1,0,1)*y[2**o|2**x] <= 2*y[2**o])
     #   m.Equation(y[2**o | 2**x] <= y[2**o]*y[2**x]) #y_o\cap x <= y_oy_x' for o in O, x in X (X is X from paper, O is square)
        
        #m.Equation(m.if2(1/4 - y[2**x],0,1) * ((y[2**o] + 2*m.sqrt(y[2**x]) - 1) * m.abs2(y[2**o]+2*m.sqrt(y[2**x]) - 1))/4 <= y[2**x | 2**o])

        #m.Equation(m.if2(y[2**x] - 1/4,0,1) * m.if2(y[2**o] - m.sqrt(2-4*y[2**x]),0,1)*(y[2**x] - (1-m.sqrt(2-4*y[2**x]))/2) <= y[2**o | 2**x])

        #m.Equation(m.if2(y[2**x] - 1/4,0,1) * m.if2(m.sqrt(2-4*y[2**x])-y[2**o],0,1)*((y[2**o]*(1-m.sqrt(2-4*y[2**x]))/2)+(y[2**o]**2)/4) <= y[2**o | 2**x])
        
        #m.Equation((m.sqrt(2*y[2**D0]) + m.sqrt(2*y[2**A0])-1)* m.abs2(m.sqrt(2*y[2**D0]) + m.sqrt(2*y[2**A0])-1)/2 <= y[2**D0|2**A0])

        #m.Equation((m.sqrt(2*y[2**D1]) + m.sqrt(2*y[2**A1])-1)* m.abs2(m.sqrt(2*y[2**D1]) + m.sqrt(2*y[2**A1])-1)/2 <= y[2**D1|2**A1])

for a in [D0,A0]:
    for b in [D1,A1] :
        m.Equation(y[2**a | 2**b] == 0)

for x in X:
    m.Equation(y[2**x] <= 1/2)

m.Equation(z[2**R | 2**C | 2**D0 | 2**A0 ]+z[2**R | 2**C | 2**D1 | 2**A1] >= z[0])    
m.Maximize(z[0])
#m.Maximize(m.min2(z[15], z[0]))

m.options.SOLVER=1
#m.options.OTOL = 1e-12
#m.solver_options = ['tol 0.0000000001']
m.solve()


print("*****")
print("Theorem 1.5 a(n) <= ", z[0][0],"n^2") 
print("*****")
print("")


print("*****")
print("Validating no better solution found....") 
print("*****")
print("")
try:
    m.Equation(z[0] > 0.172)    
    m.solve()
except: print("better solution does not exist")

def printsol(sol,name):
    for i in range(64):
         s = name + ":"
         for j in range(6):
             S = ["R","C","D0","D1","A0","A1"]
             if(2**j & i):
                 s = s + S[j] + " "
         print(s + "=", sol[i][0])
