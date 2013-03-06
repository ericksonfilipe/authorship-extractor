from subprocess import Popen, PIPE

def hg(classe):
    return Popen('hg blame -uv {0}'.format(classe), shell=True, stdout=PIPE).stdout
