FROM jupyterhub/jupyterhub:1.1.0

COPY jupyterhub_config.py .

RUN wget https://raw.githubusercontent.com/jupyterhub/jupyterhub/1.1.0/examples/cull-idle/cull_idle_servers.py

RUN pip install \
    dockerspawner==12.0.0 \
    #jhub_cas_authenticator==1.0.0
    #jupyterhub-ldapauthenticator # oficial
    jupyterhub-ldap-authenticator # oficioso
