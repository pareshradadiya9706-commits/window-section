import os
import time
from pathlib import Path

def save_pdf_to_downloads(pdf_bytes, filename):
    # Android નું Downloads ફોલ્ડર
    downloads = Path("/storage/emulated/0/Download")
    
    # જો ફોન માં ન મળે તો બીજું ફોલ્ડર
    if not downloads.exists():
        downloads = Path.home() / "Downloads"
        if not downloads.exists():
            downloads = Path.cwd()
    
    # History માટે બેકઅપ ફોલ્ડર
    app_dir = Path.home() / ".dharam_window"
    app_dir.mkdir(exist_ok=True)
    
    # નામ માં ટાઈમ લગાવીએ એટલે ડુપ્લીકેટ ન થાય
    timestamp = int(time.time() * 1000)
    name, ext = os.path.splitext(filename)
    if not ext:
        ext = ".pdf"
    final_name = f"{name}_{timestamp}{ext}"
    
    # બે જગ્યાએ Save કરીએ
    final_path = downloads / final_name
    backup_path = app_dir / final_name
    
    final_path.write_bytes(pdf_bytes)
    backup_path.write_bytes(pdf_bytes)
    
    print(f"PDF Saved to: {final_path}")
    return str(final_path)
