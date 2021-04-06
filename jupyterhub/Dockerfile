FROM jupyterhub/jupyterhub:1.2.2
### 1.1.0 es la que usa el CERN, pero tiene problemas para ejecutarse de forma nativa; ellos lo solucionan porque usan su propia web, de ahí el cambio a 1.2.2

RUN apt-get update \
  && apt-get install -y wget

RUN wget https://raw.githubusercontent.com/jupyterhub/jupyterhub/1.2.2/examples/cull-idle/cull_idle_servers.py

RUN pip install \
    dockerspawner==12.0 \
    jupyterhub-ldap-authenticator # oficioso
    # 0.11.1 ultima version anterior, compatible a priori con 1.1.0
    #jhub_cas_authenticator==1.0.0
    #jupyterhub-ldapauthenticator # oficial
