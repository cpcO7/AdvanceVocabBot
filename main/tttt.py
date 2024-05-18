# # # with open('../tg_bot/vocab.txt', 'r') as f:
# # #     with open('nvocab.txt', 'w') as f_2:
# # #         for i in f.readlines():
# # #             a = []
# # #             for j in i.strip('\n').split('-'):
# # #                 a.append(j.strip())
# # #             f_2.writelines('-'.join(a) + '\n')
# # #
# # # #
# # # with open('vocab.txt', 'r') as f:
# # #     units = f.readlines()
# # #     for i in range(0, 188 - 10, 11):
# # #         # print(units[i])
# # #             with open('units/' + units[i] + '.txt', 'w') as file:
# # #                 file.writelines(units[i + 1])
# # #                 file.writelines(units[i + 2])
# # #                 file.writelines(units[i + 3])
# # #                 file.writelines(units[i + 4])
# # #                 file.writelines(units[i + 5])
# # #                 file.writelines(units[i + 6])
# # #                 file.writelines(units[i + 7])
# # #                 file.writelines(units[i + 8])
# # #                 file.writelines(units[i + 9])
# # #
# #
# # from redis_dict import RedisDict
# #
# # tests = RedisDict()
# # print(tests)
# # read_file = [v for k, v in tests.items()]
# # eng = [k for k in tests.keys()]
# # print(read_file)
#
#
# from random import sample, shuffle
#
# ch = []
# a = [1, 2, 3, 4, 5, 6, 7,7, 8, 9, 10]
# # shuffle(a)
# # print(a)
# def fun(b):
#     p = sample(b, 1)
#     if p not in ch:
#         # return p
#         ch.append(p)
#
#         print(p)
#     else:
#         fun(b)
#
#
# for i in range(11):
#     fun(a)
#
#
#

#
import os
#
# for i in range(len(os.listdir('units/'))):
#     os.rename('units/' + os.listdir('units/')[i],
#               'units/' + "Unit_" + str(
#                 i + 1) + '.txt')
