# Naar de juiste dir
cd /var/www/farm-site

# Nieuwste code pakken
git pull

# NGINX restarten om het project te updaten
systemctl restart nginx