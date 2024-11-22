from my_module.scraper import crawl


def test_crawl():
    # Просто проверяем, что функция не вызывает исключения
    try:
        crawl(time_limit=10, source='lrytas', return_format='csv')
    except Exception as e:
        assert False, f"Ошибка при выполнении crawl: {e}"
    assert True
