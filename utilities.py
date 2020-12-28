import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
from matplotlib.colors import LinearSegmentedColormap

def plot_v(V):
    
    x_range = np.arange(1, 11)
    y_range = np.arange(12, 22)
    ace_arr = np.zeros((len(y_range), len(x_range)))
    no_ace_arr = np.zeros((len(y_range), len(x_range)))
    
    for k, v in V.items():
        if k[0] < y_range[0]:
            continue
        if k[2]:
            ace_arr[y_range[-1]- k[0]][k[1]-len(x_range)] = v
        else:
            no_ace_arr[y_range[-1]- k[0]][k[1]-len(x_range)] = v
    
    fig = plt.figure(figsize=(12,6))
    fig.suptitle('Approximate State-Value Functions', fontsize=16)
    plt.subplot(121)
    plt.title('Usable ace')
    h1 = sns.heatmap(ace_arr, cmap="YlGnBu", 
                           xticklabels=x_range, yticklabels=np.flip(y_range))
    h1.set_xlabel('Dealer showing')
    h1.set_ylabel('Player sum')

    plt.subplot(122)
    plt.title('No usable ace')
    h2= sns.heatmap(no_ace_arr, cmap="YlGnBu", 
                           xticklabels=x_range, yticklabels=np.flip(y_range))
    h2.set_xlabel('Dealer showing')
    h2.set_ylabel('Player sum')

    plt.show()
    
def plot_policy(policy):
    
    x_range = np.arange(1, 11)
    y_range = np.arange(12, 22)
    ace_arr = np.zeros((len(y_range), len(x_range)))
    no_ace_arr = np.zeros((len(y_range), len(x_range)))
    
    for k, v in policy.items():
        if k[0] < y_range[0]:
            continue
        if k[2]:
            ace_arr[y_range[-1]- k[0]][k[1]-len(x_range)] = v
        else:
            no_ace_arr[y_range[-1]- k[0]][k[1]-len(x_range)] = v
            
    colors = ["#fcf6f5ff", "#89abe3ff"] 
    cmap = LinearSegmentedColormap.from_list('Custom', colors, len(colors))
    
    widths = [6, 6, 0.5]
    heights = [6]
    gs_kw = dict(width_ratios=widths, height_ratios=heights)
    
    fig, axes = plt.subplots(1, 3, figsize=(12,6),
                            gridspec_kw=gs_kw)
    fig.suptitle('Approximate Optimal Policy')
    
    axes[0].set_title("Usable ace")
    
    h1 = sns.heatmap(ace_arr, cmap=cmap, ax=axes[0], cbar=False,
                     xticklabels=x_range, yticklabels=np.flip(y_range))
    h1.set_xlabel('Dealer showing')
    h1.set_ylabel('Player sum')
    
    axes[1].set_title("No usable ace")
    
    h2 = sns.heatmap(no_ace_arr, cmap=cmap, ax=axes[1], cbar_ax=axes[2],
                     xticklabels=x_range, yticklabels=np.flip(y_range))
    h2.set_xlabel('Dealer showing')
    h2.set_ylabel('Player sum')
    colorbar = h2.collections[0].colorbar
    colorbar.set_ticks([0.25, 0.75])
    colorbar.set_ticklabels(["STICK", "HIT"])

    plt.show()