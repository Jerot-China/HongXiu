############功能描述   
红袖飘香小说网免费小说章节爬取

###########环境依赖
python3.6 
scrapy

########## 目录结构描述
items.py  需要存储的字段名
middlewares.py  下载中间件，使用了ip代理池
piplines 将数据存储进mysql数据库
settings.py 配置文件
proxies.py  爬取西刺代理的脚本
proxies.txt  爬取下来并验证过的代理ip

执行命令scrapy crawl fiction_free  执行脚本

############## 数据库建表语句
CREEATE DATABASE hongxiu;
CREATE TABLE `fiction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(50) NOT NULL,
  `category` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `status` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `gender` char(1) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `words` float(11,2) NOT NULL,
  `collections` int(11) NOT NULL,
  `clicks` int(11) NOT NULL,
  `author` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `introduce` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `url` varchar(400) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=751 DEFAULT CHARSET=utf8;

CREATE TABLE `fiction_directory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fiction_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `fiction_directory_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `fiction_id` int(10) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fiction_id` (`fiction_id`),
  CONSTRAINT `fiction_id` FOREIGN KEY (`fiction_id`) REFERENCES `fiction` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2667 DEFAULT CHARSET=utf8;




