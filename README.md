# reproducible-dl-seg-article
This repo contains example for reproducible deep learning segmentation article

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

https://www.dropbox.com/scl/fo/t737rmz43wdyeaq03p3k5/AK0UPRFxvwz0FiQu4oa2vmI?rlkey=5cs7w4esi77tsz6if69dqbig7&st=juq9k0ng&dl=0

	<a href="https://www.dropbox.com/scl/fo/t737rmz43wdyeaq03p3k5/AK0UPRFxvwz0FiQu4oa2vmI?rlkey=5cs7w4esi77tsz6if69dqbig7&st=juq9k0ng&dl=0">Open test images on Dropbox</a>
- Direct download (HTML):
	<a href="https://www.dropbox.com/scl/fo/t737rmz43wdyeaq03p3k5/AK0UPRFxvwz0FiQu4oa2vmI?rlkey=5cs7w4esi77tsz6if69dqbig7&st=juq9k0ng&dl=1">Download test images (.zip)</a>
- For relative links in the examples to work properly, after downloading put the image in this repo under: `data/test_images`
