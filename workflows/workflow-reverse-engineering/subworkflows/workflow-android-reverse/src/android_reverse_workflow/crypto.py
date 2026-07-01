from __future__ import annotations

import hashlib
from collections.abc import Mapping

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def ordered_query(params: Mapping[str, object]) -> str:
    return "&".join(
        f"{key}={'' if value is None else value}"
        for key, value in sorted(params.items())
    )


def sha256_sign(params_text: str, salt: str) -> str:
    return hashlib.sha256((params_text + salt).encode("utf-8")).hexdigest()


def aes_cbc_pkcs5_encrypt(plaintext: str, key: str, iv: str) -> bytes:
    cipher = AES.new(key.encode("utf-8"), AES.MODE_CBC, iv.encode("utf-8"))
    return cipher.encrypt(pad(plaintext.encode("utf-8"), AES.block_size))
