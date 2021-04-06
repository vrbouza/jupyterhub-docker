# JupyterHub configuration
#
## If you update this file, do not forget to delete the `jupyterhub_data` volume before restarting the jupyterhub service:
##
##     docker volume rm jupyterhub_jupyterhub_data
##
## or, if you changed the COMPOSE_PROJECT_NAME to <name>:
##
##    docker volume rm <name>_jupyterhub_data
##

import os, sys

## Generic
c.JupyterHub.admin_access = True
c.Spawner.default_url     = '/lab'

## Authenticator
c.Authenticator.admin_users = { 'vrbouza', "root" }

c.JupyterHub.authenticator_class                = 'ldapauthenticator.LDAPAuthenticator'
c.LDAPAuthenticator.server_hosts                = ['ldaps://gaeipa.geol.uniovi.es:636', 'ldaps://gaeipa.c3.uniovi.es:636']
c.LDAPAuthenticator.bind_user_dn                = 'uid=admin,cn=users,cn=accounts,dc=hep,dc=uniovi,dc=es'
c.LDAPAuthenticator.bind_user_password          = ''
c.LDAPAuthenticator.user_search_base            = 'cn=users,cn=accounts,dc=hep,dc=uniovi,dc=es'
c.LDAPAuthenticator.user_search_filter          = '(&(objectClass=person)(uid={username}))'
c.LDAPAuthenticator.user_membership_attribute   = 'memberOf'
c.LDAPAuthenticator.group_search_base           = 'cn=groups,cn=accounts,dc=hep,dc=uniovi,dc=es'
c.LDAPAuthenticator.group_search_filter         = '(&(objectClass=ipausergroup)(memberOf={group}))'
c.LDAPAuthenticator.allowed_groups              = ['cn=jupyterhub-users,cn=groups,cn=accounts,dc=hep,dc=uniovi,dc=es']
c.LDAPAuthenticator.allow_nested_groups         = True
c.LDAPAuthenticator.username_pattern            = '[a-zA-Z0-9_.][a-zA-Z0-9_.-]{0,252}[a-zA-Z0-9_.$-]?'
c.LDAPAuthenticator.create_user_home_dir        = True
c.LDAPAuthenticator.create_user_home_dir_cmd    = ['mkhomedir_helper']


## Docker spawner
c.JupyterHub.spawner_class      = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image           = os.environ['DOCKER_JUPYTER_CONTAINER']
c.DockerSpawner.network_name    = os.environ['DOCKER_NETWORK_NAME']
# See https://github.com/jupyterhub/dockerspawner/blob/master/examples/oauth/jupyterhub_config.py
c.JupyterHub.hub_ip             = os.environ['HUB_IP']

# user data persistence
# see https://github.com/jupyterhub/dockerspawner#data-persistence-and-dockerspawner
#notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan'
#c.DockerSpawner.notebook_dir = notebook_dir
#c.DockerSpawner.volumes = { 'jupyterhub-user-{username}': notebook_dir }
c.DockerSpawner.notebook_dir = "/nfs/fanae/user/{username}"

# Other stuff
c.Spawner.cpu_limit = 1
c.Spawner.mem_limit = '1G'


## Services
c.JupyterHub.services = [
    {
        'name': 'idle-culler',
        'admin': True,
        'command': [
            sys.executable,
            '-m', 'jupyterhub_idle_culler',
            '--timeout=3600'
        ],
    },
]
