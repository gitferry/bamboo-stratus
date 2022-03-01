import matplotlib.pyplot as plt
import numpy as np

SMALL_SIZE = 8
MEDIUM_SIZE = 16
BIGGER_SIZE = 20

plt.rc('font', size=BIGGER_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=BIGGER_SIZE)    # legend fontsize

plt.rcParams['text.usetex'] = True

# Measurements from responsiveness.data
dead = [
    (r'SMP-HS',[
        25, 25, 25, 25, 25, 25, 25, 25, 25, 25,
        13, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        1.317, 1.762, 1.09, 2.496, 5.484, 10.439, 9.503, 12.894, 18.449, 23.587,
    ], [
       1.1, 0.8, 1.2, 1.0, 0.9, 0.9, 2, 1.5, 2.1, 1.2,
       9.4, 1.2, 0, 0, 0, 0, 0, 0, 0, 0,
       1.2, 1.5, 1, 2.1, 3.2, 3.1, 2.5, 3.1, 4.2, 2.4, 
    ],
     '--d', 'steelblue'),
    (r'\textbf{S-HS}',[
        25, 25, 25, 25, 25, 25, 25, 25, 25, 25,
        25, 25, 25, 25, 25, 25, 25, 25, 25, 25,
        25, 25, 25, 25, 25, 25, 25, 25, 25, 25,
    ], [
        0.8, 0.9, 1.1, 1.2, 0.7, 1.1, 0.9, 1.1, 0.8, 0.9,
        15.1, 14.9, 13.2, 12.9, 15.2, 16.3, 12.7, 15.2, 14.9, 13.7,
        9.9, 1.2, 0.9, 0.8, 1.1, 0.5, 0.7, 0.8, 0.9, 1.1,
    ],
    '-o', 'coral'),
    ]



def do_plot():
    f = plt.figure(1, figsize=(10,4), constrained_layout=True)
    plt.clf()
    ax = f.add_subplot(1, 1, 1)
    y = np.arange(-100, 1000, 0.2)
    time = range(1,31)
    for name, entries, errors, style, color in dead:
        plt.plot(time, entries, style, color=color, label='%s' % name, markersize=6)
        plt.errorbar(time, entries, yerr=errors, fmt=style, color=color, capsize=4)
    # plt.legend(fancybox=True,frameon=False,framealpha=0.8,loc='best')
    plt.legend(loc='best', fancybox=True)
    plt.grid(linestyle='--', alpha=0.5)
    plt.ylabel('Throughput (KTx/s)')
    plt.xlabel('Time (s)')
    plt.xlim([0,31])
    plt.ylim([0,62])
    plt.axvline(x=10,ls="dotted",c="black", alpha=0.3)
    plt.axvline(x=20,ls="dotted",c="black", alpha=0.3)
    plt.annotate("",
            xy=(10, 45), xycoords='data',
            xytext=(20, 45), textcoords='data',
            arrowprops=dict(arrowstyle="<->",
                            connectionstyle="arc3"),
            )
    plt.fill_betweenx(y, 10, 20, facecolor='red', alpha=0.1)
    plt.text(15,52,'Network\nFluctuation', horizontalalignment='center', verticalalignment='center')
    plt.savefig('async.pdf', format='pdf')
    plt.show()

if __name__ == '__main__':
    do_plot()