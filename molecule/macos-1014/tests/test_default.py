import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_libmongocrypt(host):
    cmd = host.run("/usr/local/bin/pkg-config libmongocrypt --libs --cflags")
    assert cmd.stdout == (
        "-I/usr/local/include/mongocrypt "
        "-I/usr/local/Cellar/mongo-c-driver/1.16.2/include/libbson-1.0 "
        "-L/usr/local/lib -lmongocrypt\n"
    )
