import securexgboost as xgb
from remote_attestation_server import serve
import os

HOME_DIR = os.path.dirname(os.path.realpath(__file__)) + "/../../../../"

print("Creating enclave")

enclave = xgb.Enclave(HOME_DIR + "build/enclave/xgboost_enclave.signed")
print("Waiting for remote attestation...")
serve()
