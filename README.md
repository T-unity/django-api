# about this product

サイト売買のプラットホーム

## What can this product do?

・ユーザー登録
(role: Administrator, Buyer, Seller, transporter:サイト売買に合わせてドメインの移管作業を行う人)

・投稿の作成
(Buy, Sell)

...and other

## models,tables

・user

・post

...and other


<details>
<summary>command</summary>

## Docker

・docker-compose build

・docker-compose up

・docker-compose down

## django make PJ

docker-compose run --rm app django-admin startproject プロジェクト名

## django others

prefix: docker-compose run --rm app

prefix: python manage.py

example: docker-compose run --rm app python manage.py

after
<!-- make application -->
startapp test
<!-- make pre migrate file -->
makemigrations
<!-- exec migrate -->
migrate
<!-- make admin user -->
createsuperuser

<!-- admin -->
<!-- hoge / hoge -->
</details>
