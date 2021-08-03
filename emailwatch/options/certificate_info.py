from datetime import datetime
import OpenSSL
import OpenSSL.crypto
import requests 
from rich import print 
from socket import socket
import ssl


port = 443
cert_date_format = "%Y%m%d%H%M%SZ"
cert_encoding = "ascii"


def show_cert_info(host: requests.Response):
    """Return TLS certificate information for domain"""

    try:

        site_cert = ssl.get_server_certificate((host, port))
        crypto_cert = OpenSSL.crypto.load_certificate(
            OpenSSL.crypto.FILETYPE_PEM, site_cert
        )

        certificate_results(crypto_cert, host)

    except ssl.SSLError:
        print("[bold red] [X] Couldn't connect to target site [/]")


def certificate_results(crypto_cert, host) -> str:

    not_before = datetime.strptime(
        crypto_cert.get_notBefore().decode(cert_encoding), cert_date_format
    )
    not_after = datetime.strptime(
        crypto_cert.get_notAfter().decode(cert_encoding), cert_date_format
    )

    print(
        f"""[purple] [+]  {host}  [+] ... 
    [-] subject: {crypto_cert.get_subject().get_components()} 
    [-] issuer: {crypto_cert.get_issuer().get_components()}
    [-] serialNumber: {crypto_cert.get_serial_number()}
    [-] version: {crypto_cert.get_version()}
    [-] before: {not_before}
    [-] after: {not_after}[/]"""
    )
