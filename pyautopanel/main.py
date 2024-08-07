import logging

import pyautopanel.panel.trip_panel as trip_panel


def setup_logging():
    # 配置日志格式以包含时间戳
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )


def main():
    setup_logging()
    trip_panel.main()


if __name__ == '__main__':
    main()
