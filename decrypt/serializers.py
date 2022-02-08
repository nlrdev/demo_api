from rest_framework import serializers
import gnupg

class DecryptMessageSerializer(serializers.Serializer):
    passphrase = serializers.CharField(max_length=1024)
    encrypted_data = serializers.CharField(max_length=1024)
    
    def create(self, validated_data):
        passphrase = validated_data.pop("passphrase", None)
        encrypted_data = validated_data.pop("encrypted_data", None)
        gpg = gnupg.GPG()
        decrypted_data = gpg.decrypt(encrypted_data, passphrase=passphrase)
        data = {
            "passphrase": passphrase,
            "message": decrypted_data.data,
            }
        return data
