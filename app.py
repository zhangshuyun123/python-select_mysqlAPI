from flask import Flask, request
import pymysql
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/select/salary/", methods=["GET"])
def check():
    # 默认返回内容
    return_dict = {'code': '200', 'msg': '处理成功', 'result': False}
    # print(return_dict)
    # 判断入参是否为空
    if request.args is None:
        return_dict['return_code'] = '504'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    get_data = request.args.to_dict()
    dbname = get_data.get('dbname')
    tbname = get_data.get('tbname')
    condition = get_data.get('condition')
    value = get_data.get('value')
    return_dict['result'] = sql_result(dbname, tbname, condition, value)



    return return_dict
    #return json.dumps(return_dict, ensure_ascii=False)

def sql_result(dbname, tbname, condition, value):
    config = {
        'host': '1',
        'port': 36,
        'user': 'ro_db',
        'passwd': 'e',
        'charset': 'utf8',
        'cursorclass': pymysql.cursors.DictCursor
    }
    conn = pymysql.connect(**config)
    try:
        print("数据库连接成功")
        cursor = conn.cursor()
        sql = 'SELECT * FROM %s.%s where %s=%s'%(dbname, tbname, condition, value)
        cursor.execute(sql)

        results = cursor.fetchall()
        for data in results:
            print(data)
    except:
        print("查询失败")
    #conn.close()
    #conn.close()
    return results


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
