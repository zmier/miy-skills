import hashlib

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

from android_reverse_workflow.crypto import (
    aes_cbc_pkcs5_encrypt,
    ordered_query,
    sha256_sign,
)


def test_ordered_query_and_sign_use_stable_generic_rules() -> None:
    # GIVEN：一组与具体 App 无关的乱序参数和固定盐。
    params = {"z": 3, "a": 1, "empty": None}

    # WHEN：按 key 排序拼接并执行 SHA-256(params + salt)。
    text = ordered_query(params)
    sign = sha256_sign(text, "fixture-salt")

    # THEN：排序、空值和摘要都符合通用定义。
    assert text == "a=1&empty=&z=3"
    assert sign == hashlib.sha256(
        b"a=1&empty=&z=3fixture-salt"
    ).hexdigest()


def test_aes_output_is_deterministic_and_block_aligned() -> None:
    # GIVEN：固定明文、32 字节 AES key 与 16 字节 IV。
    plaintext = "aid=1&sign=abc"

    # WHEN：执行 AES/CBC/PKCS5Padding。
    first = aes_cbc_pkcs5_encrypt(
        plaintext,
        "fd6b639dbcff0c2a1b03b389ec763c4b",
        "77b07a672d57d64c",
    )
    second = aes_cbc_pkcs5_encrypt(
        plaintext,
        "fd6b639dbcff0c2a1b03b389ec763c4b",
        "77b07a672d57d64c",
    )

    # THEN：密文可重复、分组对齐，并能由相同配置还原。
    assert first == second
    assert len(first) % 16 == 0
    cipher = AES.new(
        b"fd6b639dbcff0c2a1b03b389ec763c4b",
        AES.MODE_CBC,
        b"77b07a672d57d64c",
    )
    assert unpad(cipher.decrypt(first), AES.block_size).decode() == plaintext
