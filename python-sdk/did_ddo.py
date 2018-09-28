#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
from binascii import a2b_hex
from time import time

from ontology.ont_sdk import OntologySdk
from ontology.wallet.wallet_manager import WalletManager

from ontology.vm import build_vm
from ontology.core.transaction import Transaction

from ontology.account.account import Account
from ontology.common.address import Address
from ontology.crypto.signature_scheme import SignatureScheme
from ontology.exception.exception import SDKException

import argparse

#rpc_address = "http://127.0.0.1:20336"
rpc_address =  "http://120.79.147.72:9009"
sdk = OntologySdk()
sdk.rpc.set_address(rpc_address)
private_key1 = "75de8489fcb2dcaf2ef3cd607feffde18789de7da129b5e97c81e001793cb7cf"
private_key2 = "c19f16785b8f3543bbaf5e1dbb5d398dfa6c85aaad54fc9d71203ce83e505c07"
# private_key3 = "1383ed1fe570b6673351f1a30a66b21204918ef8f673e864769fa2a653401114"
acc1 = Account(private_key1, SignatureScheme.SHA256withECDSA)
acc2 = Account(private_key2, SignatureScheme.SHA256withECDSA)
# acc3 = Account(private_key3, SignatureScheme.SHA256withECDSA)
did = "did:ont:" + acc2.get_address_base58()

def test_ontid():
    print("ontid")
    tx = sdk.native_vm().ont_id().new_registry_ontid_transaction(did, acc2.get_public_key(),
                                                                    acc1.get_address_base58(), 200000, 0)
    tx = sdk.sign_transaction(tx, acc2)
    tx = sdk.add_sign_transaction(tx, acc1)
    print(len(tx.hash256_hex()), "==", 64)
    print(len(tx.serialize(is_hex=True)),"==", 806)
    try:
        sdk.rpc.send_raw_transaction(tx)
    except SDKException as e:
        print(59000, "==", e.args[0])
        msg = 'Other Error, [NeoVmService] service system call error!: [SystemCall] ' \
                'service execute error!: [Invoke] Native serivce function execute error!: ' \
                'register ONT ID error: already registered'
        print(msg,"==", e.args[1])    

def new_get_ddo_transaction():
    print("get_ddo")
    tx = sdk.native_vm().ont_id().new_get_ddo_transaction(did)
    out_ddo = sdk.rpc.send_raw_transaction_pre_exec(tx)

    estimate_ddo = "26010000002102d3d048aca7bdee582a611d0b8acc45642950dc6167aee63abbdcd1a5781c6319"
    print(estimate_ddo[2:] + " == " + out_ddo[2:len(estimate_ddo)])
    parsed_ddo = sdk.native_vm().ont_id().parse_ddo(did, out_ddo)
    print(parsed_ddo)
    print(parsed_ddo['Owners'][0]['PubKeyId'][:len(did)] +" == "+ did)

def test_new_add_attribute_transaction():
    print("add attribute")
    attris = []
    attri = {}
    attri["key"] = "keyeqw"
    attri["type"] = "string"
    attri["value"] = "value100"
    attris.append(attri)
    tx = sdk.native_vm().ont_id().new_add_attribute_transaction(did, acc2.get_public_key(), attris,
                                                                acc1.get_address_base58(), 200000,
                                                                0)
    tx = sdk.sign_transaction(tx, acc2)
    tx = sdk.add_sign_transaction(tx, acc1)
    tx_hash = sdk.rpc.send_raw_transaction(tx)
    print(tx_hash +" == "+tx.hash256_explorer())    


if __name__ == '__main__':
    test_ontid()
    test_new_add_attribute_transaction()
    new_get_ddo_transaction()
