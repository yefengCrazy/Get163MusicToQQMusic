# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
QQnameList = []
nameList= []#搜索得到的用户列表
userURLList = []#搜索得到的用户链接
musicTitle = []#要爬去的歌单信息 value：url
musicURL = []#要爬取取的歌单url
musicInfo= []#已经爬到的歌曲信息 list[songName -- singer]
listlist = [];#列中列 list[list[songName --singer]]
global SONGCOUNT #音乐总数
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome("/usr/local/bin/chromedriver")
#browser = webdriver.Chrome(chrome_options=chrome_options)#可用参数，chrome设置为不可见
def init(Uusername,Ppassword):
    #browser.get("https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=%E5%95%8A");
    browser.get("https://y.qq.com/")
    
    time.sleep(5)
    return browser
def gotoQQMusic(MusicList,browser):
    for name in MusicList:
        try:
            id_songtext = browser.find_elements(By.CLASS_NAME, 'search_input__input')[1];
            MusicList.reverse();
            id_songtext.clear()
            id_songtext.send_keys(name)
            serach_btn = browser.find_elements(By.CLASS_NAME, 'search_input__btn')[1]
            serach_btn.send_keys(Keys.ENTER)
            time.sleep(1)
            list_menu__icon_add = browser.find_elements(By.CLASS_NAME, 'list_menu__add')[0];
            list_menu__icon_add.send_keys(Keys.RETURN);
            time.sleep(1)
            myLike = browser.find_element(By.CLASS_NAME,"js_addto_taogelist")
            time.sleep(1)
            myLike.send_keys(Keys.RETURN)
            print('添加'+name+'成功')
        except:
            continue

def isName(username):# 获取用户帐号
    browser.get('http://music.163.com/#/search/m/?id=37845177&s='+username+ '&type=1002')
    browser.switch_to.frame('contentFrame')
    flagname = browser.find_elements(By.CLASS_NAME,'txt');

    flagnum = 0;

    for name in flagname:
        js = flagname[flagnum].text
        userURLList.append(name.get_attribute('href'))
        nameList.append(js)
        flagnum=flagnum+1
        print(str(flagnum )+ ':'+js)
    flag = input('哪一个是你的帐号？ 没有按0输入你的id\n 注意，输入三次错误之后程序将退出')
    flagexit = 0;
    while 1:
        if flagexit==3:
            exit();
        flagexit=flagexit+1;
        if flag=='0' :
            flag = int(input());
            flag = int(flag)
            get163MusicURL(userURLList[flag-1],0)
            break
        elif flag>='1' and flag<=str(len(nameList)):
            flag = int(flag)
            get163MusicURL(userURLList[flag-1],1)
            break

        else:
            print('请重新输入。')

def get163MusicURL(url ,flag): #获取用户歌单
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # browser = webdriver.Chrome()
    if(flag ==0):
        browser.get('http://music.163.com/#/user/home?id='+url)
    else:
        browser.get(url)
    browser.switch_to.frame('contentFrame')
    cBox = browser.find_element(By.ID,'cBox').find_elements(By.CLASS_NAME,'msk')
    print (cBox)
    # exit()
    #for c in cBox:
    c=cBox[2]
    musicTitle.append(c.get_attribute('title'))#n
    musicURL.append(c.get_attribute('href'))#n
    print('已经找到歌单：'+c.get_attribute('title'))
    #musicURLdict.fromkeys(titleList,musicURlList)
    flag = input('是否开始爬取 是 ：1 否：0')
    if flag=='1':
        print('正在爬取中')
        flagnum = len(musicTitle)
        agency();
    elif flag=='0':
        exit()
def agency():#中介
    for key in musicURL:
        listlist.append(getSongs(key));#返回列表。


    input('全部爬取成功，按任意键继续');
def getSongs(url):#获取歌单列表
    global SONGCOUNT  # 音乐总数
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    # browser = webdriver.Chrome()
    browser.get(url)
    browser.switch_to.frame('contentFrame')
    musicnameList = browser.find_element(By.TAG_NAME,'tbody').find_elements(By.TAG_NAME,'b')
    arcList = browser.find_element(By.TAG_NAME,'tbody').find_elements(By.XPATH,'//div[@class="text"]')
    i = 0;
    songs = [];
    for music in musicnameList:
        str1 = music.get_attribute('title')+'--'+arcList[i].find_element(By.TAG_NAME,'span').get_attribute('title')
        songs.append(str1)
        i+=2
        SONGCOUNT+=1
        print('正在爬取第'+str(SONGCOUNT)+"首：" +str1)
    return songs
if __name__ == '__main__':
    #getSongs('http://music.163.com/#/playlist?id=472199079')
    #get163Music('http://music.163.com/#/user/home?id=337786502')
    #str1='aa'
    SONGCOUNT=0;
    print('没有加入登录失败判断，请确保密码正确')
    username = input('输入你的QQ号码');
    password = input('输入你的密码');
    #print('正在爬取第' + str(SONGCOUNT) + "首：" + str1)
    Lname = input('输入你要爬的网易云音乐的名字');
    isName(Lname)
    # for i in listlist:
    #     gotoQQMusic(i)#传入列表
    # initval = init(username,password)
    browser.get("https://y.qq.com/")
    # print(listlist)
    for  list in listlist:
        # gotoQQMusic(list,initval)  # 传入列表
        for name in list:
            try:
                print(name)
                id_songtext = browser.find_elements(By.CLASS_NAME, 'search_input__input')[0];
                # print(id_songtext)
                # list.reverse();
                id_songtext.clear()
                id_songtext.send_keys(name)
                serach_btn = browser.find_elements(By.CLASS_NAME, 'search_input__btn')[0]
                serach_btn.send_keys(Keys.ENTER)
                time.sleep(1)
                list_menu__icon_add = browser.find_elements(By.CLASS_NAME, 'list_menu__add')[0];
                list_menu__icon_add.send_keys(Keys.RETURN);
                time.sleep(1)
                myLike = browser.find_elements(By.CLASS_NAME,"js_addto_taogelist")[1]
                time.sleep(1)
                myLike.send_keys(Keys.RETURN)
                print('添加'+name+'成功')
            except Exception as e:
                print(e)
                # continue
    # getMusicList()
    # input = input(str);
    # if input == '1':
    #     filename = input('请输入文件目录')
    # elif input=='2':
    #     list = input('请选择你的音乐文件')
    # else:
    #     print('选择错误')
    # getMusicName()
    # print (nameList)
