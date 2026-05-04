import numpy as np

# Weekly Challenge 15: Kadane's Algorithm*
# Author: Ing. Arturo Javier Borbon Rojas

def kadanes_algorithm(arr):
    print(f"Analyzing Array:{arr} " )
    print("-"*50)

    # Initialice variables with the first element of the array
    max_current= max_global = arr[0]

    # Variables to track the indices of the subarray
    start_idx = end_idx= temp_start=0

    print(f"""Step 00 | 
          Element: {arr[0]:>2} | 
          Current Sum: {max_current:>2} | 
          Max Global {max_global:>2}""")

    # Loop through the array  starting from the secnond element
    for i in range(1, len(arr)):
        # Core logic: Is the current element alone bigger than the current element + the previous sum?
        if arr[i]> max_current + arr[i]:
            max_current= arr[i]
            temp_start= i
        else:
            max_current+=arr[i]

        # Upgrade the global maximum if we found a new high
        if max_current> max_global:
            max_global = max_current
            start_idx= temp_start
            end_idx=i

        print(f"""Step {i:02d} 
              Element: {arr[i]:>2}
              Current Sum: {max_current:>2}
              Max Global: {max_global:>2}  """)
        
    print("-"*50)
    print(f"Maximum Subarray Sum: {max_global}")
    print(f"Optimal Subarray: {arr[start_idx:end_idx+1]}")

    return max_global

# Testing the algorithm
daily_profits= np.random.randint(0,100, size=10)

# use def
kadanes_algorithm(daily_profits)
