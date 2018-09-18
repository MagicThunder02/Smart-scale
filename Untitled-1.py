#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
  
plt.rcParams["figure.figsize"] = [16, 9]
#plt.axis("square")
plt.axis([0, 100, 0, 150])
plt.plot([12, 13], [33, 44])
plt.savefig("/tmp/mifig3")
print("ciccio")