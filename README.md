# CatBoard 🐱

An image board for cats!

## Development

This project uses [rye](https://github.com/mitsuhiko/rye) to manage dependencies.
You can run the project using rye itself by doing

```sh
rye run server
```

You can also run the project using docker:

```sh
docker build -t catboard .
docker run -v ./src:/app/src -p 8000:8000 -t catboard
```

Both methods run uvicorn in auto-reload mode, exposing the server on `localhost:8000`.

To see the documentation, open `localhost:8000/docs`.
