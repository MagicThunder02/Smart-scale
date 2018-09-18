#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import testdb

class classPlot:
    DB = testdb.classSSdb()

    def startgrafico(self, fname):
        # ------------------------
        plt.rcParams["figure.figsize"] = [16, 9]
        plt.axis("square")
        plt.axis([0, 100, 0, 100])
        # ------------------------
        self.DB.weights_dates()
        for k in range(len(self.DB.arraydates)):
            print(self.DB.arrayweights[k])
            print(self.DB.arraydates[k])
        print(self.DB.arraydates)
        print(self.DB.arrayweights)
       # plt.plot(self.DB.arrayweights, self.DB.arraydates)
        plt.plot(self.DB.arrayweights, self.DB.arraydates)
        fff = "/tmp/{}".format(fname)
        plt.savefig(fff)
        print("grafico finito!")
        return fff

