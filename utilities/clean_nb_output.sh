#!/bin/sh

# Clear the output of all Jupyter notebooks in the ../scripts/ directory and subdirectories
# This is useful for version control, as it prevents merge conflicts due to changes in the output
# The --inplace flag overwrites the original files

find ./scripts -name "*.ipynb" -exec jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace {} \;

## Above line executes both:
# jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace ./scripts/*.ipynb
# jupyter nbconvert --ClearOutputPreprocessor.enabled=True --inplace ./scripts/*/*.ipynb
