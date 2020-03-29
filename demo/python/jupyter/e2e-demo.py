
# coding: utf-8

# # Secure XGBoost Demo Notebook
# This notebook provides an example of how one could use Secure XGBoost. In this example, we will use the client's encrypted data to train an XGBoost model on the server, within a secure enclave.
#
# For the purposes of the example, the client and server both run on the same machine. However, in an actual deployment, the client process would be executed on a separate, trusted machine. The server is assumed to be completely untrusted (except the secure enclave), so no sensitive data should be left in plaintext (i.e., unencrypted) outside the enclave.
#
# The example consists of the following steps.
#
# 1. **Key generation**: The client generates a secret symmetric key
# 2. **Data encryption**: The client uses the key to encrypt its data
# 3. **Enclave preparation**: The server creates an enclave, and starts a process within it. The client [*attests*](https://software.intel.com/en-us/articles/code-sample-intel-software-guard-extensions-remote-attestation-end-to-end-example) the enclave process, and securely transfers its key to the enclave.
# 4. **Data loading**: The enclave loads the client's encrypted data
# 5. **Training**: The enclave trains a model using the provided data
# 6. **Prediction**: The enclave runs predictions on the data, and produces a set of encrypted results; the client decrypts the results.
#
# Documentation for Secure XGBoost can be found [here](https://mc2-xgboost.readthedocs.io/en/latest/index.html).

# In[ ]:


#get_ipython().run_line_magic('load_ext', 'autoreload')
#get_ipython().run_line_magic('autoreload', '2')

import securexgboost as xgb
import os

HOME_DIR = os.getcwd() + "/../../../"

crypto = xgb.CryptoUtils()


# ## 1. Key Generation
# Generate a key to be used for encryption.

# In[ ]:


KEY_FILE = "key.txt"

# Generate a key you will be using for encryption
crypto.generate_client_key(KEY_FILE)


# ## 2. Data Encryption
# Use the key generated above to encrypt our data.

# In[ ]:


training_data = HOME_DIR + "demo/data/agaricus.txt.train"
enc_training_data = "train.enc"

# Encrypt training data
crypto.encrypt_file(training_data, enc_training_data, KEY_FILE)


# In[ ]:


test_data = HOME_DIR + "demo/data/agaricus.txt.test"
enc_test_data = "test.enc"

# Encrypt test data
crypto.encrypt_file(test_data, enc_test_data, KEY_FILE)


# ## 3. Enclave preparation
# We'll need to create an enclave, authenticate the enclave, and lastly give the enclave the key we used to encrypt the data.

# First, the server creates an enclave, and runs the secure XGBoost binary inside the enclave. (This step may take several seconds to initialize the enclave.)

# In[ ]:


# Define enclave launch parameters
flags = 0

# Uncomment these lines to run the enclave in debug mode (NOTE: this is not secure)
OE_ENCLAVE_FLAG_DEBUG = 1
flags = (flags | OE_ENCLAVE_FLAG_DEBUG)

# Uncomment these lines to run the enclave in simulation mode
# NOTE: this is not secure, and should only be used for testing purposes on non-enclave machines
OE_ENCLAVE_FLAG_SIMULATE = 2
flags = (flags | OE_ENCLAVE_FLAG_SIMULATE)

# Create an enclave
# NOTE: the directory changed 
enclave = xgb.Enclave(HOME_DIR + "build/enclave/xgboost_enclave.signed", log_verbosity = 3)


# Next, the client verifies that the enclace has been correctly deployed, using remote attestation.

# In[ ]:


# Remote Attestation

# Client gets a `report` from the server generated by the enclave
enclave.get_remote_report_with_pubkey()

# Client parses the report, and extracts a public key generated by the enclave
enclave_pem_key, enclave_key_size, remote_report, remote_report_size = enclave.get_report_attrs()

# Client veries the report
# disabled for testing purposes
# enclave.verify_remote_report_and_set_pubkey()


# Finally, the client securely transfers the symmetric key it generated to the enclave.

# In[ ]:


# Read the generated symmetric key into memory
print("testing multiple user")
multiple_user = True

sym_key = None

with open(KEY_FILE, "rb") as keyfile:
    sym_key = keyfile.read()

# Encrypt the symmetric key using the enclave's public key
enc_sym_key, enc_sym_key_size = crypto.encrypt_data_with_pk(sym_key, len(sym_key),
                                                            enclave_pem_key, enclave_key_size)

print("got past the encrypting data with public key")
# multi-user case
# the certificate also has to be sent along in the modified version because that's how you keep track of users.
# the certificate includes the user's public key and the root ra's signature of it
# crypto.add_client_key_with_certificate(user_public_key, public_key_siganture, enc_sym_key, enc_sym_key_size, sig, sig_size)

if multiple_user:

    # you can set which user you want to add
    ## this information is already included in the certificate but here we are using it to find the certificate
    user_name = "user1"
    user_id = 1 
    sig, sig_size = crypto.sign_data("userkeys/private_user_{0}.pem".format(user_id), enc_sym_key, enc_sym_key_size)

    with open("{0}.crt".format(user_name), "r") as cert_file:
        user_certificate = cert_file.read()

    crypto.add_client_key_with_certificate(user_certificate,
                                           enc_sym_key, enc_sym_key_size,
                                           sig, sig_size)

else:
    # Sign the encrypted symmetric key (so enclave can verify it came from the client)
    sig, sig_size = crypto.sign_data("keypair.pem", enc_sym_key, enc_sym_key_size)
    # Send the encrypted key to the enclave
    crypto.add_client_key(enc_sym_key, enc_sym_key_size, sig, sig_size)

print("user key added!")

# ## 4. Data loading
# The enclave is now ready to start the training process. First, load the encrypted data into a `DMatrix` within the enclave.

# In[ ]:


# Load training data
dtrain = xgb.DMatrix(os.getcwd() + "/" + enc_training_data, encrypted=True, username= user_name)


# In[ ]:


# Load test data
dtest = xgb.DMatrix(os.getcwd() + "/" + enc_test_data, encrypted=True, username = user_name)


# ## 5. Training
# Set the training parameters, and start the training process within the enclave.

# In[ ]:


# Set parameters
params = {
        "tree_method": "hist",
        "n_gpus": "0",
        "objective": "binary:logistic",
        "min_child_weight": "1",
        "gamma": "0.1",
        "max_depth": "3",
        "verbosity": "1"
}


# In[ ]:


# Train
num_rounds = 10
booster = xgb.train(params, dtrain, num_rounds, evals=[(dtrain, "train"), (dtest, "test")])


# ## 6. Prediction
# Our `predict()` function yields predictions in an encrypted manner. The buffer that it returns will need to be decrypted by the client using the same key that the original data was encrypted with.

# In[ ]:


# Get Encrypted Predictions
print(user_name)
enc_preds, num_preds = booster.predict(dtest, username = user_name)


# In[ ]:


# Decrypt Predictions
preds = crypto.decrypt_predictions(sym_key, enc_preds, num_preds)
print(preds)
