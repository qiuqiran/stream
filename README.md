 Django 的处理过程
 链接
 urls.py
 views.py
 index.html
 
 #所有电影接口-------------------------
 1.名称：查询电影列表
 2.描述：查询所有电影
 3.url：http://127.0.0.1:8000/api/s_all_list/
 4.调用方式：GET
 5.传入参数：id = all
 6.返回值：{
    "status": 200,
    "message": "success",
    "data": [
        {
            "id": 1,
            "name": "碟中谍6：全面瓦解 Mission: Impossible - Fallout",
            "rating_num": "8.2"
        },
        {
            "id": 2,
            "name": "瞒天过海：美人计 Ocean&#39;s Eight",
            "rating_num": "6.8"
        }
    ]
}
 7.状态码：{'status': 200, 'message': 'success', 'data': datas}
          {'status': 10010, 'message': 'id cannot be empty'}
 8.说明:
 
 
 
 #单个电影表接口-----------------------------
 1.名称：查询单个电影列表
 2.描述：查询电影
 3.url：http://127.0.0.1:8000/api/s_list/
 4.调用方式：GET
 5.传入参数：id 
 6.返回值：{'data':{'name':'蚁人2','rating_num':7.6},{'message':'success','satus':200}
 7.状态码：{'status':10021,'message':'id 不为空'}
          {'status':200, 'message':'success', 'data':datas}
          {'status': 10022, 'message': 'query result is empty'}
 8.说明:
 
 
 #查询短评接口
 