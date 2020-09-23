# Açıklama
Basit bir faktöryel hesaplama aracıdır. Python ile yazıldı. Kubernetes ortamına deployment için dosyaları hazırlandı. Otomasyon olarak ansible kullanıldığı için, jinja template parametreleri içermektedir. Tek başına kullanılmak istenecekse, bu parametreler düzeltilmelidir.

### Derleme ve çalıştırma
```bash
docker build -t demo:latest . && \
docker run -d -p 3000:3000 demo:latest
```
### AWS üzerinde örnek ortam kurulumu
__Not__: Ansible playbooklarının çalışabilmesi için sisteminizde python3 yüklü olmalıdır.
```bash
cd /path/to/ironman && \
  pip install -r requirements.txt && \
  ansible-playbook iaac/eks_stack.yaml --extra-vars="base_dir=$(pwd)" -e "ansible_python_interpreter=/usr/bin/python3"
```
