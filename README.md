# Django グループ交流アプリ ver1

このレポジトリは次のKindle電子書籍で作成しているアプリケーションのソースコードの一つです。  

**Webアプリケーションを作ってみよう**  
**（Bootstrap Django MySQL 活用編）**  

- アプリケーションを作成しよう１（画面遷移まで）  
- **アプリケーションを作成しよう２（基本動作まで） <--このソースコードです**  
- アプリケーションを作成しよう３（完成まで）  
- アプリケーションを作成しよう４（派生アプリ作成）  

## 動作環境
次の環境で動作を確認しています。  
OS: Ubuntu16.04  
Bootstrap: 3.3.7  
MySQL: 5.7.16  
Python: 2.7.12  
Django: 1.8.7  

## インストール手順

[0]事前にアプリが動作する環境を構築しておきます。  
（動作環境の構築については書籍の付録などをご確認ください）  

[1]GithubのレポジトリでClone or downloadボタンを押して圧縮ファイルをダウンロードします。  

[2]ファイルを解凍しdjango_talkapp_ver1-masterディレクトリに移動します。  

[3]MySQLでデータベースとユーザーを準備してその情報をmysite/settings.pyに設定します。  

（例）  
create database talkapp DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;  
grant all privileges on talkapp.* to ken@localhost identified by 'pass123';  

と準備した場合settings.pyには次のように設定します。  

'NAME': 'talkapp',  
'USER': 'ken',  
'PASSWORD': 'pass123',  

[4]次のコマンドを実行してデータベースに必要なテーブルを作成します。  
python manage.py migrate  

[5]サーバーを起動しhttp://localhost:8000でアクセス  
python manage.py runserver  

## ライセンス
DjangoのフレームワークはBSDライセンスのもとにリリースされています。このプログラムはMITライセンスを採用しています。MITライセンスの詳細についてはLICENSEファイルを参照してください。



