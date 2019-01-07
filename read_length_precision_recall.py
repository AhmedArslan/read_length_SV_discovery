import matplotlib.pyplot as plt
import pandas as pd
from argparse import ArgumentParser
from itertools import cycle
import matplotlib
matplotlib.use('Agg')


def main():
    args = get_args()
    df = pd.read_csv(filepath_or_buffer=args.pr,
                     sep="\t",
                     header=None,
                     names=['caller', 'length', 'precision', 'recall', 'opacity']) \
        .groupby("length").mean()
    marker = cycle(('+', 'x', 'v', '.', 'o', '*'))
    plt.figure()
    ax = plt.gca()
    for feat in ["precision", "recall"]:
        ax.scatter(x=df.index,
                   y=df[feat],
                   label=feat,
                   marker=next(marker),
                   s=3)
    ax.set_xscale('log')
    plt.legend(loc="lower right")
    plt.xlabel("Read length (log-transformed)")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.savefig("length-vs-pr.png")


def get_args():
    parser = ArgumentParser(
        description="Plot precision and recall in function of increasing read length")
    parser.add_argument("pr", help="file with 5 columns, of which 3 and 4 are precision and recall")
    return parser.parse_args()


if __name__ == '__main__':
    main()
