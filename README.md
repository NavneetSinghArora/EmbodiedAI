# Embodied AI Project

---
## Environment

---
### Installation

The code works best with the [conda](https://docs.conda.io/projects/conda/en/latest/) 
environment. Please complete the conda setup before moving forward with the project.
Once installed, follow the steps given below to set up the code environment.

1. Change the current working directory to project's root directory. 
    ```bash
    cd (parent_directory)/EmbodiedAI
    ```
2. Run the command to create the conda environment. This will create a conda virtual 
environment with all the required project dependencies.
    ```bash
    conda env create -f ./resources/environment.yml
    ```

### Activating the Environment
Once finished with the installation, execute this command to activate the conda environment.

```bash
conda activate EmbodiedAI
```

### Updating the Environment

Prefer using ```conda``` over ```pip``` command to install any new dependencies. However, once 
the new dependencies are installed, execute this command to update the environment.yml file.

```bash
conda env export --no-builds -n EmbodiedAI > ./resources/environment.yml
```

Once the execution completes, open the environment.yml file and delete the last line having this
structure ```prefix: ...```. This is a bug from the conda's end and needs to be handled manually everytime the environment is updated.

### Deactivating the Environment
Once finished working, execute this command to deactivate the conda environment.

```bash
conda deactivate
```

## Configuration

---
First step before executing the code is to edit the configuration properties. Open the 
```./resources/system_configuration.properties``` file. This file consists of various properties
which are to be set for specific execution. Please read the instruction written in the form of 
comments in the file and set the properties accordingly.

> **NOTE:**
> These properties and this way of execution is only valid for people/students of University of 
> Hamburg who are executing this code on the remote servers of the university. For local 
> installation, please ignore this step and move to the next set of steps. 

## Execution

---
1. Go to the root directory of the project.

   ```bash
   cd <system_path>/EmbodiedAI
   ```

2. Execute the following script. This script will set up the command line interface to run and 
execute the project seamlessly.

   ```bash
   pip install --editable .
   ```

   To verify that the command has been executed successfully, execute the following command.

   ```bash
   project --help
   ```

   This should show the help option available in this project. If this command gives an error, please check the above steps or reach out to 
the team of this project.

3. 
