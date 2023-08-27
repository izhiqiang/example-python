import paramiko


class EasySsh:
    # def __init__(self, conf):
    #     self.conf = conf
    def connect(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        self.client.connect(hostname="127.0.0.1", port=22, username="root", password="123456")
        return self

    def exec(self):
        stdin, stdout, stderr = self.client.exec_command("hostname")
        return stdout.read().decode('utf-8')

    def __del__(self):
        self.client.close()


if __name__ == '__main__':
    res = EasySsh().connect().exec()
    print(res)
