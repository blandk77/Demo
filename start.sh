source .venv/bin/activate && gunicorn app:app && python3 update.py && python3 -m bot
