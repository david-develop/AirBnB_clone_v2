#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

# Install Nginx if it not already installed
sudo apt-get -y update
sudo apt-get -y install nginx

# Create the folders
sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/

# Create a HTML file
html_str="<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>"
echo -e $html_str | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restart
sudo service nginx restart
