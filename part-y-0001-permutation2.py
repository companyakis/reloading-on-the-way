"""
P(n,r)=n×(n−1)×(n−2)×⋯×(n−r+1)

There are 20 equal students. We will assign one student to the Main Gate, one to the Cafeteria, and one to the School Hall. 
Please calculate how many different ordered arrangements (permutations) are there for these 3 positions?

 Step 1(Main Gate): 20 candidate students
 
 Step 2(Cafeteria): (20 - 1) candidate students

 Step 3(School Hall): (20 - 2) candidate students

 P(20, 3) = (Step 1) × (Step 2)  ×(Step 3)
"""

P(20, 3) = 20 * 19 * 18 = 6840
