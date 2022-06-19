from readline import get_endidx
import torch
from torch import nn
from torch.utils.data import DataLoader

"""
Attempts to understand Python's logic behind polymorphism
"""
class Parent:
    def __init__(self):
        self.parent_property = "parent"
    
    def reproduce(self):
        print("mating")

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_property = "child"


class Logger:
    def info(info):
        print(f"[INFO]: {info}")


def get_device():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    Logger.info(f"Using {device.upper()} for computation")
    return device


if __name__ == "__main__":
    get_device()
    nn.Module()
    nn.Conv2d()