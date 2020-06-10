"""The Python implementation of the GRPC Remote Attestation client."""

from __future__ import print_function
import securexgboost as xgb
import argparse
import os

DIR = os.path.dirname(os.path.realpath(__file__))
HOME_DIR = DIR + "/../../../../"
username = "user1"

def run(channel_addr, sym_key_file, priv_key_file, cert_file):
    # Remote attestation
    print("Remote attestation")
    xgb.init_client(user_name=username, sym_key_file=sym_key_file, priv_key_file=priv_key_file, cert_file=cert_file, remote_addr=channel_addr)
    # Note: Simulation mode does not support attestation
    # pass in `verify=False` to attest()
    xgb.attest()
    print("Report successfully verified")

    print("Load training matrices")
    dtrain = xgb.DMatrix({username: HOME_DIR + "demo/python/multiclient-remote-control/data/c1_train.enc", "user2": HOME_DIR + "demo/python/multiclient-remote-control/data/c2_train.enc"}, encrypted=True)
    if not dtrain:
        print("Error loading data")
        return

    print("Creating test matrix")
    dtest1 = xgb.DMatrix({username: HOME_DIR + "demo/python/multiclient-remote-control/data/c1_test.enc"})
    dtest2 = xgb.DMatrix({"user2": HOME_DIR + "demo/python/multiclient-remote-control/data/c2_test.enc"})

    if not dtest1 or not dtest2:
        print("Error creating dtest")
        return

    print("Beginning Training")

    # Set training parameters
    params = {
            "tree_method": "hist",
            "n_gpus": "0",
            "objective": "binary:logistic",
            "min_child_weight": "1",
            "gamma": "0.1",
            "max_depth": "3",
            "verbosity": "0" 
    }

    # Train and evaluate
    num_rounds = 10 
    print("Training...")
    booster = xgb.train(params, dtrain, num_rounds)

    # Get our predictions
    predictions, num_preds = booster.predict(dtest1, decrypt=False)

    # Enable the other party to get its predictions
    _, _ = booster.predict(dtest2, decrypt=False)

    # Decrypt predictions
    print("Predictions: ", booster.decrypt_predictions(predictions, num_preds)[0])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip-addr", help="server IP address", required=True)
    parser.add_argument("--symmkey", help="path to symmetrix key used to encrypt data on client", required=True)
    parser.add_argument("--privkey", help="path to user's private key for signing data", required=True)
    parser.add_argument("--cert", help="path to user's public key certificate", required=True)

    args = parser.parse_args()

    channel_addr = str(args.ip_addr) + ":50051" 
    run(channel_addr, str(args.symmkey), str(args.privkey), str(args.cert))
