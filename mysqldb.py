import pymysql as mysql



def 获取单价(name):
    conn = mysql.connect(host = 'localhost',user = 'root',password = 'root',database = '蔬菜识别')
    cursor = conn.cursor()
    try:
        sqlStr = "select 单价 from 单价 where 菜名 = '" + name + "'"
        cursor.execute(sqlStr)

        results = cursor.fetchall()

        for row in results:
            单价 = row[0]

        conn.close()
        return 单价
    except:
        return '无菜品'


def 添加记录(name, weight):
    conn = mysql.connect(host = 'localhost',user = 'root',password = 'root',database = '蔬菜识别')
    cursor = conn.cursor()

    sqlStr = "insert into 记录 (菜品类型, 重量) values ('%s', '%s')"%(name, weight)

    try:
        cursor.execute(sqlStr)
        conn.commit()
        conn.close()
        return '成功'
    except:
        conn.rollback()
        conn.close()

        return '失败'

def 添加菜品(name, cost):
    conn = mysql.connect(host = 'localhost',user = 'root',password = 'root',database = '蔬菜识别')
    cursor = conn.cursor()
    
    sqlStr = "insert into 单价 (菜名, 单价) values ('%s', '%s')"%(name, cost)
    
    try:
        cursor.execute(sqlStr)
        conn.commit()
        conn.close()
        return '成功'
    except:
        conn.rollback()
        conn.close()

        return '失败'
        
def 修改单价(name, cost):
    conn = mysql.connect(host = 'localhost',user = 'root',password = 'root',database = '蔬菜识别')
    cursor = conn.cursor()
    
    sqlStr = "update 单价 set 单价 = '%s' where 菜名 = '%s'"%(cost, name)
    
    try:
        cursor.execute(sqlStr)
        conn.commit()
        conn.close()
        return '成功'
    except:
        conn.rollback()
        conn.close()

        return '失败'
        
# print(获取单价('feng'))
# print(修改单价('白菜','10'))
