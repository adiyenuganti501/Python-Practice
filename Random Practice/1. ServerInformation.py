server_name = "    web-server-01"
environment = "production"
ip = "10.0.0.25"
status = "running"

print(f"Server Name: {server_name.strip().upper()}")
print(f"Environment: {environment.strip().upper()}")
print(f"IP Address : {ip}")
print(f"Status     : {status.strip().upper()}")
print("<---------------------------------->")
environment = " production "

val=("Production environment detected" if environment.strip().upper() == "PRODUCTION" else "Non-production environment")
print(val)
print("<---------------------------------->")
ip = "111.111.111.111"
val=("Private IP" if ip.startswith("10.") or ip.startswith("192.168.") or ip.startswith("172.16.")  else "Public IP")
print(val)