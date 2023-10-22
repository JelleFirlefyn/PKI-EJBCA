## Setting up Apache with EJBCA Certifcate ##

### Installing Apache ###

We use a debian 12 base image for the operating system.
Installing apache is no more than just running

```bash
apt update -y
apt install apache2 -y
systemctl status apache2
```

After this apache2 is installed and should be ready to go: systemctl start apache2.

Now we have to configure a few things to get a decent website running that uses SSL.

### Getting our certificate from our EJBCA Instance to serve HTTPS Webpages for Apache2 ###

- Navigate to EJBCA's RA Web interface.
- Choose Make New Request and select your TLS Server Profile.
- Set Key-pair generation to 'Provided by user'.
- Create a CSR:

  ```shell
  # CSR Configuration
  cat > tls_cert_req.cnf <<EOL
  [ req ]
  default_md = sha256
  prompt = no
  distinguished_name = dn

  [ dn ]
  CN = HOSTNAME
  O = Keyfactor Community
  C = SE
  EOL

  # Generate Key
  openssl ecparam -genkey -name prime256v1 -out tls_server.key

  # Create CSR
  openssl req -new -key tls_server.key -config tls_cert_req.cnf
  ```

- Copy & upload CSR to EJBCA.
- Verify request info & set Username to '(hostname).pki'.
- Download certificate in PEM format.

Once this is done you have the valid .pem file that we can then use in our SSL config for apache as shown down below:

### Setting up SSL for our website ### 

Setting Up Virtual Hosts for SSL in Apache2

In Apache2, websites are configured through virtual hosts. To set up SSL for your website, you will need to create a virtual host configuration. Here's how you can do it:

Start by navigating to the directory where Apache2 stores its site configurations, typically located in /etc/apache2/sites-enabled.

Inside this directory, create a new configuration file for your website. You can use any text editor to create this file. For example, let's create a file called debian11-ssl.conf:

```bash
sudo nano /etc/apache2/sites-enabled/debian11-ssl.conf
```


In the configuration file, add the following content. Be sure to replace debian11 with the actual hostname or CN (Common Name) of your certificate.
```apache
<IfModule mod_ssl.c>
    <VirtualHost *:443>
        ServerName debian11 # servername HAS TO BE THE SAME AS THE CN NAME OF THE CERTIFICATE
        DocumentRoot /var/www/html

        SSLEngine on # turn on the SSL engine to tell apache to use SSL for this virtualhost
        SSLCertificateFile /etc/apache2/sites-enabled/debian11.pem # the certifcate we created on our EJBCA website 
        SSLCertificateKeyFile /etc/apache2/sites-enabled/tls_server.key # the key we used to get the certificate from our EJBCA website
    </VirtualHost>
```

Save the configuration file and exit the text editor.

After creating the virtual host configuration, you need to enable the SSL module in Apache2. Run the following command:


```bash
sudo a2enmod ssl
```

Now that you have set up the virtual host and enabled SSL, you can restart Apache2 to apply these changes:

```bash
systemctl restart apache2
```

Your Apache2 web server should now be configured to serve your website over HTTPS using the SSL certificate you obtained from your EJBCA instance.


Completing the SSL Setup in Apache2

With the certificate and key files in place, you are now ready to complete the SSL setup in Apache2. Here are the final steps:

1. Restart Apache2

To ensure that the SSL configuration takes effect, restart the Apache2 webserver using the following command:

```bash
systemctl restart apache2
```

This command will restart Apache2, applying your SSL configuration.

2. Access the Website

Once Apache2 has been restarted, you should be able to access your website over HTTPS. Use the following URL to access your website:
https://debian11/index.html

Make sure to replace "debian11" with the actual hostname or CN name of your Apache server.

Please note that this access will only work if you have previously installed the root CA (Certificate Authority) certificate of your EJBCA instance. If you haven't installed the root CA certificate yet, you should do that before trying to access the website over HTTPS.


```bash
wget "https://ejbca-node1/ejbca/ra/cert?caid=1130883018&chain=false&format=pem" -OutFile "C:\cert.pem"
```

when we have our certificate we can activate it as follows:
```bash
certutil -addstore -user My C:\cert.pem
```
Next up we can download the certificate made in our EJBCA instance for our Apache server as follows:

```bash
wget https://debian11/ejbca/ra/cert?fp=477cade8d19d5c2d8f6537dfc79f33bde792bed0&chain=true&format=pem -OutFile "/etc/ssl/debian11.pem" debian11 is the hostname or CN name of our apache server
```
we already have the tsl_key from previous steps so this one should already be in the /etc/ssl/ folder. 

Next we can just run the below dockerfile and it should set up an apache webserver with SSL configured.

Docker file:
```dockerfile
FROM httpd:2.4

COPY ./site/index.html /usr/local/apache2/htdocs

COPY ./ssl/debian11.pem /usr/local/apache2/conf/server.crt
COPY ./ssl/tls_server.key /usr/local/apache2/conf/server.key

EXPOSE 80
EXPOSE 443
RUN sed -i 's/#LoadModule ssl_module/LoadModule ssl_module/' /usr/local/apache2/conf/httpd.conf
RUN sed -i 's/#LoadModule socache_shmcb_module/LoadModule socache_shmcb_module/' /usr/local/apache2/conf/httpd.conf


RUN echo '<IfModule mod_ssl.c>' >> /usr/local/apache2/conf/extra/httpd-ssl.conf
RUN echo '    <VirtualHost *:443>' >> /usr/local/apache2/conf/extra/httpd-ssl.conf
RUN echo '        ServerName debian11' >> /usr/local/apache2/conf/extra/httpd-ssl.conf
RUN echo '        DocumentRoot /usr/local/apache2/htdocs' >> /usr/local/apache2/conf/extra/httpd-ssl.conf
RUN echo '        SSLEngine on' >> /usr/local/apache2/conf/extra/httpd-ssl.conf
RUN echo '        SSLCertificateFile /usr/local/apache2/conf/server.crt' >> /usr/local/apache2/conf/extra/httpd-ssl.conf
RUN echo '        SSLCertificateKeyFile /usr/local/apache2/conf/server.key' >> /usr/local/apache2/conf/extra/httpd-ssl.conf
RUN echo '    </VirtualHost>' >> /usr/local/apache2/conf/extra/httpd-ssl.conf
RUN echo '</IfModule>' >> /usr/local/apache2/conf/extra/httpd-ssl.conf
RUN echo 'Include conf/extra/httpd-ssl.conf' >> /usr/local/apache2/conf/httpd.conf

CMD ["httpd-foreground"]
```



