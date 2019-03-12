import numpy as np

import matplotlib.pyplot as plt
#import talib
import matplotlib.font_manager as font_manager
from matplotlib import collections  as mc


###### CLASS SANDWICH
#### CONTAINS arrays with different info for every time point
### price, ups, downs, open, close, vol, and indexes like MACD, RSI  and increments

class Sw(object):

    def __init__(self, candles=None, **kwargs):
        if candles:
            # imported values
            self.open = np.array([float(x[1]) for x in candles])
            self.high = np.array([float(x[2]) for x in candles])
            self.low = np.array([float(x[3]) for x in candles])
            self.close = np.array([float(x[4]) for x in candles])
            self.volume = np.array([float(x[5]) for x in candles])

            # computes the inedexes
'''
            # classic
            self.rsi = ta-lib.RSI(self.close)
            self.macd, self.macdsignal, uaua = ta-lib.MACD(self.close, fastperiod=12, slowperiod=26, signalperiod=9)
            self.rocp = ta-lib.ROCP(self.close)

            # overlap
            self.sar = ta-lib.SAR(self.high, self.low)

            
            self.kama = talib.KAMA(self.close)
            self.bb_up, self.bb_mid, self.bb_low = talib.BBANDS(self.close)

            # momentum
            self.arosc = talib.AROONOSC(self.high, self.low)
            self.mom = talib.MOM(self.close)
            self.slostok, self.slostod = talib.STOCH(self.high, self.low, self.close)
            self.fasstok, self.fasstod = talib.STOCHF(self.high, self.low, self.close)

            self.ulto = talib.ULTOSC(self.high, self.low, self.close)
            self.wilr = talib.WILLR(self.high, self.low, self.close)
            self.trix = talib.TRIX(self.close)

            # vol
            self.chaos = talib.ADOSC(self.high, self.low, self.close, self.volume)
            self.obv = talib.OBV(self.close, self.volume)

            # cycle
            self.hilper = talib.HT_DCPERIOD(self.close)
            self.hilpha = talib.HT_DCPHASE(self.close)
            self.phasorin, self.phasorquad  = talib.HT_PHASOR(self.close)
            #self.hilsine = talib.HT_SINE(self.close) # gives out of range error
            self.hiltrend = talib.HT_TRENDMODE(self.close)

            '''


def plotSerie(serie, trades=None, coin=None, wins=None, timeframe="1min", numberfig=1, **kwargs):
    if not wins:
        wins = len(serie)

    prices = serie.close
    rsi = serie.rsi
    macd = serie.macd
    macdsignal = serie.macdsignal
    sar = serie.sar

    ##################################

    plt.rc('axes', grid=True)
    plt.rc('grid', color='0.75', linestyle='-', linewidth=0.5)

    textsize = 9
    left, width = 0.1, 0.8
    rect1 = [left, 0.7, width, 0.2]
    rect2 = [left, 0.3, width, 0.4]
    rect3 = [left, 0.1, width, 0.2]

    fig = plt.figure(numberfig, facecolor='white')
    axescolor = '#f6f6f6'  # the axes background color

    ax1 = fig.add_axes(rect1, axisbg=axescolor)  # left, bottom, width, height
    ax2 = fig.add_axes(rect2, axisbg=axescolor, sharex=ax1)
    ax2t = ax2.twinx()
    ax3 = fig.add_axes(rect3, axisbg=axescolor, sharex=ax1)

    fillcolor = 'purple'

    ax1.plot(rsi[-wins:], color=fillcolor)
    ax1.axhline(70, color=fillcolor)
    ax1.axhline(30, color=fillcolor)

    ax1.axhline(50, lw=0.5)

    # ax1.fill_between(rsi, 70, where=(rsi >= 70), facecolor=fillcolor, edgecolor=fillcolor)
    # ax1.fill_between(rsi, 30, where=(rsi <= 30), facecolor=fillcolor, edgecolor=fillcolor)
    ax1.text(0.6, 0.9, '>70 = overbought', va='top', transform=ax1.transAxes, fontsize=textsize)
    ax1.text(0.6, 0.1, '<30 = oversold', transform=ax1.transAxes, fontsize=textsize)
    ax1.set_ylim(0, 100)
    ax1.set_yticks([30, 70])
    ax1.text(0.025, 0.95, 'RSI (14)', va='top', transform=ax1.transAxes, fontsize=textsize)
    ax1.set_title('%s,  %s interval' % (coin, timeframe))

    # plot the price and volume data
    '''
    dx = r.adj_close - r.close
    low = r.low + dx
    high = r.high + dx

    deltas = np.zeros_like(prices)
    deltas[1:] = np.diff(prices)
    up = deltas > 0
    ax2.vlines(r.date[up], low[up], high[up], color='black', label='_nolegend_')
    ax2.vlines(r.date[~up], low[~up], high[~up], color='black', label='_nolegend_')
    '''

    ma20 = moving_average(prices[-wins:], 20, type='simple')
    # ma200 = moving_average(prices, 200, type='simple')

    linema20, = ax2.plot(ma20, color='orange', lw=1, label='MA (20)')

    lineprice = ax2.plot(prices[-wins:], color='red', lw=1.5, label='price')
    if trades:
        lines_start = [(x.ixstart, x.prices[0]) for x in trades if x.coin == coin]
        lines_end = [(x.ixend, x.prices[-1]) for x in trades if x.coin == coin]

        lines = zip(lines_start, lines_end)

        lc = mc.LineCollection(lines, colors="b", linewidths=3, label='trades')
        ax2.add_collection(lc)
        # ax2.autoscale()
        # ax2.margins(0.1)

        # plot profit

        netprof = sum([x.netprof for x in trades])
        ntrades = sum([len(x.prices) - 1 for x in trades])

        ttext = " trade intervals= %s\n net profit= %s perc" % (str(ntrades), str(round(netprof, 1)))
        # print ttext

        ax2.text(len(prices) - len(prices) / 5, max(prices) - max(prices) / 30, ttext, fontsize=10)

    #### OTHER INDICATORS

    ax2.plot(sar, "o", color='y', lw=0.3, mfc='none', label='SAR')

    # linema200, = ax2.plot(r.date, ma200, color='red', lw=2, label='MA (200)')

    '''
    last = r[-1]
    s = '%s O:%1.2f H:%1.2f L:%1.2f C:%1.2f, V:%1.1fM Chg:%+1.2f' % (
        today.strftime('%d-%b-%Y'),
        last.open, last.high,
        last.low, last.close,
        last.volume*1e-6,
        last.close - last.open)
    t4 = ax2.text(0.3, 0.9, s, transform=ax2.transAxes, fontsize=textsize)
    '''

    props = font_manager.FontProperties(size=10)
    leg = ax2.legend(loc='center left', shadow=True, fancybox=True, prop=props)
    leg.get_frame().set_alpha(0.5)

    '''

    volume = (r.close*r.volume)/1e6  # dollar volume in millions
    vmax = volume.max()
    poly = ax2t.fill_between(r.date, volume, 0, label='Volume', facecolor=fillcolor, edgecolor=fillcolor)
    ax2t.set_ylim(0, 5*vmax)
    ax2t.set_yticks([])

    '''

    # ax3.plot(macd[-wins:], color='grey', lw=1)
    # ax3.plot(macdsignal[-wins:], color='blue', lw=1)
    ax3.plot(macd[-wins:] - macdsignal[-wins:], color='black', lw=2)
    plt.axhline(y=0, color='b', linestyle='-')

    ax3.fill_between(macd[-wins:] - macdsignal[-wins:], 0, alpha=0.5, facecolor=fillcolor, edgecolor=fillcolor)

    nslow = 26;
    nfast = 12;
    nema = 9
    ax3.text(0.025, 0.95, 'MACD (%d, %d, %d)' % (nfast, nslow, nema), va='top',
             transform=ax3.transAxes, fontsize=textsize)

    '''
    #ax3.set_yticks([])
    # turn off upper axis tick labels, rotate the lower ones, etc
    for ax in ax1, ax2, ax2t, ax3:
        if ax != ax3:
            for label in ax.get_xticklabels():
                label.set_visible(False)
        else:
            for label in ax.get_xticklabels():
                label.set_rotation(30)
                label.set_horizontalalignment('right')

        ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')

    '''

    plt.show()


#####
# FIRST get your CANDLES with pyhon-binance
# compute the indexes
serie = Sw(candles)
# plot with matplotlib
plotSerie(serie)