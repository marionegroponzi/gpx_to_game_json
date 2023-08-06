
## On a fresh clone
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
...
deactivate
```

### Note
Configure the Python interpreter in intelliJ (with Python CE plugin) by selecting the python executable in the venv folder

### ref. [how to create deployable packages](https://www.infoworld.com/article/3656628/6-ways-to-package-python-apps-for-re-use.html)

## Create standalone package with zipapp
- `cd utilities`
- `python -m pip install -r gpx_to_game_json/requirements.txt --target gpx_to_game_json`
- remove unneeded folders
- `python -m zipapp -p python gpx_to_sim`

