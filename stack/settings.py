BOT_NAME = 'stack'
SPIDER_MODULES = ['stack.spiders']
#NEWSPIDER_MODULE = 'stack.spiders'
ITEM_PIPELINES = ['stack.pipelines.StackPipeline', ]


DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'mustajab',
    'password': '',
    'database': 'scrape'
}