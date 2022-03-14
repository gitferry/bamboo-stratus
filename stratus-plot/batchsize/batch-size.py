import matplotlib.pyplot as plt

SMALL_SIZE = 8
MEDIUM_SIZE = 13
BIGGER_SIZE = 16

plt.rc('font', size=BIGGER_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)    # legend fontsize

bsize = [
    ('n128-b32K',[
        # (4,703),
        (58,400),
        (62,300),
        (66,265),
        # (20,280),
        (74,350),
        (75,480),
        (77,650),
        (78,900),
        (79,1328),
    ], '-o', 'steelblue'),
    ('n128-b64K',[
        # (12,900),
        # (20,580),
        # (28,447),
        # (40,350),
        (98,415),
        (106,396),
        (122,420),
        (126,430),
        (130,590),
        (131,779),
        (130,1162),
    ], '-^', 'steelblue'),
    ('n128-128K',[
        # (28,800),
        # (36,640),
        # (44,540),
        # (52,480),
        (110,630),
        (118,600),
        (126,580),
        (130,570),
        (134,610),
        (135,812),
        (135,1302),
    ], '-*', 'steelblue'),
    ('n256-b128K',[
        (34,880),
        # (58,250),
        (42,635),
        (55,684),
        (65,746),
        (64,1582),
    ], '--p', 'coral'),
    ('n256-b256K',[ #125.3, 965
        # (8,653),
        (79,1242),
        (95,965),
        (103,1031),
        (114,1234),
        (125.4,2353),
        (125.3,2890),
    ], '--v', 'coral'),
    ('n256-b512K',[ #125.3, 965
        # (12,843),
        # (20,540),
        # (78,1654),
        (86,1651),
        # (44,320),
        (102,1363),
        (122,1532),
        (131,2365),
        (130,3102),
    ], '--d', 'coral')]

def do_plot():
    f = plt.figure(1, figsize=(7,3), constrained_layout=True)
    plt.clf()
    ax = f.add_subplot(1, 1, 1)
    for name, entries, style, color in bsize:
        throughput = []
        latency = []
        for t, l in entries:
            throughput.append(t)
            latency.append(l)
        ax.plot(throughput, latency, style, color=color, label='%s' % name, markersize=8, alpha=0.8)
    plt.legend(fancybox=True,frameon=True,framealpha=0.3,mode={"expand", None},ncol=2, loc='upper left')
    plt.grid(linestyle='--', alpha=0.5)
    plt.ylim([0,3500])
    plt.ylabel('Latency (ms)')
    plt.xlabel('Throughput (KTx/s)')
    # plt.tight_layout()
    plt.savefig('batch-size.pdf', format='pdf')
    plt.show()

if __name__ == '__main__':
    do_plot()
