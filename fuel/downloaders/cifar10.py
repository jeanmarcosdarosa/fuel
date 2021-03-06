from fuel.downloaders.base import default_downloader


def cifar10(subparser):
    """Sets up a subparser to download the CIFAR-10 dataset file.

    The CIFAR-10 dataset file is downloaded from Alex Krizhevsky's
    website [ALEX].

    .. [ALEX] http://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz

    Parameters
    ----------
    subparser : :class:`argparse.ArgumentParser`
        Subparser handling the `cifar10` command.

    """
    url = 'http://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz'
    filename = 'cifar-10-python.tar.gz'
    subparser.set_defaults(
        func=default_downloader, urls=[url], filenames=[filename])
