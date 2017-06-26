from setuptools import setup

setup(name='pdfrename',
      version='0.1',
      description='Rename pdf files from elements present in the file',
      license='MIT',
      author='Xavier Olive',
      packages=['pdfrename', ],
      entry_points={'console_scripts':
                    ['pdfrename = pdfrename.pdfrename:main']},
      install_requires=['pdfminer'],
      )
