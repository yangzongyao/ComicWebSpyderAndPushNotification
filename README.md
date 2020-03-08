# ComicWebSpyderAndPushNotification
漫畫櫃漫畫網站，最新集數推播
-------------------------


**於檔案目錄底下，加入"book_me"資料夾，在檔案資料夾內加入文字檔(.txt)，
內容需包含漫畫編號，以及現在集數。**


1. 漫畫編號如下，其中19430為漫畫編號。  
![image](https://github.com/yangzongyao/ComicWebSpyderAndPushNotification/blob/master/README_img/2020-03-08%2016-17-11%20%E7%9A%84%E8%9E%A2%E5%B9%95%E6%93%B7%E5%9C%96.png)

2. 在*main.py*程式中，第24行加入自己資料夾之路徑，內容更改為自己資料夾路徑。  
![image](https://github.com/yangzongyao/ComicWebSpyderAndPushNotification/blob/master/README_img/2020-03-08%2016-12-55%20%E7%9A%84%E8%9E%A2%E5%B9%95%E6%93%B7%E5%9C%96.png)





3. 在*comic.py*檔案中，更改email資訊，email和email_password為寄送推播之email帳號密碼，而send_to_email為收到最新推播之帳號。  
![image](https://github.com/yangzongyao/ComicWebSpyderAndPushNotification/blob/master/README_img/2020-03-08%2016-13-45%20%E7%9A%84%E8%9E%A2%E5%B9%95%E6%93%B7%E5%9C%96.png)


設定完成後將main.py設定成功做排程，即可在自訂的時間收到最新漫畫集數的推播。
