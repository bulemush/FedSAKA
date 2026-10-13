from setuptools import find_packages, setup


setup(
    name="fedsaka",
    version="0.1.0",
    description="Federated structure-aware knowledge adaptation for LLMs",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/bulemush/FedSAKA",
    packages=find_packages(include=["federatedscope*", "fedsaka*"]),
    python_requires=">=3.9",
    install_requires=[
        "numpy", "scipy", "pandas", "scikit-learn", "PyYAML",
        "fvcore", "iopath", "grpcio", "protobuf", "tensorboard",
        "tensorboardX", "wandb", "pympler", "networkx", "torch>=2.0",
        "transformers>=4.29,<5", "accelerate", "peft", "datasets",
        "sentencepiece", "dill", "torch-geometric",
    ],
    extras_require={"test": ["pytest"]},
    license="Apache-2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
    ],
)
