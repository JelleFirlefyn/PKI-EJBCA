# Setting up a EJBCA Docker container

Setting up the EJBCA container was an incredibly smooth experience, largely thanks to the comprehensive and user-friendly [documentation](https://doc.primekey.com/ejbca/tutorials-and-guides/tutorial-start-out-with-ejbca-docker-container#TutorialStartoutwithEJBCADockercontainer-AddEndEntity) provided. Every step had clear instructions.

1. Create directory

   - Create a directory for running the container and storing the database

     ```cli
     $ mkdir -p containers/datadbdir
     $ cd containers
     ```

1. Create Docker Compose file

   - Create docker-compose.yml file and add following content

     ```cli
     $ vim docker-compose.yml
     ```

     ```yml
     version: '3'
        networks:
        access-bridge:
            driver: bridge
        application-bridge:
            driver: bridge
        services:
        ejbca-database:
            container_name: ejbca-database
            image: "library/mariadb:latest"
            networks:
            - application-bridge
            environment:
            - MYSQL_ROOT_PASSWORD=foo123
            - MYSQL_DATABASE=ejbca
            - MYSQL_USER=ejbca
            - MYSQL_PASSWORD=ejbca
            volumes:
            - ./datadbdir:/var/lib/mysql:rw
        ejbca-node1:
            hostname: ejbca-node1
            container_name: ejbca
            image: keyfactor/ejbca-ce:latest
            depends_on:
            - ejbca-database
            networks:
            - access-bridge
            - application-bridge
            environment:
            - DATABASE_JDBC_URL=jdbc:mariadb://ejbca-database:3306/ejbca?characterEncoding=UTF-8
            - LOG_LEVEL_APP=INFO
            - LOG_LEVEL_SERVER=INFO
            - TLS_SETUP_ENABLED=simple
            ports:
            - "80:8080"
            - "443:8443"
     ```

1. Start EJBCA Community container

   ```cli
   $ docker-compose up -d
   ```

1. Check log output of the container starting up

   ```cli
   $ docker compose logs -f
   ```

1. The output of the logs provide the URL to access the EJBCA web interface

   ![Image of docker compose output](./docs/assets/docker-compose-output.png)

1. Use this URL in your browser (_preferably Firefox_) to access the web interface

   - Note: when using a different machine to access the web interface use the following URL `https://[ip-hosting-ejbca]:443/ejbca/adminweb/`

1. In the browser accapt the security risk by clicking **Advanced** and then **Accept the risk and continue**
