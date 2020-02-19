#! /bin/bash
cd ~/service/aviata/
source venv/bin/activate
python3 aviata/manage.py get_updates
