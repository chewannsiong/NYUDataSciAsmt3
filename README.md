
# Introduction

Assignment [here](https://nyu-cds.github.io/courses/assignments/advanced-3/) proposes 4 approaches to improve a given set of codes. 4 versions of the codes are included that represents each of the 4 approaches explored. A final optimized version that includes all the improvement is also included.

## Version 1

This approach aims to reduce function call overhead. Formulae for child functions were incorporated into their parent functions, where possible. The following functions were no longer required after the changes.
* compute_mag
* compute_b
* compute_deltas
* update_vs
* update_rs

Most performance gained through this approach. Codes can be found in nbody_1.py.

## Version 2

This approach aims to use alternatives to membership testing of lists. The double for loops in the *advance* and *report_energy* functions were changed such that an inner membership testing of lists is not required. 

Slight performance gained through this approach. Codes can be found in nbody_2.py.

## Version 3

This approach aims to use local rather than global variables. The *BODIES* global variable was converted to a local variable and passed as inputs and outputs to the *advance* and *report_energy* functions. 

Negligible performance gained through this approach. Codes can be found in nbody_3.py

## Version 4

This approach aims to use data aggregation to reduce loop overheads. The map function was used in the *report_energy* function. 

Slight performance gained through this approach. Codes can be found in nbody_4.py.

## Optimized Version

This version combines all changes to the other versions. Overall processing time slightly above 30 seconds. Relative speed up (i.e. time to run original / time to run optimized version) is around 3. Codes can be found in nbody_opt.py.

## Test Script

An additional test script is included to prompt user for which script to execute and return the time taken. Codes can be found in nbody_test.py
