import matplotlib.pyplot as plt

# set the size of the graph image
plt.rcParams["figure.figsize"] = (19, 11)


def plot(p_type: str, x_axis: list, points: list, title: str, x_label: str, y_label: str, y_min_lim=0, y_max_lim=0,
         color='blue', marker='D',
         width=0.30):
    # if y_min_lim and y_max_lim are not provided then calculate them on the basis of the min and max values in
    # points variable
    if y_min_lim == 0 and y_max_lim == 0:
        y_min_lim = int(round(min(points) - 1))
        y_max_lim = int(round(max(points) + 1))
    plt.title(title)
    plt.xlabel(x_label, fontsize=3)
    plt.ylabel(y_label)
    if p_type == 'plot':
        plt.plot(x_axis, points, marker=marker, color=color)
    elif p_type == 'stem':
        plt.stem(x_axis, points, use_line_collection=True)
    elif p_type == 'bar':
        plt.bar(x_axis, points, width=width, color=color)
    # rotate the labels on x-axis
    plt.xticks(rotation=90)
    # set the minimum and maximum value of y-axis
    axes = plt.gca()
    axes.set_ylim([y_min_lim, y_max_lim])

    # Save the graph
    plt.savefig(f'graphs/{title}.png', bbox_inches='tight')
    # NOTE: If we don't place plt.show() after plt.savefig() then it will save all the graphs in one image
    plt.show()
