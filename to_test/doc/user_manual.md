# User manual

## Running
### Ubuntu
The module can be ran with `./dist_ubuntu goodconfig.json` or any other config file.
### Windows
***TODO executable windows***

## Configuration file
A JSON configuration file is needed to provide the simulation with an initial setup. It consist of a JSON object with two members phones and nodes. Here it is possible to specify the amount of nodes and phone the simulation should contain, please note that the set of nodes can't be empty. A valid example can be seen below.

```json
{
        "phones": 10,
        "nodes": 3
}
```

## Command execution
The following commands are available in the command line. X and Y here stand for unique ids of a phone or node.

**call X Y**:
Tries to initiates a call form phone X to phone Y. 

**answer X**:
Phone X tries to answers a call. 

**hangup X**:
Phone X tries to terminates a call.

**phone_offline X**:
The phone X tries to disconnect from the handler.

**phone_malfunction X**:
A malfunction will be simulated at phone X.

**phone_online X**:
The phone X tries to connect to the handler.

**node_malfunction X**:
A malfunction will be simulated at node X.

**node_online X**:
Node X will be set ready for use, this is needed after a node malfunctioned to get it back working.
