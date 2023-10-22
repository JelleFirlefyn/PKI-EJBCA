# Setting up an NGINX server with a valid certificate

1. Copy Certificate and Key to Nginx: Transfer your private key and the signed certificate from EJBCA to your Nginx server. Store them in a safe location.

1. Configure Nginx: Create an Nginx configuration file (default.conf) and specify the paths to your certificate and private key:

   ```bash
        server {
            listen 80;
            server_name localhost;

            location / {
                return 301 https://$host$request_uri;
            }
        }

        server {
            listen 443 ssl;
            server_name localhost;

            ssl_certificate /etc/nginx/ssl/server.pem;
            ssl_certificate_key /etc/nginx/ssl/server.key;

            location / {
                root /usr/share/nginx/html;
                index index.html;
            }
        }
   ```

1. Create a Dockerfile for setting up your Nginx server. This Dockerfile makes sure that your keys move into the server and the default.conf file you set up in the previous step.

   ```bash
   FROM nginx
   COPY default.conf /etc/nginx/conf.d/
   COPY test.my.pki.pem /etc/nginx/ssl/server.pem
   COPY tls_server.key /etc/nginx/ssl/server.key
   ```

1. Once you have set this all up, build your Docker image.

   ```bash
   docker build -t nginx-ssl .
   ```

1. Run the container

   ```bash
   docker run -d -p 80:80 -p 443:443 nginx-ssl
   ```

### Sidenote:

The certificate you're using will not be trusted by public clients (browsers, etc.) because it's not signed by a public CA. But, as you mentioned, it will be correct if the client has the correct root certificate. You'd typically use this setup in a test environment or for internal services where you can control the client certificates.

Remember to secure your private key (server.key). If it's compromised, attackers can impersonate your server. Always set the appropriate permissions to ensure that only the Nginx process and superusers can read the key.
