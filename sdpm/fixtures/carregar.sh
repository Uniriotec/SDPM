#!/bin/bash
./manage.py loaddata fixtures/admin_user.yaml
./manage.py loaddata fixtures/users.yaml
./manage.py loaddata fixtures/players.yaml
./manage.py runscript create_daemon_rpg_test

