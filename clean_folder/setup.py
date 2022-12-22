from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0.0',
    description='Helps you to organize your folder content',
    url='https://github.com/Dmytrii-Shypilov/goit-python-core-hw7',
    author='Dmytrii Shypilov',
    author_email='dmytriishypilov@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:clean_func']},
)