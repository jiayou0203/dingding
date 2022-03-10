# -- coding: utf-8 --

from ldap3 import Server, Connection, ALL, SUBTREE
from ldap3.core.exceptions import LDAPException, LDAPBindError


def connect_ldap_server():
    try:
       s = Server("172.29.19.92", port=10389, get_info=ALL, connect_timeout=5)
       conn2 = Connection(s, user='cn=admin,dc=example,dc=org', password='admin')
       connection = conn2.bind()  # Returns True or False
       res=conn2.delete('uid=test,ou=people,dc=example,dc=org')
       print(res)
    except LDAPBindError as e:
        connection = e
    return connection

'''
def get_ldap_users():
    # Provide a search base to search for.
    search_base = 'cn=admin,dc=example,dc=org'
    # provide a uidNumber to search for. '*" to fetch all users/groups
    search_filter = '(uidNumber=500)'
    # Establish connection to the server
    ldap_conn = connect_ldap_server()
    print(ldap_conn)
    try:
        # only the attributes specified will be returned
        ldap_conn.search(search_base=search_base,
                         search_filter=search_filter,
                         search_scope=SUBTREE,
                         attributes=['cn', 'sn', 'uid', 'uidNumber'])
        # search will not return any values.
        # the entries method in connection object returns the results
        results = connection.entries
    except LDAPException as e:
        results = e


s=Server("172.29.19.92",port=10389,get_info=ALL,connect_timeout=5)
conn2 = Connection(s, user='cn=admin,dc=example,dc=org', password='admin')
conn2.bind()
conn2.add('cn=user1,ou=people,dc=example,dc=org',object_class='inetOrgPerson')
response=conn2.delete(dn='uid=huoquan,ou=people,dc=example,dc=org')
print(response)
print(conn2.result["description"])
'''



if __name__=='__main__':
    print(connect_ldap_server())
