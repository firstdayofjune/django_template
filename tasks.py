from invoke import task
import re


@task
def init(ctx):
	print("Installing required packages")
	required_packages = [
		('django', 'base'), ('django-debug-toolbar','dev'), ('django-environ', 'base'), ('pip-tools', 'base')
	]
	for package in required_packages:
		pip_save(ctx, package[0], package[1])

	print("Preparing django")
	ctx.run('./manage.py migrate')

	print("Initializing git repository")
	ctx.run('git init')
	

def _verify_target(target):
	targets = ['base', 'dev', 'docs', 'prod', 'test']
	if target not in targets:
		print('Invalid target was passed. Possible targets are: {}'.format(targets))
		return


@task
def pip_save(ctx, package, target, version=None):
	_verify_target(target)

	info = 'Installing package "{}" {}...'
	if version:
		print('Installing package "{}" at version {}...'.format(package, version))
		result = ctx.run("pip install {}=={}".format(package, version))
	else:
		print('Installing package "{}" at latest version...'.format(package))
		result = ctx.run("pip install {}".format(package))
	package_installed = 'Successfully installed' in result.stdout
	if result.ok and package_installed:
		pattern = "Successfully installed {}-(.*)\n".format(package)
		version_installed = re.search(pattern, result.stdout).group(1)
		requirement = '{}=={}'.format(package, version_installed)
		print('Adding {} to {}.'.format(requirement, target))
		ctx.run('echo {} >> requirements/{}.in'.format(requirement, target))


@task
def build(ctx, target):
	_verify_target(target)
	ctx.run('pip-compile requirements/{0}.in --output-file requirements/build/{0}.txt'.format(target))