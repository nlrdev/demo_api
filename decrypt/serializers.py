from rest_framework import serializers
import gnupg

class DecryptMessageSerializer(serializers.Serializer):
    passphrase = serializers.CharField(max_length=1024)
    message = serializers.CharField(max_length=1024)
    
    def decrypted_data(self):
        passphrase = self.validated_data['passphrase']
        encrypted_data = self.validated_data['message']
        gpg = gnupg.GPG()
        decrypted_data = gpg.decrypt(encrypted_data, passphrase=passphrase)
        data = {
            "passphrase": passphrase,
            "message": decrypted_data.data,
            }
        return data
