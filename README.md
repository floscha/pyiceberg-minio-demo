# PyIceberg MinIO Demo

> The simplest way to get Apache Iceberg working locally.

## ⭐ Motivation

The goal of this repository is to have a fully local, Python-based, Apache Iceberg setup that allows tinkering with Iceberg's functionality.

The setup consists of the following essential Iceberg components:
- **Compute**: [PyIceberg](https://py.iceberg.apache.org/)
- **Catalog**: [Tabular REST Catalog](https://hub.docker.com/r/tabulario/iceberg-rest)
- **Object Storage**: [MinIO](https://min.io/)

## 🚀 Usage

Start the docker-compose config (mainly taken from [here](https://iceberg.apache.org/spark-quickstart/?ref=blog.min.io#docker-compose)) which sets up the Iceberg REST Catalog and MinIO for Storage:
```sh
docker-compose up -d
```

Use [uv](https://github.com/astral-sh/uv) to run the demo script which creates an Iceberg table, writes some data to it and reads that data, all using PyIceberg and PyArrow:
```sh
uv run demo.py
```

To access the files created by Apache Iceberg you can either use the CLI:
```sh
docker-compose exec mc bash
# then
/usr/bin/mc ls minio/warehouse/default/cities
```

or the MinIO Web UI under http://localhost:9001/browser/warehouse/default%2Fcities%2F.
The latter also allows you to easily download files for local inspection.
