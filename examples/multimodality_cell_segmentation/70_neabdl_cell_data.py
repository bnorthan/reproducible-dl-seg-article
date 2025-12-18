"""
Script version of 68_neabdl_cell_data.ipynb for easier debugging.
Replicates the notebook's behavior using a plain Python script.
"""

import os
from pathlib import Path
import numpy as np
import napari
from cellpose import models, io  # kept to mirror notebook imports
from napari_easy_augment_batch_dl import easy_augment_batch_dl
from napari_easy_augment_batch_dl.frameworks.micro_sam_instance_framework import (
    MicroSamInstanceFramework,
)
import appose_cellpose_instance_framework  # ensure this module is discoverable on PYTHONPATH
from qtpy import QtWidgets, QtCore

class WideScroll(QtWidgets.QScrollArea):
    def sizeHint(self):
        return QtCore.QSize(500, 300)  # width=900, height arbitrary

def main():
    # Initialize napari and the Easy Augment Batch DL widget
    viewer = napari.Viewer()
    batch_dl = easy_augment_batch_dl.NapariEasyAugmentBatchDL(viewer, label_only=False)

    scroll = WideScroll()
    scroll.setWidgetResizable(True)
    scroll.setWidget(batch_dl)
    viewer.window.add_dock_widget(
        scroll
    )

    # Choose parent directory by number (consistent with other notebooks)
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent.parent

    parent_options = [
        repo_root / "data" / "Blood cell Cancer [ALL]" / "benign",
        repo_root / "data" / "Blood cell Cancer [ALL]" / "[Malignant] Pre-B",
        repo_root / "data" / "Blood cell Cancer [ALL]" / "reproducible",
        repo_root / "data" / "addhopin blood cells" / "subset",
        repo_root / "data" / "SOTA",
    ]

    # Index guide (set selection_index below):
    # [0] data/Blood cell Cancer [ALL]/benign
    # [1] data/Blood cell Cancer [ALL]/[Malignant] Pre-B
    # [2] data/Blood cell Cancer [ALL]/reproducible
    # [3] data/addhopin blood cells/subset
    # [4] data/SOTA

    selection_index = -1

    # Show options and choose parent_dir
    print("Available parent directories:")
    for i, p in enumerate(parent_options):
        print(f"[{i}] {p}")
    print(f"Selected index: {selection_index}")

    if selection_index == -1:
        start_dir = str((repo_root / "data").resolve())
        chosen = QtWidgets.QFileDialog.getExistingDirectory(
            None,
            "Select Parent Directory",
            start_dir,
            QtWidgets.QFileDialog.ShowDirsOnly,
        )
        parent_dir = chosen if chosen else str(parent_options[0])
    else:
        parent_dir = str(parent_options[selection_index])
    
    # cellpose3 environment path selection
    # cellpose3_env_path = r"C:\\Users\\bnort\\work\\ImageJ2022\\tnia\\reproducible-dl-seg-article\\pixi\\microsam_cellpose3\\.pixi\\envs\\default"
    cellpose3_env_path = None
    if cellpose3_env_path is None:
        start_env = str((repo_root / "pixi").resolve())
        chosen_env = QtWidgets.QFileDialog.getExistingDirectory(
            None,
            "Select Cellpose3 environment folder (.pixi/ envs / default)",
            start_env,
            QtWidgets.QFileDialog.ShowDirsOnly,
        )
        if chosen_env:
            cellpose3_env_path = chosen_env
        else:
            # Fallback to default repo location
            cellpose3_env_path = str((repo_root / "pixi" / "microsam_cellpose3" / ".pixi" / "envs" / "default").resolve())

    # Load images into the widget
    batch_dl.load_image_directory(parent_dir)

    # Optional pretrained model name
    model_name = None  # "microsam_nov2025_3.5_vitb"

    # Configure Appose Cellpose framework if available in the project
    appose_cellpose = batch_dl.deep_learning_project.frameworks["ApposeCellposeInstanceFramework"]
    appose_cellpose.appose_env_path = cellpose3_env_path
    appose_cellpose.use_appose = True

    framework_type = "Micro-sam Instance Framework"
    
    # Select the framework in the UI and sync widget state
    batch_dl.network_architecture_drop_down.setCurrentText(framework_type)
    widget = batch_dl.deep_learning_widgets[framework_type]

    # Start napari event loop
    napari.run()


if __name__ == "__main__":
    main()



