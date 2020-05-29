import securexgboost as xgb
import os

HOME_DIR = os.path.dirname(os.path.realpath(__file__)) + "/../../../../"

with open("../hosts.config") as f:
    nodes = f.readlines()
nodes = [x.strip().split(":")[0] for x in nodes]
print(nodes)

enclave = xgb.Enclave(HOME_DIR + "build/enclave/xgboost_enclave.signed", log_verbosity=0)
print("Waiting for client...")
xgb.serve(enclave, all_users=["user1", "user2"], nodes=nodes)