* Usage  
In your projects root:  

```bash
git submodule add --name stubs https://github.com/averagehat/bio-stubs  
```

include the following line in mypy.ini in your project root 

```
mypy_path = ./stubs/
```

Example:  


```
[mypy]
warn_return_any = True
warn_unused_configs = True
strict_equality = True
no_implicit_optional = True
disallow_untyped_calls = True
disallow_untyped_defs = True
mypy_path = ./stubs/
disallow_any_expr = False
```
