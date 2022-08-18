# django-coding-devops

Django SDK for Coding DevOps

## Installation

```shell
pip install django-coding-devops
```

## Usage

Define your Coding project and depot models like this:

```python
from django_coding_devops.models import BaseDepot

class CodingDepot(BaseDepot):
    class Meta:
        verbose_name = 'Coding仓库'
```

## License

[Apache 2.0](LICENSE). 
