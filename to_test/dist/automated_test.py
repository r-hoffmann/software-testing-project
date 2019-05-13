import os 
import sys
import re

# get num of rows in file
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


# 
class Network:
    def __init__(self, command, error):
        self.nodes = []
        self.phones = []
        self.command = command
        self.error = error

    def add_phone(self, phone):
        self.phones.append(phone)

    def __repr__(self):
        if self.phones and self.command:
            output = "Command: " + str(self.command) + "\n Error: " + str(self.error)
            for phone in self.phones:
                output += str(phone) + "\n"
            return output
        return "EMPTY"


class Phone:
    def __init__(self, num, status):
        self.num = num
        self.status = status

    def __repr__(self):
        return str(self.num) + ": " + str(self.status)


input_file = open('tests.txt')
input_lines = input_file.readlines()
LEN_COMMANDS = file_len('tests.txt')

success = []

# Run 
instances = 1000
json_file = "anyname.json.txt"

for i in range(instances):

    networks = []
    network = None

    counter = 0

    os.system("./dist_ubuntu anyname.json.txt <"  + json_file + " > tmp")

    with open('tmp') as fp:
        lines = fp.readlines()
        for i, line in enumerate(lines):
            # If found line contaning command:
            # Create new network
            if re.match("Command:", line) and counter < LEN_COMMANDS:
                networks.append(network)

                error = None

                if not re.match("-----=====-----", lines[i+1]):
                    error = lines[i+1]

                network = Network(input_lines[counter], error)
                counter += 1

            # If found a phone add to most recent created network
            phone = re.match("Phone (\d{4}):", line)
            if network != None and phone:
                status = re.match("Phone \d{4}: (.*)", line)
                tmp_phone = Phone(phone.group(1), status.group(1))
                network.add_phone(tmp_phone)

    networks.append(network)
    networks.pop(0)

    # EXPECTED ERROR HERE:
    if networks[1].error == "Phone 0001 is ringing other phone\n":
        success.append(True)
    # Unexpected output
    else:
        success.append(False)

print(success.count(False))
