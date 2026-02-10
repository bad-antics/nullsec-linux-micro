from setuptools import setup,find_packages
setup(name="nullsec-linux-micro",version="2.0.0",author="bad-antics",description="Minimal Linux microkernel experiments and tools",packages=find_packages(where="src"),package_dir={"":"src"},python_requires=">=3.8")
