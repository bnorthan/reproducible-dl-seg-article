from napari_easy_augment_batch_dl.frameworks.base_framework import BaseFramework, LoadMode
import numpy as np
from tnia.deeplearning.dl_helper import collect_training_data
import cellpose
from cellpose import models, io
from dataclasses import dataclass, field
from tnia.deeplearning.dl_helper import quantile_normalization
import os
from cellpose import train

@dataclass
class ApposeCellposeInstanceFramework(BaseFramework):
    """
    ApposeCellpose Instance Framework

    This framework is used to train a CellPose Instance Segmentation model via Appose.
    """
    
    # below are the parameters that are harvested for automatic GUI generation

    # first set of parameters have advanced False and training False and will be shown in the main dialog
    diameter: float = field(metadata={'type': 'float', 'harvest': True, 'advanced': False, 'training': False, 'min': 0.0, 'max': 500.0, 'default': 30.0, 'step': 1.0})
    bsize_pred: int = field(metadata={'type': 'int', 'harvest': True, 'advanced': False, 'training': False, 'min': 128, 'max': 2048, 'default': 224, 'step': 1})
    prob_thresh: float = field(metadata={'type': 'float', 'harvest': True, 'advanced': False, 'training': False, 'min': -10.0, 'max': 10.0, 'default': 0.0, 'step': 0.1})
    flow_thresh: float = field(metadata={'type': 'float', 'harvest': True, 'advanced': False, 'training': False, 'min': -10.0, 'max': 10.0, 'default': 0.4, 'step': 0.1})
    chan_segment: int = field(metadata={'type': 'int', 'harvest': True, 'advanced': False, 'training': False, 'min': 0, 'max': 100, 'default': 0, 'step': 1})
    chan2: int = field(metadata={'type': 'int', 'harvest': True, 'advanced': False, 'training': False, 'min': 0, 'max': 100, 'default': 0, 'step': 1})
    niter: int = field(metadata={'type': 'int', 'harvest': True, 'advanced': False, 'training': False, 'min': 0, 'max': 100000, 'default': 200, 'step': 1, 'show_auto_checkbox':True})

    # second set of parameters have advanced True and training False and will be shown in the advanced popup dialog
    # None yet...

    # third set of parameters have advanced False and training True and will be shown in the training popup dialog
    num_epochs: int = field(metadata={'type': 'int', 'harvest': True, 'advanced': False, 'training': True, 'min': 0, 'max': 100000, 'default': 100, 'step': 1})
    bsize_train: int = field(metadata={'type': 'int', 'harvest': True, 'advanced': False, 'training': True, 'min': 128, 'max': 2048, 'default': 224, 'step': 1})
    rescale: bool = field(metadata={'type': 'bool', 'harvest': True, 'advanced': False, 'training': True, 'default': True})
    model_name: str = field(metadata={'type': 'str', 'harvest': True, 'advanced': False, 'training': True, 'default': 'cyto3', 'step': 1})
    # Appose execution controls
    use_appose: bool = field(default=True, metadata={'type': 'bool', 'harvest': True, 'advanced': False, 'training': False, 'default': True})
    appose_env_path: str = field(default='pixi/microsam_cellpose3', metadata={'type': 'str', 'harvest': True, 'advanced': True, 'training': False, 'default': 'pixi/microsam_cellpose3'})
        
    descriptor = "ApposeCellposeInstanceFramework"

    def __init__(self, parent_path: str,  num_classes: int, start_model: str = None):
        super().__init__(parent_path, num_classes)

        # start logger (to see training across epochs)
        # logger not routed to GUI but still useful if starting Napari
        # from command line or IDE
        logger = io.logger_setup()

        # if no start model passed in, set model to none and wait until user selects a model 
        if start_model is None:
            self.model = None
        # if model passed in and is type 'Cellpose' set the model
        elif type(start_model) == models.Cellpose:
            self.model = start_model
        # otherwise if a path was passed in, load the model from the path
        else:
            self.model = models.CellposeModel(gpu=True, model_type=None, pretrained_model=start_model)

        # set defaults for parameters
        self.bsize_pred = 224
        self.prob_thresh = 0.0
        self.flow_thresh = 0.4
        self.chan_segment = 0
        self.chan2 = 0

        self.niter = 200
        self.niter_auto = True
        
        self.load_mode = LoadMode.File
        
        self.num_epochs = 100
        self.bsize_train = 224
        self.rescale = True

        self.sgd = False
        
        self.major_number = int(cellpose.version.split('.')[0])
        
        self.model_name = self.generate_model_name(f'cellpose{self.major_number}')
    
        # initial model names
        if self.major_number < 4:
            self.model_names = ['cyto3', 'tissuenet_cp3']
            self.builtin_names = ['cyto3', 'tissuenet_cp3']
            self.set_builtin_model('cyto3')
            self.diameter = 30
        else:
            self.model_names = ['cpsam']
            self.builtin_names = ['cpsam']
            self.set_builtin_model('cpsam')
            self.diameter = 50
        
        # options for optimizers
        self.optimizers = ['adam', 'sgd']
        
        # we also have the normalizaton parameters
        self.quantile_low = 0.01
        self.quantile_high = 0.998


    
    def train(self, updater=None):
        """
        Training via Appose is pending... more to come.

        This stub disables training for now.
        """
        return


    def predict(self, img: np.ndarray):
        """
        Predict segmentation using CellPose via Appose only.

        Requires Appose utilities and a valid `appose_env_path`.
        """
        # Normalize consistently with training assumptions
        img_normalized = quantile_normalization(
            img,
            quantile_low=self.quantile_low,
            quantile_high=self.quantile_high,
            channels=True,
        ).astype(np.float32)

        # Appose execution (no local fallback)
        if not (self.use_appose and self.appose_env_path):
            raise RuntimeError("Appose prediction requires 'use_appose=True' and a valid 'appose_env_path'.")

        from napari_ai_lab.Segmenters.GlobalSegmenters import CellposeSegmenter
        from napari_ai_lab.Segmenters.execute_appose import execute_appose
        segmenter = CellposeSegmenter(model_type="cyto3", diameter=self.diameter)

        masks = execute_appose(img_normalized, segmenter, self.appose_env_path)
        return masks.ndarray().copy()

    def get_model_names(self):
        return self.model_names 
    
    def get_optimizers(self):
        return self.optimizers 
   
    def set_builtin_model(self, model_name):
        self.model = models.CellposeModel(gpu=True, model_type=model_name)
    
    def load_model_from_disk(self, model_path):
        self.model = models.CellposeModel(gpu=True, model_type=None, pretrained_model=model_path)
        
        # model path needs to be the base of model_path that was loaded
        # (otherwise when training there will be an extra 'models' directory createed)
        self.model_path = os.path.dirname(model_path)

        base_name = os.path.basename(model_path)
        self.model_name = base_name
        self.model_dictionary[base_name] = self.model

    def set_optimizer(self, optimizer):
        self.sgd = optimizer == 'sgd'

# this line is needed to register the framework on import
BaseFramework.register_framework('ApposeCellposeInstanceFramework', ApposeCellposeInstanceFramework)
