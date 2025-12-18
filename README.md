# Reproducible deep learning article  

Deep learning segmentation requires special focus on both reproducibility and repeatability. These two terms are often confused; they are related but different. 

- Repeatability refers to whether the exact same result can be obtained when the experiment is performed with the same data, code, and setup. 
- Reproducibility refers to whether similar scientific conclusions are reached when the experiment is performed with similar—but not identical—data or methods. 

This repo contains examples of how to test reproducibility between deep learning segmentation approaches; that is, we run deep learning segmentation in slightly different ways to test how reproducible the results are across different architectures (e.g., Cellpose vs MicroSAM), different versions of Cellpose (v3 vs v4), different models (cyto2, cyto3, CellposeSAM), and different parameterizations (cellprob, tile sizes, watershed-related thresholds, etc.).

## Setup Instructions

### 1. Install the Pixi Environment

Navigate to the environment directory and install dependencies:

```powershell
cd pixi\microsam_cellposesam
pixi install
```

And do the same for the pixi cellpose3 environment

```powershell
cd pixi\microsam_cellpose3
pixi install
```

### 2. Register Kernel for VS Code/Jupyter

After installation, register the environment as a Jupyter kernel.  We have added a task to the pixi.toml (for both ```microsam_cellposesam``` and ```microsam_cellpose3``` environments) that registers the kernel.  So navigate into these directories and run. 

```powershell
pixi run register-kernel
```

### 3. Launch VS Code from Pixi Shell

**Important**: To ensure native libraries (CUDA, cuDNN, PyTorch) are found, launch VS Code from within the pixi shell:

```powershell
# From pixi\microsam_cellposesam directory
pixi shell
code ..\..\
```

This ensures all environment variables and library paths are properly set.

### 4. Select Kernel in VS Code (for notebooks)

1. Open any notebook (e.g., `examples/petrography/*.ipynb`)
2. Click on the kernel selector in the top-right corner
3. Select **"DL-SEG (microsam_cellposesam)"** from the list

The kernel will now have access to all native libraries!

## Test Images (Data Source)

Test images for the examples are hosted on Dropbox. 

- Preview on Dropbox (HTML):

	<a href="https://www.dropbox.com/scl/fo/t737rmz43wdyeaq03p3k5/AK0UPRFxvwz0FiQu4oa2vmI?rlkey=5cs7w4esi77tsz6if69dqbig7&st=juq9k0ng&dl=0">Open test images on Dropbox</a>
- Direct download (HTML):
	<a href="https://www.dropbox.com/scl/fo/t737rmz43wdyeaq03p3k5/AK0UPRFxvwz0FiQu4oa2vmI?rlkey=5cs7w4esi77tsz6if69dqbig7&st=juq9k0ng&dl=1">Download test images (.zip)</a>
- For relative links in the examples to work properly, after downloading put the image in this repo under: `data/test_images`
