# Flask in a Class

Flask normally is not wrapped in a class but sometimes we want to encapsulate the server and provide extra functionality like broadcasting websockets with other app logic modules.

## Development

Make sure `pyenv` and `pipenv` is installed to re-create `v3.7.1` and to re-install the project dependencies. Run the project with the following commands

```bash
pipenv shell
python __main__py
```

## Flask Blueprints

Flask doesn't call separate routers a middleware, it refers to it as a `blueprint` to logically separate endpoints. 