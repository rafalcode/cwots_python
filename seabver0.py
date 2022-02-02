#!/usr/bin/env python3
# Seaborn is the scientific visualisation library built on matplotlib
# It has  very handy annotate() function for adding text boes on a plot (most often JointGrid)
# but for some reason (maybe it was inefficient) it did away with an wanted users to use ax_joint.text instead.
# so this is proof concept that it does work, for both early and latest versions of seaborn.

import sys 
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

# OK, a JointGrid ... you must set the x and y to the header of the column of the input data, that's the way JointGrid reads it.
g = sns.JointGrid(x="total_bill", y="tip", data=tips)
# you can access those two vectors via tips.total_bill and tips.tip
g = g.plot_joint(plt.scatter, color="g", s=40, edgecolor="white")
g = g.plot_marginals(sns.distplot, kde=False, color="g")

# OK here is the deprecated annotate function,
# it was not straightforward, first arg was a function ... and it works implicitly on JointGrid's x and y vectors.
# scipy's stats.pearsonr will be used here. It returns 2 floats: the coefficient first and then the p-value.
# g = g.annotate(stats.pearsonr)
# g = g.annotate(stats.pearsonr, template="{stat}: {val:.4f}", stat="Pearson's r", loc="upper left", fontsize=15)
pearr= stats.pearsonr(tips.total_bill, tips.tip) # precalc
st=f"Pearson's r = {pearr[0]:.4f}" # stringify
# g.ax_joint.text(3.5, 10.0, st, fontsize=15) # na, not that easy .. add in the extra "chweing in order to be able to use 0.05, 0.95
g.ax_joint.text(0.05, 0.95, st, fontsize=15, transform=g.ax_joint.transAxes, verticalalignment='top')
g.savefig("d09.pdf", format="pdf")
