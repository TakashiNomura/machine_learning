# coding:UTF-8
import  matplotlib.pyplot as plt
import math

# シグモイド関数
def sigmoid(a):
    return 1.0 / (1.0 + math.exp(-a))

# ニューロン
class Neuron:
    input_sum = 0.0
    output  = 0.0

    def setInput(self, inp):
        self.input_sum += inp

    def getOutput(self):
        self.output = sigmoid(self.input_sum)
        return self.output

    def reset(self):
        self.input_sum = 0
        self.output = 0

# ニューラルネットワーク
class NeuralNetwork:
    # 入力の重み
    w_im = [[-0.496, 0.512], [-0.501, 0.998], [0.498, -0.502]]
    w_mo = [0.121, -0.4996, 0.200]

    input_layer = [0.0, 0.0, 1.0]
    middle_layer = [Neuron(), Neuron(), 1.0]
    output_layer = Neuron()

    # 実行
    def commit(self, input_data):
        #角層のリセット
        self.input_layer[0] = input_data[0]
        self.input_layer[1] = input_data[1]

        self.middle_layer[0].reset()
        self.middle_layer[1].reset()

        self.output_layer.reset()

        #入力層→中間層
        self.middle_layer[0].setInput(self.input_layer[0] * self.w_im[0][0])
        self.middle_layer[0].setInput(self.input_layer[1] * self.w_im[1][0])
        self.middle_layer[0].setInput(self.input_layer[2] * self.w_im[2][0])

        self.middle_layer[1].setInput(self.input_layer[0] * self.w_im[0][1])
        self.middle_layer[1].setInput(self.input_layer[1] * self.w_im[1][1])
        self.middle_layer[1].setInput(self.input_layer[2] * self.w_im[2][1])

        #中間層→出力層
        self.output_layer.setInput(self.middle_layer[0].getOutput() * self.w_mo[0])
        self.output_layer.setInput(self.middle_layer[1].getOutput() * self.w_mo[1])
        self.output_layer.setInput(self.middle_layer[2] * self.w_mo[2])

        return self.output_layer.getOutput()

    def learn(self,input_data):
        print(input_data)

# 基準点（データの範囲を0.0-1.0の範囲に収めるため）
refer_point0 = 34.5
refer_point1 = 137.5

# ファイル読み込み
training_data = []
training_data_file = open("training_data", "r")
for line in training_data_file:
    line = line.rstrip().split(",")
    training_data.append([float(line[0]) - refer_point0, float(line[1]) - refer_point1, int(line[2])])
training_data_file.close()

# ニューラルネットワークのインスタンス
neural_network = NeuralNetwork()

# 学習
neural_network.learn(training_data[0])

# 訓練用データの表示の準備
position_tokyo_learning = [[],[]]
position_kanagawa_learning = [[],[]]
for data in training_data:
    if data[2] < 0.5 :
        position_tokyo_learning[0].append(data[1]+refer_point1)
        position_tokyo_learning[1].append(data[0] + refer_point0)
    else:
        position_kanagawa_learning[0].append(data[1]+refer_point1)
        position_kanagawa_learning[1].append(data[0] + refer_point0)

# プロット
plt.scatter(position_tokyo_learning[0], position_tokyo_learning[1], c="red", label="Tokyo", marker="+")
plt.scatter(position_kanagawa_learning[0], position_kanagawa_learning[1], c="blue", label="kanagawa", marker="+")
plt.legend
plt.show()