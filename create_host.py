#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from zabbix_api import ZabbixAPI
import csv
import os

URL = os.environ.get('url')
USERNAME = os.environ.get('user')
PASSWORD = os.environ.get('password')

try:
    zapi = ZabbixAPI(URL, timeout=15)
    zapi.login(USERNAME, PASSWORD)
    print(f'Conectado na API do Zabbix, versao atual {zapi.api_version()}')
except Exception as err:
    print(f'Falha ao conectar na API do Zabbix, erro: {err}')

 
f = csv.reader(open('hosts.csv'), delimiter=';') #lendo-a-lista de host e separando pelo delimitador ';'

for [hostname,dns] in f:

   zapi.host.create({"host": hostname, 
      "interfaces": [ {"type": "1",
      "main": "1",
      "useip": "0",
      "ip":"",
      "dns": dns,
      "port": "10050"}], 
      "groups": [{ "groupid": "28"}], #id do host grupo
      "templates": [{ "templateid":"10436"}], #id do template
      "tags": [{
            "tag": "SERVICOS",
            "value": "www"}],

   })
   print(f'Host: [{hostname}] cadastrado com sucesso no Zabbix.')
