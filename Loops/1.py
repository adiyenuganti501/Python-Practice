# for i in range(1,10):
#     print(f"Server-{i}")

# for i in range(1,10,2):
#     print(i)
    
# for i in range(10,0,-1):
#     print(i)
    
# name = "Python"
# for ch in name:
#     print(ch)

# ip = "192.168.1.10"
# for i in ip:
#     print(i)

# servers = ["web-01", "db-01", "web-02", "db-02"]
# for s in servers:
#     if s.startswith("web"):
#         print(s)

server = {
    "name": "web-01",
    "ip": "10.0.1.10",
    "status": "running"
}

# for k in server:
#     print(k)
# for v in server.values():
#     print(v)
for k,v in server.items():
    print(k,v)