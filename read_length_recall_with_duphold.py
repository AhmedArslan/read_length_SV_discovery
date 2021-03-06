import matplotlib.pyplot as plt
import pandas as pd
from argparse import ArgumentParser


def main():
    args = get_args()
    df = pd.read_csv(
        filepath_or_buffer=args.pr,
        sep="\t",
        header=None,
        names=['caller', 'length', 'precision', 'recall', 'F-measure',
               'precision_duphold', 'recall_duphold', 'F-measure_duphold']) \
        .groupby("length").mean()
    plt.figure()
    ax = plt.gca()
    for feat, marker, color in zip(['recall', 'recall_duphold'],
                                   ['x', 'p'],
                                   ['orange', 'red']):
        ax.scatter(x=df.index,
                   y=df[feat],
                   label=feat,
                   marker=marker,
                   c=color,
                   s=16)
    ax.set_xscale('log')
    plt.legend(loc="lower right")
    plt.xlabel("Read length (log-transformed)")
    plt.ylim(0, 1)
    plt.tight_layout()
    plt.savefig("length-vs-r-with-duphold.png")


def get_args():
    parser = ArgumentParser(
        description="Plot precision and recall in function of increasing read length")
    parser.add_argument("pr", help="file with 6 columns")
    return parser.parse_args()


if __name__ == '__main__':
    main()
