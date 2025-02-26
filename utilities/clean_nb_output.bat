:: filepath: hana-ml-py-codejam/utilities/clean_nb_output.bat
@echo off

:: Clear the output of all Jupyter notebooks in the ../scripts/ directory
for /R ..\scripts %%f in (*.ipynb) do (
    jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace "%%f"
)
