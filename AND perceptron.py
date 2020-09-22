#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 14:18:09 2020

@author: vrushali
This script is written while studying introduction to neural netwroks 
and codes for a perceptron which acts as a AND operator
"""
import pandas as pd

weight1=1.0
weight2=1.0
bias=-1.1

inputs=[(0,0),(0,1),(1,0),(1,1)]
correct_outputs=[False, False, False, True]

outputs=[]

for input, correct_output in zip(inputs, correct_outputs):
    linear_combination = weight1 * input[0] + weight2 * input[1] + bias
    output = int(linear_combination > 0)
    is_correct_string = "Yes" if correct_output == output else "No"
    outputs.append([input[0], input[1], linear_combination, output, correct_output, is_correct_string])

num_error = len([output[5] for output in outputs if output[5] == 'No'])
outputs_frame=pd.DataFrame(outputs, columns=['Input 1','Input 2', 'Linear Combination','Output','Correct Output', 'Is it correct?'])
if not num_error:
    print("Great! you have got it all correct")
else:
    print("you have {} wrong. keep trying!".format(num_error))
print(outputs_frame)
    



