from pathlib import Path
import json, sys
sys.path.insert(0, str(Path(__file__).resolve().parent / "src"))
import ssl, tempfile, stat
from cert_check import create_lab, tls_exchange, fingerprint_sha256
with tempfile.TemporaryDirectory(prefix="p067-documentazione-") as temp:
    d = Path(temp)
    paths = create_lab(d / "valido")
    payload = b"ordine=42\n"
    exchange = tls_exchange(paths["cert"], paths["key"], paths["ca"], payload=payload)
    cases = [
        ("hostname", paths, paths["ca"], {"hostname": "altro.invalid"}),
        ("ip_non_in_SAN", paths, paths["ca"], {"hostname": "127.0.0.1"}),
        ("ca_sconosciuta", paths, create_lab(d / "altra_ca")["ca"], {}),
        ("scaduto", create_lab(d / "scaduto", validity="expired"), None, {}),
        ("futuro", create_lab(d / "futuro", validity="future"), None, {}),
        ("eku_client", create_lab(d / "eku_client", server_auth=False), None, {}),
    ]
    rejections = []
    for name, p, ca, options in cases:
        try:
            tls_exchange(p["cert"], p["key"], ca or p["ca"], **options)
        except ssl.SSLCertVerificationError as exc:
            rejections.append({"case": name, "status": "RIFIUTATO", "error_class": type(exc).__name__, "verify_code": exc.verify_code, "verify_message": exc.verify_message})
        else:
            raise AssertionError(f"caso negativo accettato: {name}")
    result = {"payload_hex": payload.hex(), "payload_size": len(payload), "echo_equal": exchange["payload"] == payload,
              "tls_version": exchange["tls_version"], "cipher": exchange["cipher"], "peer_sha256": exchange["peer_sha256"],
              "fingerprint_equal": exchange["peer_sha256"] == fingerprint_sha256(paths["cert"]),
              "key_mode_octal": format(stat.S_IMODE(paths["key"].stat().st_mode), "04o"), "rejections": rejections}
    assert result["echo_equal"] and result["fingerprint_equal"] and len(rejections) == 6
print(json.dumps(result, ensure_ascii=False, indent=2))
