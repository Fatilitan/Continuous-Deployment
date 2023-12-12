# 3 componenten die nodig waren voor mijn project

- ### Digital Ocean
  Digital Ocean is een bedrijf die een heleboel cloud-based services biedt. Degene die relevant is tot dit project is de droplet: Dat is een virtuele private server waar je je projecten op kan lanceren, zodat je project altijd online staat.
- ### Github
  Github is een website waar je online repositories kan plaatsen. Je kan een lokaal project direct linken met je github repository, en nieuwe/aangepaste code updaten (pushen) naar de repository. Dit maakt werken aan je projecten een stuk makkelijker, zowel in je eentje, maar vooral als je met een team samen codeert.
- ### YAML
  Met Github kan je bepaalde taken automatiseren. Dat doe je door gebruik te maken van een YAML-bestand. In de YAML bestand definieer je triggers en actions. In dit project was de trigger git push, oftewel; zodra nieuwe code wordt geupdate voer je een aantal taken uit. De taken die het YAML-bestand moest uitvoeren was de Github repository koppelen aan een Digital Ocean droplet.
  ```yml
  cd ~
  cd /var/www/farm-site
  git pull origin main
  systemctl restart farm
  systemctl status farm
  ```
  Eerst heb ik in mijn digital ocean server een gunicorn & nGINX project gemaakt. De YAML-code die gaat naar het specifieke adress van het project en doet daarna git pull, waardoor de code die in het draaiende project wordt geupdate. Daarna herstart ik de server zodat de nieuwe code zichtbaar is als je de browser opent.

# 3 Obstakels die ik ben tegengekomen tijdens het project.

- ### CMD
  Omdat je de server alleen kan bewerken door middel van bash, is het heel lastig om te weten wat je nou precies aan het doen bent. Bepaalde folders/files uberhaubt vinden was een ramp.
- ### YAML
  Om te checken of je yaml werkte, moest je telkens bij elke verandering git push doen om te kijken op github of de acties goed worden uitgevoerd. Dat duurt best lang.
- ### SSH-keys
  Het duurde heel lang voordat ik door had dat je de SSH-keys eerst moet genereren. Ik bleef maar het wachtwoord voor mijn droplet gebruiken.
