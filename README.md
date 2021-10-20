
<h1 align="center">@amirh-moshfeghi/gRPC-Central-Authentication-Service</h1>

<p align="center">
  <b>This is the simple instruction to run and test a gRpc CAS (central authentication service) </b></br>
</p>

  <p align="left">Use this instruction below so you can run and test dataflow using a RPC gui client named  <a href="https://github.com/uw-labs/bloomrpc"> bloomrpc </a> .you can <code>contribute</code> to this project and please dont hesitate to ask any kind of question.<br><br>
NOTE: this sample is not the optimum solution for NEO4J because relations and graphs has not been implemented yet. so you can use any type of databases. just change the <code>config.yaml</code> file and change your models based on the database  </p>

<br />




## ➤ Table of Contents

* [➤ Pre-Requisites]
* [➤ Execute and Run]
* [➤ Contributors]
* [➤ License]

</details>

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#installation)

## ➤ Pre-Requisites

```
- Neo4j
- bloomrpc
```

These are same Pre-Requisites for both Linux and Windows. bloomrpc is a nice tool so you can send request to grpc server like what you can do in <code>postman</code> and get response.neo4j is a graph database and this uses a query language named cypher but in this project i tried to use and ogm library called <code>neomodel</code> so queries are a lot cleaner and more pythonic

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#installation)

## ➤ Installation

```bash
$ git clone https://github.com/amirh-moshfeghi/gRPC-Central-Authentication-Service.git
```

clone the project and create a virtual environment for your project


```python
#creating virtual env
python3 -m venv env
#activating virtual env
source env/bin/activate
```

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#getting-started-slower)

## ➤ Execute and Run


```python
python main.py
```

[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#getting-started-slower)




## ➤ Contributors


| [<img alt="Amir Moshfeghi" src="https://avatars.githubusercontent.com/u/92248573?s=40&v=4" width="60">](https://amirmoshfegh.com) |  
|:--------------------------------------------------:|
| [Amirhossein  Moshfeghi](https://www.linkedin.com/in/amir-moshfeghi) |  



### License



[![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/colored.png)](#license)

## ➤ License

Licensed under [MIT](https://opensource.org/licenses/MIT).






