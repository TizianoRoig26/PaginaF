from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import bcrypt
import os

# Crear la aplicación Flask
app = Flask(__name__)

# Configuración desde variables de entorno
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
MYSQL_DB_USUARIOS = os.getenv("MYSQL_DB_USUARIOS", "pruebapython")
MYSQL_DB_RESERVAS = os.getenv("MYSQL_DB_RESERVAS", "reservas")

def get_conexion_usuarios():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB_USUARIOS,
        port=MYSQL_PORT
    )

def get_conexion_reservas():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB_RESERVAS,
        port=MYSQL_PORT
    )

# Página principal
@app.route('/')
def index():
    return render_template('index.html')

# Página tierra
@app.route('/tierra')
def tierra():
    return render_template('tierra.html')

# Página agua
@app.route('/agua')
def agua():
    return render_template('agua.html')

# Página aire
@app.route('/aire')
def aire():
    return render_template('aire.html')

# Página reservas
@app.route('/reservas')
def reservas():
    return render_template('reservas.html')

# Página de registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        telefono = request.form['telefono']
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        hash_contrasena = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())

        conn = get_conexion_usuarios()
        cursor = conn.cursor()
        sql = "INSERT INTO clientes (nombre, correo, telefono, usuario, contrasena) VALUES (%s, %s, %s, %s, %s)"
        values = (nombre, correo, telefono, usuario, hash_contrasena)
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()

        return redirect(url_for('index'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        # Crear conexión y cursor
        conn = get_conexion_usuarios()
        cursor_usuarios = conn.cursor()

        # Ejecutar consulta
        cursor_usuarios.execute("SELECT contrasena FROM clientes WHERE usuario = %s", (usuario,))
        resultado = cursor_usuarios.fetchone()

        # Cerrar conexión
        cursor_usuarios.close()
        conn.close()

        if resultado and bcrypt.checkpw(contrasena.encode('utf-8'), resultado[0].encode('utf-8')):
            return f"Bienvenido, {usuario}"
        else:
            return "Nombre de usuario o contraseña incorrectos."

    return render_template('login.html')

# Formulario de reservas
@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        telefono = request.form['telefono']
        actividad = request.form['actividad']
        fecha_reserva = request.form['fecha_reserva']
        cantidad_personas = request.form['cantidad_personas']
        comentarios = request.form['comentarios']

        # Insertar en la base de datos de reservas
        sql = """
        INSERT INTO reservas 
        (nombre, apellido, correo, telefono, actividad, fecha_reserva, cantidad_personas, comentarios)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (nombre, apellido, correo, telefono, actividad, fecha_reserva, cantidad_personas, comentarios)

        conexion_reservas = get_conexion_reservas()
        cursor_reservas = conexion_reservas.cursor()

        cursor_reservas.execute(sql, values)
        conexion_reservas.commit()

        cursor_reservas.close()
        conexion_reservas.close()

        return redirect(url_for('index'))

    return render_template('formulario.html')

# Ejecutar la app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)