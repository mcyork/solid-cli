from SOLIDserverRest import SOLIDserverRest
from SOLIDserverRest.adv import dns_record, ipaddress
import config

# Initialize SOLIDserverRest object
ssr = SOLIDserverRest(endpoint=config.api_endpoint, user=config.api_username, password=config.api_password, verify_ssl=config.ca_cert_file)

# Retrieve and print the IP address info
ip_info = ipaddress.get_info(ssr, config.ip_addr)
print(ip_info)

# Retrieve and print the A record info
a_record_info = dns_record.get_info(ssr, config.a_record)
print(a_record_info)

# Retrieve and print the CNAME record info
cname_record_info = dns_record.get_info(ssr, config.cname_record)
print(cname_record_info)
