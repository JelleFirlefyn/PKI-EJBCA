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
