# 📚 Book Summarizer Agent

Bu proje, **LangChain** ve **OpenAI** kullanarak kitap özetleri üreten basit bir agent uygular.  
Kullanıcıdan kitap adı alır ve şu çıktıları üretir:  
- Kitabın kısa özeti  
- Ana temaları  
- Hedef kitlesi  
- Benzer kitap önerileri  

Bu proje, **prompt engineering** ile **agent yapısının** birleşimini göstermek amacıyla hazırlanmış bir ödev çalışmasıdır. (Bkz: `odev-2.pdf`)

---

## 🚀 Özellikler
- 📖 Kitap adı girdiğinde özet + analiz üretir  
- 🤖 LangChain `ChatOpenAI` + `Tool` + `Agent` kullanır  
- 🔑 `.env` dosyası ile OpenAI API anahtarı yönetilir  
- 📝 Ödev raporu (`odev-2.pdf`) ve örnek çıktılar dahildir  

---

## ⚙️ Kurulum

1. Depoyu klonla veya indir:
   ```bash
   git clone https://github.com/<kullanici-adi>/book_summarizer_agent.git
   cd book_summarizer_agent
   
2.Sanal ortam oluştur ve aktif et:
python -m venv .venv
# Windows (PowerShell):
. .venv/Scripts/Activate.ps1
# Linux/macOS:
# source .venv/bin/activate

3.Bağımlılıkları yükle:
pip install -r requirements.txt

4..env dosyasını oluştur:
cp .env.example .env          ve içine OpenAI API anahtarını ekle:       OPENAI_API_KEY=senin_openai_api_keyin

▶️ Çalıştırma

python book_summarizer_agent.py

---

📌 Program çalışınca senden kitap adı isteyecek. Örn:

Kitap adını girin: Suç ve Ceza

---



👤 Geliştirici
Ad Soyad: DAMLA ARPA

Bu proje, **Kairu Bootcamp Eğitimleri** kapsamında bir ödev/proje olarak geliştirilmiştir.

