from setuptools import find_packages, setup


def get_requirements():
    requirement_list = []
    file_path = 'requirements.txt'
    with open(file_path) as file:
        requirement_list = file.readlines()
        requirement_list = [require.replace('\n','') for require in requirement_list]
        if '- e. ' in requirement_list:
            requirement_list.remove('- e. ')
    return requirement_list


setup(
    name='api',
    version='1.0.0',
    description='This is openai task',
    author='Rajan Devkota',
    author_email='r.devkota.98@gmail.com',
    packages=find_packages(),
    install_require = get_requirements(),
)