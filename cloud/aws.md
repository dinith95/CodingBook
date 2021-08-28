## common tricks 

### connecting aws ec2

you can connect to the *aws ec2* instance by the commandline through **SSH**. A *.pem* file is needed . 

> execute following commands when connecting from windows.

```powershell

# assing the pem file name 
 $varPem = ".\ec2test.pem"

## reset the permission 
icacls.exe $varPem /reset  

# Give current user explicit read-permission
icacls.exe $varPem  /GRANT:R "$($env:USERNAME):(R)"

# Disable inheritance and remove inherited permissions
icacls.exe $varPem /inheritance:r

```


## aws sequrity 

### creating a self signed certificate 

first create a config file 

> distinguished_name = req_distinguished_name \
 x509_extensions = v3_req \
prompt = no \
[req_distinguished_name]\
C = country_code\
ST = state\
L = city \
O = company\
OU = .\
CN = devapi.rushwheel.com \
[v3_req]\
keyUsage = critical, digitalSignature, keyAgreement\
extendedKeyUsage = serverAuth\
subjectAltName = @alt_names\
[alt_names]\
DNS.1 = devapi.rushwheel.com\
DNS.2 = https://devapi.rushwheel.com\


important variables 

 - CN => the *common name* , has to put the **domain name / sub domain name**. ```required``` 

- subjectAltName => additional  host name . failinig to provide this will create **NET CERT ERROR** . ```required```. 


Then give the following command to create key 

```bash
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/RushwheelApi.key -out /etc/ssl/certs/RushwheelApi.crt -config cert.cnf 
```
important variables 
> days => no of days which the SSL is valid \
> keyout => path which private key is saved \
> out => path which certificate is stored \
> config => path to the above created config file 

