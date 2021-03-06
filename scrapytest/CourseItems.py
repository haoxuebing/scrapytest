import scrapy


class CourseItem(scrapy.Item):
    # 课程标题
    title = scrapy.Field()
    # 课程url
    url = scrapy.Field()
    # 课程标题图片
    image_url = scrapy.Field()
    # 课程描述
    introduction = scrapy.Field()
    # 学习人数
    student = scrapy.Field()


course = CourseItem()
# 赋值
course['title'] = "语文"
# 取值
course['title']
course.get('title')
# 获取全部键
course.keys()
# 获取全部值
course.items()
