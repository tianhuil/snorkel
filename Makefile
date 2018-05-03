SHELL=bash
CONDA=source activate snorkel

install:
	conda env update -n snorkel -f environment.yaml
	$(CONDA) && jupyter nbextension enable --py widgetsnbextension --sys-prefix
	$(CONDA) && pip install .

run:
	$(CONDA) && ./run.sh
