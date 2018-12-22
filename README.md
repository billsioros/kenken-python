# Kenken puzzle solver

## Benchmarking various algorithms

| Algorithm     |  Size |  Constraint checks  |  Assignments        |  Completion time        | 
|---------------|-------|---------------------|---------------------|-------------------------| 
| BT            |  3    |  21.666666666666664 |  5.0                |  0.00021251042683919274 | 
| BT            |  4    |  103.0              |  13.0               |  0.001128832499186198   | 
| BT            |  5    |  1145.0             |  75.66666666666666  |  0.008542219797770183   | 
| BT            |  6    |  22509.333333333336 |  496.33333333333337 |  0.10041244824727376    | 
| BT            |  7    |  123685.0           |  1851.0             |  0.6239778200785319     | 
| BT            |  8    |  393801.3333333334  |  6301.333333333334  |  2.151556094487508      | 
| BT            |  9    |  4858985.0          |  70936.66666666667  |  26.367678642272953     | 
| BT+MRV        |  3    |  34.66666666666667  |  4.333333333333333  |  0.00026408831278483075 | 
| BT+MRV        |  4    |  158.33333333333331 |  8.0                |  0.000804742177327474   | 
| BT+MRV        |  5    |  1248.3333333333333 |  26.000000000000004 |  0.005061626434326172   | 
| BT+MRV        |  6    |  2231.333333333333  |  29.000000000000004 |  0.010144233703613281   | 
| BT+MRV        |  7    |  237872.6666666667  |  1753.3333333333333 |  1.1216808954874673     | 
| BT+MRV        |  8    |  270559.6666666667  |  1124.0             |  1.0661603609720864     | 
| BT+MRV        |  9    |  28516120.0         |  95700.33333333333  |  122.92057545979819     | 
| FC            |  3    |  33.333333333333336 |  5.333333333333333  |  0.00033926963806152344 | 
| FC            |  4    |  278.3333333333333  |  15.0               |  0.001443783442179362   | 
| FC            |  5    |  373.0              |  22.0               |  0.002213557561238607   | 
| FC            |  6    |  1808.0             |  69.66666666666666  |  0.01231710116068522    | 
| FC            |  7    |  7585.0             |  231.33333333333331 |  0.04612509409586589    | 
| FC            |  8    |  28311.333333333336 |  355.3333333333333  |  0.15033292770385742    | 
| FC            |  9    |  513172.6666666667  |  4070.666666666667  |  4.509950081507365      | 
| FC+MRV        |  3    |  34.666666666666664 |  4.666666666666666  |  0.00020130475362141925 | 
| FC+MRV        |  4    |  124.66666666666669 |  8.666666666666666  |  0.0006211598714192708  | 
| FC+MRV        |  5    |  406.66666666666663 |  13.0               |  0.002089103062947591   | 
| FC+MRV        |  6    |  933.3333333333335  |  18.333333333333332 |  0.003720998764038086   | 
| FC+MRV        |  7    |  2144.666666666667  |  37.0               |  0.020891904830932617   | 
| FC+MRV        |  8    |  14311.0            |  150.0              |  0.07213409741719563    | 
| FC+MRV        |  9    |  16871.0            |  167.0              |  0.07013694445292154    | 
| MAC           |  3    |  54.333333333333336 |  5.0                |  0.0002544720967610677  | 
| MAC           |  4    |  230.33333333333331 |  8.0                |  0.0010233720143636067  | 
| MAC           |  5    |  3257.9999999999995 |  12.999999999999998 |  0.012428522109985353   | 
| MAC           |  6    |  33296.0            |  36.0               |  0.12111242612202963    | 
| MAC           |  7    |  86430.0            |  39.666666666666664 |  0.33033068974812824    | 
| MAC           |  8    |  1817476.3333333335 |  188.66666666666669 |  8.844631592432659      | 
| MAC           |  9    |  8430812.333333334  |  2792.333333333333  |  36.47878551483154      | 
| MIN_CONFLICTS |  3    |  107.66666666666667 |  7.666666666666668  |  0.00036700566609700524 | 
| MIN_CONFLICTS |  4    |  622.3333333333334  |  14.666666666666666 |  0.0021456082661946616  | 
| MIN_CONFLICTS |  5    |  3607.0             |  31.0               |  0.012328863143920898   | 
| MIN_CONFLICTS |  6    |  31629.0            |  129.33333333333331 |  0.11575563748677573    | 
| MIN_CONFLICTS |  7    |  49782441.666666664 |  66726.33333333334  |  203.58154924710593     | 
| MIN_CONFLICTS |  8    |  58982099.333333336 |  66770.33333333333  |  257.1670039494832      | 
| MIN_CONFLICTS |  9    |  32220588.666666668 |  34105.666666666664 |  119.98163326581319     | 

------

### **Kenken puzzles of size 3 :**
The algorithms sorted by <span style="color: #f45c42">constraint check count</span> are ['MIN_CONFLICTS', 'BT', 'FC', 'FC+MRV', 'BT+MRV', 'MAC']

The algorithms sorted by <span style="color: #f45c42">assignment count</span> are ['BT+MRV', 'FC+MRV', 'BT', 'MAC', 'FC', 'MIN_CONFLICTS']

The algorithms sorted by <span style="color: #f45c42">completion time</span> are ['FC+MRV', 'BT', 'MAC', 'BT+MRV', 'FC', 'MIN_CONFLICTS']

### **Kenken puzzles of size 4 :**
The algorithms sorted by <span style="color: #f45c42">constraint check count</span> are ['BT', 'FC+MRV', 'BT+MRV', 'MAC', 'FC', 'MIN_CONFLICTS']

The algorithms sorted by <span style="color: #f45c42">assignment count</span> are ['BT+MRV', 'MAC', 'FC+MRV', 'BT', 'MIN_CONFLICTS', 'FC']

The algorithms sorted by <span style="color: #f45c42">completion time</span> are ['FC+MRV', 'BT+MRV', 'MAC', 'BT', 'FC', 'MIN_CONFLICTS']

### **Kenken puzzles of size 5 :**
The algorithms sorted by <span style="color: #f45c42">constraint check count</span> are ['BT', 'BT+MRV', 'MAC', 'MIN_CONFLICTS', 'FC', 'FC+MRV']

The algorithms sorted by <span style="color: #f45c42">assignment count</span> are ['MAC', 'FC+MRV', 'FC', 'BT+MRV', 'MIN_CONFLICTS', 'BT']

The algorithms sorted by <span style="color: #f45c42">completion time</span> are ['FC+MRV', 'FC', 'BT+MRV', 'BT', 'MIN_CONFLICTS', 'MAC']

### **Kenken puzzles of size 6 :**
The algorithms sorted by <span style="color: #f45c42">constraint check count</span> are ['FC', 'BT+MRV', 'BT', 'MIN_CONFLICTS', 'MAC', 'FC+MRV']

The algorithms sorted by <span style="color: #f45c42">assignment count</span> are ['FC+MRV', 'BT+MRV', 'MAC', 'FC', 'MIN_CONFLICTS', 'BT']

The algorithms sorted by <span style="color: #f45c42">completion time</span> are ['FC+MRV', 'BT+MRV', 'FC', 'BT', 'MIN_CONFLICTS', 'MAC']

### **Kenken puzzles of size 7 :**
The algorithms sorted by <span style="color: #f45c42">constraint check count</span> are ['BT', 'FC+MRV', 'BT+MRV', 'MIN_CONFLICTS', 'FC', 'MAC']

The algorithms sorted by <span style="color: #f45c42">assignment count</span> are ['FC+MRV', 'MAC', 'FC', 'BT+MRV', 'BT', 'MIN_CONFLICTS']

The algorithms sorted by <span style="color: #f45c42">completion time</span> are ['FC+MRV', 'FC', 'MAC', 'BT', 'BT+MRV', 'MIN_CONFLICTS']

### **Kenken puzzles of size 8 :**
The algorithms sorted by <span style="color: #f45c42">constraint check count</span> are ['FC+MRV', 'MAC', 'BT+MRV', 'FC', 'BT', 'MIN_CONFLICTS']

The algorithms sorted by <span style="color: #f45c42">assignment count</span> are ['FC+MRV', 'MAC', 'FC', 'BT+MRV', 'BT', 'MIN_CONFLICTS']

The algorithms sorted by <span style="color: #f45c42">completion time</span> are ['FC+MRV', 'FC', 'BT+MRV', 'BT', 'MAC', 'MIN_CONFLICTS']

### **Kenken puzzles of size 9 :**
The algorithms sorted by <span style="color: #f45c42">constraint check count</span> are ['FC+MRV', 'BT+MRV', 'MIN_CONFLICTS', 'BT', 'FC', 'MAC']

The algorithms sorted by <span style="color: #f45c42">assignment count</span> are ['FC+MRV', 'MAC', 'FC', 'MIN_CONFLICTS', 'BT', 'BT+MRV']

The algorithms sorted by <span style="color: #f45c42">completion time</span> are ['FC+MRV', 'FC', 'BT', 'MAC', 'MIN_CONFLICTS', 'BT+MRV']

------

## External sources [csp.py, search.py, utils.py](https://github.com/aimacode/aima-python)
