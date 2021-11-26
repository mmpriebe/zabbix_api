from zabbix_api import ZabbixAPI

URL = 'http://{ip}'
USERNAME = 'user'
PASSWORD = 'Password'

try:
    zapi = ZabbixAPI(URL, timeout=15)
    zapi.login(USERNAME, PASSWORD)
    print(f'Conectado na API do Zabbix, versao atual {zapi.api_version()}')
except Exception as err:
    print(f'Falha ao conectar na API do Zabbix, erro: {err}')

groupids = ['28']
groups = [{"groupid": groupid} for groupid in groupids]
info_interfaces = {
    "1": {"type": "agent", "id": "1", "port": "10050"},
    "2": {"type": "SNMP", "id": "2", "port": "161"},
}
interface = {
    "type": info_interfaces['1']['id'],
    "main": 1,
    "useip": 0,
    "dns": "www.facebook.com",
    "ip": "",
    "port": info_interfaces['1']['port']
}
try:
    create_host = zapi.host.create({
        "groups": groups,
        "host": "FACEBOOK",
        "interfaces": interface,
        "tags": [{
            "tag": "SERVICOS",
            "value": "www"}],
        "templates": [{"templateid": "10436"}],
    })
    print(f'Host cadastrado com sucesso!')
except Exception as err:
    print(f'Falha ao cadastrar o host: {err}')
