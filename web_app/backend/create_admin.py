from passlib.context import CryptContext
from sqlalchemy.orm import Session
from models import User  # importa il tuo modello User
from database import SessionLocal  # importa la tua sessione
from datetime import datetime

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_admin():
    db: Session = SessionLocal()

    existing_user = db.query(User).filter(User.username == "admin").first()
    if existing_user:
        print("⚠️ L'utente admin esiste già.")
        return

    hashed_password = pwd_context.hash("admin123")  # cambia la password se vuoi
    admin = User(
        username="admin",
        hashed_password=hashed_password,
        is_active=True,
        is_admin=True,
        created_at=datetime.utcnow()
    )
    db.add(admin)
    db.commit()
    db.refresh(admin)
    print("✅ Utente admin creato!")

if __name__ == "__main__":
    create_admin()
