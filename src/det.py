from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from opts import opts
from inference.normal_inference import normal_inference
from inference.stream_inference import stream_inference
from inference.speed_inference import speed_inference_backbone, speed_inference_det
import torch
import random
import time
import numpy as np


def set_seed(seed):
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    random.seed(seed)
    np.random.seed(seed)


if __name__ == '__main__':
    opt = opts().parse()
    t1 = time.time()
    set_seed(opt.seed)
    if opt.task == 'normal':
        normal_inference(opt)
    elif opt.task == 'stream':
        stream_inference(opt)
    elif opt.task == 'speed_backbone':
        speed_inference_backbone(opt)
    elif opt.task == 'speed_branch':
        speed_inference_det(opt)
    else:
        raise NotImplementedError
    print('total_time: ', (time.time() - t1) / 60)