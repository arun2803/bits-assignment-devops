import ldap


def ldap_connect(ldap_group_name):
    try:

        con = ldap.initialize('ldap://abc.com:389')
        con.simple_bind_s("cn=user,ou=Users,o=adc", "password")
        ldap_base = "ou=Groups,o=adc"
        # print ldap_group_name
        query = "(cn={})".format(ldap_group_name)
        result = con.search_s(ldap_base, ldap.SCOPE_SUBTREE, query)
        # print result
        list_of_users = []
        for i in result[0][1]['uniqueMember']:
            j = i.split(',')
            k = j[0].split('=')
            list_of_users.append(k[1])

        return list_of_users


    except ldap.LDAPError, e:
        print e
