# Açıklama
Lambda fonksiyon testi için yazılmış bir uygulama. İşi, s3 üzerinden gelen dosya yükleme tetikleyicisyle birlikte çalışmak ve yüklenen csv formatındaki dosyayı işleyerek DynamoDB üzerine kayıt etmektir.

__Not__: Ansible playbooklarının çalışabilmesi için sisteminizde python3 yüklü olmalıdır.

Örnek kurulum için, aşağıdaki ansible komutunu kullanabilirsiniz. Scripti çalıştırmadan önce değişkenleri düzenlemeyi unutmayın.
```bash
cd /path/to/ironman && \
  pip install -r requirements.txt && \
  ansible-playbook iaac/lambda_stack.yaml --extra-vars="base_dir=$(pwd)" -e "ansible_python_interpreter=/usr/bin/python3"
```
