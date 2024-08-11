# PKI-EJBCA

_Groep 4 - Jelle, Ilias, Sem, Mayk, Robbe, Jentse, Cedric_

_[GitHub Repository](https://github.com/JelleFirlefyn/PKI-EJBCA/)_

# Wat is een PKI?
Er is een probleem bij assymetrische encryptie. Als Bob een prive bericht wil sturen naar Alice dat niet onderschept mag worden zal hij de publieke sleutel krijgen van Alice om zijn bericht te encrypteren. Vervolgens stuurt hij het bericht naar Alice en kan Alice dit bericht decrypteren met haar eigen private sleutel. Het probleem hierbij is de integriteit van de publieke sleutel van Alice. Hoe kan Bob weten dat Alice echt Alice is en niet iemand die zich als haar voordoet?
Het antwoord is met het gebruik van een PKI (Public Key Infrastructure). Er moet een CA (Certificate Authority) aanwezig zijn die Bob vertrouwt. Deze CA zal een certificaat maken voor Alice. Bob kan deze certificaat ontvangen van de CA zelf, van Alice of van iemand anders en hiermee kan Bob weten dat Alice echt Alice is.
PKI is dus een systeem die gebruikt wordt om veilige omgevingen aan te maken waarbij iedereen zich kan verifieeren en vertrouwd met elkaar kunnen communiceren.

## Static setup

- [EJBCA Docker container install](./docs/EJBCA-Docker-container-install.md)

- [Issue SSL/TLS server certificates with EJBCA](./docs/EJBCA-TLS-issue.md)

- [Set up SSL/TLS with EJBCA for Nginx](./docs/NGINX-Certificate-setup.md)

- [Set up SSL/TLS with EJBCA for Apache](./docs/EJBCA-Apache-setup.md)
- [Set up SSL/TLS for Microsoft IIS](./docs/MS_IIS.md)

## Automated setup

- [Set up EJBCA with ansible](./docs/EJBCA-Ansible-setup.md)

## Automation scripts

- [Automatic updater for Apache and Nginx](./updater.py)

- [Automatic certificate checker](./certificate_check.py)
