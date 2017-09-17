from fabric.api import env, run
from fabric.operations import sudo 


GIT_REPO = "git@github.com:linuxying/blogproject.git"

env.user = 'linuxliu'
env.password = 'liuruiying'

env.hosts = ['10.0.0.3']
env.port = '22'

def deploy():
    source_folder = '/home/linuxliu/sites/demo.ruiying.com/blogproject'

    run('cd %s && git pull' % source_folder)
    run("""
	cd {} &&
        ../env/bin/pip3 install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py makemigrations
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('systemctl restart linuxliu.service')
    sudo('systemctl restart nginx.service')
