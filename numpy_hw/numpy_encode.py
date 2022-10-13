import numpy as np


def encode(x):
   
    # ensure array
    x = np.asanyarray(x)
    if x.ndim != 1:
        raise ValueError('only 1D array supported')
    n = x.shape[0]

    # handle empty array
    if n == 0:
        return np.array([]), np.array([])

    else:
        # find run starts
        loc_run_start = np.empty(n, dtype=bool)
        loc_run_start[0] = True
        np.not_equal(x[:-1], x[1:], out=loc_run_start[1:])
        run_starts = np.nonzero(loc_run_start)[0]
        
        # find run values
        run_values = x[loc_run_start]
        
        # find run lengths
        run_lengths = np.diff(np.append(run_starts, n))
        return run_values, run_lengths
    
   
str_array = np.array([1, 2, 2, 3, 3, 1, 1, 5, 5, 2, 3, 3])
print(encode(str_array))
