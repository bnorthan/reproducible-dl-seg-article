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
	<a href="https://www.dropbox.com/scl/fo/qc8viopyji4nhdftb9izo/AJAjsIpEGbwKuhawQTPjUYs?rlkey=v1jj01tmneti74a28ervptjhx&amp;st=bbxezz5w&amp;dl=0">Open test images on Dropbox</a>
- Direct download (HTML):
	<a href="https://www.dropbox.com/scl/fo/qc8viopyji4nhdftb9izo/AJAjsIpEGbwKuhawQTPjUYs?rlkey=v1jj01tmneti74a28ervptjhx&amp;st=bbxezz5w&amp;dl=1">Download test images (.zip)</a>
- Suggested location after download: `data/test_images`

Setup steps (PowerShell):

```powershell
# Create a folder for test images
New-Item -ItemType Directory -Force -Path data\test_images | Out-Null

# Option A: Manually download from the Dropbox link above and extract into data\test_images

# Option B: Use the direct-download link above (dl=1):
curl.exe -L "https://www.dropbox.com/scl/fo/qc8viopyji4nhdftb9izo/AJAjsIpEGbwKuhawQTPjUYs?rlkey=v1jj01tmneti74a28ervptjhx&st=bbxezz5w&dl=1" -o data\test_images.zip
# Expand-Archive -Path data\test_images.zip -DestinationPath data\test_images -Force
```

Optional: set an environment variable to point tools/notebooks at your test images directory.

```powershell
$env:TEST_IMAGES_DIR = (Resolve-Path .\data\test_images).Path
```

If you share the final Dropbox URL, I can replace the placeholder above and, if needed, update notebooks to reference `TEST_IMAGES_DIR` or `data/test_images` consistently.
