from database import SessionLocal

try:
    db = SessionLocal()
    print("✅ Conexão bem-sucedida com o banco de dados!")
except Exception as e:
    print(f"❌ Erro ao conectar ao banco: {e}")
finally:
    db.close()
