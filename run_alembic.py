#!/usr/bin/env python
import sys
import os

# Adiciona o diretório atual ao PYTHONPATH
sys.path.insert(0, os.getcwd())

from alembic.config import Config
from alembic import command

# Configura o alembic
alembic_cfg = Config("alembic.ini")

# Executa o comando revision
command.revision(alembic_cfg, autogenerate=True, message="Add clients table with enum source")