import pwn

conn = pwn.remote("139.59.184.138","2300")
s = conn.interactive()
print(s) 
