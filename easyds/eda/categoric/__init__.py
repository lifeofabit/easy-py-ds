import seaborn as sns
import pandas as pd

def conditional_bar(input_df, col1, col2, title=None, axis=None, x_label=None, y_label=None):
    target_df = pd.crosstab(input_df[col1], input_df[col2])
    target_df['Total'] = target_df.sum(axis=1)

    target_columns = list(target_df.columns.values)
    for i in target_columns:
        target_df[i] = target_df.apply(lambda x: x[i] / x['Total'], axis=1)

    top = plt.Rectangle((0,0), 1, 1, fc='red', edgecolor='none')
    bot = plt.Rectangle((0,0), 1, 1, fc='blue', edgecolor='none')

    sns.barplot(x=target_df.index, y='Total', data=target_df, color='blue', ax=axis)
    G = sns.barplot(x=target_df.index, y=target_columns[0], data=target_df, color='red', ax=axis)

    axis.legend([bot, top], [target_columns[1], target_columns[0]], loc=1, ncol=2)
    axis.draw_frame(False)

    if title:
        G.set_title(title)

    if x_label:
        G.set_xlabel(x_label)

    if y_label:
        G.set_ylabel(y_label)

    return target_df
