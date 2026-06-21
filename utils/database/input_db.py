import subprocess
from pathlib import Path
import logging


def generate(length : int , bulk : int , path : str) -> bool:
        
    if Path(path).is_file == False or length < 8 or bulk < 1:
        return False

    app_root = Path(__file__).resolve().parents[2]
    csprng_path = app_root / "binaries" / "csprng"          
    if not csprng_path.exists():
        return False     
                
    try:
        subprocess.run(
            [str(csprng_path), f"{length}", f"{bulk}" , path], 
            text=True, 
            check=True
        )    
    except subprocess.CalledProcessError as e:
        logging.error("ERROR! Input Database not initialised!")
        raise SystemExit(1)

    return True