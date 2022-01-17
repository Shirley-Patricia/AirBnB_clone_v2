#!/usr/bin/env bash
# Write a Bash script that sets up your web servers for the deployment of web_static. It must:
# Install Nginx if it not already installed.

sudo apt-get update
sudo apt-get -q -y install nginx
sudo service nginx start
# Creating of the folders if it doesn’t already exist
sudo mkdir -p /data/web_static/{releases/test,shared}

# Create a fake HTML file 
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Creating of a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group.
# This should be recursive; everything inside should be created/owned by this user/group

sudo chown -hR ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static

sudo sed -i "54 i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\t}\n" /etc/nginx/sites-available/default

sudo service nginx restart
