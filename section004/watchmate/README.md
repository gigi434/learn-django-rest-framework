### activate 
```console
vscode ➜ /workspaces/django-rest-frameworkapi/section003/watchmate (main) $ python manage.py runserver
```

### init
これらのアプリケーションは最低1つデータベースのテーブルを使うので、使い始める前にデータベースにテーブルを作る必要があります。以下のコマンドを実行してください:

```console
python manage.py maekmigrations
```

これからモデルを定義します。モデルは本質的には、データベースのレイアウトと、それに付随するメタデータです。
modelファイルを編集した後に書きコマンドを打つ
```console
python manage.py migrate
```
