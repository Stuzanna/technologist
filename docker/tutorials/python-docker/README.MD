

Instructions said pip Im trying Conda as prefer
cd /path/to/python-docker
python3 -m venv .venv
source .venv/bin/activate
(.venv) $ python3 -m pip install Flask
(.venv) $ python3 -m pip freeze > requirements.txt
(.venv) $ touch app.py

conda install Flask
conda list -e > requirements.txt # Export the env definion, though probably not needed as its just Flask

