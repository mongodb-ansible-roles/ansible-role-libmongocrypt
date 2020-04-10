Ansible role for libmongocrypt
==================================

Installs libmongocrypt library

[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-libmongocrypt/workflows/Molecule%20Test/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-libmongocrypt/actions?query=workflow%3A%22Molecule+Test%22)
[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-libmongocrypt/workflows/Release/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-libmongocrypt/actions?query=workflow%3A%22Release%22)

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| `libmongocrypt_version` | The version of libmongocrypt to download | string | `"1.0.1-0"` | yes |
| `libmongocrypt_clone_url` | URL of libmongocrypt source code | string | `git@github.com:mongodb/libmongocrypt.git` | yes |
| `libmongocrypt_clone_dest` | Destination where to clone libmongocrypt | string | `/tmp/libmongocrypt` | yes |

Instructions
------------

Official documentation can be found here from the official repo: <https://github.com/mongodb/libmongocrypt>

To uninstall libmongocrypt, you can run the following command to remove the files installed:
`xargs rm < install_manifest.txt`


Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: ansible-role-libmongocrypt
      vars:
        libmongocrypt_version: 1.0.3
```

License
-------

[Apache License](LICENSE)
