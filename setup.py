from setuptools import setup

setup(
    name="prox-ez",
    version="1.0.0",
    description="Prox-Ez: an HTTP proxy that transparently handles HTTP "
                "authentications (NTLM EPA, Kerberos, pass-the-hash, "
                "overpass-the-hash, pass-the-ticket).",
    long_description=(
        "Prox-Ez is an intercepting HTTP proxy that performs HTTP "
        "authentication on your behalf, supporting NTLM with EPA "
        "(channel and service binding), Kerberos, pass-the-hash, "
        "overpass-the-hash (pass-the-key) and pass-the-ticket. See the "
        "project README for usage."
    ),
    url="https://github.com/synacktiv/Prox-Ez",
    license="GPL-3.0",
    # Prox-Ez is a single top-level module (proxy.py), not a package.
    py_modules=["proxy"],
    python_requires=">=3.9",
    install_requires=[
        "cryptography>=42.0.0",
        # < 26.2 keeps the legacy crypto.X509Extension / X509.add_extensions
        # API that proxy.py uses for certificate generation.
        "pyOpenSSL>=25.0.0,<26.2",
        # < 0.13 keeps mutable h11 event objects (proxy.py mutates
        # Request.target); 0.13+ froze them.
        "h11>=0.12,<0.13",
        "pyspnego>=0.10.0",
        "impacket>=0.11.0",
        "pyasn1>=0.5.0",
    ],
    entry_points={
        "console_scripts": [
            "prox-ez=proxy:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "Topic :: Security",
    ],
)
