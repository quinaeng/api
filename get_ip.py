from flask import Flask, request

app = Flask(__name__)

@app.route('/get_ip', methods=['GET'])
def get_ip():
    # クライアントのIPアドレスを取得
    client_ip = request.remote_addr
    return f'The client IP address is: {client_ip}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)

