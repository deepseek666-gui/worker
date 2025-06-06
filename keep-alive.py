import paramiko
import time

SSH_HOST = "sgp1.tmate.io"
SSH_PORT = 22
SSH_USER = "4tguucEERxtEDFJfvR9yRFL4s"
SSH_PASS = None  # agar password hai to use karo, nahi to None

def keep_alive_ssh():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    # Create Transport separately to tweak compression
    transport = paramiko.Transport((SSH_HOST, SSH_PORT))
    
    # Disable all compression methods:
    transport._preferred_compression = ('none',)  # force 'none' compression
    
    transport.connect(username=SSH_USER, password=SSH_PASS)
    
    ssh._transport = transport
    
    try:
        while True:
            stdin, stdout, stderr = ssh.exec_command('echo alive')
            time.sleep(10)
    except Exception as e:
        print("Error:", e)
    finally:
        ssh.close()

if __name__ == "__main__":
    keep_alive_ssh()
