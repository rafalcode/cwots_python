#!/usr/bin/env python2
# beware this is from a code golf contest
# ref. http://codegolf.stackexchange.com/questions/52808/shortest-longest-common-subsequence-code

def o(t):
 t=[[y for y in x if y in reduce(lambda x,y:x.intersection(y),t,set(t[0]))]for x in t];l=map(len,t);C=[0]*reduce(lambda x,y:x*-~y,l,1);y=lambda z:[x-1for x in z];m=len(t);e=enumerate
 def g(h):
    r,x=0,1
    for k,j in e(h):r+=-~j*x;x*=-~l[k]
    return r
 def f(h):
    i=len(h)
    if i==m:
     b=g(h);c=t[0][h[0]]
     for k,j in e(h):
         if t[k][j]!=c:break
     else:C[b]=1+C[g(y(h))];return
     r=0
     for k,_ in e(h):a=h[:];a[k]-=1;r=max(r,C[g(a)])
     C[b]=r;return
    for j,_ in e(t[i]):f(h+[j])
 def p(h):
    if min(h)==-1:return''
    v=C[g(h)]
    for k,_ in e(h):
        a=h[:];a[k]-=1
        if v==C[g(a)]:return p(a)
    return p(y(h))+t[0][h[0]]
 f([]);return p(y(l))

tests = [
"""
a
ab
""",
"""
aaaaxbbbb
bbbbxcccc
ccccxaaaa
""",
"""
hxbecqibzpyqhosszypghkdddykjfjcajnwfmtfhqcpavqrtoipocijrmqpgzoufkjkyurczxuhkcpehbhpsuieqgjcepuhbpronmlrcgvipvibhuyqndbjbrrzpqbdegmqgjliclcgahxoouqxqpujsyfwbdthteidvigudsuoznykkzskspjufgkhaxorbrdvgodlb
qnnprxqpnafnhekcxljyysobbpyhynvolgtrntqtjpxpchqwgtkpxxvmwwcohxplsailheuzhkbtayvmxnttycdkbdvryjkfhshulptkuarqwuidrnjsydftsyhuueebnrjvkfvhqmyrclehcwethsqzcyfvyohzskvgttggndmdvdgollryqoswviqurrqhiqrqtyrl
""",
"""
riikscwpvsbxrvkpymvbbpmwclizxlhihiubycxmxwviuajdzoonjpkgiuiulbjdpkztsqznhbjhymwzkutmkkkhirryabricvhb
jnrzutfnbqhbaueicsvltalvqoorafnadevojjcsnlftoskhntashydksoheydbeuwlswdzivxnvcrxbgxmquvdnfairsppodznm
kzimnldhqklxyezcuyjaiasaeslicegmnwfavllanoolkhvqkjdvxrsjapqqwnrplcwqginwinktxnkfcuuvoyntrqwwucarfvjg
""",
"""
rblartqkfggrjpiipuzzypkycnyckkcqceeujiyy
yfpnedyjtiwrhyuktripdwyvgkblzodeufkelhub
ywcyboxwqkibwvredkrbdsyudkulpvmhixeqxynh
bnxwahbzhwjxkotnvbxrojkkldtsodtjmvdrmbgr
""",
"""
bwfscmotshoczmduwaev
coywaaizdaxjovipsmeh
dobzcpoiedenzlfdjpiu
bbhfeqscvvbwkuoxdoge
drqrzwbcpcsvneodelja
""",
"""
nqrualgoedlf
jgqorzglfnpa
fgttvnogldfx
pgostsulyfug
sgnhoyjlnfvr
wdttgkolfkbt
""",
"""
epopyfuhgowedpiqpgfj
ddxyestqynpwmytxhozm
ptubgzyqqksieoovuezv
tovotqmnhgzttfpywjgr
aomvytkgaijlgqzkljls
vzvxpaixrnprxvenbbuo
syfuwxlpcyontqlmfvib
arxleuomstkjegpduwcx
xgqrxaopouvkvwgbzewn
yggunddigctgpnuztzai
izroomywwztdymqszsuo
kiawjnxjncdtufhkrjsp
"""
]

for s in tests:
    print o(s.strip().split())
