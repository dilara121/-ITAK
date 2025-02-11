from flask import Flask, render_template
from config import Config
from database.db_setup import db
from routes.auth import auth

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Blueprint'leri ekle
app.register_blueprint(auth)

# Ana Sayfa Route
@app.route('/')
def index():
    return render_template('index.html')

# Veritabanını başlat (ilk çalıştırmada tabloları oluşturur)
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
