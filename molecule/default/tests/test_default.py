import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_libmongocrypt(host):
    assert host.file("/usr/include/mongocrypt").exists
    assert host.file("/usr/include/mongocrypt").is_directory

    assert host.file("/usr/include/mongocrypt/mongocrypt-compat.h").exists
    assert host.file("/usr/include/mongocrypt/mongocrypt.h").exists
    assert host.file("/usr/include/mongocrypt/mongocrypt-export.h").exists
    assert host.file("/usr/lib/x86_64-linux-gnu/libmongocrypt.so").exists

    cmd = host.run("sudo dpkg -s libmongocrypt-dev | grep 1.0.1-0")
    assert cmd.succeeded
