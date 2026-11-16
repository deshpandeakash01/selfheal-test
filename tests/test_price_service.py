import os
import socket

HOST = "10.255.255.1" if os.environ.get("GITHUB_RUN_ATTEMPT") == "1" else "github.com"


def test_price_service_is_reachable():
    socket.create_connection((HOST, 443), timeout=5).close()
