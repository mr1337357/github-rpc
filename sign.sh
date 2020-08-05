#!/bin/bash
openssl dgst -sha256 -sign ~/.keys/privkey-rpc.pem -out runme.sh.sig runme.sh
