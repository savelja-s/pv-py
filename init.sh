#!/bin/bash

python3 -m venv venv
source venv/bin/activate
pip3 install --no-cache-dir --trusted-host pypy.org --trusted-host files.pythonhosted.org -r requirements.txt
pip3 install --upgrade pip
python -m pip install --upgrade pip
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@admin.dev', '1234')"
python manage.py shell -c "from django.contrib.sites.models import Site; Site.objects.filter(id=1).update(domain='127.0.0.1', name='local')"
deactivate
