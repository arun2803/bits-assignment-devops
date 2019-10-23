import pymysql


def mysqldb_connect():
    db_host = 'localhost'
    db_pass = 'cha'
    db_name = 's'
    db_user = 'rot'
    try:
        conn = pymysql.connect(db=(db_name), user=(db_user), passwd=(db_pass), host=(db_host))
        return conn
    except Exception as e:
        print e


def get_ldapgroup_from_mysqldb(pack_name):
    try:
        conn = mysqldb_connect()
        cursor = conn.cursor()
        sql = "SELECT ldap_group_name FROM mapping_pack_group WHERE pack_name  = %s"
        cursor.execute(sql, pack_name)
        ldap_group_name = cursor.fetchone()
        ldap_group_name = str(ldap_group_name[0])
        return ldap_group_name

    except Exception as e:
        print e
