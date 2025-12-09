# reproducible-dl-seg-article
This repo contains example for reproducible deep learning segmentation article

## Setup Instructions

### 1. Install the Pixi Environment

Navigate to the environment directory and install dependencies:

```powershell
cd pixi\microsam_cellposesam
pixi install
```

### 2. Register Kernel for VS Code/Jupyter

After installation, register the environment as a Jupyter kernel:

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

### 4. Select Kernel in VS Code

1. Open any notebook (e.g., `examples/petrography/*.ipynb`)
2. Click on the kernel selector in the top-right corner
3. Select **"DL-SEG (microsam_cellposesam)"** from the list

The kernel will now have access to all native libraries!
