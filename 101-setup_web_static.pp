# Sets up web servers for the deployment of web_static

exec {'install':
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx',
  provider => shell,
}

exec {'makedir':
  command  => 'sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/',
  provider => shell,
}

exec {'htmlfile':
      command  => 'html_str="<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>" ; echo -e "$html_str" | sudo tee /data/web_static/releases/test/index.html',
      provider => shell,
}

exec {'sym link':
      command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
      provider => shell,
}

file {'/data/':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

exec {'config_nginx':
      command  => 'sudo sed -i "38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default',
      provider => shell,
}

exec {'restart':
      command  => 'sudo service nginx restart',
      provider => shell,
}
