"""

E. Wes Bethel, Copyright (C) 2022

October 2022

Description: This code loads a .csv file and creates a 3-variable plot, and saves it to a file named "myplot.png"

Inputs: the named file "sample_data_3vars.csv"

Outputs: displays a chart with matplotlib

Dependencies: matplotlib, pandas modules

Assumptions: developed and tested using Python version 3.8.8 on macOS 11.6

"""

import pandas as pd
import matplotlib.pyplot as plt

fname = "data_3vars.csv"
df = pd.read_csv(fname, comment="#")
print(df)

var_names = list(df.columns)

print("var names =", var_names)

# split the df into individual vars
# assumption: column order - 0=problem size, 1=blas time, 2=basic time

problem_sizes = df[var_names[0]].values.tolist()
code1_time = df[var_names[1]].values.tolist()
code2_time = df[var_names[2]].values.tolist()
code3_time = df[var_names[3]].values.tolist()

# MFLOPS
plt.figure()
plt.title("MFLOPS Comparison")
xlocs = [i for i in range(len(problem_sizes))]
plt.xticks(xlocs, problem_sizes)
plt.plot([1000000 / x for x in code1_time], "r-o")
plt.plot([1000000 / x for x in code2_time], "b-x")
plt.plot([1000000 / x for x in code3_time], "g-^")
plt.xlabel("Problem Sizes")
plt.ylabel("MFLOPS")
varNames = [var_names[1], var_names[2], var_names[3]]
plt.legend(varNames, loc="best")
plt.grid(axis='both')
plt.savefig("mflops_plot.png", dpi=300)
plt.close()

# Memory Bandwidth
plt.figure()
plt.title("Memory Bandwidth Comparison")
xlocs = [i for i in range(len(problem_sizes))]
plt.xticks(xlocs, problem_sizes)
plt.plot([(4000000 / x) / (204.8 * 1073741824) for x in code1_time], "r-o")
plt.plot([(4000000 / x) / (204.8 * 1073741824) for x in code2_time], "b-x")
plt.plot([(4000000 / x) / (204.8 * 1073741824) for x in code3_time], "g-^")
plt.xlabel("Problem Sizes")
plt.ylabel("Memeory Bandwidth")
varNames = [var_names[1], var_names[2], var_names[3]]
plt.legend(varNames, loc="best")
plt.grid(axis='both')
plt.savefig("bandwidth_plot.png", dpi=300)
plt.close()

# Memory Latency
plt.figure()
plt.title("Memory Latency Comparison")
xlocs = [i for i in range(len(problem_sizes))]
plt.xticks(xlocs, problem_sizes)
plt.plot([x / 4000000 for x in code1_time], "r-o")
plt.plot([x / 4000000 for x in code2_time], "b-x")
plt.plot([x / 4000000 for x in code3_time], "g-^")
plt.xlabel("Problem Sizes")
plt.ylabel("Memeory Latency")
varNames = [var_names[1], var_names[2], var_names[3]]
plt.legend(varNames, loc="best")
plt.grid(axis='both')
plt.savefig("latency_plot.png", dpi=300)
plt.close()

plt.show()

# EOF
