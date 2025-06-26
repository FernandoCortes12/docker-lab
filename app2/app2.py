from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Renderiza la plantilla y pasa la IP del cliente
    return render_template('index.html', ip=request.remote_addr)

if __name__ == '__main__':
    # Escucha en todas las interfaces, puerto 8181
    app.run(host='0.0.0.0', port=8181)
