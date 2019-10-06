--- setup python backend ---
python3 -m venv myprojectenv
source myprojectenv/bin/activate
pip install wheel
pip install uwsgi flask

--- start dev server --
sudo ufw allow|deny 5000
python holy-cow.py

create config.py



--- CONFIG FOR PRODUCTION --

--- create WSGI entry point ---
in a wsgi.py file let’s import the Flask instance from our application and then run it

--- configure & test uWSGI --- (not a durable solution)
uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app
deactivate ( --> the virtual env)

--- create uWSGI Configuration File (robust!) --- 
nano holy-cow.ini

--- create a systemctl startup file /etc/systemd/system/holy-cow.service --
--- start and enable service ---
sudo systemctl start holy-cow
sudo systemctl enable holy-cow

--- check service ---
sudo systemctl status holy-cow

--- Configuring Nginx to Proxy Requests ---
sudo nano /etc/nginx/sites-available/holy-cow
- to enable the Nginx server block configuration you’ve just created, link the file to the sites-enabled directory

sudo systemctl restart nginx

-- Configuring for Apache ---
#todo

