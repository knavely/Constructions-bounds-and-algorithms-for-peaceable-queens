# Constructions-bounds-and-algorithms-for-peaceable-queens
Supporting repo for https://arxiv.org/abs/2406.06974


# Description 
We have a python file for each upper bound optimization model in the paper. These allow us to compute: 

Theorem 1.2 (Even Torus Upper Bound) -- even_torus.py

Theorem 1.3 (Odd Torus Upper Bound) -- odd_torus.py

Theorem 1.5 (Even Torus Upper Bound) -- regular_board.py

# Instructions without Docker
1. install Gekko with> pip install gekko 
2. verify Theorem 1.2 with > python even_torus.py \
we should see final lines output: \

better upper bound beyond numeric error is infeasible \
*****
Theorem 1.2 t(n_even) <=  0.14013154232 n^2
*****

3. verify Theorem 1.3 with > python odd_torus.py \
we should see final lines of output: \

better upper bound beyond numeric error is infeasible \
*****
Theorem 1.4 t(n_odd) <=  0.1249968765 n^2
*****

4. verify Theorem 1.5 with > python regular_board.py \

we should see final lines output: \
better upper bound beyond numeric error is infeasible
*****
Theorem 1.5 a(n) <=  0.17157287525 n^2
*****


# Instructions using Docker
You need docker and python installed.

1. download peaceablequeens.tar
2. docker load -i peaceablequeens.tar
3. docker run --rm --network=host peaceable_queens_upperbounds

This will run our models and should look similar to the sample_output file.

The models first find the optimal solution, then perform a sanity check that there is not a better feasible solution by forcing an objective lower bound constraint close to the reported optimal. Look for the resulting lines int he output:

---------------------------------------------------
 Solver         :  IPOPT (v3.12)
 Solution time  :   1.879999999073334E-002 sec
 Objective      :  -0.124996876496913     
 Successful solution
 ---------------------------------------------------
 
*****
Theorem 1.4 t(n_odd) <=  0.1249968765 n^2
*****

 
 
 ---------------------------------------------------
 Solver         :  IPOPT (v3.12)
 Solution time  :   0.232799999997951      sec
 Objective      :  -0.140131542319769     
 Successful solution
 ---------------------------------------------------
 
*****
Theorem 1.2 t(n_even) <=  0.14013154232 n^2
*****


---------------------------------------------------
 Solver         :  APOPT (v1.0)
 Solution time  :   2.129999999306165E-002 sec
 Objective      :  -0.171572875253810     
 Successful solution
 ---------------------------------------------------
 

*****
Theorem 1.5 a(n) <=  0.17157287525 n^2
*****
