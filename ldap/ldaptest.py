# -- coding: utf-8 --

from ldap3 import Server, Connection, ALL

server1=Server("172.29.19.92",port=10389,use_ssl=True,get_info=ALL,connect_timeout=5)
server2=Server("172.29.19.92",port=10389,get_info=ALL,connect_timeout=5)

LDAP_SERVER_POOL=[server2]
SERVER_USER='cn=admin,dc=example,dc=org'
SERVER_PASSWORD='admin'


class AD():
    def __init__(self):
        self.conn=Connection(
        server=LDAP_SERVER_POOL,
        auto_bind=True,
        read_only=False,
        user=SERVER_USER,
        password=SERVER_PASSWORD,
    )

    def create_obj(self,dn="cn=admin,dc=example,dc=org",type="user",attr=None):
        print(self.conn)
        '''
        :param dn:dn="uid=pythontest,ou=people,dc=example,dc=org"
        '''
        dn = "uid=pythontest,ou=people,dc=example,dc=org"
        res = self.conn.add(dn, attributes={'userPassword':'312321'},object_class=['inetOrgPerson'])
        print(res)
        print(self.conn.result)

if __name__=='__main__':
    ad=AD()
    ad.create_obj()