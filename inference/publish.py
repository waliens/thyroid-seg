import sys

from cytomine import Cytomine
from cytomine.utilities.descriptor_reader import read_descriptor

if __name__ == "__main__":
    with Cytomine.connect_from_cli(sys.argv[1:]):
        read_descriptor("descriptor.json")
