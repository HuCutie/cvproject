from math import cos, pi 

def warmup_cosinear(optimizer, epoch, max_epoch, lr_min=0, lr_max=0.1, warmup_epoch = 10):     
    if epoch < warmup_epoch:         
        lr = lr_max * epoch / warmup_epoch     
    else:        
        lr = lr = lr_min + (lr_max-lr_min)*(1 + cos(pi * (epoch - warmup_epoch) / (max_epoch - warmup_epoch))) / 2     
    for param_group in optimizer.param_groups:         
        param_group["lr"] = lr

def adjust_learning_rate(args, optimizer, epoch):
    """
     For AlexNet, the lr starts from 0.05, and is divided by 10 at 90 and 120 epochs
    """
    if args.lr_type == 'step':
        if epoch < args.milestones[0]:
            lr = args.lr
        elif epoch < args.milestones[1]:
            lr = args.lr * 0.1
        else:
            lr = args.lr * 0.01
        for param_group in optimizer.param_groups:
            param_group['lr'] = lr
            
    elif args.optimizer == 'custom':
        """
            You can achieve your own learning_rate schedule here
        """
        pass
    else:
        raise KeyError('learning_rate schedule method {} is not achieved')

