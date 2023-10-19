import requests

# Set the EJBCA REST API URL
ejbca_rest_api_url = "https://192.168.0.157:443/ejbca/ejbca-rest-api/v1/certificate"

# Set the EJBCA username and password
ejbca_username = "Administrator"
ejbca_password = "Password"

# Set the certificate profile
certificate_profile = "server"

# Set the certificate name
certificate_name = "tls-server"

# Set the certificate subject
certificate_subject = "/C=BE/ST=Antwerp/L=Antwerp/O=My Company/OU=IT/CN=www.example.com"

# Set the certificate private key
certificate_private_key = "-----BEGIN RSA PRIVATE KEY-----\nMIIEogIBAAKCAQEA+f34hJ/bC7+2bW1/l38w7v1b/v31/w87e1/63f/8x/7P/w8z/87/9P+\n/87/9P+3/7P/9P+3/7P/9P+3/7P/9P+3/7P/9P+3/7P/9P+3/7P/9P+3/7P/9P+3/7P/\n... (truncated) \n-----END RSA PRIVATE KEY-----"

# Create the certificate request data
certificate_request_data = {
    "certificateProfile:name": certificate_profile,
    "certificateProfile:type": "ENDENTITY",
    "certificateRequest:certificateName": certificate_name,
    "certificateRequest:subjectDN": certificate_subject,
    "certificateRequest:publicKey": certificate_private_key,
}

# Make a POST request to the EJBCA REST API to create the certificate
response = requests.post(
    ejbca_rest_api_url,
    auth=(ejbca_username, ejbca_password),
    json=certificate_request_data,
    verify=False,
)

# Check the response status code
if response.status_code == 201:
    # The certificate was created successfully
    certificate_pem = response.json()["certificate"]

    # Save the certificate to a file
    with open("certificate.pem", "w") as f:
        f.write(certificate_pem)

    print("The certificate was created successfully and saved to certificate.pem")
else:
    # An error occurred
    print(response.content)
