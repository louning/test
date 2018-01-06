#coding:utf-8
import numpy as np
import pandas as pd
# 将‘招聘.csv’文件中的职位按照企业名称归类并按照时间先后排序，然后另存为一个新的csv文件，命名为‘招聘信息1.csv’。
# 将‘机器学习.xlsx’等Excel文件中的时间信息‘今天…’‘昨天…’替换成绝对时间。‘昨天…’替换为2017-08-08， ‘今天…’ 替换成 2017-08-09。
# 将所有Excel类型招聘信息文件中的内容整合成一个csv文件，并添加一列信息‘岗位类型’，岗位类型定义采用来源文件的文件名，整合后的csv文件命名为‘招聘信息2.csv’。
# 最后按照企业->岗位类型->发布时间三级排序‘招聘信息2.csv’并保存文件。
import sys
sys._enablelegacywindowsfsencoding()

def sortData(indata, sortlist, asc_flag = True):
    if type(indata) == pd.core.frame.DataFrame :
        data = indata
    else:
        data = pd.read_csv(indata)
    outdata = data.sort_values(by=sortlist, ascending=asc_flag)#ascending=True 为升序排列,反之降序
    return outdata

def sortRecruitment1(filein, fileout):
    sortData(filein, ['companyName', 'createTime']).to_csv(fileout)

def timeClean(files, rootdir, resultfile):
    concat_df = pd.DataFrame()
    for filename in files:
        path = rootdir + filename + '.xlsx'
        #sheetname指定为读取几个sheet，sheet数目从0开始
        df = pd.read_excel(path, sheet_name=0)
        df['职位类型'] = filename
        concat_df = pd.concat([concat_df,df], ignore_index=True)
    concat_df.发布日期 = concat_df.发布日期.map(lambda x:'2017-08-09' if '今天' in x else '2017-08-08' if  '昨天' in x else x)
    sortData(concat_df, ['公司全称', '职位类型', '发布日期']).to_csv(resultfile)

if __name__ == '__main__':
    rootdir = 'D:/Project/dima/Python可视化/data/'
    sortRecruitment1(rootdir+'招聘.csv', rootdir+'招聘信息1.csv')
    files = ['机器学习', '深度学习', '算法工程师', '机器视觉',
             '图像处理', '图像识别', '语音识别', '自然语言处理']
timeClean(files, rootdir, rootdir+'招聘信息2.csv')


# df = pd.read_csv('data\招聘.csv')
# df['createTime'] = pd.to_datetime(df['createTime'])
# x = df.sort_values(by=['companyName','createTime'])
# x.to_csv('招聘信息1.csv')
#
# machine = pd.read_excel('data\机器学习.xlsx')
# a = pd.read_excel('data\机器学习.xlsx',sep=',',usecols=[3])
#
#
# print(len(a.values))
# for i in range(len(a.values)):
#     if str(a.values[i]).find('昨天') != -1:
#         a.values[i] = '2017-08-08'
#     elif str(a.values[i]).find('今天') != -1:
#         a.values[i] = '2017-08-09'
#     else:
#         continue
# machine[u'发布日期'] = a
# print(machine)
#
# spoke = pd.read_excel('data\语音识别.xlsx')
# photo = pd.read_excel('data\图像处理.xlsx')
# photo1 = pd.read_excel('data\图像识别.xlsx')
# machine1 = pd.read_excel('data\机器视觉.xlsx')
# deep = pd.read_excel('data\深度学习.xlsx')
# suanfa = pd.read_excel('data\算法工程师.xlsx')
# nature = pd.read_excel('data\自然语言处理.xlsx')
# spoke['岗位信息'] = '语音识别'
# photo['岗位信息'] = '图像处理'
# photo1['岗位信息'] = '图像识别'
# machine['岗位信息'] = '机器学习'
# machine1['岗位信息'] = '机器视觉'
# deep['岗位信息'] = '深度学习'
# suanfa['岗位信息'] = '算法工程师'
# nature['岗位信息'] = '自然语言处理'
#
# data = pd.concat([spoke,photo,photo1,machine,machine1,deep,suanfa,nature])
# data.to_csv('招聘信息2.csv')
#
#
# dataout = pd.read_csv('招聘信息2.csv')
# dataout.sort_values(['公司全称','岗位信息','发布日期']).to_csv('招聘信息2.csv')

