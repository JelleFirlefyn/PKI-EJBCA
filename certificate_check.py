import ssl
import socket
import datetime
import certifi
import json

#To use this class, you create an instance with the domain/IP address as a property like this: scanner = cert_checker("google.com"). 
#Then, you can use the report method of the class to get the results in JSON format: scanner.report().
# The data looks like this, for example, for google.com
#{"target": "google.com", "issuer": [[["countryName", "US"]], [["organizationName", "Google Trust Services LLC"]], [["commonName", "GTS CA 1C3"]]], "subject": [[["commonName", "*.google.com"]]], "expiration date": "Nov 27 08:17:05 2023 GMT", "expired": false}


class cert_checker:
    def __init__(self, hostname) -> None:
        self.hostname = hostname

    def report(self) -> json:
        # Create an SSL context with certificate validation
        context = ssl.create_default_context(cafile=certifi.where())
            # Create a socket and wrap it with SSL
        with socket.create_connection((self.hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=self.hostname) as ssock:
                cert = ssock.getpeercert()
            
                # Extract certificate information
                issuer = cert['issuer']
                subject = cert['subject']
                expiration_date = datetime.datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
            
            
                # Check if the certificate is expired
                if expiration_date < datetime.datetime.now():
                    expired = True
                else:
                    expired = False

                scan_results = {
                    "target": self.hostname,
                    "issuer": issuer,
                    "subject": subject,
                    "expiration date": cert['notAfter'],
                    "expired": expired
                    }
                return json.dumps(scan_results)
            
c = cert_checker("ap.be")
d = c.report()
print(d)