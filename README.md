Ansible role for libmongocrypt
==================================

Installs libmongocrypt library

[![CircleCI](https://img.shields.io/circleci/build/github/mongodb-ansible-roles/ansible-role-libmongocrypt/master?style=flat-square)](https://circleci.com/gh/mongodb-ansible-roles/ansible-role-libmongocrypt)

Requirements
------------

None

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| `libmongocrypt_version` | The version of libmongocrypt to download | string | `"1.0.1-0"` | yes |


Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: ansible-role-libmongocrypt
      vars:
        libmongocrypt_version: 1.0.1-0
```

License
-------

[Apache License](LICENSE)
