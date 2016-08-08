# /usr/bin/python
# -*- coding:utf-8 -*-
# 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中.
# 下面贴一下常用的函数：

# commit() 提交,不提交的话是不会输入到mysql中的！
# rollback() 回滚
# cursor用来执行命令的方法:
# callproc(self, procname, args):用来执行存储过程,接收的参数为存储过程名和参数列表,返回值为受影响的行数
# execute(self, query, args):执行单条sql语句,接收的参数为sql语句本身和使用的参数列表,返回值为受影响的行数
# executemany(self, query, args):执行单挑sql语句,但是重复执行参数列表里的参数,返回值为受影响的行数
# nextset(self):移动到下一个结果集

# cursor用来接收返回值的方法:
# fetchall(self):接收全部的返回结果行.
# fetchmany(self, size=None):接收size条返回结果行.如果size的值大于返回的结果行的数量,则会返回cursor.arraysize条数据.
# fetchone(self):返回一条结果行.

# scroll(self, value, mode='relative'):移动指针到某一行.如果mode='relative',则表示从当前所在行移动value条,
# 如果 mode='absolute',则表示从结果集的第一行移动value条.

import MySQLdb
import warnings


# warnings.filterwarnings("ignore")忽略警告
def store_mysql(filepath):
    conn = MySQLdb.connect(host='localhost', user='root', passwd='JWW930729', port=3306,
                           unix_socket='/var/lib/mysql/mysql.sock', charset='utf8')
    cur = conn.cursor()

    cur.execute('create database if not exists python_test ')
    conn.select_db('python_test')

    cur.execute('show tables;')
    tables = cur.fetchall()
    findtables = False
    for table in tables:
        if 'YHM' in table:
            findtables = True

    if not findtables:
        cur.execute('''
		create table if not exists python_test.YHM (
		`id` int not null auto_increment,
		`YHMcode` varchar(40) not null,
		primary key(`id`));
		''')

    fo = open(filepath, 'rb')
    # Call readline() repeatedly and return a list of the lines so read.
    for line in fo.readlines():
        cur.execute("insert into YHM (YHMcode) values(%s);", line.strip())

    conn.commit()
    cur.close()
    conn.close()
    print "数据导入成功！"


if __name__ == "__main__":
    store_mysql('/root/pythondir/YHM.txt')
