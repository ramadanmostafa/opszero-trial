import os
from subprocess import PIPE,Popen
import shlex
from datetime import datetime

DB_PRIMARY_HOST = os.environ['DB_PRIMARY_HOST']
DB_PRIMARY_PORT = os.environ['DB_PRIMARY_PORT']
DB_PRIMARY_USERNAME = os.environ['DB_PRIMARY_USERNAME']
DB_PRIMARY_PASSWORD = os.environ['DB_PRIMARY_PASSWORD']
DB_PRIMARY_NAME = os.environ['DB_PRIMARY_NAME']

DB_SECONDARY_HOST = os.environ['DB_SECONDARY_HOST']
DB_SECONDARY_PORT = os.environ['DB_SECONDARY_PORT']
DB_SECONDARY_USERNAME = os.environ['DB_SECONDARY_USERNAME']
DB_SECONDARY_PASSWORD = os.environ['DB_SECONDARY_PASSWORD']


def dump_table(host, database, user, password, port):

    command = f'pg_dump -h {host} -d {database} -U {user} -p {port} -Fc -f /tmp/table.dmp'

    p = Popen(command,shell=True,stdin=PIPE,stdout=PIPE,stderr=PIPE)

    return p.communicate(bytearray(f'{password}\n', 'utf-8'))

def restore_table(host,database,user,password, port):

    command = f'pg_restore -h {host} -d {database} -U {user} -p {port} /tmp/table.dmp'

    command = shlex.split(command)

    p = Popen(command,shell=False,stdin=PIPE,stdout=PIPE,stderr=PIPE)

    return p.communicate(bytearray(f'{password}\n', 'utf-8'))

def main():
    dump_table(
        host=DB_PRIMARY_HOST,
        database=DB_PRIMARY_NAME,
        user=DB_PRIMARY_USERNAME,
        password=DB_PRIMARY_PASSWORD,
        port=DB_PRIMARY_PORT
    )

    now = datetime.now()
    database_name = f'canal_prod_{now.month}_{now.day}_{now.year}'
    restore_table(
        host=DB_SECONDARY_HOST,
        user=DB_SECONDARY_USERNAME,
        password=DB_SECONDARY_PASSWORD,
        port=DB_SECONDARY_PORT,
        database=database_name,
    )


if __name__ == '__main__':
    main()
