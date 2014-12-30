#! /usr/bin/env python

import random
from scapy.all import *
import time
import Queue

# (2014) AJ NOURI  ajn.bin@gmail.com

dsthost = '66.66.66.66'

q = Queue.Queue(maxsize=5)

for i in xrange(1000):
    rint = random.randint(1,10)
    if rint % 5 == 0:
        print '==> Random queue processing'
        if not q.full():
            ipin = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
            q.put(ipin)
            srchost = ipin
            print ipin,' into the queue'
        else:
            ipout = q.get()
            srchost = ipout
            print ' *** This is sticky src IP',ipout
    else:
        srchost = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        print 'one time src IP', srchost
    #srchost = scapy.RandIP()
    p = IP(src=srchost,dst=dsthost) / UDP(dport=5555)
    print 'src= ',srchost, 'dst= ',dsthost
    send(p, iface='tap2')
    print 'sending packet\n'
    time.sleep(1)
