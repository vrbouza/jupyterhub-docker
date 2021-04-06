cp -f ./jupyterhub/jupyterhub_config.py /opt/jupyterhub-swaneau/data/srv/jupyterhub/
restorecon -R -v /run/docker.sock
