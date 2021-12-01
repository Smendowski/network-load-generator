import re
import socket
import subprocess
import argparse


def get_local_machine_ipv4_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


IPERF_CONFIGURATION = {
    "-c" : f"{get_local_machine_ipv4_address()}",
    "-p" : "7000",
    "-t" : "300",
    "-b" : "10m",
    "-i" : "1"
}


def modify_telegraf_configuration():
    with open("telegraf.conf", "r") as telegraf_conf:
        telegraf_configuration = telegraf_conf.readlines()

    for idx, line in enumerate(telegraf_configuration):
        if "iperf" in line:
            telegraf_configuration[idx] = get_updated_iperf_command()
            break
    
    with open("telegraf.conf", "w") as telegraf_conf:
        for line in telegraf_configuration:
            telegraf_conf.write(line)


def get_updated_iperf_command():  
    parameters = " ".join({
        f'{param} {value}' for param, value in IPERF_CONFIGURATION.items()
    })
    return f'\tcommands = ["iperf {parameters}"]\n'


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--build', action='store_true')
    args = parser.parse_args()

    modify_telegraf_configuration()

    if args.build:
        subprocess.run("docker-compose up --build", shell=True)
    else:
        subprocess.run("docker-compose up", shell=True)
