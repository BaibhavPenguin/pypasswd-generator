from pathlib import Path

def initialize() -> str:
    app_root = Path(__file__).resolve().parents[2]
    default_path =  app_root / "output"
    default_path.mkdir(parents=True,exist_ok=True)
   
    input_db = default_path / "pypasswd-session.db"
    input_db.touch(exist_ok=True)

    return str(input_db)
