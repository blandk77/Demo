import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", "27394279"))
API_HASH = os.environ.get("API_HASH", "90a9aa4c31afa3750da5fd686c410851")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7567477886:AAEMI6V1ImkbEkwUIkMfHNfVrQFFB4GKNtI")
ADMIN = int(os.environ.get("ADMIN", "7465574522"))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "-1002226481922")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002288135729"))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://telegramguy21:tnkIwvbNkJ5U3fZ7@botsuse.bpgag.mongodb.net/?retryWrites=true&w=majority&appName=Botsuse")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "TechifyBotz")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/ada3f739fed7efdbe7b08.jpg")
