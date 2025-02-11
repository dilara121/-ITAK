📈 Ihale Uygunluk Takip Sistemi

🌟 Proje Hakkında
Bu proje, şirketlerin SGK, vergi ve ihale uygunluk durumlarını takip edebilmesi için geliştirilen bir web tabanlı uygulamadır. Kullanıcılar giriş yaparak borç durumlarını görüntüleyebilir, rapor oluşturabilir ve detaylı analizler yapabilir.

💪 Temel Özellikler
- Kullanıcı Yönetimi: Üye olma, giriş yapma, şifre kontrolü.
- Ana Sayfa & Hakkında: Web sitesinin amacı ve kullanılabilir işlemler hakkında bilgi.
- Borç Takip Modülü: SGK, vergi ve ihale uygunluk borçlarını takip etme.
- Raporlama & Görselleştirme: Grafiklerle veri analizi ve geçmiş raporları görüntüleme.
- Bildirim Sistemi: Borç süresi yaklaşınca e-posta/SMS uyarıları.
- Web Tabanlı Yönetim Paneli: Yetkililerin kullanıcıları ve verileri yönetebileceği bir sistem.

📚 Kullanılan Teknolojiler
- Backend: Flask, Flask-SQLAlchemy, Flask-WTF, Flask-Login
- Frontend: HTML, CSS, Bootstrap
- Veritabanı: SQLite (isteğe bağlı PostgreSQL)
- Görselleştirme: Plotly, Chart.js

📌 Kullanım
   
1️⃣ Üye Olun → Giriş ekranından kayıt işlemini tamamlayın.    
2️⃣ Giriş Yapın → Doğru şifre ile giriş yaparak borçları görüntüleyin.     
3️⃣ Borçlarınızı Takip Edin → SGK ve vergi borçlarınızı listeleyin.     
4️⃣ Raporlar Oluşturun → Borç durumlarına göre PDF veya grafik raporları alın.     

🔒 Güvenlik Önlemleri
🔹 Şifreleme → Kullanıcı şifreleri bcrypt ile hashlenerek saklanır.
🔹 Yetkilendirme → Yetkisiz kullanıcılar kritik işlemleri gerçekleştiremez.
🔹 SQL Injection Koruması → Tüm girişler doğrulanır ve filtrelenir.
