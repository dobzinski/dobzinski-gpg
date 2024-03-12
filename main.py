import os
import subprocess
import configparser

iniFile = './config.ini'

config = configparser.ConfigParser()
config.read(iniFile)
iniPassphrase = config['config']['passphrase']
iniRecursive = config['config']['recursive']
iniPath = config['config']['path']

recursive = eval(iniRecursive)
folders = iniPath.split(',')
