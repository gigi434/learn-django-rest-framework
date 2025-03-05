from rest_framework import serializers


class MovieSerializer(serializers.Serializer):
    """
    リクエストやレスポンスのデータをシリアライズするためのクラス
    シリアライズとは、この場合JSON形式からPythonオブジェクトへの変換を指す
    デシリアライズとは、この場合PythonオブジェクトからJSON形式への変換を指す
    """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=100)
    active = serializers.BooleanField()
