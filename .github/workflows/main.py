import os
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# 获取环境变量
NEWSAPI_KEY = os.getenv('NEWSAPI_KEY')
EMAIL_FROM = os.getenv('EMAIL_ 'smtp.qq.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', 465))
KEYWORDS = os.getenv('KEYWORDS', '').split(',')

def fetch_news(keyword):
    """从 NewsAPI 获取新闻"""
    url = f"https://newsapi.org/v2/everything?q={keyword}&sortBy=publishedAt&language=en&apiKey={NEWSAPI_KEY}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json().get('articles', [])[:5]
    except Exception as e:
        print(f"Error: {e}")
    return []

def create_email_body(news_dict):
    """创建 HTML 邮件"""
    html = f"""
    <html><head><meta charset="utf-8"><style>
    body {{ font-family: Arial; background: #f5f5f5; }}
    .container {{ max-width: 800px; margin: 0 auto; background: white; padding: 20px; }}
    h1 {{ color: #333; text-align: center; }}
    .category {{ margin: 20px 0; }}
    .category h2 {{ color: #0066cc; border-bottom: 2px solid #0066cc; padding-bottom: 10px; }}
    .news-item {{ margin: 15px 0; padding: 15px; background: #f9f9f9; border-leftFROM')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_TO = os.getenv('EMAIL_TO')
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.qq.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', 465))
KEYWORDS = os.getenv('KEYWORDS', '').split(',')

def fetch_news(keyword):
    """从 NewsAPI 获取新闻"""
    url = f"https://newsapi.org/v2/everything?q={keyword}&sortBy=publishedAt&language=en&apiKey={NEWSAPI_KEY}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json().get('articles', [])[:5]
    except Exception as e:
        print(f"Error fetching news for {keyword}: {e}")
    return []

def create_email_body(news_dict):
    """创建 HTML 邮件内容"""
    html = f"""
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #f5f5f5; }}
            .container {{ max-width: 800px; margin: 0 auto; background-color: white; padding: 20px; }}
            h1 {{ color: #333; text-align: center; }}
            .category {{ margin: 20px 0; }}
            .category h2 {{ color: #0066cc; border-bottom: 2px solid #: 4px solid #0066cc; }}
    .news-title {{ font-weight: bold; font-size: 16px; }}
    .news-description {{ color: #666; margin: 10px 0; }}
    .news-source {{ font-size: 12px; color: #999; }}
    a {{ color: #0066cc; text-decoration: none; }}
    .footer {{ text-align: center; color: #999; font-size: 12px; margin-top: 30px; border-top: 1px solid #ddd; padding-top: 10px; }}
    </style></head><body>
    <div class="container">
    <h1>📰 Daily News Digest</h1>
    <p style="text-align: center; color: #666;">{datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
    """
    
    for category, articles in news_dict.items():
        if articles:
            html += f'<div class="category"><h2>{category}</h2>'
            for article in articles:
                html += f'''
                <div class="news-item">
                    <div class="news-title">{article.get('title', 'N/A')}</div>
                    <div class="news-description">{article.get('description', 'N/A')[:200]}...</div>
                    <div class="news-source">
                        Source: {article.get('source', {}).get('name', 'Unknown')} | 
                        0066cc; padding-bottom: 10px; }}
            .news-item {{ margin: 15px 0; padding: 15px; background-color: #f9f9f9; border-left: 4px solid #0066cc; }}
            .news-title {{ font-weight: bold; font-size: 16px; color: #333; }}
            .news-description {{ color: #666; margin: 10px 0; }}
            .news-source {{ font-size: 12px; color: #999; }}
            a {{ color: #0066cc; text-decoration: none; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📰 Daily News Digest</h1>
            <p style="text-align: center; color: #666;">{datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
    """
    
    for category, articles in news_dict.items():
        if articles:
            html += f'<div class="category"><h2>{category}</h2>'
            for article in articles:
                html += f'''
                <div class="news-item">
                    <div class="news-title">{article.get('title', 'N/A')}</div>
                    <div class="news-description">{article.get('description', 'N/A')[:200]}...</div>
                    <div class="news-source">
                        来源: {article.get('source', {}).get('name', 'Unknown')} | 
                        <a href="{article.get('url', '#<a href="{article.get('url', '#')}">Read More</a>
                    </div>
                </div>
                '''
            html += '</div>'
    
    html += """
    <div class="footer"><p>Auto-generated email, do not reply</p></div>
    </div></body></html>
    """
    return html

def send_email(subject, html_content):
    """发送邮件"""
    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = EMAIL_FROM
        msg['To'] = EMAIL_TO
        msg.attach(MIMEText(html_content, 'html', 'utf-8'))
        
        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, timeout=10)
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
        server.quit()
        print(f"✅ Email sent to {EMAIL_TO}")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("🔄 Starting news subscription...")
    news_dict = {}
    for keyword in KEYWORDS:
        keyword = keyword.strip()
        if keyword:
            print(f"📥 Fetching: {keyword}")
            articles = fetch_news(keyword)
            if articles:
                news_dict[keyword] = articles
    
    if not news_dict:
        print("❌ No')}">阅读全文</a>
                    </div>
                </div>
                '''
            html += '</div>'
    
    html += """
            <div class="footer">
                <p>这是一条自动生成的邮件，请勿回复</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html

def send_email(subject, html_content):
    """发送邮件"""
    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = EMAIL_FROM
        msg['To'] = EMAIL_TO
        
        msg.attach(MIMEText(html_content, 'html', 'utf-8'))
        
        server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, timeout=10)
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
        server.quit()
        print(f"✅ Email sent successfully to {EMAIL_TO}")
        return True
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return False

def main():
    print("🔄 Starting daily news subscription...")
    
    news_dict = {}
    for keyword in KEYWORDS:
        keyword = keyword.strip()
        if keyword:
            print(f"📥 Fetching news for: {keyword}")
            articles = fetch_news(keyword)
            if articles:
                news_dict[ news found")
        return
    
    html_content = create_email_body(news_dict)
    subject = f"📰 Daily News - {datetime.now().strftime('%Y-%m-%d')}"
    send_email(subject, html_content)

if __name__ == "__main__":
    main()
