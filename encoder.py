import torch
import torch.nn


class Encoder:
    def __init__(self, pretrain_encoder: str):
        # The path of encoder.pt
        self.encoder = torch.load(pretrain_encoder) 

    def embed(self, dataset):
        pass
