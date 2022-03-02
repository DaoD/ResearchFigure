import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
import torch

# fname must be the absolute path !!!
myfont1 = FontProperties(fname="/Users/yutao/Desktop/TIMES.ttf", size=22)  
myfont2 = FontProperties(fname='/Users/yutao/Desktop/LinLibertine_R.ttf', size=32)
myfont3 = FontProperties(fname='/Users/yutao/Desktop/LinLibertine_R.ttf', size=22)
myfont4 = FontProperties(fname='/Users/yutao/Desktop/LinLibertine_R.ttf', size=26)
myfont5 = FontProperties(fname='/Users/yutao/Desktop/LinLibertine_R.ttf', size=24)
myfont6 = FontProperties(fname='/Users/yutao/Desktop/LinLibertine_R.ttf', size=20)

def draw_figrue_1():
    r2_1 = [0.740, 0.746, 0.748, 0.756, 0.744, 0.750, 0.761, 0.744, 0.742, 0.734]
    r10_1 = [0.376, 0.384, 0.388, 0.387, 0.377, 0.379, 0.398, 0.373, 0.378, 0.367]
    mrr = [0.489, 0.485, 0.491, 0.489, 0.493, 0.489, 0.502, 0.491, 0.498, 0.494]

    fig, ax = plt.subplots(3, sharex=True, figsize=(8, 6))
    plt.subplots_adjust(hspace=0)

    x_ticks = np.linspace(0.1, 1.0, 10)
    x_labels = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    y_ticks1 = np.linspace(0.72, 0.77, 6)
    y_ticks2 = np.linspace(0.48, 0.51, 4)
    y_ticks3 = np.linspace(0.36, 0.4, 5)
    ax[0].plot(x_labels, r2_1, 'go-', label="R2@1")
    ax[1].plot(x_labels, mrr, 'b^-', label="MRR")
    ax[2].plot(x_labels, r10_1, 'rv-', label="R10@1")
    ax[2].set_xticks(x_ticks)
    ax[2].xaxis.set_tick_params(labelsize=14)
    ax[0].set_yticks(y_ticks1)
    ax[1].set_yticks(y_ticks2)
    ax[2].set_yticks(y_ticks3)
    ax[0].yaxis.set_tick_params(labelsize=14)
    ax[1].yaxis.set_tick_params(labelsize=14)
    ax[2].yaxis.set_tick_params(labelsize=14)
    ax[0].set_ylim(0.725, 0.77)
    ax[1].set_ylim(0.475, 0.51)
    ax[2].set_ylim(0.365, 0.4)
    ax[0].tick_params(bottom=False)
    ax[0].spines['bottom'].set_visible(False)
    ax[1].spines['top'].set_visible(False)
    ax[1].spines['bottom'].set_visible(False)
    ax[2].spines['top'].set_visible(False)
    for i, txt in enumerate(r2_1):
        t = ax[0].annotate("%.3f" % txt, (x_labels[i], r2_1[i] + 0.002), ha='center')
        t.set_fontsize(14)
    for i, txt in enumerate(mrr):
        t = ax[1].annotate("%.3f" % txt, (x_labels[i], mrr[i] + 0.002), ha='center')
        t.set_fontsize(14)
    for i, txt in enumerate(r10_1):
        t = ax[2].annotate("%.3f" % txt, (x_labels[i], r10_1[i] + 0.002), ha='center')
        t.set_fontsize(14)
    d = .005
    kwargs = dict(transform=ax[0].transAxes, color='k', clip_on=False)
    ax[0].plot((-d, +d), (-d, +d), **kwargs)
    ax[0].plot((1 - d, 1 + d), (-d, +d), **kwargs)

    kwargs.update(transform=ax[1].transAxes)
    ax[0].plot((-d, +d), (1 - d, 1 + d), **kwargs)
    ax[0].plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)

    kwargs = dict(transform=ax[1].transAxes, color='k', clip_on=False)
    ax[1].plot((-d, +d), (-d, +d), **kwargs)
    ax[1].plot((1 - d, 1 + d), (-d, +d), **kwargs)

    kwargs.update(transform=ax[2].transAxes)
    ax[1].plot((-d, +d), (1 - d, 1 + d), **kwargs)
    ax[1].plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)

    ax[0].grid(alpha=0.8, linestyle='-')
    ax[0].legend(prop={'size': 16})
    ax[1].grid(alpha=0.8, linestyle='-')
    ax[1].legend(prop={'size': 16}, loc="upper left")
    ax[2].grid(alpha=0.8, linestyle='-')
    ax[2].legend(prop={'size': 16})
    plt.xlabel(r'$\lambda$', fontsize=14)
    plt.tight_layout()
    # plt.show()
    plt.savefig("./figure1.pdf")

def draw_figure_2():
    label_list = ['0', '(0,0.2)', '[0.2,0.4)', '[0.4,0.6)', '[0.6,0.8)', '[0.8,1]']
    p_strict_sws = [0.2091269841269841, 0.3030013247226363, 0.44205425061906556, 0.4910003050246953, 0.5527537277537277, 0.49428571428571433]
    p_weak_sws = [0.22106392106392106, 0.3205253648901191, 0.46131253006253015, 0.510060828963268, 0.563666426166426, 0.5276190476190475]
    p_strict_sw = [0.22857679107679105, 0.26725332954841174, 0.4182105445994338, 0.47823062213306106, 0.5194083694083694, 0.5461904761904762]
    p_weak_sw = [0.23413234663234656, 0.2731276464883025, 0.43141846151105434, 0.4834700078602517, 0.5233766233766234, 0.5461904761904762]
    # p_strict_dua = [0.1721364221364221, 0.18431800439997173, 0.23367415335007943, 0.27002281819354973, 0.30228475228475227, 0.2752380952380952]
    # p_weak_dua = [0.1828346203346203, 0.22036450571286653, 0.26307597580745756, 0.2975747603796383, 0.3290043290043291, 0.3038095238095238]
    p_strict_msn = [0.19460531960531957, 0.233750413975824, 0.3419656218267334, 0.4102632011168599, 0.48554593554593556, 0.5342857142857144]
    p_weak_msn = [0.21825396825396817, 0.27174348875168575, 0.37706151016336237, 0.4297240699679726, 0.512000962000962, 0.5676190476190476]
    coverage_ratio = [0.09181141439205956, 0.3027295285359802, 0.40074441687344914, 0.15384615384615385, 0.04466501240694789, 0.00620347394540943]
    
    x = np.arange(6)

    total_width, n = 0.8, 7  # 有多少个类型，只需更改n即可
    width = total_width / n
    x = x - (total_width - width) / 2

    plt.figure(figsize=(16, 8))
    plt.bar(x, p_strict_sws, width=width, label='P strict of SW*', hatch=2*'//', edgecolor='w')
    plt.bar(x + width, p_weak_sws, width=width, label='P weak of SW*', hatch=2*'.', edgecolor='w')
    # plt.bar(x + 2 * width, num_list_3, width=width, label='CEOS', hatch=4*'\\', edgecolor='w')
    plt.bar(x + 2 * width, p_strict_sw, width=width, label='P strict of SW', hatch=4*'//', edgecolor='w')
    plt.bar(x + 3 * width, p_weak_sw, width=width, label='P weak of SW', hatch=4*'.', edgecolor='w')
    plt.bar(x + 4 * width, p_strict_msn, width=width, label='P strict of MSN', hatch=4*'\\', edgecolor='w')
    plt.bar(x + 5 * width, p_weak_msn, width=width, label='P weak of MSN', hatch='.', edgecolor='w')
    plt.bar(x + 6 * width, coverage_ratio, width=width, label='Percentage(%)', hatch=2*'\\', edgecolor='w')
    plt.xticks([index + 3 * width for index in x], label_list, fontproperties=myfont1)
    plt.yticks(fontproperties=myfont1)
    plt.legend(prop=myfont1)
    plt.tight_layout()
    plt.savefig("./figure2.pdf", format="pdf")
    # plt.show()

def draw_figure_3():
    coca_map = [0.552700927070873, 0.543403267053195, 0.4876967263751009]
    duet_map = [0.4031463588267755, 0.39543176001219477, 0.384521141975356]
    cars_map = [0.4331293302456068, 0.4232857811441042, 0.3982938125484895]
    hba_map = [0.5315612397803664, 0.5264386514846908, 0.4780848161335488]

    coca_ndcg3 = [0.5502390266892377, 0.5390684662493154, 0.48418425092634415]
    duet_ndcg3 = [0.38460203985733127, 0.3762263757389652, 0.3671913235364889]
    cars_ndcg3 = [0.41548140827936514, 0.4038658384980803, 0.38140468885004214]
    hba_ndcg3 = [0.5277788066111762, 0.5212777296124101, 0.4729313905099101]

    x = np.arange(3)
    total_width, n = 0.8, 4  # 有多少个类型，只需更改n即可
    width = total_width / n
    x = x - (total_width - width) / 2
    label_list = ["Short", "Medium", "Long"]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    ax1.bar(x, duet_map, width=width, label='Duet', hatch=2 * '\\', edgecolor='w', color="#d62728")
    ax1.bar(x + width, cars_map, width=width, label='CARS', hatch=2 * '//', edgecolor='w', color="#1f77b4")
    ax1.bar(x + 2 * width, hba_map, width=width, label='HBA', hatch=2 * '.', edgecolor='w', color="#ff7f0e")
    ax1.bar(x + 3 * width, coca_map, width=width, label='COCA', hatch=4 * '\\', edgecolor='w', color="#2ca02c")
    ax1.set_xticks([index + 1.5 * width for index in x])
    ax1.set_xticklabels(label_list, fontproperties=myfont2)
    # plt.yticks(y_label)
    ax1.set_yticklabels(["0.30", "0.35", "0.40", "0.45", "0.50", "0.55", "0.60"], fontproperties=myfont2)
    ax1.set_ylim(0.3, 0.6)
    ax1.legend(prop=myfont3)
    ax1.set_ylabel("MAP", fontproperties=myfont2)

    ax2.bar(x, duet_ndcg3, width=width, label='Duet', hatch=2 * '\\', edgecolor='w', color="#d62728")
    ax2.bar(x + width, cars_ndcg3, width=width, label='CARS', hatch=2 * '//', edgecolor='w', color="#1f77b4")
    ax2.bar(x + 2 * width, hba_ndcg3, width=width, label='HBA', hatch=2 * '.', edgecolor='w', color="#ff7f0e")
    ax2.bar(x + 3 * width, coca_ndcg3, width=width, label='COCA', hatch=4 * '\\', edgecolor='w', color="#2ca02c")
    ax2.set_xticks([index + 1.5 * width for index in x])
    ax2.set_xticklabels(label_list, fontproperties=myfont2)
    ax2.set_yticklabels(["0.30", "0.35", "0.40", "0.45", "0.50", "0.55", "0.60"], fontproperties=myfont2)
    ax2.set_ylim(0.3, 0.6)
    ax2.legend(prop=myfont3)
    ax2.set_ylabel("NDCG@3", fontproperties=myfont2)

    plt.tight_layout()
    plt.savefig("./figure3.pdf", format="pdf")

def draw_figure_4():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    x = [0.2, 0.4, 0.6, 0.8, 1]
    map = [0.5458, 0.5469, 0.5468, 0.5496, 0.5500]
    ndcg3 = [0.5429, 0.5433, 0.5441, 0.5475, 0.5478]
    nocl_map = [0.5341, 0.5341, 0.5341, 0.5341, 0.5341]
    nocal_ndcg3 = [0.5296, 0.5296, 0.5296, 0.5296, 0.5296]
    x_value = [0.2, 0.4, 0.6, 0.8, 1.0]
    x_label = ["20%", "40%", "60%", "80%", "100%"]
    ax1.plot(x, map, 'o-', color='#1f77b4', label="CL-MAP")
    ax1.plot(x, ndcg3, '^-' ,color='#ff7f0e', label="CL-NDCG@3")
    ax1.plot(x, nocl_map, 'o--', color='#1f77b4', label="None-MAP")
    ax1.plot(x, nocal_ndcg3, '^--' ,color='#ff7f0e', label="None-NDCG@3")
    ax1.set_ylim(0.525, 0.551)
    ax1.set_xticks(x_value)
    ax1.set_xticklabels(x_label, fontproperties=myfont4)
    ax1.set_yticklabels(["0.525", "0.530", "0.535", "0.540", "0.545", "0.550"], fontproperties=myfont4)
    ax1.legend(prop=myfont3, loc="center right", bbox_to_anchor=(1.0, 0.55))
    ax1.set_xlabel("Data Amount", fontproperties=myfont4)
    ax1.grid(alpha=0.3, linestyle='--')

    map = [0.5462, 0.5472, 0.5481, 0.5500, 0.5497]
    ndcg3 = [0.5433, 0.5450, 0.5452, 0.5478, 0.5476]
    nocl_map = [0.5341, 0.5341, 0.5341, 0.5341, 0.5341]
    nocal_ndcg3 = [0.5296, 0.5296, 0.5296, 0.5296, 0.5296]

    x = [1, 2, 3, 4, 5]
    ax2.plot(x, map, 'o-', color='#1f77b4', label="CL-MAP")
    ax2.plot(x, ndcg3, '^-' ,color='#ff7f0e', label="CL-NDCG@3")
    ax2.plot(x, nocl_map, 'o--', color='#1f77b4', label="None-MAP")
    ax2.plot(x, nocal_ndcg3, '^--' ,color='#ff7f0e', label="None-NDCG@3")
    ax2.set_ylim(0.525, 0.551)
    ax2.set_xticks(x)
    ax2.set_xticklabels([1, 2, 3, 4, 5], fontproperties=myfont4)
    ax2.set_yticklabels(["0.525", "0.530", "0.535", "0.540", "0.545", "0.550"], fontproperties=myfont4)
    ax2.legend(prop=myfont3, loc="center right", bbox_to_anchor=(1.0, 0.55))
    ax2.set_xlabel("Training Epoch", fontproperties=myfont4)
    ax2.grid(alpha=0.3, linestyle='--')

    plt.tight_layout()
    plt.savefig("./figure4.pdf")

def draw_figure_5():
    pmr_5_pred = [8.23, 12.54, 15.01, 14.78, 15.05, 14.74]
    pmr_5_ground = [33.85, 65.88, 89.50, 100.0, 100.0, 100.0]
    pmr_3_pred = [10.72, 17.57, 18.42, 18.44, 18.75, 18.89]
    pmr_3_ground = [60.47, 100.0, 100.0, 100.0, 100.0, 100.0]
    pmr_2_pred = [17.33, 17.53 ,17.43, 17.59, 17.53, 17.61]
    pmr_2_ground = [100.0, 100.0, 100.0, 100.0, 100.0, 100.0]
    x_labels = [1, 2, 3, 4, 5, 6]

    fig, ax = plt.subplots(2, sharex=True, figsize=(9, 6))
    plt.subplots_adjust(hspace=0.01)

    y_ticks1 = np.linspace(30, 100, 8)
    y_ticks2 = np.linspace(6, 20, 8)

    ax[1].plot(x_labels, pmr_5_pred, 'o-', label=r'$d=1$')
    ax[1].plot(x_labels, pmr_3_pred, 'o-', label=r'$d=2$')
    ax[1].plot(x_labels, pmr_2_pred, 'o-', label=r'$d=4$')
    ax[0].plot(x_labels, pmr_5_ground, 'o--', label=r'$d=1$ ground-turth')
    ax[0].plot(x_labels, pmr_3_ground, 'o--', label=r'$d=2$ ground-turth')
    ax[0].plot(x_labels, pmr_2_ground, 'o--', label=r'$d=4$ ground-turth')

    ax[1].xaxis.set_tick_params(labelsize=14)
    ax[0].set_yticks(y_ticks1)
    ax[1].set_yticks(y_ticks2)
    ax[0].yaxis.set_tick_params(labelsize=14)
    ax[1].yaxis.set_tick_params(labelsize=14)
    ax[0].tick_params(bottom=False)
    ax[0].spines['bottom'].set_visible(False)
    ax[1].spines['top'].set_visible(False)
    d = .008
    kwargs = dict(transform=ax[0].transAxes, color='k', clip_on=False)
    ax[0].plot((-d, +d), (-d, +d), **kwargs)
    ax[0].plot((1 - d, 1 + d), (-d, +d), **kwargs)
    kwargs.update(transform=ax[1].transAxes)
    ax[0].plot((-d, +d), (1 - d, 1 + d), **kwargs)
    ax[0].plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)

    ax[0].grid(alpha=0.8, linestyle='-')
    legend = ax[0].legend(prop={'size': 15}, title='PMR')
    legend.get_title().set_fontsize('15')
    ax[1].grid(alpha=0.8, linestyle='-')
    legend = ax[1].legend(prop={'size': 15}, title='PMR')
    legend.get_title().set_fontsize('15')
 
    plt.xlabel(r'$L$', fontsize=16)
    plt.tight_layout()
    plt.savefig('./figure5.pdf')

def draw_figure_6():
    node_sne, inp_sne = torch.load("./tsne_results")
    (fig, subplots) = plt.subplots(1, 2, figsize=(10, 4))
    c_target = [0, 1, 2, 3, 4]

    ax = subplots[0]
    for i in range(len(inp_sne[0])):
        result_x = [inp_sne[0][i, 0], inp_sne[1][i, 0], inp_sne[2][i, 0], inp_sne[3][i, 0], inp_sne[4][i, 0]]
        result_y = [inp_sne[0][i, 1], inp_sne[1][i, 1], inp_sne[2][i, 1], inp_sne[3][i, 1], inp_sne[4][i, 1]] 
        im = ax.scatter(result_x, result_y, c=c_target, cmap="jet", s=1)
    ax.axis('off')
    ax.set_title('(a) Input embeddings', y=-0.1, fontproperties=myfont5)

    ax = subplots[1]
    for i in range(len(node_sne[0])):
        result_x = [node_sne[0][i, 0], node_sne[1][i, 0], node_sne[2][i, 0], node_sne[3][i, 0], node_sne[4][i, 0]]
        result_y = [node_sne[0][i, 1], node_sne[1][i, 1], node_sne[2][i, 1], node_sne[3][i, 1], node_sne[4][i, 1]]
        im = ax.scatter(result_x, result_y, c=c_target, cmap="jet", s=1)
    ax.axis('off')

    ax.set_title('(b) Updated representations', y=-0.1, fontproperties=myfont5)
    
    divider = make_axes_locatable(plt.gca())
    cax = divider.append_axes("right", "3%", pad="7%")
    cbar = plt.colorbar(im, cax=cax)
    cbar.set_ticks([0, 4])
    cbar.set_ticklabels(["First\nSentences", "Last\nSentence"])
    for label in cbar.ax.get_yticklabels():
        label.set_fontproperties(myfont6)
    cbar.ax.tick_params(size=0)
    cbar.outline.set_visible(False)
    plt.tight_layout()
    plt.savefig("./figure6.png", dpi=300)  # tsne figure has a lot of points, use png instead of pdf

# draw_figrue_1()
# draw_figure_2()
# draw_figure_3()
# draw_figure_4()
# draw_figure_5()
# draw_figure_6()