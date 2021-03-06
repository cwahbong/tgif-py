import argparse

from tgif import (
    agent,
    friday,
    )

argparser = argparse.ArgumentParser()
argparser.add_argument("-l", "--level", type=int, required=True)


def main():
    args = argparser.parse_args()
    result = friday.start(args.level, agent.console())
    print(result)


if __name__ == "__main__":
    main()
