from concurrent import futures
import click
import grpc
import yaml
from neomodel import config as config_neo

from account import AccountService
from account_pb2_grpc import add_AccountServiceServicer_to_server


_ONE_DAY_IN_SECONDS = 60 * 60 * 24

@click.option('--port', default=5000)   # noqa
@click.option('--max-workers', default=16)
def run():
    with open('./config.yaml') as f:
        config = yaml.safe_load(f)
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10)
    )
    server.add_insecure_port('127.0.0.1' + ':' + str('5000'))
    neo = config['neo4j']
    config_neo.DATABASE_URL = f'bolt://{neo["user"]}:{neo["pass"]}@{neo["host"]}:{neo["port"]}'
    add_AccountServiceServicer_to_server(
        AccountService(config), server
    )
    server.start()

    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    run()
