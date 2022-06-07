from brownie import *
import logging
from dotenv import load_dotenv
import json
from os.path import exists
load_dotenv()

def main():
    acc = accounts.load('huitzil_test_zeniq')
    acc.transfer('0x11E59Cf068c02f2fb22F488b3cce87FB26261455', 10000000000000000)
    t = Transaction.deploy('0x11E59Cf068c02f2fb22F488b3cce87FB26261455', 1e21, {'from': acc, "gas_limit": 600000, "allow_revert": True} )  
    print(t.address)
    print(acc)
    
    flag = True
    while flag:
        try:
            path = './build/deployments/383414847825/{address}.json'.format(address=t.address)
            f = open(path)
            data = json.load(f)
            if data:
                flag = False
            f.close()
            #print('abi',data['abi'])
            abi = json.dumps(data['abi'])
            contractAddresses = {
                data['deployment']['chainid']: data['deployment']['address']
            }            
            #print('contract',contractAddresses)
            contractAddresses = json.dumps(contractAddresses)
            print(abi)
            print(contractAddresses)
            
        except:
            pass

    #t.payBill()