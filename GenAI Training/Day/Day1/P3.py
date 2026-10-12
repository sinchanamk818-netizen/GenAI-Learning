# pip,virtul environment, .env file
# pip:pip installs Package. Package manager

# virtul environment: A 'venv' is a directory that contains 
# 1. A copy of the python interpreter 
# 2. Its own 'pip'
# 3. Its own site-packages directory. Default traget location
# where python installs third party libraries
# 4. Activation scripts that modify PATH

python3 --version
python3 -m venv .venv

# Activate virtual envirnoment
source .venv/bin/activate

# deactivate
deactivate

# pip installation (install dependencies/libraries)
pip install package_name # syntax

pip install python-dotenv