import ssl
import socket

def check_ssl_status(hostname, port=443):
    context = ssl.create_default_context()
    try:
        with socket.create_connection((hostname, port), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert_info = ssock.getpeercert()
                return cert_info
    except socket.gaierror as e:
        return f"Error: Could not resolve hostname: {e}"
    except socket.timeout:
         return "Error: Connection timed out"
    except ssl.SSLError as e:
        return f"SSL Error: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

hostname = "www.youtube.com"
ssl_info = check_ssl_status(hostname)

if isinstance(ssl_info, str):
    print(ssl_info)
else:
    print(f"SSL certificate information for {hostname}:")
    print(f"  Subject: {ssl_info['subject']}")
    print(f"  Issuer: {ssl_info['issuer']}")
    print(f"  Valid from: {ssl_info['notBefore']}")
    print(f"  Valid until: {ssl_info['notAfter']}")