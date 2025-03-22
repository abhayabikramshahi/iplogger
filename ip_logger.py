from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def log_ip():
    ip = request.remote_addr
    with open("ip_logs.txt", "a") as file:
        file.write(f"{ip}\n")
    return "Your IP has been logged."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
