import numpy as np
import pandas as pd
# import this after importing all other packages.
from idcempy import zmiopc
import matplotlib.pyplot as plt
import seaborn as sns

DAT = pd.read_stata("C:/Users/Nguyen/Box/Summer 20/bp_exact_for_analysis.dta")
# Ziop and ziopc examples
# Specifying Xs, Zs, and Y
X = ['logGDPpc', 'parliament', 'disaster', 'major_oil', 'major_primary']
Xsmall = ['logGDPpc', 'parliament', 'disaster']
Z = ['logGDPpc', 'parliament']
Y = ['rep_civwar_DV']
data = DAT

pstartziop = np.array([-1.31, .32, 2.5, -.21, .2, -0.2, -0.4, 0.2, .9, -.4])

pstartziopsmall = np.array([-1.31, .32, 2.5, -.21, .2, -0.2, -0.4, 0.2])

pstartziopc = np.array([-1.31, .32, 2.5, -.21,
                        .2, -0.2, -0.4, 0.2, .9, -.4, .1])

# These are correct pstart
##Numbers all over the place (copied from R codes)
pstartx = np.array(
    [-0.77, 0.90, 18.78, -2, .2, 0.04, -0.09, 0.26, 1.70, -0.42, -.1])

ziopc_JCR = zmiopc.iopcmod('ziopc',
                           data, X, Y, Z, pstart=pstartziopc, method='bfgs',
                           weights=1,
                           offsetx=0, offsetz=0)

ziop_JCR = zmiopc.iopmod('ziop',
                         data, X, Y, Z, pstart=pstartziop,
                         method='bfgs', weights=1,
                         offsetx=0,
                         offsetz=0)

ziopc_JCR_test = zmiopc.iopcmod('ziopc', data, X, Y, Z)

ziop_JCR = zmiopc.iopmod('ziop', data, X, Y, Z)

ziop_JCRsmall = zmiopc.iopmod('ziop', pstartziopsmall,
                              data, Xsmall, Y, Z, method='bfgs', weights=1,
                              offsetx=0, offsetz=0)

# ziopc_JCR.coefs.to_csv("ZIOPC_0131.csv")
# ziop_JCR.coefs.to_csv("ZIOP_0131.csv")


fitttedziopc = zmiopc.iopcfit(ziopc_JCR)
fitttedziop = zmiopc.iopfit(ziop_JCR)


print(ziopc_JCR.coefs)
print(ziop_JCR.coefs)


# OP Model
pstartop = np.array([-1, 0.3, -0.2, -0.5, 0.2, .9, -.4])

array1 = np.array([1, 2, 3])
array2 = np.array([1, 2, 3])
list1 = [1, 2, 3]
list2 = [1, 2, 3]
pstartcut = [-1, 0.3]
pstartx = [-0.2, -0.5, 0.2, .9, -.4]

DAT = pd.read_stata("C:/Users/Nguyen/Box/Summer 20/bp_exact_for_analysis.dta")
# Ziop and ziopc examples
# Specifying Xs, Zs, and Y
X = ['logGDPpc', 'parliament', 'disaster', 'major_oil', 'major_primary']
Y = ['rep_civwar_DV']
data = DAT
JCR_OP = zmiopc.opmod(pstartop, data, X, Y, method='bfgs', weights=1, offsetx=0)

# Plots

sns.set(style="ticks", color_codes=True)

num_bins = 3
n, bins, patches = plt.hist(yx_, num_bins, facecolor='blue', rwidth=0.9)
data = data.dropna(how='any')
data['rep_civwar_DV'] = data['rep_civwar_DV'].astype(int)
sns.catplot(x='rep_civwar_DV', kind="count", palette="hls", data=data)

# Vuong test
zmiopc.vuong_opiop(JCR_OP, ziop_JCR)
zmiopc.vuong_opiopc(JCR_OP, ziopc_JCR)

# Box plots for predicted probabilities
ziopparl = zmiopc.split_effects(ziop_JCR, 2)
ziopcparl = zmiopc.split_effects(ziopc_JCR, 2)

ziopparl.plot.box(grid='False')
ziopcparl.plot.box(grid='False')

ziopord = zmiopc.ordered_effects(ziop_JCR, 1)
ziopcord = zmiopc.ordered_effects(ziopc_JCR, 1)

ziopord.plot.box(grid='False')
ziopcord.plot.box(grid='False')

# MiOP Examples

DAT = pd.read_stata("C:/Users/Nguyen/Box/Summer 20/EUKnowledge.dta")

Y = ["EU_support_ET"]
X = ['Xenophobia', 'discuss_politics']
Z = ['discuss_politics', 'EU_Know_obj']

miopc_EU = zmiopc.iopcmod('miopc', DAT, X, Y, Z)
op_EU = zmiopc.opmod(DAT, X, Y)

zmiopc.vuong_opiopc(op_EU, miopc_EU)

miopc_EU_xeno = zmiopc.ordered_effects(miopc_EU, 0)
miopc_EU__diss = zmiopc.ordered_effects(miopc_EU, 1)

miopc_EU_xeno.plot.box(grid='False')
miopc_EU__diss.plot.box(grid='False')

miopc_EU_diss = zmiopc.split_effects(miopc_EU, 1)
miopc_EU_know = zmiopc.split_effects(miopc_EU, 2)

miopc_EU_diss.plot.box(grid='False')
miopc_EU_know.plot.box(grid='False')


###Tobacco data


DAT = pd.read_csv("C:/Users/Nguyen/Google "
                  "Drive/zmiopc/zmiopc/data/tobacco_cons.csv")
X = ['age', 'grade', 'gender_dum']
Y = ['cig_count']
Z = ['gender_dum']
pstart = np.array([.01, .01, .01, .01, .01, .01, .01, .01, .01, .01])

ziopc_tob = zmiopc.iopcmod('ziopc', DAT, X, Y, Z)
op_tob = zmiopc.opmod(DAT, X, Y)

zmiopc.vuong_opiopc(op_tob,ziopc_tob)

ziopcage = zmiopc.ordered_effects(ziopc_tob, 0)
ziopcgrade = zmiopc.ordered_effects(ziopc_tob, 1)
ziopcgender = zmiopc.ordered_effects(ziopc_tob, 2)

ziopcage.plot.box(grid='False')
ziopcgrade.plot.box(grid='False',fontsize='small')
ziopcgender.plot.box(grid='False',fontsize='small')


ziopcgenders = zmiopc.split_effects(ziopc_tob, 1)
ziopcgenders.plot.box(grid='False')
ziopcgenders = zmiopc.split_effects(ziopc_tob, 0)
ziopcgenders.plot.box(grid='False')