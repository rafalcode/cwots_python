#!/usr/bin/env python2.7
# seemingly redundant script: outputs the module list command.
# however it does so capturing everything into a variable. No small task considering how slippery "module" can be

import regex, subprocess

def hilite(string, status, bold):
    attr = []
    if status==0:
        # green
        attr.append('32')
    elif status ==1:
        # other color (31 is red BTW)
        attr.append('33')
    elif status ==2:
        attr.append('35')
    if bold:
        attr.append('1')
    return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)


echo_for_cmd = ['/usr/local/Modules/3.2.10/bin/modulecmd', 'python', 'list']
echocmdproc = subprocess.Popen(echo_for_cmd, stderr=subprocess.PIPE)
o=subprocess.check_output("cat", stdin=echocmdproc.stderr)
echocmdproc.wait()

# RGX=regex.compile(r'  +')
# m=RGX.split(o)
RGX=regex.compile(r'\d\) ([\w/.]{4,})')
m=RGX.findall(o)
print type(m)
msz=len(m)
for i in xrange(msz):
    idx=i%3
    print hilite(m[i], idx, 0)
