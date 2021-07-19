__author__ = "Graeme Ford"
__copyright__ = "Copyright 2021, Graeme Ford"
__email__ = "graeme.ford@tuks.co.za"
__license__ = "GNU GPLv3"

import os
import json
import re
from glob import glob
from typing import List


config = dict()

with open(os.path.join("config", "config.json"), 'r') as f:
    config = json.load(f)


def GetInputFile(wildcards: object = dict()) -> str:
    """A function that returns the absolute path of a file,
    given its input name and the provided paths

    Args:
        wildcards (object): The name of the file

    Returns:
        str: The relative file path
    """
    reX = r"^([A-Z]{0,1}:{1}[\\|\/]{1,2}){0,1}(.+[\\\/])*(.+)(\.fa|\.fa\.gz|\.fa\.gz\.fai|\.fa\.gz\.dict)$"
    # regexMatches = re.search(
    #     reX,
    #     wildcards.file
    # )

    try:
        item = next(next(file for file in dataset['Files'] if re.search(reX, file).group(
            4) == wildcards.ext and re.search(reX, file).group(3) == wildcards.filename) for dataset in config["Data"])
    except Exception:
        item = ""
        print("Error: No Match Found for this input request. FILENAME: results/" +
              wildcards.filename + wildcards.ext)
    return item
