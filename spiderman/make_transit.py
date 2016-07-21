import spiderman.web as web
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

sb.set_style('ticks')

sb.set_palette('colorblind')

# test case parameters
tc = 200.0
per = 0.81347753
a = 0.01526
inc = 82.33
ecc = 0.0
omega = np.pi
xi = 5.1
T_n = 294.7
delta_T = 471.8
rp = 1.0/6.448
a_rs = 4.92
star_bright = 1e14

tc = 2456601.0274800002
per = 0.81347753
a = 0.01526
inc = 82.33
ecc = 0.0
omega = np.pi
xi = 0.72078
T_n = 161.20425161635964
delta_T = 290.77876311195195
rp = 0.15941919545762004
a_rs = 4.92
star_bright =175802758853757.03

n_ts = 1001

ts = np.linspace(tc,tc+per*3,n_ts)

ts=[ 2456600.97307,2456600.97471,2456600.97636,2456600.978,2456600.97965
,2456600.98129,2456600.98293,2456600.98458,2456600.98622,2456600.98786
,2456600.98951,2456600.99115,2456600.99279,2456600.99444,2456600.99608
,2456600.99773,2456600.99937,2456601.00101,2456601.03952,2456601.04117
,2456601.04281,2456601.04445,2456601.0461, 2456601.04774,2456601.04938
,2456601.05103,2456601.05267,2456601.05432,2456601.05596,2456601.0576
,2456601.05925,2456601.06089,2456601.06253,2456601.06418,2456601.06582
,2456601.06746,2456601.10599,2456601.10763,2456601.10927,2456601.11092
,2456601.11256,2456601.11421,2456601.11585,2456601.11749,2456601.11914
,2456601.12078,2456601.12242,2456601.12407,2456601.12571,2456601.12735
,2456601.129,2456601.13064,2456601.13229,2456601.13393,2456601.17244
,2456601.17408,2456601.17573,2456601.17737,2456601.17901,2456601.18066
,2456601.1823, 2456601.18394,2456601.18559,2456601.18723,2456601.18888
,2456601.19052,2456601.19216,2456601.19381,2456601.19545,2456601.19709
,2456601.19874,2456601.20038,2456601.2389, 2456601.24055,2456601.24219
,2456601.24383,2456601.24548,2456601.24712,2456601.24876,2456601.25041
,2456601.25205,2456601.2537, 2456601.25534,2456601.25698,2456601.25863
,2456601.26027,2456601.26191,2456601.26356,2456601.2652, 2456601.26685
,2456601.30536,2456601.307,2456601.30864,2456601.31029,2456601.31193
,2456601.31357,2456601.31522,2456601.31686,2456601.3185, 2456601.32015
,2456601.32179,2456601.32344,2456601.32508,2456601.32672,2456601.32837
,2456601.33001,2456601.33165,2456601.3333, 2456601.37182,2456601.37346
,2456601.37511,2456601.37675,2456601.37839,2456601.38004,2456601.38168
,2456601.38333,2456601.38497,2456601.38661,2456601.38826,2456601.3899
,2456601.39154,2456601.39319,2456601.39483,2456601.39647,2456601.39812
,2456601.39976,2456601.43827,2456601.43992,2456601.44156,2456601.4432
,2456601.44485,2456601.44649,2456601.44813,2456601.44978,2456601.45142
,2456601.45306,2456601.45471,2456601.45635,2456601.458,2456601.45964
,2456601.46128,2456601.46293,2456601.46457,2456601.46621,2456601.50474
,2456601.50638,2456601.50802,2456601.50967,2456601.51131,2456601.51295
,2456601.5146, 2456601.51624,2456601.51788,2456601.51953,2456601.52117
,2456601.52282,2456601.52446,2456601.5261, 2456601.52775,2456601.52939
,2456601.53103,2456601.53268,2456601.57172,2456601.57336,2456601.57501
,2456601.57665,2456601.5783, 2456601.57994,2456601.58158,2456601.58323
,2456601.58487,2456601.58651,2456601.58816,2456601.5898, 2456601.59144
,2456601.59309,2456601.59473,2456601.59638,2456601.59802,2456601.59966
,2456601.6397, 2456601.64134,2456601.64299,2456601.64463,2456601.64628
,2456601.64792,2456601.64956,2456601.65121,2456601.65285,2456601.65449
,2456601.65614,2456601.65778,2456601.65942,2456601.66107,2456601.66271
,2456601.66436,2456601.666,2456601.66764,2456601.70657,2456601.70821
,2456601.70986,2456601.7115, 2456601.71314,2456601.71479,2456601.71643
,2456601.71808,2456601.71972,2456601.72136,2456601.72301,2456601.72465
,2456601.72629,2456601.72794,2456601.72958,2456601.73122,2456601.73287
,2456601.73451]

ts = np.array(ts)

n_slice = 20
lc = np.array(web.lightcurve(n_slice,ts,tc,per,a,inc,ecc,omega,a_rs,rp,xi,T_n,delta_T,star_bright))

plt.plot(ts-tc,lc,'bo')

#lc = np.array(web.lightcurve(n_slice,ts,tc,per,a,inc,ecc,omega,r_s,star_r,xi,T_n,delta_T,star_bright))
#plt.plot(ts-tc,lc-1)

plt.ylim(1-0.0001,1.0016)
#plt.xlim(-0.4,0.4)
#plt.xlim(-0.05,0.05)

plt.yticks([1,1.0005,1.0010,1.0015],['1.0000','1.0005','1.0010','1.0015'])

plt.ylabel('Relative flux')
plt.xlabel('t-t$_0$ (days)')

plt.savefig('lc.pdf',set_bbox_inches='tight')
plt.savefig('lc.png',set_bbox_inches='tight')