import pygal

from die import Die
# 创建两个D6骰子
die_1 = Die(num_sides=6)
die_2 = Die(num_sides=6)

# 掷骰子多次，并将结果存储到一个列表中
results = []
number = 1000
for roll_num in range(number):
    result = die_1.roll() + die_2.roll()    #计算两个骰子的总点数
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides  #可能出现的最大点数12
for value in range(2, max_result+1):    #计算2到max_result间各点数出现的次数
    frequency = results.count(value)
    frequencies.append(frequency)

# 可视化结果
hist = pygal.Bar()

hist.title = "D%d、D%d"%(die_1.num_sides,die_2.num_sides) + \
             "两个骰子各投掷%d"%number + "次点数之和的直方图"
hist.x_labels = list(range(2,max_result+1))
hist.x_title = "点数"
hist.y_title = "各点数出现的次数"
hist.add('D%d + D%d'%(die_1.num_sides,die_2.num_sides), frequencies)
hist.render_to_file('dice_visual.svg')