# Setup SAP Business Application Studio and a dev space

## [1/11] Use SAP Business Technology Platform
It is assumed that you have access to the SAP Business Technology Platform - either via your organization or via a free trial, as described in [prerequisites](../../prerequisites.md).

If you are using SAP BTP Trial, then open it: https://hanatrial.ondemand.com/

## [2/11] Open SAP Business Application Studio
If you are using the [SAP BTP free trial](https://account.hanatrial.ondemand.com/trial/#/home/trial), then open [SAP Business Application Studio trial](https://triallink.us10.trial.applicationstudio.cloud.sap/) from the "Quick Tool Access" section.

![Open BAS Trial](img/setup0010.png)

Should you have issues opening SAP Business Application Studio (for example when you have had the account for a long time), then check the steps in [this tutorial - Set Up SAP Business Application Studio for Development](https://developers.sap.com/tutorials/appstudio-onboarding.html)

## [3/11] Create a new Dev Space for CodeJam exercises

Go to your instance of SAP Business Application Studio (further referred to as "BAS").

For this SAP CodeJam exercise create a new Dev Space called `CodeJamHANAAI` of a kind **Basic** with an additional extension **Python Tools** in BAS:

|Screen element|Value|
|-|-|
|Dev Space name|`CodeJamHANAAI`|
|Kind|**Basic**|
|Additional extension|**Python Tools**|

![Create a Dev Space](img/setup0021hanaai.png)

You should see the dev space **STARTING**.

![Dev Space is Starting](img/setup0023hanaai.png)

Wait for the dev space to get into the **RUNNING** state and then open that dev space.

![Dev Space is Running](img/setup0026hanaai.png)

## [4/11] Clone the exercises from the Git repository

Once your dev space is open in the BAS, use one of the available options to clone this Git repository with exercises using the URL 👇🏼 
```sh
https://github.com/Sygyzmundovych/hana-ai-ve-kg-codejam.git
```
☝🏻 into your `project` directory in the BAS Dev Space.

![Clone the repo](img/setup0030.png)

Click **Open** to open a project in the Explorer view.

![Open a project](img/setup0040.png)

## [5/11] Open the Workspace

The cloned repository contains a file `codejam.code-workspace` and therefore you will be asked, if you want to open it. Click **Open Workspace**.

![Automatic notification to open a workspace](img/setup0042.png)

If you missed the previous dialog, then you can go to the BAS Explorer, click on the `codejam.code-workspace` file, and then click on the **Open Workspace**.

![Open a workspace](img/setup0045hanaai.png)

You should see:
* **CODEJAM** as the workspace at the root of the hierarchy of the project, and
* **`hana-ai-ve-kg-codejam`** as the name of the top level folder.

![Open a workspace](img/setup0047hanaai.png)

## [6/11] Check that the required extensions are installed

> SAP provides you with a mechanism to access third-party sites to view and download open-source, 3rd party or its own tools, libraries, or software components ("Extensions") to dev spaces in SAP Business Application Studio. Using this mechanism, you can view and install VS Code Extensions from the [VSX Open Registry](https://open-vsx.org/) at your own risk.

Go to **Extensions** using the activity bar (the left-most bar in the IDE) and type `@builtin Py` in the search bar. 

You should see **Python** and **Jupyter** extensions installed already. If you do not, then you might have missed selecting **Python Tools** as an additional extension, when created a dev space.

![Extensions to install](img/setup0051.png)

## [7/11] Disable "Exposing router ports" extension

While still in the **Extensions** activity, type `@builtin Exposing router ports` in the search bar.

Click on the **Manage** icon of that extension and then **disable** it for the workspace. You might need to **reload the window** to disable that extension as intended.

![Extension to disable](img/setup0053.png)

> While this SAP-provided extension is useful for CAP or Fiori projects, it doesn’t add value when working with Python in Jupyter Notebooks on SAP BAS.


## [8/11] Create a virtual environment with `venv` from a command line

The built-in [venv module](https://docs.python.org/3.9/library/venv.html#module-venv) in Python provides support for creating lightweight “virtual environments”. Each virtual environment has its own Python binary (which matches the version of the binary that was used to create this environment) and can have its own independent set of installed Python packages in its site directories.

Open a built-in **terminal** in BAS, eg. using the menu option.

![Open a terminal](img/setup0060.png)

Make sure you are in the `/home/user/projects/hana-ai-ve-kg-codejam` directory, e.g., using the `pwd` command.

Use `venv` to create a virtual environment for your project in the new directory `~/projects/hana-ai-ve-kg-codejam/env` by using the following command:

```shell
python3 -m venv ~/projects/hana-ai-ve-kg-codejam/.venv --upgrade-deps
```

Check that the virtual environment was successfully created:

```shell
ls -l ~/projects/hana-ai-ve-kg-codejam/.venv
```

![Create an venv](img/setup0071.png)

## [9/11] Activate the virtual environment `.venv` from a command line

Activate the virtual environment using the following command:

```shell
source ~/projects/hana-ai-ve-kg-codejam/.venv/bin/activate
```

You should see you are in a virtual environment as indicated by the `(.venv)` prefix in a shell's prompt.

![Activate the venv](img/setup0080hanaai.png)

## [10/11] Install required Python packages in the virtual environment

Install:

1. the `ipykernel` package to be able to run Python code in a Jupyter extension plus Jupyter's own [utilities for programmatic work with notebook documents](https://docs.jupyter.org/en/latest/projects/conversion.html): `nbformat` to be able to run one notebook from another, and `nbconvert` to be able to clean the output of notebooks, eg. before pushing to the Git repository,  using the following command:

    ```shell
    python -m pip install --require-virtualenv -U 'ipykernel' 'nbformat' 'nbconvert'
    ```

![Install ipykernel](img/setup0091hanaai.png)

2. the [Python machine learning client for SAP HANA](https://pypi.org/project/hana-ml/) (`hana-ml`) and other required dependencies using the following command:

    ```shell
    python -m pip install --require-virtualenv -U 'hana-ml<2.27' 'python-dotenv' 'sqlalchemy-hana' 'jupysql'
    ```

    > JFYI: To use with the old `'ipython-sql'` instead of the new and supported `jupysql'`, you would need to import `'prettytable<3.12'`
    >    ```shell
    >    python -m pip install --require-virtualenv -U 'hana-ml<2.27' 'python-dotenv' 'sqlalchemy-hana' 'ipython-sql' 'prettytable<3.12'
    >    ```

3. Install the [LangChain integration for SAP HANA Cloud](https://pypi.org/project/langchain-hana/) that integrates LangChain with SAP HANA Cloud to make use of vector search, knowledge graph, and further in-database capabilities as part of LLM-driven applications, plus the remaining required dependencies using the following command:

    ```shell
    python -m pip install --require-virtualenv -U 'langchain-hana' 'Markdown' 'markdownify' 'webcolors' 'pillow'
    ```

## [11/11] Open the "Check Setup" notebook from the exercises

In your BAS hide the terminal.

![Hide the terminal](img/setup0108.png)

Go to Explorer and open a [`scripts/01-check_setup.ipynb`](../01-check_setup.ipynb) notebook. 

The notebook should open in a Jupyter extension.

Check that the kernel of the notebook is set to `.venv` (the virtual environment you set up earlier).

![Select the kernel](img/setup0112.png)

## 🤓 Now you are ready to use SAP Business Application Studio to go one-by-one through exercises! 

### Engage, learn and enjoy!