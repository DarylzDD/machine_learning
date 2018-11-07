#!/usr/bin/env python
# -*- coding: utf-8 -*-
#encoding=utf8

import time

class GradientDescent():

    __ALPHA = 0.0001
    __ITERATE = 1500
    __FEATURE = 0
    __SAMPLE = 0

    __x = []
    __y = []
    __theta = []

    __feature_num = __FEATURE
    __sample_num = __SAMPLE

    __alpha = __ALPHA
    __iterate = __ITERATE

    def __init__(self):
        self.__alpha = GradientDescent.__ALPHA
        self.__iterate = GradientDescent.__ITERATE
        __x = []
        __y = []
        __theta = []
        __feature_num = GradientDescent.__FEATURE
        __sample_num = GradientDescent.__SAMPLE

    ######################## IO #########################

    def setAlgha(self, alpha):
        self.__alpha = alpha

    def getAlgha(self):
        return self.__alpha

    def setIterate(self, iterate):
        self.__iterate = iterate

    def getIterate(self):
        return self.__iterate

    def setX(self, x_matrix):
        self.__x = []
        self.__theta = []
        self.__feature_num = 0
        self.__sample_num = 0
        # copy x & get feature num & get sample num
        count_sample = 0
        for x_list in x_matrix:
            tmp = []
            for x in x_list:
                tmp.append(x)
            if len(tmp) > self.__feature_num:
                self.__feature_num = len(tmp)
            self.__x.append(tmp)
            count_sample += 1
        self.__sample_num = count_sample
        # format x
        for x_list_item in range(0, len(self.__x)):
            if len(self.__x[x_list_item]) < self.__feature_num:
                diff = self.__feature_num - len(self.__x[x_list_item])
                for i in range(0, diff):
                    self.__x[x_list_item].append(0)
        # format theta
        for i in range(0, self.__feature_num):
            self.__theta.append(0)

    def getX(self):
        return list(self.__x)

    def setY(self, y_list):
        self.__y = []
        # copy y
        for i in range(0, self.__sample_num):
            if i < len(y_list):
                self.__y.append(y_list[i])
            else:
                self.__sample_num = len(y_list)
                self.__x = self.__x[:self.__sample_num]
                break

    def getY(self):
        return list(self.__y)

    def getFeatureNum(self):
        return self.__feature_num

    def getSampleNum(self):
        return self.__sample_num

    def getTheta(self):
        return self.__theta

    ####################################### algo ###################################

    def __getThetaTmp(self):
        theta_tmp = []
        for i in range(0, self.__feature_num):
            theta_tmp.append(0)
        return theta_tmp

    def __gradient(self, feature_pos):
        sum_res = 0
        for i in range(0, self.__sample_num):
            res = 0
            for j in range(0, self.__feature_num):
                res += self.__theta[j] * self.__x[i][j]
            sum_res += (res - self.__y[i]) * x[i][feature_pos]
        gradient = sum_res/self.__sample_num
        return gradient

    def train(self):
        # train sample
        for i in range(0, self.__iterate):
            theta_tmp = self.__getThetaTmp()
            for j in range(0, self.__feature_num):
                theta_tmp[j] = self.__theta[j] - self.__alpha * self.__gradient(j)
            for j in range(0, self.__feature_num):
                self.__theta[j] = theta_tmp[j]

    def cost(self):
        sum_res = 0
        for i in range(0, self.__sample_num):
            res = 0
            for j in range(0, self.__feature_num):
                res += self.__theta[j] * self.__x[i][j]
            sum_res += (res - self.__y[i]) ** 2
        return sum_res/(2 * self.__sample_num)

    def predict(self, vals):
        if len(vals) < self.__feature_num:
            diff = self.__feature_num - len(vals)
            for i in range(0, diff):
                vals.append(0)
        sum_res = 0
        for i in range(0, self.__feature_num):
            sum_res += self.__theta[i] * vals[i]
        return sum_res



if __name__=="__main__":
    # get data
    print("begin...")
    x = [
        [1, 96.79, 2, 1, 2],
        [1, 110.39, 3, 1, 0],
        [1, 70.25, 1, 0, 2],
        [1, 99.96, 2, 1, 1],
        [1, 118.15, 3, 1, 0],
        [1, 115.08, 3, 1, 2],
    ]
    y = [287, 343, 199, 298, 340, 350]
    # model init
    print("\ninit...")
    model = GradientDescent()
    model.setX(x)
    model.setY(y)
    print("feature: %s, sample: %s" % (model.getFeatureNum(), model.getSampleNum()))
    print("alpha: %s, iterate: %s" % (model.getAlgha(), model.getIterate()))
    print("x:")
    x_m = model.getX()
    for x_l in x_m:
        print(x_l)
    print("y:")
    print(model.getY())
    # train parameters
    time.sleep(1)
    print("\ntraining...")
    model.train()
    print("theta:")
    print(model.getTheta())
    print("cost: %s" % (model.cost()))
    print("\npredict...")
    test1 = [1, 112, 3, 1, 0]
    test2 = [1, 110, 3, 1, 0]
    print("test1: %s, predict1: %s" % (test1, model.predict(test1)))
    print("test2: %s, predict2: %s" % (test2, model.predict(test2)))
