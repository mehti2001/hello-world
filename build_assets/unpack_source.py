from __future__ import annotations

import base64
import hashlib
from pathlib import Path
from zipfile import ZipFile

bundle_path = Path("build_assets/rus_monitor_source.zip.b64")
zip_path = Path("build_assets/rus_monitor_source.zip")
print("cwd", Path.cwd())
print("bundle_path", bundle_path, "exists", bundle_path.exists())
print("bundle_size", bundle_path.stat().st_size if bundle_path.exists() else -1)
payload = base64.b64decode(bundle_path.read_text(encoding="utf-8"))
print("payload_sha256", hashlib.sha256(payload).hexdigest())
zip_path.write_bytes(payload)
with ZipFile(zip_path) as archive:
    corrupted_member = archive.testzip()
    if corrupted_member:
        raise RuntimeError(f"Corrupted member in bundle: {corrupted_member}")
    archive.extractall(Path("."))
print("unpacked", zip_path)
