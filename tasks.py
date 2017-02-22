from invoke import task


@task
def run_dev(ctx):
    ctx.run('python server/server.py')
