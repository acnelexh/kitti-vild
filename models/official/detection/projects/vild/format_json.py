from pathlib import Path
import json

file = Path("./Amodal-Instance-Segmentation-through-KINS-Dataset/instances_train.json")

with open(file) as f:
    dict = json.load(f)
    with open("./instances_train.json", "w") as o:
        json.dump(dict, o, indent=2)