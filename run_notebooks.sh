
#!/bin/bash

# List of notebooks to run
notebooks=(
    "notebook1.ipynb"
    "notebook2.ipynb"
    "notebook3.ipynb"
)

# Loop through the notebooks and run them
for notebook in "${notebooks[@]}"
do
    jupyter nbconvert --execute "$notebook"
done
