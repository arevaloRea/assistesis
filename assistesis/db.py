# Import this file in your Django settings to configure the database.

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Django settings for database configuration

# SQLite3 configuration  
SQLITE3 = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # You can change the path if you want to store the DB elsewhere
    }
}


# PostgreSQL configuration
POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',         # Replace with your PostgreSQL database name
        'USER': 'your_db_user',         # Replace with your PostgreSQL username
        'PASSWORD': 'your_db_password', # Replace with your PostgreSQL password
        'HOST': 'localhost',            # Or your PostgreSQL host in production
        'PORT': '5432',                 # Default PostgreSQL port
    }
}

# MySQL configuration
MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',         # Replace with your MySQL database name
        'USER': 'your_db_user',         # Replace with your MySQL username
        'PASSWORD': 'your_db_password', # Replace with your MySQL password
        'HOST': 'localhost',            # Or your MySQL host in production
        'PORT': '3306',                 # Default MySQL port
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# MongoDB configuration (if needed)
MONGODB = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'your_db_name',         # Replace with your MongoDB database name
        'ENFORCE_SCHEMA': False,        # Set to True if you want to enforce schema
        'CLIENT': {
            'host': 'localhost',         # Or your MongoDB host in production
            'port': 27017,               # Default MongoDB port
            'username': 'your_db_user',  # Replace with your MongoDB username
            'password': 'your_db_password', # Replace with your MongoDB password
        }
    }
}

