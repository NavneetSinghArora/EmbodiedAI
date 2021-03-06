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

3. Make sure you are connected to the University's VPN. 

4. Once the basic setup is done, there are two ways to execute the main code on the remote server.
   1. Using the Configuration file.
      1. Open the ```system.configurations.properties``` file.
      2. Edit the properties according to where you want to execute the code.
      3. Once completed, run the following command:
         ```bash
         project --system 'MacOS' --config 'True' 
         ```
   2. Using the CLI interface.
      1. With this interface, there is no need to edit the ```system.configurations.properties``` file.
      2. Execute ```project --help``` to see the different set of commands with which you can run the project.
      3. Finally, use the arguments to run. Sample command will look like the following:
         ```bash
         project --system 'MacOS' --config 'False' --username '<username>' --password '<password>' 
         ```
      4. This way of execution is still under progress. If any option is missing for your execution,
         please use the method of Configuration to your convenience.
      
5. Once the code execution is completed, you will see that the code has been set-up on the remote directory. 
Entire structure including the conda virtual environment has been set up.

6. On the remote directory, go to ```<home_directory>/AI2Thor/resources``` and execute ```source activate.sh```. This  
will activate the conda environment.

7. We will soon create a main script which will execute the entire project automatically.

8. However, there are few mandatory steps which are to be followed to keep the conda environment consistent.
   1. In order to make sure this entire setup runs consistently, please execute the project everytime some changes 
   are checked in. This code will update the entire structure and will provide consistency for all the users currently developing the project.
   2. When new changes are applied to the code and new dependencies are added, please update the environment.yml file in the following way:
      1. On the remote server, run the following command:
         ```bash
         conda list --explicit > <project_directory>/resources/linux64.txt
         ```
         This command will make sure that all the dependencies required for successful execution on the remote server are captured in this file.
      2. Remove the already existing conda environment.
         ```bash
         rm -rf <home_directory>/anaconda3/envs/AI2Thor
         ```
      3. Create temporary virtual environment using:
         ```bash
         conda create --name AI2Thor --file <project_directory>/resources/linux64.txt
         ```
      4. Export the dependencies to the environment.yml file, using
         ```bash
         conda env export --no-builds -n AI2Thor > <project_directory>/resources/environment.yml
         ```
      5. Remove this temporary environment.
         ```bash
         rm -rf <home_directory>/anaconda3/envs/AI2Thor
         ```
      6. Create the stable conda environment, using
         ```bash
         conda env create -f <project_directory>/resources/environment.yml
         ```
      7. Activate the environment
         ```bash
         conda activate AI2Thor
         ```
9. Please feel free to make the changes or else, reach out to the Administrator.
