from module.base.timer import Timer
from module.logger import logger
from tasks.base.page import page_main
from tasks.base.ui import UI
from tasks.login.assets.assets_login import LOGIN_START_GAME, ANNOUNCEMENT, \
    CHECKIN_REWARDS, GET_CHECKIN_REWARDS, ACTIVITY_POPUP, SUPPLY_POPUP


class Login(UI):
    def _handle_app_login(self):
        """
        Pages:
            in: Any page
            out: page_main

        Raises:
            GameStuckError:
            GameTooManyClickError:
        """
        logger.hr('App login')

        orientation_timer = Timer(5)
        main_page_timer = Timer(1.5, count=5).start()
        login_success = False

        while 1:
            # Watch device rotation
            if not login_success and orientation_timer.reached():
                # Screen may rotate after starting an app
                self.device.get_orientation()
                orientation_timer.reset()

            self.device.screenshot()

            # End
            if self.ui_page_appear(page_main):  # and main_page_timer.reached():
                if main_page_timer.reached():
                    logger.info('Login to main confirm')
                    break
            else:
                main_page_timer.reset()

            # # Login
            # if self.appear_then_click(LOGIN_CONFIRM):
            #     continue
            # if self.appear_then_click(USER_AGREEMENT_ACCEPT):
            #     continue
            # # Additional
            # if self.ui_additional():
            #     continue

            # Login
            if self.appear_then_click(LOGIN_START_GAME):
                continue

            if self.appear_then_click(ANNOUNCEMENT):
                continue

            if self.appear_then_click(GET_CHECKIN_REWARDS):
                continue

            if self.appear_then_click(CHECKIN_REWARDS):
                continue

            if self.appear_then_click(ACTIVITY_POPUP):
                continue

            if self.appear_then_click(SUPPLY_POPUP):
                continue

        return True

    def handle_app_login(self):
        self.device.screenshot_interval_set(1.0)
        try:
            self._handle_app_login()
        finally:
            self.device.screenshot_interval_set()

    def app_stop(self):
        logger.hr('App stop')
        self.device.app_stop()

    def app_start(self):
        logger.hr('App start')
        self.device.app_start()
        self.handle_app_login()

    def app_restart(self):
        logger.hr('App restart')
        self.device.app_stop()
        self.device.app_start()
        self.handle_app_login()
        self.config.task_delay(server_update=True)


if __name__ == '__main__':
    tmp = Login(config="nce", task="login")
    tmp.app_start()
    # tmp.image_file = "tasks/login/tmp.png"

    # print(tmp.appear())
    pass
