from setuptools import setup

setup(name='edflow',
      version='0.2',
      description='Logistics for Deep Learning',
      url='https://github.com/pesser/edflow',
      author='Mimo Tilbich et al.',
      author_email='{patrick.esser, johannes.haux}'
                   '@iwr.uni-heidelberg.de',
      license='MIT',
      packages=['edflow'],
      install_requires=[
          'pyyaml',
          'opencv-python',
          'tqdm',
          'Pillow',
          'chainer',
          'numpy',
          'scipy',
          'h5py',
          'scikit-learn',
          'scikit-image',
          'natsort',
          'pandas'
          ],
      extras_require={
          'docs': [
            'sphinx >= 1.4',
            'sphinx_rtd_theme']},
      zip_safe=False,
      scripts=["edflow/edflow", "edflow/edcache", "edflow/edlist"])
