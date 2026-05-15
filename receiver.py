import os
import socket
from pathlib import Path

from aes_socket_utils import (
    LENGTH_HEADER_SIZE,
    decrypt_aes_cbc,
    parse_key_packet,
    parse_length_header,
    recv_exact,
)

HOST = os.getenv("RECEIVER_HOST", "0.0.0.0")
DATA_PORT = int(os.getenv("DATA_PORT", "6000"))
KEY_PORT = int(os.getenv("KEY_PORT", "6001"))
TIMEOUT = float(os.getenv("SOCKET_TIMEOUT", "10"))
OUTPUT_FILE = os.getenv("OUTPUT_FILE", "")
LOG_FILE = os.getenv("RECEIVER_LOG_FILE", "")


def main() -> None:
    lines = []

    # =========================
    # KEY CHANNEL
    # =========================
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as key_server:
        key_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        key_server.settimeout(TIMEOUT)

        key_server.bind((HOST, KEY_PORT))
        key_server.listen(1)

        line = f"[*] Receiver đang lắng nghe kênh khóa tại {HOST}:{KEY_PORT}"
        print(line, flush=True)
        lines.append(line)

        conn, _ = key_server.accept()

        with conn:
            conn.settimeout(TIMEOUT)

            key_len_header = recv_exact(conn, 4)
            key_len = int.from_bytes(key_len_header, "big")

            rest = recv_exact(conn, key_len + 16)

            key_packet = key_len_header + rest

    key, iv = parse_key_packet(key_packet)

    line = "[+] Đã nhận AES key và IV."
    print(line, flush=True)
    lines.append(line)

    # =========================
    # DATA CHANNEL
    # =========================
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as data_server:
        data_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        data_server.settimeout(TIMEOUT)

        data_server.bind((HOST, DATA_PORT))
        data_server.listen(1)

        line = f"[*] Receiver đang lắng nghe kênh dữ liệu tại {HOST}:{DATA_PORT}"
        print(line, flush=True)
        lines.append(line)

        conn, _ = data_server.accept()

        with conn:
            conn.settimeout(TIMEOUT)

            length_header = recv_exact(conn, LENGTH_HEADER_SIZE)

            length = parse_length_header(length_header)

            ciphertext = recv_exact(conn, length)

            data_packet = length_header + ciphertext

    ciphertext = data_packet[LENGTH_HEADER_SIZE:]

    if len(ciphertext) != length:
        raise ValueError("Ciphertext nhận được không khớp length header.")

    line = "[+] Đã nhận ciphertext."
    print(line, flush=True)
    lines.append(line)

    plaintext = decrypt_aes_cbc(key, iv, ciphertext)

    message = plaintext.decode("utf-8", errors="replace")

    line = "[+] Đã giải mã thành công."
    print(line, flush=True)
    lines.append(line)

    line = f"[+] Bản tin gốc: {message}"
    print(line, flush=True)
    lines.append(line)

    if OUTPUT_FILE:
        Path(OUTPUT_FILE).write_bytes(plaintext)

    if LOG_FILE:
        Path(LOG_FILE).parent.mkdir(parents=True, exist_ok=True)
        Path(LOG_FILE).write_text(
            "\n".join(lines) + "\n",
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()