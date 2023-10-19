# Issue TLS server certificates with EJBCA

Setting up the EJBCA TLS server certificates was an incredibly smooth experience, largely thanks to the comprehensive and user-friendly [documentation](https://doc.primekey.com/ejbca/tutorials-and-guides/tutorial-issue-tls-server-certificates-with-ejbca) provided. Every step had clear instructions.

## Certificate Management in EJBCA

### 1. **Create Certificate Profile**

- Navigate to: EJBCA > CA Functions > Certificate Profiles.
- Clone the SERVER template, name it 'TLS Server Profile' and create from template.
- Edit the new profile:
  - Set Key Algorithms to ECDSA.
  - Choose ECDSA curve: P-256 / prime256v1 / secp256r1.
  - Set Signature Algorithm to 'Inherit from Issuing CA'.
  - Set Validity: 1y.
  - Restrict expiration to Tuesdays to Thursdays.
  - Under X.509v3 extensions:
    - Clear Basic Constraints.
    - Ensure Digital Signature, Key Encipherment, and Server Authentication are selected.
  - Validate using CRL Distribution Points & CA-defined points.
- Save changes.

### 2. **Create End Entity Profile**

- Navigate to: EJBCA > RA Functions > End Entity Profiles.
- Add a new profile named 'TLS Server Profile' and edit it.
  - Under Subject DN Attributes:
    - Add Organization and Country fields.
    - Set CN as required & modifiable.
    - Set O to 'Keyfactor Community' and C to 'SE'.
  - Under Other Subject Attributes, add DNS Name and match it with entity CN field.
  - Main Certificate Data:
    - Use the 'TLS Server Profile' and select your Sub CA 'MyPKISubCA-G1'.
- Save changes.

### 3. **Issue Server Certificate**

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
  CN = test.my.pki
  O = Keyfactor Community
  C = SE
  EOL

  # Generate Key
  openssl ecparam -genkey -name prime256v1 -out tls_server.key

  # Create CSR
  openssl req -new -key tls_server.key -config tls_cert_req.cnf
  ```

- Copy & upload CSR to EJBCA.
- Verify request info & set Username to 'test.my.pki'.
- Download certificate in PEM format.
