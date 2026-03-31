from __future__ import annotations

from pathlib import Path
from zipfile import ZipFile
import base64

bundle_path = Path("build_assets/rus_monitor_source.zip.b64")
zip_path = Path("build_assets/rus_monitor_source.zip")
zip_path.write_bytes(base64.b64decode(bundle_path.read_text(encoding="utf-8")))
with ZipFile(zip_path) as archive:
    archive.extractall(Path("."))
print("unpacked", zip_path)
