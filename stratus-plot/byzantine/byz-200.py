import matplotlib.pyplot as plt

SMALL_SIZE = 8
MEDIUM_SIZE = 16
BIGGER_SIZE = 20

plt.rc('font', size=BIGGER_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize

plt.rcParams['text.usetex'] = True

# batchsize = 512000
def do_plot():
    f, ax = plt.subplots(1,2,figsize=(10,3),constrained_layout=True)
    replicaNo = [0, 20, 40, 60]
    thru = [
    ('SMP-HS',[
        126.2,
        81.1,
        32.1,
        6.2,
    ], 'o', 'steelblue'),
    (r'\textbf{S-HS-f}',[
        117.2,
        110.2,
        84.2,
        60.1,
    ], 'p', 'coral'),
    (r'\textbf{S-HS-2f}',[
        117.2,
        112.2,
        102.1,
        92.1,
    ], '^', 'darkseagreen'),
    ]
    for name, entries, style, color in thru:
        ax[0].plot(replicaNo, entries, marker=style, mec=color, color=color, mfc='none', label='%s'%name, markersize=8)
        ax[0].set_ylabel("Throughput (KTx/s)")
        # ax[0].set_xticks(xticks)
        ax[0].set_ylim([0,150])
        # ax[0].set_xticklabels(xticks_label)
        # ax[0].set_xticklabels(("", "", "", "", "", ""))
    lat = [
    ('SMP-HS',[
        1603,
        8500,
        19322,
        19210,
    ], 'o', 'steelblue'),
    (r'\textbf{S-HS-f}',[
        2616,
        2622,
        2618,
        2616,
    ], 'p', 'coral'),
    (r'\textbf{S-HS-2f}',[
        3916,
        3922,
        3918,
        3916,
    ], '^', 'darkseagreen')
    ]
    for name, entries, style, color in lat:
        ax[1].plot(replicaNo, entries, marker=style, color=color, mec=color, mfc='none', label='%s' % name, markersize=8)
        ax[1].set_ylabel("Latency (ms)")
        ax[1].set_xticks(replicaNo)
        ax[1].set_ylim([0,10000])
    ax[0].grid(linestyle='--', alpha=0.5)
    ax[1].grid(linestyle='--', alpha=0.5)
    ax[1].legend(loc='best', fancybox=True,frameon=True,framealpha=0.3)
    f.supxlabel('\# of Byz. replicas')
    plt.savefig('byz-200.pdf', format='pdf')
    plt.show()

if __name__ == '__main__':
    do_plot()
