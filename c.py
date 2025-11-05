import hashlib
from Crypto.Cipher import AES
from Crypto.Util import Counter
import base64
from pathlib import Path

ROOT = Path(__file__).parent
ASSET_IMG = ROOT / "mascot.png"
REQUIREMENTS = ROOT / "requirements.txt"

# Ciphertext
ct_b64 = "tPs6dF3fildR9kI5xUeKPLdweL7SJPQojYVr5gW2rcE="

# Key from mascot.png SHA256
img_bytes = (ASSET_IMG.read_bytes())
key = hashlib.sha256(img_bytes).digest()  # 32 bytes (AES-256)
#print(key)

# Nonce from SHA1("gradio==4.44.0")
requirements = "gradio==4.44.0"
nonce = hashlib.sha1(requirements.encode()).digest()[:8]


# Decrypt
ct = base64.b64decode(ct_b64)
ctr = Counter.new(64, prefix=nonce, initial_value=0)
cipher = AES.new(key, AES.MODE_CTR, counter=ctr)
flag = cipher.decrypt(ct).decode("utf-8")
print(flag)