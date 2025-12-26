import requests
from bs4 import BeautifulSoup
import csv

# 定义请求头，模拟浏览器访问
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# 存储所有高校数据的列表
universities = []

# 翻页爬取（假设分页参数为page，需根据实际网站调整）
def crawl_university_ranking():
    page = 1
    while True:
        # 替换为实际的大学排名网站URL，需根据目标站点调整分页参数
        url = f"https://www.example.com/university-ranking?page={page}"
        response = requests.get(url, headers=headers, timeout=10)
        
        # 页面访问失败或无数据时终止循环
        if response.status_code != 200:
            break
        
        soup = BeautifulSoup(response.text, "html.parser")
        # 定位高校信息的HTML节点（需根据目标网站的结构调整选择器）
        university_items = soup.select(".university-item")
        
        # 无数据则退出翻页
        if not university_items:
            break
        
        # 提取单页高校信息
        for item in university_items:
            try:
                rank = item.select_one(".rank").text.strip()  # 排名
                name = item.select_one(".name").text.strip()  # 学校名称
                score = item.select_one(".score").text.strip()  # 评分（可选）
                universities.append({"排名": rank, "学校名称": name, "评分": score})
            except Exception as e:
                print(f"提取数据失败：{e}")
                continue
        
        print(f"已爬取第{page}页，累计{len(universities)}所高校")
        page += 1

# 将数据保存为CSV文件
def save_to_csv():
    with open("university_ranking.csv", "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["排名", "学校名称", "评分"])
        writer.writeheader()
        writer.writerows(universities)
    print("数据已保存至university_ranking.csv")

if __name__ == "__main__":
    crawl_university_ranking()
    save_to_csv()
# 在这里编写代码
