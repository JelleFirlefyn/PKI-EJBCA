# PKI-EJBCA

_Groep 4 - Jelle, Ilias, Sem, Mayk, Robbe, Jentse, Cedric_

_[GitHub Repository](https://github.com/JelleFirlefyn/PKI-EJBCA/)_

## Wat is een PKI?
Er is een probleem bij asymmetrische encryptie. Als Bob een privébericht wil sturen naar Alice dat niet onderschept mag worden, zal hij de publieke sleutel krijgen van Alice om zijn bericht te encrypteren. Vervolgens stuurt hij het bericht naar Alice, en kan Alice dit bericht decrypteren met haar eigen private sleutel. Het probleem hierbij is de integriteit van de publieke sleutel van Alice. Hoe kan Bob weten dat Alice echt Alice is en niet iemand die zich als haar voordoet?
Het antwoord is het gebruik van een PKI (Public Key Infrastructure). Er moet een CA (Certificate Authority) aanwezig zijn die Bob vertrouwt. Deze CA zal een certificaat maken voor Alice. Bob kan dit certificaat ontvangen van de CA zelf, van Alice of van iemand anders, en hiermee kan Bob weten dat Alice echt Alice is.
PKI is dus een systeem dat gebruikt wordt om veilige omgevingen te creëren waarbij iedereen zich kan verifiëren en vertrouwd met elkaar kan communiceren.

## Waarom zou je een Windows PKI systeem kiezen?
Een Windows PKI-systeem is volledig geïntegreerd met Active Directory, wat het eenvoudiger maakt om certificaten uit te geven en te beheren binnen een Windows-omgeving. Daarnaast hoef je geen extra software aan te kopen, omdat Windows Server alle benodigde functionaliteiten al bevat. Windows PKI-systemen staan uiteraard ook bekend voor hun betrouwbaarheid, en Microsoft biedt uitgebreide documentatie. Een Windows PKI is ook zeer veilig omdat Microsoft regelmatig beveiligingsupdates biedt.

## Opdracht
In deze opdracht gaan we een HTTP-website hosten via Apache, IIS en Nginx. Ons doel is om de communicatie op de website te beveiligen, dus zullen we de HTTP-website moeten omzetten naar een HTTPS-website. Hiervoor hebben we een SSL/TLS-certificaat nodig. Dit certificaat kunnen we aanvragen via onze interne CA, beheerd door onze EJBCA-server, door een CSR (Certificate Signing Request) naar EJBCA te sturen. De CSR bevat de publieke sleutel en details van de website. Tenslotte zullen we Apache, IIS en Nginx configureren om het SSL/TLS-certificaat te gebruiken en de website met HTTPS te hosten.

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
