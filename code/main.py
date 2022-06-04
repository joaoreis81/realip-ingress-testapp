# ["uvicorn", "main:app", "--proxy-headers", "--forwarded-allow-ips","0.0.0.0/0","--host", "0.0.0.0", "--port", "8000"]
# uvicorn main:app --proxy-headers --forwarded-allow-ips 0.0.0.0/0 --host 0.0.0.0 --port 8000
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/realip-ingress-testapp")
def read_root(request: Request):
    x_real_ip = None
    user_agent = None
    client_host = request.client.host
    if 'x-real-ip' in request.headers:
        x_real_ip = request.headers['x-real-ip']
    if 'user-agent' in request.headers:
        user_agent = request.headers['user-agent']
    return {'client_host': client_host, 'x_real_ip': x_real_ip, 'user_agent': user_agent}