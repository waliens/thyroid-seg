from cytomine import Cytomine
from cytomine.models import ImageInstance


def main(argv):
    with Cytomine.connect_from_cli(argv):
        instance = ImageInstance().fetch(77150955)


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
