## 项目介绍
最近最近看到了一个非常有意思的[文章](https://hackernoon.com/learn-blockchains-by-building-one-117428612f46)，
作者用python做了一个非常简单的区块链，这也符合我现在做的事情---让更多的人更简单方便的了解区块链，比如我另一个[开源项目](https://github.com/zslomo/SLBlockchainJ)
没有什么是比实际构建一条链更cool、更有意思的事情了
但是作者可能是为了省事，代码非常紊乱，bug不断，而且有逻辑上的硬伤（比如竟然没有创世区块？？）所以我修改了文章中的代码，加入了抽象类，增加工厂设计模式，然后实现了这个项目
### 项目依赖
* python-3.6 +
* Flask 0.12.2 
* requests 2.18.4 
### 部署区块链
 你可以用任何喜欢的容器部署Flask 框架，如果仅仅是玩一玩，可以直接运行:
```angular2html
$ python Controller.py
```
 API开放在5000端口（Flask默认端口）
 
### 区块结构
```angular2html
block = {
    'index': 1,
    'timestamp': 1506057125.900785,
    'transactions': [
        {
            'sender': "8527147fe1f5426f9dd545de4b27ee00",
            'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
            'amount': 5,
        }
    ],
    'proof': 324984774000,
    'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}
```
### API访问：
#### 发送交交易格式
```angular2html
{
 "sender": "my address",
 "recipient": "someone else's address",
 "amount": 5
}
```
请求示例：
```angular2html
$ curl -X POST -H "Content-Type: application/json" -d '{
 "sender": "d4ee26eee15148ee92c6cd394edd974e",
 "recipient": "someone-other-address",
 "amount": 5
}' "http://localhost:5000/transactions/new"
```
返回示例：
```angular2html
{
    "message": "Transaction will be added to Block 3"
}
```
#### 获得区块链信息
```angular2html
$ curl  http://localhost:5000/chain
```
返回示例：
```angular2html
{
    "chain": [
        {
            "index": 1,
            "previous_hash": "",
            "proof": 0,
            "timestamp": 1509964373.2914333,
            "transactions": ""
        },
        {
            "index": 2,
            "previous_hash": "8663cd6bae9b7c3efeff24f213533635737feb47ac2bbd5f27c663920c2b6116",
            "proof": 69732,
            "timestamp": 1509964377.6662602,
            "transactions": [
                {
                    "amount": 1,
                    "recipient": "1f19dbc874314416b66507e0abfb7df1",
                    "sender": "0"
                }
            ]
        }
    ],
    "length": 2
}
```
#### 挖矿
```angular2html
$ curl  http://localhost:5000/mine
```
返回示例：
```angular2html
{
  "hash": "96cae35ce8a9b0244178bf28e4966c2ce1b8385723a96a6b838858cdd6ca0a1e",
  "transactions": [
    {
      "amount": 1,
      "recipient": "",
      "sender": ""
    },  
  "length": 1
}
```
### TODO
* 项目可能存在潜在的bug，我没有全面测试
* 没有使用数据库，下一步准备使用levelDB存储数据
* 仅仅是一个sample 很多安全性问题没有处理
### 联系作者
*bintan@fudan.edu.cn*