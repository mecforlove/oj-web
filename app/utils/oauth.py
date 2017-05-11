#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mec
import binascii
from Crypto import Random
from Crypto.Cipher import AES


def cookie_encrypt(key, val):
    if len(key) > 32:
        key = key[:32]
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    return binascii.hexlify(iv + cipher.encrypt(val))


def cookie_decrypt(key, val):
    if len(key) > 32:
        key = key[:32]
    val = binascii.unhexlify(val)
    iv = val[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CFB, iv)
    return cipher.decrypt(val[AES.block_size:])