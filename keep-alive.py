import paramiko
import time

SSH_HOST = "sgp1.tmate.io"
SSH_PORT = 22
SSH_USER = "4tguucEERxtEDFJfvR9yRFL4s"
SSH_PASS = None  # if using password, put here, else keep None

def keep_alive_ssh():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(SSH_HOST, SSH_PORT, SSH_USER, password=SSH_PASS)

    try:
        while True:
            ssh.exec_command("echo alive")
            time.sleep(10)
    except Exception as e:
        print("Error:", e)
    finally:
        ssh.close()

if __name__ == "__main__":
    keep_alive_ssh()
