Ansible role for libmongocrypt
==================================

Installs libmongocrypt library

![](https://github.com/mongodb-ansible-roles/ansible-role-libmongocrypt/workflows/Molecule%20Test/badge.svg)
![](https://github.com/mongodb-ansible-roles/ansible-role-libmongocrypt/workflows/Release/badge.svg)

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
