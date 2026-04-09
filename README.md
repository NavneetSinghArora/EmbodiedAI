# Embodied AI Infrastructure Framework

> [!IMPORTANT]
> **Legal Disclaimer & Attribution**: This framework is an **adaptation** of existing research scripts and utilities designed to streamline Embodied AI research. It is specifically tailored to support environments like [AI2-THOR](https://ai2thor.allenai.org/). This project is provided for research purposes and is not intended to claim ownership of the underlying simulation technologies.

## Overview

The **Embodied AI Infrastructure Framework** is a specialized Python toolkit designed to automate and streamline the deployment of Embodied AI research environments. This framework simplifies the complex process of setting up multi-agent, multi-modal simulation environments on remote high-performance computing (HPC) clusters.

By providing a unified Command Line Interface (CLI), the framework handles SSH connectivity, Conda environment synchronization, and code deployment, allowing researchers to focus on model development rather than infrastructure overhead.

### 🔗 Primary Application: COLMAN
This infrastructure serves as the backbone for the **[COLMAN Project](https://github.com/NavneetSinghArora/COLMAN)** (Collaborative Multi-Agent Navigation). While COLMAN focuses on the implementation of textual-visual embeddings and multi-agent logic, this framework ensures those models can be trained and evaluated seamlessly across distributed university servers.

---

## 🚀 Key Features

- **Automated Remote Setup**: One-click initialization of remote server environments including directory structures and dependencies.
- **Environment Management**: Seamless synchronization of Conda environments between local and remote systems.
- **UHH Infrastructure Integration**: Built-in configurations for UHH CV servers (cvpc series, large/small systems).
- **CLI-Driven Workflow**: Intuitive command-line interface for managing configurations and deployments.
- **Robust Dependency Tracking**: Automated export and cleanup of environment specifications to ensure reproducibility.

---

## 🛠️ Local Environment Setup

The framework requires a [Conda](https://docs.conda.io/projects/conda/en/latest/) environment for optimal performance.

### 1. Installation

Clone the repository and navigate to the project root:

```bash
cd EmbodiedAI
```

Create the virtual environment using the provided specification:

```bash
conda env create -f ./resources/environment.yml
```

### 2. Activation & Initialization

Activate the environment:

```bash
conda activate EmbodiedAI
```

Install the package in editable mode to enable the `project` CLI utility:

```bash
pip install --editable .
```

Verify the installation:

```bash
project --help
```

---

## ⚙️ Configuration

Before executing remote deployments, you must configure the system properties to match your environment.

### System Configurations
Open `./resources/system_configurations.properties` to define your target systems and credentials.

> [!IMPORTANT]
> **For UHH Researchers**: You must be connected to the **University VPN** to interact with the remote servers.

#### Core Properties:
- `username`: Your university credentials.
- `system_name`: Target server (e.g., `cvpc18`, `cvpc20`).
- `system_type`: `large` (data1-backed) or `small` (scratch-backed).

---

## 🖥️ Remote Execution

There are two primary ways to execute the deployment logic:

### Method A: Configuration-Based (Recommended)
Populate your credentials in the `.properties` file and run:

```bash
project --system 'MacOS' --config 'True' 
```

### Method B: CLI-Based (On-the-fly)
Provide credentials directly via the command line:

```bash
project --system 'MacOS' --config 'False' --username '<your_username>' --password '<your_password>' 
```

---

## 🔧 Environment Maintenance

To keep environments consistent across systems, follow these maintenance procedures:

### Updating Local Environment
1. Install new dependencies via `conda install`.
2. Export the updated environment:
   ```bash
   conda env export --no-builds -n EmbodiedAI > ./resources/environment.yml
   ```
3. **Manual Fix**: Open `environment.yml` and remove the `prefix: ...` line (last line) to ensure cross-platform compatibility.

### Synchronizing Remote Dependencies
If you've added dependencies on a Linux remote server:
1. Generate an explicit list:
   ```bash
   conda list --explicit > ./resources/linux64.txt
   ```
2. The `project` CLI will automatically use this file during the next synchronization run to update the remote environment.

---

## ⚖️ License & Acknowledgements

### Acknowledgements
This work was developed at the **University of Hamburg (Informatik)** as a research utility for the COLMAN project. It is an adaptation of existing industry and academic patterns for remote environment management.

We gratefully acknowledge the researchers and developers behind [AI2-THOR](https://ai2thor.allenai.org/) (Allen Institute for AI) whose platform is the primary target for this infrastructure.

### Contributors
- **Adaptation & Maintenance**: Navneet Singh Arora
- **Institution**: University of Hamburg (Informatik)

### License
This project is open-source and intended for academic and research use. Users must adhere to the licenses of the underlying software and frameworks, including AI2-THOR's [Apache 2.0](https://github.com/allenai/ai2thor/blob/main/LICENSE) license.

---

## 🛑 Cleanup

When finished working, deactivate the environment:

```bash
conda deactivate
```
