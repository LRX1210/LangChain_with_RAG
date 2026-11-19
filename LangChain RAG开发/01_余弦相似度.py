import numpy as np
#计算2个向量的积，2个向量同维度数字乘积之和
def www(x1,y1):#点积
    #如果维度不同，就返回异常
    if len(x1)!=len(y1):
        raise ValueError("2个向量同维度必须相同")
    dot_sum = 0
    for a,b in zip(x1,y1): #zip 类似键值对
        dot_sum += a*b
    return dot_sum

def ww(x1):#模长
    dot_square = 0
    for i in x1:
        dot_square += i*i
    # numpy(库) sqrt（用于开根号）
    return np.sqrt(dot_square)

def cosine(x1,y1):  #余弦相似度：2个向量的点积，乘以2个向量模长的乘积
    result= www(x1,y1) / (ww(x1) * ww(y1))
    return result


if __name__=='__main__':
    a=[0.5,0.5]
    b=[0.7,0.7]
    c=[0.7,0.5]
    d=[-0.6,-0.5]
    print()
    print("ab:",cosine(a,b))
    print("ac:",cosine(a,c))
    print("bd:",cosine(b,d))