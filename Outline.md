## 1. 网络架构
`Densenet121`  `Resnet30`
## 2. 数据增广
先实现`CutOut`和`CutMix`以及其他方式看看效果；  
再使用`ReMixMatch`文章中的方式，即随机取几种并定义力度；  
## 3. 训练策略
先使用`warm up`、`cosine`学习率  
再使用标签平滑  
后使用知识蒸馏
## 4. 优化算法
先使用`SGD`  
再使用`RMSprop`  
后使用`Adam`  

## 5. 实验设计
尽量加上`Tensorboard`  
