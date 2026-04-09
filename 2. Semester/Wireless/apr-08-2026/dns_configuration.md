# What we did 
today we set up and configured our own DNS server on a ubuntu server as well as making our own NAS server, and webpage 

## DNS 
For the dns server we hosted we used bind9, after the instalation we created our own configurations for it

Most of the configuration was done within the /etc/bind9 directory

The main configs to make sure to set is your listening interface as well as making sure you allow trafic to pass through

We then set up our own db file to make our own dns entery that would then later become our webserver

After all the configuring was done we set up the dns with the command systemctl restart bind9, if everything you should then have you own dns

its a good idea to allow forwarding if your own dns doesnt know something to ensure you still have access to the web

Make sure to then change the dns your dhcp sends out with its requests to allow your clients to access the dns,
as well as setting it to the new dns on the machiens that are staticly set via the netplan

## Web server
For the web server we used the server called apache2 and then configured it in the /ect/apache2 directory

For the initial setup there wasnt much since it works right out of the box if your server allows incomming tarfic to reach you on port 80
but we make our own website from scratch which required a bit more, 

we started by making our .conf file in /ect/apache2/sites-available called school.conf and setting it up for basic use

we then made our the directory school and html page in /var/www/school where we then worte the html for our own page

After writing the html and setting it all up we then restarted the server with systemctl restart apache2
