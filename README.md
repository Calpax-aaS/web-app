# web-app


## Local Development on macOS
1. Install python with [pyenv](https://github.com/pyenv/pyenv)
```
brew install pyenv
pyenv install 3.8
```
2. Install [pipenv](https://pipenv-fork.readthedocs.io/en/latest/install.html)
```
brew install pipenv
```
3. Install [Docker](https://hub.docker.com/editions/community/docker-ce-desktop-mac)
```
docker run --name database -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres:11
```
4. Run the application
```
cp .env.template .env
pipenv install
pipenv migrate
pipenv run start
```



## Tech choices
### IdP
External IdP -> Auth0
https://auth0.com/blog/django-authentication/

### Deployment
Clever Cloud, a bit expensive but PaaS solution with good feedbacks
Github + actions to store and deploy code

### Framework
Django for the quality of ecosystem and the built-in admin interface

### Libs Django
#### Multi tenant
https://djangopackages.org/grids/g/multi-tenancy/

Selection of https://github.com/django-tenants/django-tenants
* Production/Stable
* Still maintained
* Forked from https://github.com/bernardopires/django-tenant-schemas/issues (started in 2013)
* 650 stars