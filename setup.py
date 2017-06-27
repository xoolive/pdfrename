from setuptools import setup


def get_long_description():
    import codecs
    with codecs.open('readme.md', encoding='utf-8') as f:
        readme = f.read()
    try:
        from pypandoc import convert
        return convert(readme, 'rst', 'md')
    except ImportError:
        return ""


setup(name='pdfrename',
      version='0.1',
      description='A tool for renaming a batch of pdf files',
      long_description=get_long_description(),
      license='MIT',
      author='Xavier Olive',
      author_email='xo.olive@gmail.com',
      packages=['pdfrename', ],
      entry_points={'console_scripts':
                    ['pdfrename = pdfrename.pdfrename:main']},
      install_requires=['pdfminer'],
      url="https://github.com/xoolive/pdfrename",
      )
