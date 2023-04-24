import torch
import numpy as np
import random

class CutMix(object):
    def __init__(self, alpha):
        self.alpha = alpha

    def __call__(self, img):
        w, h = img.size(2), img.size(1)
        lam = np.random.beta(self.alpha, self.alpha)
        rand_index = torch.randperm(img.size()[0])
        img_a, img_b = img, img[rand_index]
        bbx1, bby1, bbx2, bby2 = self.rand_bbox(w, h, lam)
        img_a[:, bby1: bby2, bbx1: bbx2] = img_b[:, bby1: bby2, bbx1: bbx2]
        lam = 1 - ((bbx2 - bbx1) * (bby2 - bby1) / (w * h))
        return img_a, lam

    def rand_bbox(self, w, h, lam):
        cut_rat = np.sqrt(1. - lam)
        cut_w = np.int(w * cut_rat)
        cut_h = np.int(h * cut_rat)
        cx = np.random.randint(w)
        cy = np.random.randint(h)
        bbx1 = np.clip(cx - cut_w // 2, 0, w)
        bby1 = np.clip(cy - cut_h // 2, 0, h)
        bbx2 = np.clip(cx + cut_w // 2, 0, w)
        bby2 = np.clip(cy + cut_h // 2, 0, h)
        return bbx1, bby1, bbx2, bby2