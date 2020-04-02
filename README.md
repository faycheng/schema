# schema

Fetch and parse table structure information from mysql.

### Usage

```
>>> import schema
>>> s = schema.Schema("mysql://test:test@127.0.0.1:3306/test")
>>> # list all tables
>>> s.tables
[<schema.Table object at 0x105e05ac0>, <schema.Table object at 0x105df9700>, <schema.Table object at 0x105dad610>, <schema.Table object at 0x105dad3a0>, <schema.Table object at 0x105d88d30>, <schema.Table object at 0x105e14cd0>, <schema.Table object at 0x105e14d00>, <schema.Table object at 0x105defb20>, <schema.Table object at 0x105defc70>, <schema.Tab
le object at 0x105defd60>, <schema.Table object at 0x105defd30>, <schema.Table object at 0x105defc40>, <schema.Table object at 0x105df69d0>, <schema.Table object at 0x105df6f40>, <schema.Table object at 0x105df6070>, <schema.Table object at 0x105e994f0>, <schema.Table object at 0x105e99bb0>, <schema.Table object at 0x105e99af0>, <schema.Table object at
 0x105e992e0>, <schema.Table object at 0x105e990a0>, <schema.Table object at 0x105e99310>, <schema.Table object at 0x105e99fa0>, <schema.Table object at 0x105e99ca0>, <schema.Table object at 0x105df3820>, <schema.Table object at 0x105df3b80>, <schema.Table object at 0x105df3a90>, <schema.Table object at 0x105df3c10>, <schema.Table object at 0x105df31c0
>, <schema.Table object at 0x105df3a60>, <schema.Table object at 0x105df3340>, <schema.Table object at 0x105e0a6d0>, <schema.Table object at 0x105e0a460>, <schema.Table object at 0x105e0a130>, <schema.Table object at 0x105e0a820>, <schema.Table object at 0x105e0a400>]
>>> # show the first table information
>>> s.tables[0].__dict__
{'name': 'cancel_order', 'comment': '取消单表'}
>>> # show all fields's information of the first table
>>> [field.__dict__ for field in s.tables[0].fields]
[{'name': 'order_id', 'comment': '订单id', 'origin: 'bigint(20) unsigned'}, {'name': 'status', 'comment': '取消状态 2:申请 3:回复 4:仲裁中 5: 失败 6:成功', 'origin_type}, {'name': 'category', 'comment': '取消类别 0:普通取消', 'origin_type': 'tinyint(4)'}, {'name': 'total', 'comment': 'origin_type': 'decimal(10,2) unsigned'}, {'name': 'user_id', 'comment': '用户id', 'origin_type': 'bigint(20)'}, {'name':
'rst_id', 'comment': '商户id', 'origin_type': 'bigint(20)'}}]
```