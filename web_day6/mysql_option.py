"""
作者：张浩
时间：2023/7/25  14:51
邮箱：88302599@qq.com
"""

import pymysql


class Mysql_Option:
    def __init__(self, host, user, pwd, port, db):
        self.conn = pymysql.connect(host=host,
                                    user=user,
                                    password=pwd,
                                    port=port,
                                    database=db,
                                    charset='utf8')

    def find_all(self, sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        return res

    def find_one(self, sql):
        cur = self.conn.cursor()
        cur.execute(sql)
        res = cur.fetchone()
        cur.close()
        return res

    def find_count(self, sql):
        cur = self.conn.cursor()
        res = cur.execute(sql)
        cur.close()
        return res

    def __del__(self):
        self.conn.close()


if __name__== "__main__":
    db = Mysql_Option(host="192.168.2.109",
                     user = "root",
                     pwd="root",
                     port=3306,
                     db = "fire")

    res = db.find_one("select * from manager")
    print(res)