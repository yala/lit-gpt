import sys
from pathlib import Path
# support running without installing as a package
wd = Path(__file__).parent.parent.resolve()
sys.path.append(str(wd))
import csv

from lit_gpt.utils import CLI

COLUMN_NAMES = ["instruction", "input", "output"]


def preprocess(
        path_to_csv: str = "data/ucsf_pathology.csv",
        path_to_output: str = "data/ucsf_pathology_preprocessed.csv"
):
    """
    Preprocess UCSF Pathology dataset
    Args:
     
        path_to_csv: Location of orginial patholog dataset


    """
    print("hello world")

if __name__ == "__main__":
    CLI(preprocess)
