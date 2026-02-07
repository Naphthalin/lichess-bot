
## Leela backend server

Server can be configured to start when any bot starts. Alternative is to starts the server manually before starting any of bots. Server watching script reads configuration from `server.yml` file.

The python script manages startup, configuration and automatic restart if server isn't responding. It makes sure that only one server is started in the system.

### Automatic start of server

All bots require configuration change to enable server start. Add following lines to each bot configuration file.

```yaml
backendserver:
  script: "leela_backenserver.py"
  arguments: []
```

### Manual start of server

Server is started by running `leela_backendserver.py` script. Server startup could be sone using `python3 leela_backendserver.py` command.

### Configuration

Server configuration is stored in `server.yaml` file. Example configuration:

```yaml

token: "xxxx"
url: "https://lichess.org"
server_lock_file: "leela_backendserver.lock"

engine:
  dir: "./engines/"
  name: "lc0"
  positional_arguments: ["backenserver"]
  working_dir: ""
  protocl: uci

engine_options:
  network-directory: "./networks/"
  backend: "onnx-trt"

  silence_stderr: false
```

### Bot configuration

Bots need to use `client` backend. Default is to use local stream connection using `unix` protocol. Unix sockets are stored in working directory on Windows. This means both server and client should use the same working directory or custom socket path configuration.

Example bot configuration:

```yaml
  engine_options:
    backend: "client"
```
