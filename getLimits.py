import os, subprocess

def countFiles(pid):
    pidPath = '/proc/{}/fd'.format(pid)
    cmd = 'ls {} | wc -l'.format(pidPath)
    count = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    return count

class OpenFiles():
    def __init__(self, process_name):
        self.process = subprocess.Popen(['pidof', process_name], stdout=subprocess.PIPE, encoding='utf-8')

    def count(self):
        pid = []
        for line in iter(self.process.stdout.readline,''):
            pid = line.rstrip().split()
        counts = []
        for p in pid:
          getCount = countFiles(p)
          for c in iter(getCount.stdout.readline,''):
            counts.append(c.rstrip())
        return dict(zip(pid, counts))
          
